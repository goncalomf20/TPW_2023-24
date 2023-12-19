import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExclusiveModalComponent } from './exclusive-modal.component';

describe('ExclusiveModalComponent', () => {
  let component: ExclusiveModalComponent;
  let fixture: ComponentFixture<ExclusiveModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ExclusiveModalComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ExclusiveModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
