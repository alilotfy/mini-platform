import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Metric {
  id: number;
  athlete_id: number;
  video_id: number;
  name: string;
  metric_type: string;
  metric_value: number;
  timestamp: number;
}


@Injectable({
  providedIn: 'root'
})
export class MetricService {
  private apiUrl = 'http://localhost:8000/metrics/';

  constructor(private http: HttpClient) { }

  getMetrics(): Observable<Metric[]> {
    return this.http.get<Metric[]>(this.apiUrl + 'by-athlete-video/');
  }

  addMetric(metric: Metric): Observable<Metric> {

    return this.http.post<Metric>(this.apiUrl, metric);
  }
  getMetricsByAthlete(athleteId: number): Observable<Metric[]> {
    return this.http.get<Metric[]>(this.apiUrl + "?athlete_id=" + athleteId);
  }

  getMetricsByVideo(video_id: number): Observable<Metric[]> {
    return this.http.get<Metric[]>(this.apiUrl + "by-video/" + video_id);
  }
}
