import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { Metric, MetricService } from 'src/app/services/metric.service';
import { Athlete, AthleteService } from 'src/app/services/athlete.service';
import { Video, VideoService } from 'src/app/services/video.service';

@Component({
  selector: 'app-metrics',
  templateUrl: './metrics.component.html',
  styleUrls: ['./metrics.component.scss'],
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class MetricsComponent implements OnInit {
  metrics: Metric[] = [];
  athletes: Athlete[] = [];
  videos: Video[] = [];

  newMetric: Partial<Metric> = {
    athlete_id: undefined,
    video_id: undefined,
    metric_type: '',
    metric_value: 0,
    timestamp:0
  };

  constructor(
    private metricService: MetricService,
    private athleteService: AthleteService,
    private videoService: VideoService
  ) {}

  ngOnInit(): void {
    this.loadData();
  }

  loadData(): void {
    this.metricService.getMetrics().subscribe(data => this.metrics = data);
    this.athleteService.getAthletes().subscribe(data => this.athletes = data);
    this.videoService.getVideos().subscribe(data => this.videos = data);
  }

  addMetric(): void {
    if (
      this.newMetric.athlete_id &&
      this.newMetric.video_id &&
      this.newMetric.metric_type &&
      this.newMetric.metric_value &&
      this.newMetric.timestamp
    ) {
      this.metricService.addMetric(this.newMetric as Metric).subscribe(() => {
        this.loadData();
        this.resetForm();
      });
    }
  }

  resetForm(): void {
    this.newMetric = {
      athlete_id: undefined,
      video_id: undefined,
      metric_type: '',
      metric_value: 0,
      timestamp: 0
    };
  }
}
