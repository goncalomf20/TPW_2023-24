import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AllFantasyTeamsComponent } from './all-fantasy-teams.component';

describe('AllFantasyTeamsComponent', () => {
  let component: AllFantasyTeamsComponent;
  let fixture: ComponentFixture<AllFantasyTeamsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AllFantasyTeamsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AllFantasyTeamsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
