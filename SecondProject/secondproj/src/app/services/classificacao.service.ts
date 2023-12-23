import { Injectable } from '@angular/core';
import { Classificacao } from '../models/classificacao';

@Injectable({
  providedIn: 'root'
})
export class ClassificacaoService {

  private url: string = "http://127.0.0.1:8000/ws/"

  constructor() { }

  async getClassificacaoByLiga(id:number): Promise<Classificacao[]> {
    const url = this.url + "classificacao/get/liga/" + id
    const response: Response = await fetch(url)
    return await response.json() ?? []
    } 

}
