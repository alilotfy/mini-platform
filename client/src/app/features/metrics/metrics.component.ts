import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Metric, MetricService } from 'src/app/services/metric.service';

@Component({
  selector: 'app-metrics',
  imports: [CommonModule],
  templateUrl: './metrics.component.html',
  styleUrl: './metrics.component.scss'
})
export class MetricsComponent {
  metrics: Metric[] = [];

  constructor(private metricService: MetricService) { }

  ngOnInit(): void {
    this.metricService.getMetrics().subscribe(data => {
      this.metrics = data;
    });
  }
}
