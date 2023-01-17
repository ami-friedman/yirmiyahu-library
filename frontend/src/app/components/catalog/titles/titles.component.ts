import { Component, OnInit } from '@angular/core';
import { Sort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Observable } from 'rxjs';
import { Book } from 'src/app/models/book.model';
import { BookDataService } from '../book/book-data.service';
import { BookEntityService } from '../book/book-entity.service';

@Component({
  selector: 'app-titles',
  templateUrl: './titles.component.html',
  styleUrls: ['./titles.component.scss']
})
export class TitlesComponent {

  displayedColumns: string[] = ['title', 'author', 'availability',  'action1'];
  titles: MatTableDataSource<Book>;
  titles$: Observable<Book[]>;

  constructor(
    private bookEntityService: BookEntityService,
    private bookDataService: BookDataService,
  ) { 
    this.titles = new MatTableDataSource();
    this.titles$ = this.bookEntityService.entities$;
  }

  onSortChange(sort: Sort) {
    const data = this.titles.data.slice();
    if (!sort.active || sort.direction === '') {
      this.titles.data = data;
      return;
    }

    this.titles.data = data.sort((a, b) => {
      const isAsc = sort.direction === 'asc';
      switch (sort.active) {
        case 'title':
          return compare(a.title, b.title, isAsc);
        case 'author':
          return compare(a.author.last_name, b.author.last_name, isAsc);
        default:
          return 0;
      }
    });

    function compare(a: number | string, b: number | string, isAsc: boolean) {
      return (a < b ? -1 : 1) * (isAsc ? 1 : -1);
  }
}

 

}
