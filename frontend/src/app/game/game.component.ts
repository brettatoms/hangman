import { Component, OnInit } from "@angular/core";
import { ActivatedRoute, ParamMap, Router } from "@angular/router";
import { take } from "rxjs/operators";
import { map, range } from "lodash";

import { Game, GameService } from "../game.service";

interface Score {
  email: string;
  score: number;
}

@Component({
  selector: "app-game",
  templateUrl: "./game.component.html",
  styleUrls: ["./game.component.scss"]
})
export class GameComponent {
  guessWord: string;
  game: Game;
  highScores: Score[];
  readonly MAX_WRONG_GUESSES = 5;

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

      this.gameSvc.highScores().subscribe(
        (scores: Score[]) => {
          this.highScores = scores;
        }
        // err => console.error(err)
      );
    });
  }

  createGame() {
    this.gameSvc.create().subscribe(
      game => this.router.navigateByUrl(`/game/${game.id}`)
      // err => console.error(err)
    );
  }

  get progress(): number {
    return this.MAX_WRONG_GUESSES - this.game.guesses_left;
  }

  get progressClass() {
    const progress = this.progress;
    if (progress <= 2) {
      return "is-success";
    } else if (progress > 2 && progress < 4) {
      return "is-warning";
    } else {
      return "is-danger";
    }
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
