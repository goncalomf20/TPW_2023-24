import { Component, OnInit, inject } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';
import { RouterModule } from '@angular/router';
import { Users } from '../../models/users';
import { UsersService } from '../../services/users.service';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [NavbarComponent,FooterComponent,RouterModule,ReactiveFormsModule,FormsModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {

  usersService: UsersService = inject(UsersService)
  formGroup = new FormGroup({
    username : new FormControl('',[Validators.required]),
    password : new FormControl('',[Validators.required]),
    fname : new FormControl('',[Validators.required]),
    lname : new FormControl('',[Validators.required]),
    email : new FormControl('',[Validators.required]),
  })
  
  

  constructor(){} 
  
  onSubmit() {
    this.usersService.addUser(this.formGroup.value).then((createdUser : Users) => {
      localStorage.setItem('token', createdUser.token);
      window.location.replace("http://localhost:4200/")
    });
   }

  ngOnInit(){
    this.formGroup = new FormGroup({
      username : new FormControl('',[Validators.required]),
      password : new FormControl('',[Validators.required]),
      fname : new FormControl('',[Validators.required]),
      lname : new FormControl('',[Validators.required]),
      email : new FormControl('',[Validators.required]),
    })
  }
}
