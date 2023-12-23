import { Injectable } from '@angular/core';
import { Liga } from "../models/liga"
import { Data } from "@angular/router";
import { Equipa } from '../models/equipa';

@Injectable({
  providedIn: 'root'
})
export class LigaService {

  private url: string = "http://127.0.0.1:8000/ws/"


  constructor() { 
    
  }
  

  async getLigasFutebol(): Promise<any> {
    const url = this.url + "liga/ligaByModalidade/3"
    const response = await fetch(url)
    const ligas = await response.json()
    return ligas
    } 

  async getLigasBasket(): Promise<any> {
      const url = this.url + "liga/ligaByModalidade/4"
      const response = await fetch(url)
      const ligas = await response.json()
      return ligas
  }
  
  async getLigas(): Promise<any> {
    const url = this.url + "liga/get"
    const response = await fetch(url)
    const ligas = await response.json()
    return ligas
    }  
  
}
