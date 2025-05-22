import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Video {
  id: number;
  path: string;
  status: string;
  filename: string;
}

@Injectable({
  providedIn: 'root'
})
export class VideoService {
  private apiUrl = 'http://localhost:8000/videos/';

  constructor(private http: HttpClient) {}

  getVideos(): Observable<Video[]> {
    return this.http.get<Video[]>(this.apiUrl);
  }

  UploadVideo(formData: FormData): Observable<Video> {
    return this.http.post<Video>(this.apiUrl+'upload', formData);
  }

  getVideosByAthlete(athlete_id :number): Observable<Video[]> {
    return this.http.get<Video[]>(this.apiUrl+"by-athlete/"+athlete_id) ;
  }
}
