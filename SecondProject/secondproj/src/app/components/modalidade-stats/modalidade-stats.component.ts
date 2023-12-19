import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { FooterComponent } from '../footer/footer.component';
import { NavbarComponent } from '../navbar/navbar.component';
import {  CardModalidadeComponent  } from '../card-modalidade/card-modalidade.component';
import { ModalidadesService } from '../../services/modalidades.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-modalidade-stats',
  standalone: true,
  imports: [RouterModule,
    FooterComponent,
    NavbarComponent,
    CardModalidadeComponent,
    HttpClientModule,
    ],
  templateUrl: './modalidade-stats.component.html',
  styleUrl: './modalidade-stats.component.css'
})
export class ModalidadeStatsComponent {
  constructor(private modalidade: ModalidadesService ) { 
    this.modalidade.getModal().then(modalidades => {
     console.warn(modalidades);
    });


  }
}
