import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Genre } from 'src/app/models/book.model';
import { GenresService } from './genres.service';

@Component({
  selector: 'app-genres',
  templateUrl: './genres.component.html',
  styleUrls: ['./genres.component.scss']
})
export class GenresComponent {

  genres$: Observable<Genre[]>;

  constructor(private genreService: GenresService) { 
    this.genres$ = this.genreService.getAll();
  }

}
