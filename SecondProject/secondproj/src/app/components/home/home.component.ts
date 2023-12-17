import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NavbarMainComponent } from '../navbar-main/navbar-main.component';
import { FooterComponent } from '../footer/footer.component';
import { AboutComponent } from '../about/about.component';
import { ContactComponent } from '../contact/contact.component';
import { FeedbackComponent } from '../feedback/feedback.component';
import { PortfolioComponent } from '../portfolio/portfolio.component';
import { BlogComponent } from '../blog/blog.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [NavbarMainComponent,
    RouterModule,
    FooterComponent,
    AboutComponent,
    ContactComponent,
    FeedbackComponent,
    PortfolioComponent,
    BlogComponent,
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

}
