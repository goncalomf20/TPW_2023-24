import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalidadeStatsComponent } from './modalidade-stats.component';

describe('ModalidadeStatsComponent', () => {
  let component: ModalidadeStatsComponent;
  let fixture: ComponentFixture<ModalidadeStatsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ModalidadeStatsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ModalidadeStatsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
