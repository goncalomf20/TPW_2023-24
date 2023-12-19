import { Injectable, importProvidersFrom } from '@angular/core';
import { Modalidade } from './../models/modalidade'

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
  
  }

