import { Component , Input } from '@angular/core';
import { Equipa } from '../../models/equipa';
import { CommonModule } from '@angular/common';
import { GetModalIdService } from '../../services/shared/get-modal-id.service';

@Component({
  selector: 'app-t-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './t-card.component.html',
  styleUrl: './t-card.component.css'
})
export class TCardComponent {
  id: number = 0
  won: number = 0
  lost: number = 0
  draws: number = 0
  @Input() equipa:Equipa | undefined
  shared: GetModalIdService
  url: string = "https://img-aws.ehowcdn.com/640x960/s3-us-west-1.amazonaws.com/contentlab.studiod/getty/cache.gettyimages.com/3a5bf7ffb81b474397bbf1cd1887a720.jpg"
  constructor(sh:GetModalIdService){
    this.shared = sh
    this.id = this.shared.getId()
    if (this.shared.getId() == 3){
      this.url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRL2-ci3xRSfjx120uiix6KptCRI_mCbPmhQ&usqp=CAU"
   }
  }
}
