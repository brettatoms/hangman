import { ErrorHandler, Injectable, Injector, NgModule } from "@angular/core";
import { AngularFireAuth } from "angularfire2/auth";
import { Router } from "@angular/router";

@Injectable()
export class DefaultErrorHandler implements ErrorHandler {
  // constructor(private router: Router) {}
  constructor(private injector: Injector) {}

  handleError(error) {
    const router = this.injector.get(Router);
    console.log("DEFAULT ERROR HANDLER");
    console.log(error);
    console.log(error.code);
    console.log(error.message);
    if (error.status === 401) {
      router.navigateByUrl("/logout");
    }
  }
}

// @NgModule({
//   providers: [{ provide: ErrorHandler, useClass: DefaultErrorHandler }]
// })
// export class ErrorHandlerModule {}
