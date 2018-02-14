import { Component, OnInit } from "@angular/core";
import { ActivatedRoute, ParamMap, Router } from "@angular/router";
import { take } from "rxjs/operators";

import { Game, GameService } from "../game.service";

@Component({
  selector: "app-game",
  templateUrl: "./game.component.html",
  styleUrls: ["./game.component.scss"]
})
export class GameComponent {
  game: Game;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private gameSvc: GameService
  ) {
    this.route.paramMap.pipe(take(1)).subscribe(params => {
      const gameId = params.get("gameId");
      if (gameId) {
        this.gameSvc.get(gameId).subscribe(game => (this.game = game));
      }
    });
  }

  createGame() {
    this.gameSvc
      .create()
      .subscribe(
        game => this.router.navigateByUrl("/game/${game.id}"),
        err => console.error(err)
      );
  }
}
