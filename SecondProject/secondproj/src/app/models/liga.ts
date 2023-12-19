import { Data } from "@angular/router";
import { Equipa } from './equipa';
import { Modalidade } from "./modalidade";
export interface Liga{
    id: number,
    nome: string,
    ano: Data,
    fase : string,
    pais : string,
    modalidade : Modalidade,
    equipas : Equipa[]
}   