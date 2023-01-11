import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot } from '@angular/router';
import { Store } from '@ngrx/store';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { AppState } from 'src/app/app.state';
import { User } from 'src/app/models/user.model';
import { selectCurrentUser } from './auth.selector';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService implements CanActivate {

  currentUser: User;


  constructor(private router: Router, private store: Store<AppState>, private authService: AuthService) {
    this.store.select(selectCurrentUser).subscribe ( user => { this.currentUser = user })
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> {

    if (!this.currentUser) {
      this.router.navigate(['auth/login'], {queryParams: {returnUrl: state.url}});
      return of(false);
    }

    return this.authService.login(this.currentUser.email)
    .pipe(
      (user ) => {return of(true)},
      catchError( () => {
        this.router.navigate(['auth/login'], {queryParams: {returnUrl: state.url}});
        return of(false);
      })
    )
  }
}
