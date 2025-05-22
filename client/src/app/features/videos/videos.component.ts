import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Video, VideoService } from 'src/app/services/video.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-videos',
  imports: [CommonModule],
  templateUrl: './videos.component.html',
  styleUrl: './videos.component.scss'
})
export class VideosComponent {
  videos: Video[] = [];

  constructor(private videoService: VideoService, private snackBar: MatSnackBar) { }

  ngOnInit(): void {
    this.videoService.getVideos().subscribe(data => {
      this.videos = data;
    });
  }


  onVideoSelected(event: Event): void {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (file) {
      const formData = new FormData();
      formData.append('file', file);

      this.videoService.UploadVideo(formData).subscribe({
        next: (res) => {
          console.log('Upload success:', res);
          this.snackBar.open('Video uploaded! Reload to View videos', 'Close', {
            duration: 3000, // 3 seconds
          });
        }, error: (err) => console.error('Upload error:', err),
      });
    }
  }
}
