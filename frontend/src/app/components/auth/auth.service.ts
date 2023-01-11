import {Injectable} from "@angular/core";
import {HttpClient, HttpErrorResponse} from "@angular/common/http";
import {noop, Observable, tap} from "rxjs";
import { User } from "src/app/models/user.model";
import { SocialAuthService, SocialUser } from "angularx-social-login";
import { Router } from "@angular/router";
import { Store } from "@ngrx/store";
import { AppState } from "src/app/app.state";
import * as AuthActions from '../auth/auth.actions'


@Injectable({
    providedIn: 'root'
  })
export class AuthService {

    constructor(private http:HttpClient, 
        private socialAuthService: SocialAuthService,  
        private router: Router, 
        private store: Store<AppState>,) {
            this.socialAuthService.authState.subscribe((user: SocialUser) => { 
                if (!user) {
                  return
                }
                this.login(user.idToken)
                .pipe(
                  tap(user => {
                  this.store.dispatch(AuthActions.login({user}));
                  this.router.navigateByUrl('');
                })
              )
              .subscribe({
                next: noop,
                error:  (error: HttpErrorResponse) => {
                  if (error.status == 401) {
                    alert('Not Authorized')
                }
              }});
              })

    }

    login(token: string): Observable<User> {
        return this.http.post<User>('api/user/login', {token})
    }

    logout(user: User): Observable<User> {
        return this.http.post<User>('api/user/logout', user)
    }
}
