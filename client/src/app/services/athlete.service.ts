import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Athlete {
  id: number;
  name: string;
  sport: string;
  age: number;
}

@Injectable({
  providedIn: 'root'
})
export class AthleteService {
  private apiUrl = 'http://localhost:8000/athletes/';
  constructor(private http: HttpClient) { }

  getAthletes(): Observable<Athlete[]> {
    return this.http.get<Athlete[]>(this.apiUrl);
  }

  getAthlete(id: number): Observable<Athlete> {
    return this.http.get<Athlete>(this.apiUrl + id);
  }

  getAthletePerformanceSummary(id: number): Observable<{ [key: string]: number } > {
    return this.http.get<{ [key: string]: number } >(this.apiUrl + id+'/performance-summary');
  }

  addAthlete(athlete: Athlete): Observable<Athlete> {
    return this.http.post<Athlete>(this.apiUrl, athlete);
  }

  getAthletesInVideo(video_id: number): Observable<Athlete[]> {
    return this.http.get<Athlete[]>(this.apiUrl + "by-video/" + video_id);
  }
}
