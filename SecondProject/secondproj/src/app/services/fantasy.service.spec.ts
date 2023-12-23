import { TestBed } from '@angular/core/testing';
import { FantastyService } from './fantasy.service';

describe('FantastyService', () => {
  let service: FantastyService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FantastyService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
