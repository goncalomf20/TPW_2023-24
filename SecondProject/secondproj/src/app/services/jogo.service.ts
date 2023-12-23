import { Injectable } from '@angular/core';
import { Jogo } from '../models/jogo';

@Injectable({
  providedIn: 'root'
})
export class JogoService {
  private url: string = "http://127.0.0.1:8000/ws/"

  constructor() { }

      async getJogoByEquipaCasa(id:number): Promise<Jogo[]> {
        const url1 = this.url + "jogo/get/equipa_casa/" + id
        const response: Response = await fetch(url1)
        return await response.json() ?? []
        }
        
      async getJogoByEquipaFora(id:number): Promise<Jogo[]> {
          const url2 = this.url + "jogo/get/equipa_fora/" + id
          const response: Response = await fetch(url2)
          return await response.json() ?? []          
        }
}
