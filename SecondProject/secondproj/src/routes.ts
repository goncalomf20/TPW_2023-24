import { Routes } from '@angular/router';
import { LoginComponent } from './app/components/login/login.component';
import { AppComponent } from './app/app.component';
import { RegisterComponent } from './app/components/register/register.component';
import { HomeComponent } from './app/components/home/home.component';
import { FantasyComponent } from './app/components/fantasy/fantasy.component';
import { ProfileComponent } from './app/components/profile/profile.component';
import { ModalidadeStatsComponent } from './app/components/modalidade-stats/modalidade-stats.component';
import { ExclusiveModalComponent } from './app/components/exclusive-modal/exclusive-modal.component';

const routeConfig: Routes = [
   {
    path: '',
    component: HomeComponent,
    title: 'Home Page',
    },
    {
    path: 'login',
    component: LoginComponent,
    title: 'Login Page'
    },
    {
    path: 'register',
    component: RegisterComponent,
    title: 'Register Page'    
    },
    {
    path: 'home',
    component: HomeComponent,
    title: 'Home Page'    
    },
    {
    path: 'fantasy',
    component: FantasyComponent,
    title: 'Fantasy Page',    
    },
    {
    path: 'profile',
    component: ProfileComponent,
    title: 'Profile Page',    
    },
    {
    path: 'statistics',
    component: ModalidadeStatsComponent,
    title: 'Statistics Page',    
    },
    {
    path: 'modal/:id',
    component: ExclusiveModalComponent,
    title: 'Modalidade',    
    },
    
];

export default routeConfig;
