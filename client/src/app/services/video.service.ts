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
    console.log(this.apiUrl)
    return this.http.get<Video[]>(this.apiUrl);
  }
}
