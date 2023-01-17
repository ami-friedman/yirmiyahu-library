import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { DefaultDataService, HttpUrlGenerator } from "@ngrx/data";
import { Observable } from "rxjs";
import { Author } from "src/app/models/book.model";
import { User } from "src/app/models/user.model";
import { UserFacadeService } from "../../auth/user-facade.service";


@Injectable()
export class AuthorDataService extends DefaultDataService<Author> {
    currentUser: User

    constructor(http: HttpClient, httpUrlGenerator: HttpUrlGenerator, private userService: UserFacadeService) {
        super('Author', http, httpUrlGenerator)
        this.userService.currentUser$
        .subscribe(
            (user: User) => {
                this.currentUser = user;
      });

    }

    getAll(): Observable<Author[]> {
        return this.http.get<Author[]>('api/authors')
    }

    add(author: Author): Observable<Author> {
        return this.http.post<Author>('api/authors', author)
    }

}