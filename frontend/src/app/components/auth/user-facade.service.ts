import { Injectable } from '@angular/core';
import { Store } from '@ngrx/store';
import { AppState } from 'src/app/app.state';
import { User } from 'src/app/models/user.model';
import * as AuthActions from '../auth/auth.actions'
import { selectCurrentUser } from './auth.selector';

@Injectable({
  providedIn: 'root'
})
export class UserFacadeService {

  currentUser$ = this.store.select(selectCurrentUser)

  constructor(private store: Store<AppState>) { }

  login(user: User) {
    this.store.dispatch(AuthActions.login({user}))
  }

  logout() {
    this.store.dispatch(AuthActions.logout())
  }
}
