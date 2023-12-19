import { TestBed } from '@angular/core/testing';

import { EquipasService } from './equipas.service';

describe('EquipasService', () => {
  let service: EquipasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EquipasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
