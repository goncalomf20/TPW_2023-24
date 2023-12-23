import { TestBed } from '@angular/core/testing';
import { LigaIDService } from './liga-id.service';

describe('LigaIDService', () => {
  let service: LigaIDService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LigaIDService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
