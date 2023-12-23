import { TestBed } from '@angular/core/testing';

import { GetModalIdService } from './get-modal-id.service';

describe('GetModalIdService', () => {
  let service: GetModalIdService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GetModalIdService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
