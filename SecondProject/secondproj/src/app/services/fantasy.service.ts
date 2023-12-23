import { Injectable } from '@angular/core';
import { FantasyTeam } from '../models/fantasy';

@Injectable({
  providedIn: 'root'
})
export class FantastyService {


  private url: string = "http://127.0.0.1:8000/ws/"

  constructor() { }

  async getFantasies(): Promise<FantasyTeam[]> {
    const url = this.url + "fantasyteam/get"
    const response: Response = await fetch(url)
    return await response.json() ?? []
    } 


  async getFantasiesByUser(id_user : number): Promise<FantasyTeam[]> {
    const url = this.url + "fantasyteam/getByuser/" + id_user
    const response: Response = await fetch(url)
    return await response.json() ?? []
    } 

  async getFantasiesByModalidade(modalidade : string): Promise<FantasyTeam[]> {
    const url = this.url + "fantasyteam/fantaByModalidade/" + modalidade
    const response: Response = await fetch(url)
    return await response.json() ?? []
    }


    async addFantasyTeam(proto: Partial<{ user: number | null; modalidade: number | null; team_name: string | null; }>): Promise<FantasyTeam> {
      const url = this.url + "fantasyteam/post";
    
      let fantasyTeam = {
        user: proto.user ?? 0, // Set a default user value or handle it based on your requirements
        modalidade: proto.modalidade ?? 0, // Set a default modalidade value or handle it based on your requirements
        team_name: proto.team_name ?? ""
      };
    
      const response: Response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(fantasyTeam)
      });
    
      return await response.json();
    }

    async deleteFantasyTeam(id: number): Promise<void> {
      const url = this.url + `fantasyteam/delete/${id}`;
    
      const response: Response = await fetch(url, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json"
        },
      });
    
      if (!response.ok) {
        throw new Error(`Failed to delete fantasy team with ID ${id}`);
      }
    }

    async updateFantasyTeam(id: number, updates: Partial<FantasyTeam>): Promise<FantasyTeam> {
      const url = this.url + `fantasyteam/update/${id}`;
      
      console.log("service" + updates);

      let players_array: number[] =  [];

      updates.players?.forEach(element => {
        players_array.push(element);
      }
      );
      console.log(players_array)

      
      let fantasyTeam = {
        user: updates.user ?? 0, 
        modalidade: updates.modalidade ?? 0, 
        team_name: updates.team_name ?? "",
        players: players_array,
        capitan: updates.capitan?.fullname ?? ""
      };

      const response: Response = await fetch(url, {
        method: "PUT",  // Use PUT for update
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(fantasyTeam),
      });
  
      return await response.json();
    }
    
}

