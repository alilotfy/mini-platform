import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Athlete, AthleteService } from 'src/app/services/athlete.service';

@Component({
  selector: 'app-athletes',
  templateUrl: './athletes.component.html',
  styleUrls: ['./athletes.component.scss'],
  imports: [CommonModule]
})
export class AthletesComponent implements OnInit {
  athletes: Athlete[] = [];

  constructor(private athleteService: AthleteService) {}

  ngOnInit(): void {
    this.athleteService.getAthletes().subscribe(data => {
      this.athletes = data;
      console.log(data)
    });
  }

}
