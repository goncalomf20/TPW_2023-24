import { Component , Input, OnInit } from '@angular/core';
import { Jogador } from '../../models/jogador';
import { GetModalIdService } from '../../services/shared/get-modal-id.service';
import { CommonModule } from '@angular/common';
import { Evento } from '../../models/evento';
import { JogadorService } from '../../services/jogador.service';

@Component({
  selector: 'app-p-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './p-card.component.html',
  styleUrl: './p-card.component.css'
})
export class PCardComponent implements OnInit{
  id: number = 0
  goals: number = 0
  yellow_cards: number = 0
  red_cards: number = 0
  points: number = 0
  assists: number = 0
  rebounds: number = 0
  @Input() jogador:Jogador | undefined
  jogadorService: JogadorService
  shared: GetModalIdService
  url: string = "https://img-aws.ehowcdn.com/640x960/s3-us-west-1.amazonaws.com/contentlab.studiod/getty/cache.gettyimages.com/3a5bf7ffb81b474397bbf1cd1887a720.jpg"
  constructor(sh:GetModalIdService,jS:JogadorService){
    this.shared = sh
    this.id = this.shared.getId()
    if (this.shared.getId() == 3){
      this.url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRL2-ci3xRSfjx120uiix6KptCRI_mCbPmhQ&usqp=CAU"
   }
   this.jogadorService = jS
   
  }
  ngOnInit(): void {
    if (this.jogador?.id == undefined){
      this.jogadorService.getEventosByJogadorID(0).then((eventos : Evento[]) => {
      });
     }
     else{
      this.jogadorService.getEventosByJogadorID(this.jogador.id).then((eventos : Evento[]) => {
        console.log(eventos)
        for (let index = 0; index < eventos.length; index++) {
          const element = eventos[index];
          if (element.tipo == "golo"){
            this.goals = this.goals + 1
          }
          if (element.tipo == "amarelo"){
            this.yellow_cards = this.yellow_cards + 1
          }
          if (element.tipo == "vermelho"){
            this.red_cards = this.red_cards + 1
          }
          if (element.tipo == "points"){
            this.points = this.points + 1
          }
          if (element.tipo == "rebounds"){
            this.rebounds = this.rebounds + 1
          }
          if (element.tipo == "assists"){
            this.assists = this.assists + 1
          }
          
        }
      });
     }
  }
  
}
