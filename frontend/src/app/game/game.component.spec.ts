import { Injectable } from "@angular/core";
import { async, ComponentFixture, TestBed } from "@angular/core/testing";
import { RouterTestingModule } from "@angular/router/testing";
import { FormsModule } from "@angular/forms";
import { Observable } from "rxjs/Observable";
import "rxjs/add/observable/of";
import * as sinon from "sinon";

import { GameService } from "../game.service";
import { GameComponent } from "./game.component";

@Injectable()
export class GameServiceMock {
  get = sinon.stub().returns(Observable.of({}));
  highScores = sinon.stub().returns(Observable.of([]));
}

describe("GameComponent", () => {
  let component: GameComponent;
  let fixture: ComponentFixture<GameComponent>;

  beforeEach(
    async(() => {
      TestBed.configureTestingModule({
        imports: [FormsModule, RouterTestingModule],
        declarations: [GameComponent],
        providers: [
          {
            provide: GameService,
            useClass: GameServiceMock
          }
        ]
      }).compileComponents();
    })
  );

  beforeEach(() => {
    fixture = TestBed.createComponent(GameComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("should create", () => {
    expect(component).toBeTruthy();
  });
});
