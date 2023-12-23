import { Component, OnInit } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';
import { Classificacao } from '../../models/classificacao';
import { ClassificacaoService } from '../../services/classificacao.service';
import { JogadorService } from '../../services/jogador.service';
import { GetModalIdService } from '../../services/shared/get-modal-id.service';
import { LigaIDService } from '../../services/shared/liga-id.service';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { EquipasService } from '../../services/equipas.service';
import { Equipa } from '../../models/equipa';

@Component({
  selector: 'app-standings',
  standalone: true,
  imports: [NavbarComponent,FooterComponent,CommonModule,RouterLink],
  templateUrl: './standings.component.html',
  styleUrl: './standings.component.css'
})
export class StandingsComponent implements OnInit{
  shared: GetModalIdService;
  m_id: number;
  shared2: LigaIDService;
  liga_id: number;
  classService: ClassificacaoService;
  class: Classificacao[] = [];
  equipaService: EquipasService;
  equipas:Equipa[] = []
  names_to_id: Map<number, string> = new Map();


  constructor(gI:GetModalIdService,sh2:LigaIDService,cL:ClassificacaoService,eS:EquipasService){
    this.shared = gI
    this.m_id = this.shared.getId()
    this.shared2 = sh2
    this.liga_id = this.shared2.getId()
    this.classService = cL
    this.equipaService = eS
    
  }
  ngOnInit(): void {

      this.classService.getClassificacaoByLiga(this.liga_id).then((cl: Classificacao[]) => {
        this.class = cl.slice().sort((a, b) => (b.nrPontos) - (a.nrPontos));
        for (let index = 0; index < cl.length; index++) {
          const element = cl[index];
          this.equipaService.getEquipaById(element.equipa).then((equipa: Equipa) =>{
            this.names_to_id.set(element.equipa,equipa.nome)
          }) 
          
        }
      });
  }



}



  


