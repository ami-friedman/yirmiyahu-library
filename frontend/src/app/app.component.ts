import { Component } from '@angular/core';
import { Store } from '@ngrx/store';
import { AppState } from './app.state';
import * as AuthActions from './components/auth/auth.actions';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'yirmiyahu-library';

  constructor(private store: Store<AppState>) {
    const user = localStorage.getItem('user');
    if (user) {
      this.store.dispatch(AuthActions.login({user: JSON.parse(user)}))
    }
  }
}
