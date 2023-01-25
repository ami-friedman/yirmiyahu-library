import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { Genre } from 'src/app/models/book.model';

@Injectable({
  providedIn: 'root'
})
export class GenresService {

  genres$: BehaviorSubject<Genre[]> = new BehaviorSubject<Genre[]>(null);

  constructor(private http: HttpClient) { }

  getAll() {
    this.http.get<Genre[]>('api/genres').subscribe( genres => this.genres$.next(genres))
  }

  add(genre: Genre) {
    this.http.post<Genre>('api/genres', genre).subscribe(
      () => {this.getAll()}
    )
  }

  update(genre: Genre) {
    this.http.put<Genre>(`api/genres/${genre.id}`, {updated_genre: genre}).subscribe(
      () => {this.getAll()}
    )
  }

  delete(genreId: number) {
    this.http.delete<number>(`api/genres/${genreId}`, {params: {id: genreId}}).subscribe(
      () => {this.getAll()}
    )
  }

}
