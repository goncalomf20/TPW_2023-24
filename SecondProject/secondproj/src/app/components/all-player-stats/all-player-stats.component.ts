import { Component, Input, OnInit } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';
import { RouterModule } from '@angular/router';
import { PCardComponent } from '../p-card/p-card.component';
import { Jogador } from '../../models/jogador';
import { JogadorService } from '../../services/jogador.service';
import { GetModalIdService } from '../../services/shared/get-modal-id.service';
import { CommonModule } from '@angular/common';
import { LigaIDService } from '../../services/shared/liga-id.service';
import { Liga } from '../../models/liga';

@Component({
  selector: 'app-all-player-stats',
  standalone: true,
  imports: [RouterModule,FooterComponent,NavbarComponent,PCardComponent,CommonModule],
  templateUrl: './all-player-stats.component.html',
  styleUrl: './all-player-stats.component.css'
})
export class AllPlayerStatsComponent implements OnInit{
  jogadorService: JogadorService
  shared: GetModalIdService
  jogadores: Jogador[] = []
  m_id: number
  shared2: LigaIDService
  liga_id: number

  constructor(jS:JogadorService,gI:GetModalIdService,sh2:LigaIDService){
    this.jogadorService = jS
    this.shared = gI
    this.m_id = this.shared.getId()
    this.shared2 = sh2
    this.liga_id = this.shared2.getId()
  }
  ngOnInit(): void {
    this.jogadorService.getJogadoresByLigaID(this.liga_id).then((jogadores : Jogador[]) => {
      this.jogadores = jogadores
      console.log(this.jogadores)
    })
  }

  

  

}
