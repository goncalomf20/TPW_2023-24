import { Data } from "@angular/router";
export interface Liga{
    id: number,
    nome: string,
    ano: Data,
    fase : string,
    pais : string,
    modalidade : number,
    equipas : number[]
}   