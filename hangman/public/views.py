# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
# import httplib2

from flask import Blueprint
from flask import current_app as app
from flask import redirect, request, url_for
from flask_login import current_user, login_required
from googleapiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow

from hangman.extensions import login_manager
from hangman.user.models import User

blueprint = Blueprint('public', __name__, static_folder='../static')

CLIENT_ID = '862579870309-001s3qa9usg6bi7ci61vbb55vaustovj.apps.googleusercontent.com'
CLIENT_SECRET = 'leuMXo3UWWmh5u0x41COQzok'


def oauth_flow_factory():
    redirect_uri = url_for('public.auth_redirect', _external=True)
    oauth_flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                                     client_secret=CLIENT_SECRET,
                                     scope='profile email',
                                     redirect_uri=redirect_uri)
    return oauth_flow


@login_manager.request_loader
def load_user_from_request(request):
    """Load the user from the request."""
    # first, try to login using the api_key url arg
    request_token = request.args.get('token')
    if request_token:
        user = User.query.filter_by(request_token=request_token).first()
        if user:
            return user

    # next, try to login using Basic Auth
    header = request.headers.get('Authorization')
    if header:
        request_token = header.replace('Bearer ', '', 1)
        user = User.query.filter_by(request_token=request_token).first()
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None


@blueprint.route('/auth')
def auth():
    oauth_flow = oauth_flow_factory()
    auth_uri = oauth_flow.step1_get_authorize_url()
    return redirect(auth_uri)


@blueprint.route('/auth/redirect')
def auth_redirect():
    # get the users request and access tokens
    request_token = request.args['code']
    oauth_flow = oauth_flow_factory()
    credentials = oauth_flow.step2_exchange(request_token)
    access_token = credentials.get_access_token().access_token

    # get the user's email from google
    service = build('plus', 'v1', credentials=credentials)
    me = service.people().get(userId='me').execute()
    email = filter(lambda x: x['type'] == 'account', me['emails'])
    email = list(email)[0]['value']

    # find or create the user
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email)

    # set the user's tokens and save in the db
    user.request_token = request_token
    user.access_token = access_token
    user.save()

    return redirect(app.config['APP_URL'] + f'/hangman/auth/success?token={request_token}')


@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    current_user.request_token = None
    current_user.access_token = None
    current_user.save()
    return '', 204
