import { CommonModule } from '@angular/common';
import { Component, OnInit, inject } from '@angular/core';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { FantasyTeam } from '../../models/fantasy';
import { Jogador } from '../../models/jogador';
import { Liga } from '../../models/liga';
import { Modalidade } from '../../models/modalidade';
import { Users } from '../../models/users';
import { FantastyService } from '../../services/fantasy.service';
import { JogadorService } from "../../services/jogador.service";
import { LigaService } from '../../services/liga.service';
import { ModalidadesService } from '../../services/modalidades.service';
import { UsersService } from '../../services/users.service';
import { FooterComponent } from '../footer/footer.component';
import { NavbarComponent } from '../navbar/navbar.component';


@Component({
  selector: 'app-fantasy',
  standalone: true,
  imports: [RouterModule,
  FooterComponent,
  NavbarComponent,
  CommonModule,
  ReactiveFormsModule,
  FormsModule
  ],
  templateUrl: './fantasy.component.html',
  styles: ['./fantasy.component.css',   "node_modules/bootstrap/dist/css/bootstrap.min.css"],
  
})
export class FantasyComponent implements OnInit {
  jogadores: Jogador[] = [];
  jogService : JogadorService = inject(JogadorService)
  jogador: any;


  modService: ModalidadesService = inject(ModalidadesService)

  fantasyService : FantastyService = inject(FantastyService);

  usersService: UsersService = inject(UsersService);

  ligaService : LigaService = inject(LigaService)

  modalidades : Modalidade[] = [];

  modalidadePlayers: { [modalidade: string]: Jogador[] } = {};

  modalidadeLiga : {[modalidade:string]: Liga[]} = {};

  selectedModalidade : string = "";

  selected_fantasy : FantasyTeam | null = null;

  nr_players_select : number = 0;

  teamButtonIndices: number[] = Array.from({ length: this.nr_players_select }, (_, index) => index);

  user: Users | undefined;

  users_Fantasies_modality :  { [modalidade: string]: FantasyTeam } = {};

  selectedModality_ligas : Liga[] |  undefined

  formGroup = new FormGroup({
    teamName: new FormControl('', [Validators.required])
  })

  team_capi : Jogador | undefined;

  total_team_price : number = 0;

  constructor(private userService: UsersService, private router: Router) {  


  }

