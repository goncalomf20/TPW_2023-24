import { Component , Input } from '@angular/core';
import { Jogador } from '../../models/jogador';
import { GetModalIdService } from '../../services/shared/get-modal-id.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-p-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './p-card.component.html',
  styleUrl: './p-card.component.css'
})
export class PCardComponent {
  id: number = 0
  goals: number = 0
  yellow_cards: number = 0
  red_cards: number = 0
  points: number = 0
  assists: number = 0
  rebounds: number = 0
  @Input() jogador:Jogador | undefined
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
