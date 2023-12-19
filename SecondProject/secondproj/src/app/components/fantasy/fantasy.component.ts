import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { RouterModule } from '@angular/router';
import { Jogador } from '../../models/jogador';
import { JogadorService } from "../../services/jogador.service";
import { FooterComponent } from '../footer/footer.component';
import { NavbarComponent } from '../navbar/navbar.component';

@Component({
  selector: 'app-fantasy',
  standalone: true,
  imports: [RouterModule,
  FooterComponent,
  NavbarComponent,
  CommonModule
  ],
  templateUrl: './fantasy.component.html',
  styleUrl: './fantasy.component.css'
})
export class FantasyComponent {
  jogadores: Jogador[] = [];
  jogService : JogadorService = inject(JogadorService)
jogador: any;


  constructor() {
    this.jogService.getJogadores().then((jogadores: Jogador[]) => {
      
        this.jogadores.push(...jogadores);
        console.log(this.jogadores);
    });
    
  }
  
}
