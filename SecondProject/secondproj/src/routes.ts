import { Routes } from '@angular/router';
import { LoginComponent } from './app/components/login/login.component';
import { AppComponent } from './app/app.component';

const routeConfig: Routes = [
   {
    path: '',
    component: AppComponent,
    title: 'HomePage'
    },
    {
    path: 'login',
    component: LoginComponent,
    title: 'Login Page'
    }
    
];

export default routeConfig;
