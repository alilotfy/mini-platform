import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AthletesComponent } from './features/athletes/athletes.component';
import { VideosComponent } from './features/videos/videos.component';
import { MetricsComponent } from './features/metrics/metrics.component';
import { AppComponent } from './app.component';

const routes: Routes = [
  { path: 'athletes', component: AthletesComponent },
  { path: 'videos', component: VideosComponent },
  { path: 'metrics', component: MetricsComponent },
  { path: '', redirectTo: '/athletes', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes), AppComponent],
  exports: [RouterModule, AppComponent]
})
export class AppModule {}
