import { CommonModule } from '@angular/common';
import { Component, OnInit, inject } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { Equipa } from '../../models/equipa';
import { FantasyTeam } from '../../models/fantasy';
import { Jogador } from '../../models/jogador';
import { Users } from '../../models/users';
import { EquipasService } from '../../services/equipas.service';
import { FantastyService } from '../../services/fantasy.service';
import { JogadorService } from '../../services/jogador.service';
import { ModalidadesService } from '../../services/modalidades.service';
import { UsersService } from '../../services/users.service';
import { FooterComponent } from '../footer/footer.component';
import { NavbarComponent } from '../navbar/navbar.component';

@Component({
  selector: 'app-all-fantasy-teams',
  standalone: true,
  imports: [RouterModule,
    FooterComponent,
    NavbarComponent,
    CommonModule,
    ReactiveFormsModule,
    FormsModule
    ],
  templateUrl: './all-fantasy-teams.component.html',
  styleUrls: ['./all-fantasy-teams.component.css']
})
export class AllFantasyTeamsComponent implements OnInit {
  modalidade: string | null = null;

  nr_jogadores: number = 0;

  user_fanta : {[user_name: string]: FantasyTeam[]} = {};

  user_players : {[user_name: string]: Jogador[]} = {};

  user_total_price : {[user_name: string]: number} = {};  

  user_total_points : {[user_name: string]: number} = {};

  jogador_equipa : {[nome: string]: Equipa} = {};

  sortedUsers : string[] = [];

  fantasyService : FantastyService = inject(FantastyService);
  
  usersService: UsersService = inject(UsersService);

  modService: ModalidadesService = inject(ModalidadesService);

  jogService: JogadorService = inject(JogadorService);

  equipaService: EquipasService = inject(EquipasService);


  constructor(private route: ActivatedRoute) {}

  ngOnInit() {
    console.log('AllFantasyTeamsComponent initialized');
    
    // Access the modalidade parameter from the route
    this.route.params.subscribe(params => {
      this.modalidade = params['modalidade'];
      console.log('Modalidade:', this.modalidade);

      
    });

    console.log('Modalidade:', this.modalidade);
    if (this.modalidade !== null) {
      this.modService.getByName(this.modalidade).then((modalidade: any) => {
        console.log('Modalidade:', modalidade);
        this.modalidade = modalidade.nome;
        this.nr_jogadores = modalidade.nr_jogadores;
      })

      this.fantasyService.getFantasiesByModalidade(this.modalidade).then((fantasyTeams: FantasyTeam[]) => {
        console.log('Fantasy teams:', fantasyTeams);


        fantasyTeams.forEach((fantasyTeam: FantasyTeam) => {
          this.usersService.getUsersById(fantasyTeam.user).then((user: Users) => {
            // console.log('User:', user.id);
            fantasyTeam.players.forEach((player: number) => {
              // console.log('Player:', player);
              this.jogService.getJogadoresById(player).then((jogador: Jogador) => {
                // console.log('Jogador:', jogador.valor + " " + jogador.pontos + " " + jogador.id_equipa);
                this.user_players[user.username] = (this.user_players[user.username] ?? []).concat(jogador);
                this.user_total_price[user.username] = (this.user_total_price[user.username] ?? 0) + parseInt(jogador.valor.toString(), 10);
                this.user_total_points[user.username] = (this.user_total_points[user.username] ?? 0) + parseInt(jogador.pontos.toString(),10);
                this.equipaService.getEquipaById(jogador.id_equipa).then((equipa: Equipa) => {
                  // console.log('Equipa:', equipa.nome);
                  this.jogador_equipa[jogador.fullname] = equipa;
                });

              });
                
              
            }
            );

            this.sortedUsers = Object.keys(this.user_total_points).sort(
              (a: string, b: string) => this.user_total_points[b] - this.user_total_points[a]
            );
            
            if (fantasyTeam.user in this.user_fanta) {
              this.user_fanta[user.username].push(fantasyTeam);
            }
            else {
              this.user_fanta[user.username] = [fantasyTeam];
            }
            


          });

          
      });
     
    }) 
   
  };

  }
}