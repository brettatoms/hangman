import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs/Observable";

export interface Game {
  id: string;
  word: string;
  guesses: string[];
  score: number;
  status: string;
}

@Injectable()
export class GameService {
  BASE_URL = "http://localhost:5000";
  constructor(private http: HttpClient) {}

  getToken() {
    return localStorage.getItem("token");
  }

  create(): Observable<Game> {
    const url = `${this.BASE_URL}/games`;
    const token = this.getToken();
    return this.http.post(
      url,
      {},
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    ) as Observable<Game>;
  }

  get(gameId): Observable<Game> {
    const url = `${this.BASE_URL}/games/${gameId}`;
    const token = this.getToken();
    return this.http.get(url, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }) as Observable<Game>;
  }

  guess(gameId, char): Observable<Game> {
    const url = `${this.BASE_URL}/games/${gameId}`;
    const token = this.getToken();
    const data = { guess: char };
    return this.http.patch(url, data, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }) as Observable<Game>;
  }

  highScores(): Observable<any> {
    const url = `${this.BASE_URL}/games/highscores`;
    const token = this.getToken();
    return this.http.get(url, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
  }
}
