import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Athlete, AthleteService } from 'src/app/services/athlete.service';

@Component({
  selector: 'app-athletes',
  templateUrl: './athletes.component.html',
  styleUrls: ['./athletes.component.scss'],
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class AthletesComponent implements OnInit {
  athletes: Athlete[] = [];

  newAthlete: Partial<Athlete> = {
    name: '',
    sport: '',
    age: undefined
  };

  constructor(private athleteService: AthleteService, private snackBar: MatSnackBar) {}

  ngOnInit(): void {
    this.loadAthletes();
  }

  loadAthletes(): void {
    this.athleteService.getAthletes().subscribe(data => {
      this.athletes = data;
    });
  }

  addAthlete(): void {
    if (this.newAthlete.name && this.newAthlete.sport && this.newAthlete.age) {
      this.athleteService.addAthlete(this.newAthlete as Athlete).subscribe(() => {
          this.loadAthletes();
        
        this.newAthlete = { name: '', sport: '', age: undefined }; // reset form
          this.snackBar.open('Athlete Created', 'Close', {
            duration: 3000,
          });
        
      });
    }
  }
}
