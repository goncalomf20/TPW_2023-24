import { Component, Input } from '@angular/core';
import { RouterModule } from '@angular/router';
import { Liga } from '../../models/liga';
import { GetModalIdService } from '../../services/shared/get-modal-id.service';
import { LigaIDService } from '../../services/shared/liga-id.service';
@Component({
  selector: 'app-card-player',
  standalone: true,
  imports: [RouterModule,CardPlayerComponent],
  templateUrl: './card-player.component.html',
  styleUrl: './card-player.component.css'
})
export class CardPlayerComponent {
  shared2:LigaIDService
  @Input() data:Liga | undefined
  constructor(shared2:LigaIDService){
    this.shared2 = shared2
  }

  setS(id:number | undefined){
    if (id == undefined){
    this.shared2.setId(0)
    }
    else{
      this.shared2.setId(id)
    }
  }

  
}
