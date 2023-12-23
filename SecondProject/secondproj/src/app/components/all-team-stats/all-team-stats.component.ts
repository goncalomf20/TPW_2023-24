import { Component, Input, OnInit } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';
import { RouterModule } from '@angular/router';
import { GetModalIdService } from '../../services/shared/get-modal-id.service';
import { CommonModule } from '@angular/common';
import { LigaIDService } from '../../services/shared/liga-id.service';
import { EquipasService } from '../../services/equipas.service';
import { Equipa } from '../../models/equipa';
import { TCardComponent } from '../t-card/t-card.component';

@Component({
  selector: 'app-all-team-stats',
  standalone: true,
  imports: [RouterModule,FooterComponent,NavbarComponent, TCardComponent,CommonModule],
  templateUrl: './all-team-stats.component.html',
  styleUrl: './all-team-stats.component.css'
})
export class AllTeamStatsComponent implements OnInit{
    equipaService: EquipasService
    shared: GetModalIdService
    equipas: Equipa[] = []
    m_id: number
    shared2: LigaIDService
    liga_id: number
  
    constructor(jS:EquipasService,gI:GetModalIdService,sh2:LigaIDService){
      this.equipaService = jS
      this.shared = gI
      this.m_id = this.shared.getId()
      this.shared2 = sh2
      this.liga_id = this.shared2.getId()
    }
    ngOnInit(): void {
      this.equipaService.getEquipasbyLiga(this.liga_id).then((equipas : Equipa[]) => {
        this.equipas = equipas
        console.log(this.equipas)
      })
    }
  
    
  
    
  
  }
