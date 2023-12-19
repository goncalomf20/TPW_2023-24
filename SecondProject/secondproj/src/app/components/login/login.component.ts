import { Component, OnInit, inject } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';
import { RouterModule } from '@angular/router';
import { Users } from '../../models/users';
import { UsersService } from '../../services/users.service';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [NavbarComponent,FooterComponent,RouterModule,ReactiveFormsModule,FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit{
users: Users[] = []
usersService: UsersService = inject(UsersService)
formGroup = new FormGroup({
  username : new FormControl('',[Validators.required]),
  password : new FormControl('',[Validators.required])
})


constructor(){
  this.usersService.getUsers().then((users : Users[]) => {
    this.users = users
    console.log(this.formGroup)
  })
} 

onSubmit() {
  console.log("" + this.formGroup.value.username)
  const user = this.users.find(user => user.username === "" + this.formGroup.value.username && user.password === "" + this.formGroup.value.password);
  console.log(user)
  if (user) {
   localStorage.setItem('token', user.token);
   window.location.replace("http://localhost:4200/")
    
  } else {
   // If there's no user with the same username and password, log an error message
   console.error('Invalid username or password');
  }
 }
ngOnInit(){
  this.formGroup = new FormGroup({
    username : new FormControl('',[Validators.required]),
    password : new FormControl('',[Validators.required])
  })
}

}

