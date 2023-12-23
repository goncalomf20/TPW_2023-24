import { Jogador } from './jogador';

export interface FantasyTeam{
    id: number,
    user: number,
    modalidade: number,
    team_name: string,
    players: number[],
    capitan : Jogador | null,
   
}