import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardModalidadeComponent } from './card-modalidade.component';

describe('CardModalidadeComponent', () => {
  let component: CardModalidadeComponent;
  let fixture: ComponentFixture<CardModalidadeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CardModalidadeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CardModalidadeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
