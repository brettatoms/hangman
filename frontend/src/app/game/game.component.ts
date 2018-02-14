import { Component, OnInit } from "@angular/core";
import { ActivatedRoute, ParamMap, Router } from "@angular/router";
import { take } from "rxjs/operators";
import { map, range } from "lodash";

import { Game, GameService } from "../game.service";

@Component({
  selector: "app-game",
  templateUrl: "./game.component.html",
  styleUrls: ["./game.component.scss"]
})
export class GameComponent {
  guessWord: string;
  game: Game;
  characters = map(range(97, 123), n => String.fromCharCode(n)[0]).concat([
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
  ]);

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private gameSvc: GameService
  ) {
    this.route.paramMap.subscribe(params => {
      const gameId = params.get("gameId");
      if (gameId) {
        this.gameSvc.get(gameId).subscribe(game => (this.game = game));
      }
    });

    console.log(this.characters);
  }

  createGame() {
    this.gameSvc
      .create()
      .subscribe(
        game => this.router.navigateByUrl(`/game/${game.id}`),
        err => console.error(err)
      );
  }

  hasGuessed(char) {
    // console.log(this.game.guesses, "includes", char);
    return this.game.guesses.includes(char);
  }

  guess(char, $event) {
    if ($event) {
      this.guessWord = null;
      $event.preventDefault();
    }

    this.gameSvc
      .guess(this.game.id, char)
      .subscribe(game => (this.game = game));
  }
}
