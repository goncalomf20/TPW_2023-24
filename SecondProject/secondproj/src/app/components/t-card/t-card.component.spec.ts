import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TCardComponent } from './t-card.component';

describe('TCardComponent', () => {
  let component: TCardComponent;
  let fixture: ComponentFixture<TCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TCardComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
