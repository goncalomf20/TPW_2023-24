import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { ExclusiveModalComponent } from '../exclusive-modal/exclusive-modal.component';

@Component({
  selector: 'app-card-modalidade',
  standalone: true,
  imports: [RouterModule,ExclusiveModalComponent],
  templateUrl: './card-modalidade.component.html',
  styleUrl: './card-modalidade.component.css'
})
export class CardModalidadeComponent {

}
