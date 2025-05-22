import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Athlete, AthleteService } from 'src/app/services/athlete.service';
import { Metric, MetricService } from 'src/app/services/metric.service';
import { Video, VideoService } from 'src/app/services/video.service';

@Component({
    selector: 'app-athlete',
    templateUrl: './athlete.component.html',
    styleUrls: ['./athlete.component.scss'],
    imports: [CommonModule]
})
export class AthleteComponent implements OnInit {
    athlete?: Athlete;
    metrics: Metric[] = [];
    videos: Video[] = [];
    summary: { [key: string]: number } = {};

    athleteId!: number;

    constructor(
        private route: ActivatedRoute,
        private athleteService: AthleteService,
        private metricService: MetricService,
        private athleteVideoService: VideoService
    ) { }

    ngOnInit(): void {
        this.athleteId = Number(this.route.snapshot.paramMap.get('id'));
        this.loadAthleteData();
    }

    loadAthleteData() {
        this.athleteService.getAthlete(this.athleteId).subscribe(
            a => this.athlete = a);
        this.metricService.getMetricsByAthlete(this.athleteId).subscribe(
            m => { this.metrics = m; });
        this.athleteVideoService.getVideosByAthlete(this.athleteId).subscribe(
            v => this.videos = v);
        this.athleteService.getAthletePerformanceSummary(this.athleteId).subscribe(
            v => this.summary = v);

    }
    
    getMetricKeys(summaryObj: { [key: string]: number }): string[] {
        return Object.keys(summaryObj);
    }
}
