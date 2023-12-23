import { Component, OnInit , inject } from '@angular/core';
import { RouterModule } from '@angular/router';
import { Users } from '../../models/users';
import { UsersService } from '../../services/users.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [RouterModule,CommonModule],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})

export class NavbarComponent{
users: Users[] = []
tkn: string | null = localStorage.getItem('token') 
usersService: UsersService = inject(UsersService)
auth: boolean = false
username: string = ""

logout(){
  localStorage.removeItem('token')
  window.location.replace("http://localhost:4200/")
}

constructor(){
  this.usersService.getUsers().then((users : Users[]) => {
    this.users = users
    console.log(this.users)
    const user = this.users.find(user => user.token === "" + this.tkn);
    console.log(user)
    if (user) {
      this.username = user.username
      this.usersService.setUserName(user.username);
      this.auth = true;
    } else {
     console.error('Invalid token or unexistent token');
    }
   })
  }

} 


