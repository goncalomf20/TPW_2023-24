import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { ExclusiveModalComponent } from '../exclusive-modal/exclusive-modal.component';
import { GetModalIdService } from '../../services/shared/get-modal-id.service';

@Component({
  selector: 'app-card-modalidade',
  standalone: true,
  imports: [RouterModule,ExclusiveModalComponent],
  templateUrl: './card-modalidade.component.html',
  styleUrl: './card-modalidade.component.css'
})
export class CardModalidadeComponent {

  shared: GetModalIdService
  constructor(shared:GetModalIdService){
    this.shared = shared
  }
  setS(id:number){
    this.shared?.setId(id)
  }

}
