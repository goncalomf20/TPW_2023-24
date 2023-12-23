import { Component , Input, OnInit } from '@angular/core';
import { Equipa } from '../../models/equipa';
import { CommonModule } from '@angular/common';
import { GetModalIdService } from '../../services/shared/get-modal-id.service';
import { JogoService } from '../../services/jogo.service';
import { Jogo } from '../../models/jogo';

@Component({
  selector: 'app-t-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './t-card.component.html',
  styleUrl: './t-card.component.css'
})
export class TCardComponent implements OnInit {
  id: number = 0
  won: number = 0
  lost: number = 0
  draws: number = 0
  jogoService:JogoService
  @Input() equipa:Equipa | undefined
  shared: GetModalIdService
  url: string = "https://img-aws.ehowcdn.com/640x960/s3-us-west-1.amazonaws.com/contentlab.studiod/getty/cache.gettyimages.com/3a5bf7ffb81b474397bbf1cd1887a720.jpg"
  constructor(sh:GetModalIdService,jS:JogoService){
    this.shared = sh
    this.jogoService = jS
    this.id = this.shared.getId()
    if (this.shared.getId() == 3){
      this.url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRL2-ci3xRSfjx120uiix6KptCRI_mCbPmhQ&usqp=CAU"
   }
  }
  ngOnInit(): void {
    if (this.equipa == undefined){
      console.log("deu asneira")
    }
    else{
      this.jogoService.getJogoByEquipaCasa(this.equipa.id).then((jogos: Jogo[]) => {
        for (let index = 0; index < jogos.length; index++) {
          const jogo = jogos[index];
          console.log("JOGOS CASA ", jogo);  // Use ',' instead of '+'
          
          if (jogo.golos_eq_casa > jogo.equipa_fora){
            this.won = this.won + 1
          }
          if (jogo.golos_eq_casa < jogo.equipa_fora){
            this.lost = this.lost + 1
          }
          if (jogo.golos_eq_casa == jogo.equipa_fora){
            this.draws = this.draws + 1
          }
          
        }
      })
      this.jogoService.getJogoByEquipaFora(this.equipa.id).then((jogos: Jogo[]) => {

        for (let index = 0; index < jogos.length; index++) {
          const jogo = jogos[index];
          console.log("JOGO FORA " + jogo)
          if (jogo.golos_eq_casa < jogo.equipa_fora){
            this.won = this.won + 1
          }
          if (jogo.golos_eq_casa > jogo.equipa_fora){
            this.lost = this.lost + 1
          }
          if (jogo.golos_eq_casa == jogo.equipa_fora){
            this.draws = this.draws + 1
          }
          
        }
      })
    }
  }
}
