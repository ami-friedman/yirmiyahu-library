import { Component } from '@angular/core';
import { Store } from '@ngrx/store';
import { AppState } from './app.state';
import * as AuthActions from './components/auth/auth.actions';
import { UserFacadeService } from './components/auth/user-facade.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'yirmiyahu-library';

  constructor(private userService: UserFacadeService) {
    const user = localStorage.getItem('user');
    if (user) {
      this.userService.loggedIn(JSON.parse(user))
    }
  }
}
