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
  private apiUrl = 'http://localhost:8000/metrics/by-athlete-video/';

  constructor(private http: HttpClient) { }

  getMetrics(): Observable<Metric[]> {
    return this.http.get<Metric[]>(this.apiUrl);
  }

  addMetric(metric: Metric): Observable<Metric> {

    return this.http.post<Metric>("http://localhost:8000/metrics/", metric);
  }
  getMetricsByAthlete(athleteId: number): Observable<Metric[]> {
    return this.http.get<Metric[]>(this.apiUrl+"?athlete_id="+athleteId);
  }
}
