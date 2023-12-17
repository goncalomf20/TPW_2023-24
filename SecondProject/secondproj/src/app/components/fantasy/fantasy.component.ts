import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { FooterComponent } from '../footer/footer.component';
import { NavbarComponent } from '../navbar/navbar.component';

@Component({
  selector: 'app-fantasy',
  standalone: true,
  imports: [RouterModule,
  FooterComponent,
  NavbarComponent,
  ],
  templateUrl: './fantasy.component.html',
  styleUrl: './fantasy.component.css'
})
export class FantasyComponent {

}