  ngOnInit() {
    // this.selectedModalidade = "Football";
    // this.changeModalidade("Football");
    this.modService.getModal().then( (modalidade: Modalidade[]) => {
      this.modalidades = modalidade;
      
      const promises = this.modalidades.map((element) => {
        return this.jogService.getJogadoresByModalidade(element.id).then((j: Jogador[]) => {
          this.modalidadePlayers[element.nome] = j;
        });
      });
      
      Promise.all(promises).then(() => {
        this.selectedModalidade = this.modalidades[0].nome.toString();
        this.nr_players_select = this.modalidades[0].nr_jogadores;
        
        this.jogadores = this.modalidadePlayers[this.selectedModalidade];

        this.userService.userName$.subscribe((userName:any) => {
          console.log(userName + " --")
          this.usersService.getUsersByName(userName).then( (us: Users) => {
            this.user = us;
            if (this.user && this.user.id !== undefined) {
              this.fantasyService.getFantasiesByUser(this.user.id).then((fanta: FantasyTeam[]) => {
                
                console.log("fantas", fanta)
                fanta.forEach(team => {
                  this.modalidades.forEach(mod => {
                    if (mod.id == team.modalidade) {
                      this.users_Fantasies_modality[mod.nome] = team;
                    }
                  }
                  );
    
                });
                console.log("fantas", this.users_Fantasies_modality);
    
                Object.keys(this.users_Fantasies_modality).forEach((key) => {
                  console.log(key + " --");
                  const value = this.users_Fantasies_modality[key];
                  console.log(value.id + " "+ value.team_name+ "  " + value.user + " " + value.players+" --value");
                  
    
                  this.modalidades.forEach(mod => {
                    if (mod.id == value.modalidade) {
                      console.log(mod.nome + " --escolhido");
                      this.selected_fantasy = value;
                      console.log(value + " --players");

                      if (value.players.length == 0) {
                        this.teamButtonIndices = Array.from({ length: this.nr_players_select }, (_, index) => 0);
                      } else {
                        this.teamButtonIndices = value.players;
                      }

                      // this.teamButtonIndices = value.players;
    
                      this.team_capi = undefined;
                      const nome = String(value.capitan);
                      console.log(this.jogadores + " --jogadores");
                      const jogadorCapitan = this.jogadores.find(jog => jog.fullname === nome);
                      console.log(jogadorCapitan + " --capitan");

                      this.team_capi = jogadorCapitan ?? undefined;
                      console.log(this.team_capi + " --capitan1");

                      this.jogadores.forEach(jog => {
                        if (this.teamButtonIndices.includes(jog.id)) {
                          console.log(jog.id + " --jogador");
                          console.log(this.total_team_price + " --total");
                          const valorAsInt = parseInt(jog.valor.toString(), 10);

                          this.total_team_price += valorAsInt;
                        }
                      });
                    }
                  }
                  );
    
            
                });
    
    
              });
    
              this.ligaService.getLigas().then((ligas : Liga[])=> {
                for (let index = 0; index < ligas.length; index++) {
                  const element = ligas[index];
                  const mod_liga = element.modalidade;
                  this.modalidades.forEach(e => {
                      if (e.id == mod_liga) {
                        if (e.nome in this.modalidadeLiga) {
                          this.modalidadeLiga[e.nome].push(element);
                        } else {
                          this.modalidadeLiga[e.nome] = [element];
                        }
                      }
                  });
    
                }
              });
    
    
            } else {
            }
          })
        });
      
      });

      
    });
    // console.log(this.jogadores + " asdadas");
    




  }

  changeModalidade(modalidade: string) {

      if (this.users_Fantasies_modality && this.users_Fantasies_modality[modalidade]) {
        this.selected_fantasy = this.users_Fantasies_modality[modalidade];
        console.log(this.users_Fantasies_modality[modalidade])
        this.modalidades.forEach(mod => {
          // console.log(mod.nr_jogadores, modalidade, mod.nome)
          if(mod.id == this.selected_fantasy?.modalidade) {
            
            this.nr_players_select = mod.nr_jogadores;
          }
        }
        );
        console.log(this.nr_players_select, this.selected_fantasy?.players)
        // this.teamButtonIndices = Array.from({ length: this.nr_players_select }, (_, index) => 0);
        
        if (this.selected_fantasy.players.length == 0) {
          this.teamButtonIndices = Array.from({ length: this.nr_players_select }, (_, index) => 0);
        } else {
          this.teamButtonIndices = this.selected_fantasy.players;
        }

        
      }

      this.selectedModalidade = modalidade;
   
      this.jogadores = this.modalidadePlayers[modalidade];
      
      console.log(this.selected_fantasy?.capitan)
      this.team_capi = undefined;
      const nome = String(this.selected_fantasy?.capitan);
      const jogadorCapitan = this.jogadores.find(jog => jog.fullname === nome);
      this.team_capi = jogadorCapitan ?? undefined;

      this.total_team_price = 0;
      this.jogadores.forEach(jog => {
        if (this.teamButtonIndices.includes(jog.id)) {
          this.total_team_price += parseInt(jog.valor.toString(), 10);
        }
      }
      );

      console.log(this.team_capi)
      

      

  }

  createFantasyTeam() {

    const teamName = this.formGroup.get('teamName')?.value;
    let mod_id = 0;

    this.modalidades.forEach(mod => {
      if(mod.nome == this.selectedModalidade) {
        mod_id = mod.id;
      }
    });


    this.fantasyService.addFantasyTeam({user: this.user?.id, modalidade: mod_id, team_name: teamName}).then((fantasy: FantasyTeam) => {
      // console.log(fantasy);
      this.selected_fantasy = fantasy;
      alert("Fantasy Team created successfully!");
      window.location.reload();
    }
    );
  }

