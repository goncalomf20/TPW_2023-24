import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { FooterComponent } from '../footer/footer.component';
import { NavbarComponent } from '../navbar/navbar.component';
import {  CardPlayerComponent  } from '../card-player/card-player.component';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-statistics',
  standalone: true,
  imports: [RouterModule,
  FooterComponent,
  NavbarComponent,
  CardPlayerComponent,
  HttpClientModule,
  ],
  templateUrl: './statistics.component.html',
  styleUrl: './statistics.component.css'
})
export class StatisticsComponent {

}
