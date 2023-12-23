import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AllPlayerStatsComponent } from './all-player-stats.component';

describe('AllPlayerStatsComponent', () => {
  let component: AllPlayerStatsComponent;
  let fixture: ComponentFixture<AllPlayerStatsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AllPlayerStatsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AllPlayerStatsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
