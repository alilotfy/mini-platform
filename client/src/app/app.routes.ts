import { Routes } from '@angular/router';
import { AthletesComponent } from './features/athletes/athletes.component';
import { MetricsComponent } from './features/metrics/metrics.component';
import { VideosComponent } from './features/videos/videos.component';
import { AthleteComponent } from './features/athlete/athlete.component';

 

export const routes: Routes = [
  { path: 'athletes', component: AthletesComponent },
  { path: 'videos', component: VideosComponent },
  { path: 'metrics', component: MetricsComponent },
  { path: 'athlete/:id', component: AthleteComponent },
  { path: '', redirectTo: '/athletes', pathMatch: 'full' },
];

