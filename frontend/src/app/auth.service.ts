import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";

import { map } from "rxjs/operators";

@Injectable()
export class AuthService {
  API_URL = true
    ? "https://hangman-ba.herokuapp.com/"
    : "http://localhost:5000";

  constructor(private http: HttpClient) {}

  login() {
    const url = `${this.API_URL}/auth`;
    location.href = url;
  }
}
