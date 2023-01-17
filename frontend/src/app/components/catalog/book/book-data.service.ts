import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { DefaultDataService, HttpUrlGenerator } from "@ngrx/data";
import { Observable } from "rxjs";
import { Book } from "src/app/models/book.model";
import { User } from "src/app/models/user.model";
import { UserFacadeService } from "../../auth/user-facade.service";


@Injectable()
export class BookDataService extends DefaultDataService<Book> {
    currentUser: User

    constructor(http: HttpClient, httpUrlGenerator: HttpUrlGenerator, private userService: UserFacadeService) {
        super('Book', http, httpUrlGenerator)
        this.userService.currentUser$
        .subscribe(
            (user: User) => {
                this.currentUser = user;
      });

    }

    getAll(): Observable<Book[]> {
        return this.http.get<Book[]>('api/books')
    }

    add(book: Book): Observable<Book> {
        return this.http.post<Book>('api/books', book)
    }

}