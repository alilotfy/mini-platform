import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Video, VideoService } from 'src/app/services/video.service';

@Component({
  selector: 'app-videos',
  imports: [CommonModule],
  templateUrl: './videos.component.html',
  styleUrl: './videos.component.scss'
})
export class VideosComponent {
  videos: Video[] = [];

  constructor(private videoService: VideoService) { }

  ngOnInit(): void {
    this.videoService.getVideos().subscribe(data => {
      this.videos = data;
    });
  }
}
