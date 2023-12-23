import { Routes } from '@angular/router';
import { AllFantasyTeamsComponent } from './app/components/all-fantasy-teams/all-fantasy-teams.component';
import { ExclusiveModalComponent } from './app/components/exclusive-modal/exclusive-modal.component';
import { FantasyComponent } from './app/components/fantasy/fantasy.component';
import { HomeComponent } from './app/components/home/home.component';
import { LoginComponent } from './app/components/login/login.component';
import { ModalidadeStatsComponent } from './app/components/modalidade-stats/modalidade-stats.component';
import { ProfileComponent } from './app/components/profile/profile.component';
import { RegisterComponent } from './app/components/register/register.component';

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
    {
    path: 'all/:modalidade',
    component: AllFantasyTeamsComponent, // Add the new component for 'All Fantasy Teams'
    title: 'All Fantasy Teams Page',
    },
    
];

export default routeConfig;
