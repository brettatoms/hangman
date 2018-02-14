import { Injectable } from "@angular/core";
import { Location } from "@angular/common";
import { HttpClient } from "@angular/common/http";

import { map } from "rxjs/operators";

@Injectable()
export class AuthService {
  API_URL = "http://localhost:5000";

  constructor(private http: HttpClient, private location: Location) {}

  login() {
    const url = `${this.API_URL}/auth`;
    console.log(url);
    // this.location.go(url);
    location.href = url;
  }
}
