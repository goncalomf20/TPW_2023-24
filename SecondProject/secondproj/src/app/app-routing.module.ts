import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FantasyComponent } from './components/fantasy/fantasy.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';

const routes: Routes = [

  // { path: '', redirectTo: '/home', pathMatch: 'full' }, 

  { path: '/', component: HomeComponent},

  { path: '/login', component: LoginComponent },

  { path: '/register', component: HomeComponent},

  { path: '/home', component: HomeComponent},
  
  { path : '/fantasy', component: FantasyComponent},


];

@NgModule({
  declarations: [],
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }