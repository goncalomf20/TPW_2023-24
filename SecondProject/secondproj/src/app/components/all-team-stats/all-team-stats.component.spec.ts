import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AllTeamStatsComponent } from './all-team-stats.component';

describe('AllTeamStatsComponent', () => {
  let component: AllTeamStatsComponent;
  let fixture: ComponentFixture<AllTeamStatsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AllTeamStatsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AllTeamStatsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
