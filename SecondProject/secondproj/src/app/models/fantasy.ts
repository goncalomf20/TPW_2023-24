import { Jogador } from './jogador';
import { Liga } from './liga';
import { Users } from './users';

export interface FantasyTeam{
    id: number,
    user: Users,
    liga: Liga,
    team_name: string,
    players: Jogador[],
    capitan : Jogador
   
}