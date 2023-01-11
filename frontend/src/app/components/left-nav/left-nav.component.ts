import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { SocialAuthService } from 'angularx-social-login';
import { User } from 'src/app/models/user.model';
import { UserFacadeService } from '../auth/user-facade.service';

@Component({
  selector: 'app-left-nav',
  templateUrl: './left-nav.component.html',
  styleUrls: ['./left-nav.component.scss']
})
export class LeftNavComponent {

  currentUser: User;

  constructor(
    private router: Router,
    private socialAuthService: SocialAuthService,
    private userService: UserFacadeService
    ) { 
      this.userService.currentUser$.subscribe(
        (user: User) => {
          this.currentUser = user;
      }
    )
    }

    onLogout() {
    this.socialAuthService.signOut();
    this.userService.logout();
    this.router.navigateByUrl('auth/login');
  }

}
