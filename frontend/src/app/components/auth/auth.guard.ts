import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot } from '@angular/router';
import { Observable, of } from 'rxjs';
import { User } from 'src/app/models/user.model';
import { AuthService } from './auth.service';
import { UserFacadeService } from './user-facade.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService implements CanActivate {

  currentUser: User;


  constructor(private router: Router, private userService: UserFacadeService, private authService: AuthService) {
    this.userService.currentUser$.subscribe( user => { this.currentUser = user })
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> {

    if (!this.currentUser) {
      this.router.navigate(['auth/login'], {queryParams: {returnUrl: state.url}});
      return of(false);
    }

    return of(true);

    // return this.authService.login(this.currentUser.email)
    // .pipe(
    //   (user ) => {return of(true)},
    //   catchError( () => {
    //     this.router.navigate(['auth/login'], {queryParams: {returnUrl: state.url}});
    //     return of(false);
    //   })
    // )
  }
}