  deleteFantasyTeam(fantasyTeamId: number | undefined): void {
    if (fantasyTeamId) {
      this.fantasyService.deleteFantasyTeam(fantasyTeamId)
        .then(() => {
          alert("Fantasy Team deleted successfully!");
          window.location.reload();
        })
        .catch((error) => {
          console.error('Error deleting fantasy team:', error);
        });
    } else {
      console.error('Invalid fantasy team ID. Cannot delete the fantasy team.');
    }
  }

  add_to_team(jogador: Jogador) {
    if (this.selected_fantasy) {
      // console.log(jogador.id, this.selected_fantasy.id) 
      if (this.teamButtonIndices.includes(jogador.id)) {
        alert("Jogador already in team!");
        return;
      }


      if (!this.teamButtonIndices.includes(0)) {
        alert("Team is full!");
        return;
      }


      if (this.total_team_price + parseInt(jogador.valor.toString(),10) > 300000000) {
        alert("Team price is too high!");
        return;
      }

      this.total_team_price += parseInt(jogador.valor.toString(),10);

      let first = true;
   
      for (let index = 0; index < this.teamButtonIndices.length; index++) {
        const element = this.teamButtonIndices[index];
        // console.log(element, first)
        
        if (element == 0){
          this.teamButtonIndices[index] = jogador.id;
          break;
        }
      }

      let novos_jogadores: number[] = [];

      let uniquePlayerIds = new Set<number>();
      
      this.jogadores.forEach(jog => {
        if (this.teamButtonIndices.includes(jog.id) && !uniquePlayerIds.has(jog.id)) {
          novos_jogadores.push(jog.id);
          uniquePlayerIds.add(jog.id);
        }
      });

      this.selected_fantasy.players = novos_jogadores;

      // console.log(this.teamButtonIndices, this.selected_fantasy.players)

      // console.log(this.selected_fantasy)

    
    }
  }

  remove_from_team(jogador: Jogador) {

    const valorAsInt = parseInt(jogador.valor.toString(), 10);

    this.total_team_price -= valorAsInt;
    for (let index = 0; index < this.teamButtonIndices.length; index++) {
      const element = this.teamButtonIndices[index];
      if (element == jogador.id){
        this.teamButtonIndices[index] = 0;
        break;
      }
    }
  }

  getJogadorById(id: number): Jogador | undefined {
    return this.jogadores.find(j => j.id === id);
  }
  
  shouldShowUpdateButton(): boolean {
    
    for (let index = 0; index < this.teamButtonIndices.length; index++) {
      const element = this.teamButtonIndices[index];

      if (element == 0){
        return false;
      }
      
    }
    return true;
  }

  updateTeam()  {
    console.log(this.selected_fantasy?.id, this.selected_fantasy?.players , this.selected_fantasy?.capitan?.fullname);
    if (this.selected_fantasy?.capitan?.id == undefined) {
      alert("Please select a capitan!");
      return;
    }
    
    this.fantasyService.updateFantasyTeam(this.selected_fantasy?.id ?? 0, this.selected_fantasy).then((fantasy: FantasyTeam) => {
      console.log(fantasy);
      this.selected_fantasy = fantasy;
      alert("Fantasy Team updated successfully!");
      // window.location.reload();
    });
  }

  select_a_capiton(jogador: Jogador) {
    this.team_capi = jogador ?? undefined; 

    if (this.selected_fantasy) {
      this.selected_fantasy.capitan = jogador;
    }
  }

  remove_capiton() {
    this.team_capi = undefined;
    if (this.selected_fantasy) {
      this.selected_fantasy.capitan = null;
    }
  }

  navigateToComponent(component: string) {
    console.log(component);
    this.router.navigateByUrl('/all/'+component);
   }
}
