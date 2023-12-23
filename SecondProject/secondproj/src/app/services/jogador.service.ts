import { Injectable } from '@angular/core';
import { Jogador } from '../models/jogador';
import { Evento } from '../models/evento'

@Injectable({
  providedIn: 'root'
})
export class JogadorService {

  private url: string = "http://127.0.0.1:8000/ws/"

  constructor() { }

      async getJogadores(): Promise<Jogador[]> {
        const url = this.url + "jogador/get"
        const response: Response = await fetch(url)
        return await response.json() ?? []
        }

    async getJogadoresByModalID(id:number): Promise<Jogador[]> {
        const url = this.url + "jogador/get/byModalidade/" + id
        const response: Response = await fetch(url)
        return await response.json() ?? []
        } 

    async getJogadoresByLigaID(id:number): Promise<Jogador[]> {
        const url = this.url + "jogador/get/jogadorByLiga/" + id
        const response: Response = await fetch(url)
        return await response.json() ?? []
        }

    async getEventosByJogadorID(id:number): Promise<Evento[]> {
      const url = this.url + "evento/get/jogador" + id
      const response: Response = await fetch(url)
      return await response.json() ?? []
    }

    async getJogadoresById(id : number): Promise<Jogador> {
      const url = this.url + "jogador/get/" + id
      const response: Response = await fetch(url)
      return await response.json() ?? []
      }
      
    async getJogadoresByModalidade(id_modalidade : number): Promise<Jogador[]> {
      const url = this.url + "jogador/jogadorByModalidade/" + id_modalidade
      const response: Response = await fetch(url)
      return await response.json() ?? []
      } 

  // async addUser(proto: Partial<{ username: string | null; password: string | null; fname: string | null; lname: string | null; email: string | null; }>): Promise<Users> {
  //   const z = this.url + "user/post"
  //   let user: Users = {
  //     id: 0, // You can set a default value or generate a unique id
  //     username: proto.username ?? "",
  //     FirstName: proto.fname ?? "",
  //     LastName: proto.lname ?? "",
  //     password: proto.password ?? "",
  //     email: proto.email ?? "",
  //     role: 'user', // You can set a default value or generate a role based on your requirements
  //     token: '' // The token will be set after the user is created
  //   };
    
  //   const response: Response = await fetch(z, {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "application/json"
  //     },
  //     body: JSON.stringify(user)
  //   })
  //   return await response.json()
  // }
}

