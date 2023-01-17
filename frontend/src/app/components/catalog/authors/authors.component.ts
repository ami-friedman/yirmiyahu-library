import { Component, OnInit } from '@angular/core';
import { Sort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Observable } from 'rxjs';
import { Author } from 'src/app/models/book.model';
import { AuthorDataService } from '../author/author-data.service';
import { AuthorEntityService } from '../author/author-entity.service';

@Component({
  selector: 'app-authors',
  templateUrl: './authors.component.html',
  styleUrls: ['./authors.component.scss']
})
export class AuthorsComponent {

  displayedColumns: string[] = ['firtName', 'lastName'];
  authors: MatTableDataSource<Author>;
  authors$: Observable<Author[]>;

  constructor(
    private authorEntityService: AuthorEntityService,
    private authorDataService: AuthorDataService,
  ) { 
    this.authors = new MatTableDataSource();
    this.authors$ = this.authorEntityService.entities$;

  }

  onSortChange(sort: Sort) {
    const data = this.authors.data.slice();
    if (!sort.active || sort.direction === '') {
      this.authors.data = data;
      return;
    }

    this.authors.data = data.sort((a, b) => {
      const isAsc = sort.direction === 'asc';
      switch (sort.active) {
        case 'first_name':
          return compare(a.first_name, b.first_name, isAsc);
        case 'last_name':
          return compare(a.last_name, b.last_name, isAsc);
        default:
          return 0;
      }
    });

    function compare(a: number | string, b: number | string, isAsc: boolean) {
      return (a < b ? -1 : 1) * (isAsc ? 1 : -1);
  }
}
}
