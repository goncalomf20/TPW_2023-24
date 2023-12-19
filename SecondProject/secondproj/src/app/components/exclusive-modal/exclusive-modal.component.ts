import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';

@Component({
  selector: 'app-exclusive-modal',
  standalone: true,
  imports: [RouterModule,NavbarComponent,FooterComponent],
  templateUrl: './exclusive-modal.component.html',
  styleUrl: './exclusive-modal.component.css'
})
export class ExclusiveModalComponent {

}
