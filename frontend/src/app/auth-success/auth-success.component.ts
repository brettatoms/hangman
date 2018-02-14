import { Component, OnInit } from "@angular/core";
import { ActivatedRoute, ParamMap, Router } from "@angular/router";
import { take } from "rxjs/operators";

@Component({
  selector: "app-auth-success",
  templateUrl: "./auth-success.component.html",
  styleUrls: ["./auth-success.component.scss"]
})
export class AuthSuccessComponent {
  constructor(private route: ActivatedRoute, private router: Router) {
    console.log("AuthSuccessComponent");

    this.route.queryParamMap.pipe(take(1)).subscribe(params => {
      const token = params.get("token");
      if (token === null) {
        console.error("No token");
        return;
      }

      localStorage.setItem("token", token);
      this.router.navigateByUrl("/");
    });
  }
}
