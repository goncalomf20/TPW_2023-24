import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LigaIDService {

  id:number = 0
  constructor() { }

  setId(id:number){
    this.id = id
  }


  getId(){
    return this.id
  }
}
