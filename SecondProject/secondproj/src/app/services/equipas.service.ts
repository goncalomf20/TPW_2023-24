import { Injectable } from '@angular/core';
import { Equipa } from '../models/equipa';

@Injectable({
  providedIn: 'root'
})
export class EquipasService {

  private url: string = "http://127.0.0.1:8000/ws/"
  constructor() {}
  

  async getEquipas(): Promise<any> {
    const url = this.url + "equipa/get"
    const response = await fetch(url)
    const equipas = await response.json()
    return equipas
    } 

  async getEquipaById(id : number): Promise<Equipa> {
    const url = this.url + "equipa/get/" + id
    const response = await fetch(url)
    const equipa = await response.json()
    return equipa
    }

  
  }

