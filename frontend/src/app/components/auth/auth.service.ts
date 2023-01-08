import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import { User } from "src/app/models/user.model";


@Injectable()
export class AuthService {

    constructor(private http:HttpClient) {}

    login(email: string): Observable<User> {
        return this.http.post<User>('api/user/login', {email})
    }

    logout(user: User): Observable<User> {
        return this.http.post<User>('api/user/logout', user)
    }
}
