import { Injectable } from '@angular/core';
import { Store } from '@ngrx/store';
import { SocialAuthService } from 'angularx-social-login';
import { AppState } from 'src/app/app.state';
import { Role, User } from 'src/app/models/user.model';
import * as AuthActions from '../auth/auth.actions'
import { selectCurrentUser } from './auth.selector';

@Injectable({
  providedIn: 'root'
})
export class UserFacadeService {

  currentUser$ = this.store.select(selectCurrentUser)
  currentUser: User;

  constructor(private store: Store<AppState>, private socialAuthService: SocialAuthService) { 
    this.currentUser$.subscribe( user => {this.currentUser = user})
    this.socialAuthService.authState.subscribe
  }

  loggedIn(user: User) {
    this.store.dispatch(AuthActions.login({user}))
  }

  loggedOut() {
    this.store.dispatch(AuthActions.logout())
  }

  hasRole(role: Role): boolean {
    return this.currentUser?.role === role
  }

}
