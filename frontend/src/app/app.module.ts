import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { HttpClientModule } from "@angular/common/http";

import { AppComponent } from "./app.component";
import { LoginComponent } from "./login/login.component";
import { GameComponent } from "./game/game.component";
import { AuthGuard } from "./auth.guard";
import { GameService } from "./game.service";
import { AuthService } from "./auth.service";
import { AuthSuccessComponent } from "./auth-success/auth-success.component";
import { LogoutComponent } from "./logout/logout.component";

export const routes: Routes = [
  { path: "login", component: LoginComponent },
  { path: "logout", component: LogoutComponent },
  {
    path: "game",
    component: GameComponent,
    canActivate: [AuthGuard]
  },
  {
    path: "game:/gameId",
    component: GameComponent,
    canActivate: [AuthGuard]
  },
  {
    path: "auth/success",
    component: AuthSuccessComponent
  },
  {
    path: "",
    redirectTo: "game",
    pathMatch: "full"
  }
  // { path: "404", component: PageNotFoundComponent },
  // { path: "**", component: PageNotFoundComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    GameComponent,
    AuthSuccessComponent,
    LogoutComponent
  ],
  imports: [BrowserModule, RouterModule.forRoot(routes), HttpClientModule],
  providers: [AuthGuard, AuthService, GameService],
  bootstrap: [AppComponent]
})
export class AppModule {}
