import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ModalidadesService {

  private url: string = "http://127.0.0.1:8000/ws/"

  constructor() { }

  async getModal(): Promise<any> {
    const url = this.url + "modalidade/get"
    const response = await fetch(url)
    const modalidades = await response.json()
    return modalidades
    } 
  
  
}
