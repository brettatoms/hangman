import { TestBed, inject } from "@angular/core/testing";
import { HttpClientTestingModule } from "@angular/common/http/testing";

import { GameService } from "./game.service";

describe("GameService", () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [GameService]
    });
  });

  it(
    "should be created",
    inject([GameService], (service: GameService) => {
      expect(service).toBeTruthy();
    })
  );
});
