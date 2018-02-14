import { Component, OnInit } from "@angular/core";

import { AuthService } from "../auth.service";

@Component({
  selector: "app-login",
  templateUrl: "./login.component.html",
  styleUrls: ["./login.component.scss"]
})
export class LoginComponent {
  constructor(private authSvc: AuthService) {}

  login() {
    this.authSvc.login(); // .subscribe();
  }
}