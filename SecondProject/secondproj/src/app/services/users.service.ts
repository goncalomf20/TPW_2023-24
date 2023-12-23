import { Injectable, importProvidersFrom } from '@angular/core';
import { Users } from './../models/users'
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  private userNameSubject = new BehaviorSubject<string | null>(null);
  private url: string = "http://127.0.0.1:8000/ws/"

  constructor() { }

  async getUsers(): Promise<Users[]> {
    const url = this.url + "user/get"
    const response: Response = await fetch(url)
    return await response.json() ?? []
    } 

  async getUsersByName(name : string): Promise<Users> {
      const url = this.url + "user/getByName/" + name
      const response: Response = await fetch(url)
      return await response.json() ?? []
      } 
  
  async getUsersById(id : number): Promise<Users> {
      const url = this.url + "user/get/" + id
      const response: Response = await fetch(url)
      return await response.json() ?? []
      }

  get userName$() {
        return this.userNameSubject.asObservable();
      }
    
  setUserName(userName: string) {
        this.userNameSubject.next(userName);
      }

  async addUser(proto: Partial<{ username: string | null; password: string | null; fname: string | null; lname: string | null; email: string | null; }>): Promise<Users> {
    const z = this.url + "user/post"
    let user: Users = {
      id: 0, // You can set a default value or generate a unique id
      username: proto.username ?? "",
      FirstName: proto.fname ?? "",
      LastName: proto.lname ?? "",
      password: proto.password ?? "",
      email: proto.email ?? "",
      role: 'user', // You can set a default value or generate a role based on your requirements
      token: '' // The token will be set after the user is created
    };
    
    const response: Response = await fetch(z, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(user)
    })
    return await response.json()
  }
}

