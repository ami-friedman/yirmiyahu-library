import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Genre } from 'src/app/models/book.model';

@Injectable({
  providedIn: 'root'
})
export class GenresService {

  constructor(private http: HttpClient) { }

  getAll(): Observable<Genre[]> {
    return this.http.get<Genre[]>('api/genres')
  }

  add(genre: Genre): Observable<Genre> {
    return this.http.post<Genre>('api/genres', genre)
  }

  delete(genreId: number): Observable<number> {
    return this.http.delete<number>('api/genres', {params: {id: genreId}})
  }

}
