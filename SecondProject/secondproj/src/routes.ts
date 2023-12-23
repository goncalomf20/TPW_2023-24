import { Routes } from '@angular/router';
import { LoginComponent } from './app/components/login/login.component';
import { AppComponent } from './app/app.component';
import { RegisterComponent } from './app/components/register/register.component';
import { HomeComponent } from './app/components/home/home.component';
import { FantasyComponent } from './app/components/fantasy/fantasy.component';
import { ModalidadeStatsComponent } from './app/components/modalidade-stats/modalidade-stats.component';
import { ExclusiveModalComponent } from './app/components/exclusive-modal/exclusive-modal.component';
import { StandingsComponent } from './app/components/standings/standings.component';
import { AllPlayerStatsComponent } from './app/components/all-player-stats/all-player-stats.component';
import { AllTeamStatsComponent } from './app/components/all-team-stats/all-team-stats.component';
import { AllFantasyTeamsComponent } from './app/components/all-fantasy-teams/all-fantasy-teams.component';

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
    path: 'standings',
    component: StandingsComponent,
    title: "Standings",
    },
    {
    path: 'players',
    component: AllPlayerStatsComponent,
    title: "Players",
    },
    {
    path: 'teams' ,
    component: AllTeamStatsComponent,
    title: "Teams"
    },
    {
    path: 'all/:modalidade',
    component: AllFantasyTeamsComponent, // Add the new component for 'All Fantasy Teams'
    title: 'All Fantasy Teams Page',
    },
    
];

export default routeConfig;
