import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { Book } from 'src/app/models/book.model';
import { BookDataService } from './book/book-data.service';
import { BookEntityService } from './book/book-entity.service';

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styleUrls: ['./catalog.component.scss']
})
export class CatalogComponent implements OnInit {

  books$: Observable<Book[]>;

  constructor(private bookEntityService: BookEntityService,
    private router: Router,
    ) { 
    this.bookEntityService.getAll();
    this.books$ = this.bookEntityService.entities$
  }

  get currentRoute(): string {
    return this.router.url
  }

  ngOnInit(): void {
  }

}
