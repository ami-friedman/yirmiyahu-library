import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import { User } from "src/app/models/user.model";



@Injectable({
    providedIn: 'root'
  })
export class AuthService {

    constructor(private http:HttpClient) {
    }

    login(token: string): Observable<User> {
        return this.http.post<User>('api/user/login', {token})
    }

    logout(user: User): Observable<User> {
        return this.http.post<User>('api/user/logout', user)
    }
}
