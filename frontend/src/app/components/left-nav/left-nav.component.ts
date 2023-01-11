import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Store } from '@ngrx/store';
import { SocialAuthService } from 'angularx-social-login';
import { AppState } from 'src/app/app.state';
import { User } from 'src/app/models/user.model';
import * as AuthActions from '../auth/auth.actions';
import { selectCurrentUser } from '../auth/auth.selector';

@Component({
  selector: 'app-left-nav',
  templateUrl: './left-nav.component.html',
  styleUrls: ['./left-nav.component.scss']
})
export class LeftNavComponent implements OnInit {

  currentUser: User;

  constructor(
    private store: Store<AppState>, 
    private router: Router,
    private socialAuthService: SocialAuthService
    ) { 
      this.store.select(selectCurrentUser).subscribe(
        (user: User) => {
          this.currentUser = user;
      }
    )
    }

  ngOnInit(): void {
  }

  onLogout() {
    this.socialAuthService.signOut();
    this.store.dispatch(AuthActions.logout());
    this.router.navigateByUrl('auth/login');
  }

}
