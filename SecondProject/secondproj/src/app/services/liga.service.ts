import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LigaService {

  private url: string = "http://127.0.0.1:8000/ws/"
  constructor() {}
  

  async getLigas(): Promise<any> {
    const url = this.url + "liga/get"
    const response = await fetch(url)
    const ligas = await response.json()
    return ligas
    } 


  
  }

