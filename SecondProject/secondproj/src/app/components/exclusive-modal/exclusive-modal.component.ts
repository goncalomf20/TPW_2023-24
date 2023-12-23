import { Component, Input, inject } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';
import { CardPlayerComponent } from '../card-player/card-player.component';
import { Liga } from "../../models/liga"
import { LigaService } from '../../services/liga.service';
import { CommonModule } from '@angular/common';
import { GetModalIdService } from '../../services/shared/get-modal-id.service';
import { LigaIDService } from '../../services/shared/liga-id.service';

@Component({
  selector: 'app-exclusive-modal',
  standalone: true,
  imports: [RouterModule,NavbarComponent,FooterComponent,CardPlayerComponent,CommonModule],
  templateUrl: './exclusive-modal.component.html',
  styleUrl: './exclusive-modal.component.css'
})
export class ExclusiveModalComponent {
  ligas: Liga[] = [];
  jogService : LigaService = inject(LigaService)
  shared:GetModalIdService
  id: number | undefined 
  
  constructor(shared:GetModalIdService) {
    this.shared = shared
    this.id = this.shared.getId()
    if (this.id == 3 ) {
      this.jogService.getLigasFutebol().then((ligas: Liga[]) => {
        this.ligas.push(...ligas);
        console.log(this.ligas);
    });
  }
    
    if (this.id == 4) {
      this.jogService.getLigasBasket().then((ligas: Liga[]) => {
        this.ligas.push(...ligas);
        console.log(this.ligas);
    });
  }
    }


  }
