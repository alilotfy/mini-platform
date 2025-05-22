import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AthleteService, Athlete } from 'src/app/services/athlete.service';
import { MetricService, Metric } from 'src/app/services/metric.service';
import { VideoService, Video } from 'src/app/services/video.service';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-video',
  templateUrl: './video.component.html',
  styleUrls: ['./video.component.scss'],
  imports: [FormsModule, CommonModule, ReactiveFormsModule]
})
export class VideoComponent implements OnInit {
  videoId!: number;
  video!: Video;
  metrics: Metric[] = [];
  athletes: Athlete[] = [];
  allAthletes: Athlete[] = [];

  metricForm!: FormGroup;
  tagForm!: FormGroup;

  constructor(
    private route: ActivatedRoute,
    private athleteService: AthleteService,
    private metricService: MetricService,
    private videoService: VideoService,
    private fb: FormBuilder
  ) {}

  ngOnInit(): void {
    this.videoId = Number(this.route.snapshot.paramMap.get('id'));
    this.loadVideo();
    this.loadMetrics();
    this.loadTaggedAthletes();
    this.loadAllAthletes();

    this.metricForm = this.fb.group({
      athlete_id: 0,
      metric_type: [''],
      metric_value: 0,
      timestamp: 0
    });

    this.tagForm = this.fb.group({
      athlete_id: ['']
    });
  }

  loadVideo() {
    this.videoService.getVideoById( this.videoId).subscribe(data => {
      this.video = data;
    });
  }

  loadMetrics() {
    this.metricService.getMetricsByVideo(this.videoId).subscribe(data => {
      this.metrics = data;
    });
  }

  loadTaggedAthletes() {
    this.athleteService.getAthletesInVideo(this.videoId).subscribe(data => {
      this.athletes = data;
    });
  }

  loadAllAthletes() {
    this.athleteService.getAthletes().subscribe(data => {
      this.allAthletes = data;
    });
  }

  submitMetric() {
    const metric = {
      ...this.metricForm.value,
      video_id: this.videoId
    };
    this.metricService.addMetric(metric).subscribe(() => this.loadMetrics());
  }

  submitTag() {
    const tag = {
      athlete_id: this.tagForm.value.athlete_id,
      video_id: this.videoId
    };
    this.videoService.tagAthlete(tag).subscribe(() => this.loadTaggedAthletes());
  }
}
