import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GetModalIdService {
  id:number = 0
  constructor() {}
  
  public setId(v : number) {
    this.id = v;
    console.log("SETTOU " + this.id)
  }
  
  public getId() : number {
    console.log("GETTOU " + this.id)
    return this.id
  }
  
  
}
