import { HttpErrorResponse } from '@angular/common/http';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { GoogleLoginProvider, SocialAuthService, SocialUser } from 'angularx-social-login';
import { noop, tap } from 'rxjs';
import { AuthService } from '../auth.service';
import { UserFacadeService } from '../user-facade.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  socialUser!: SocialUser;


  constructor(
    private socialAuthService: SocialAuthService, 
    private authService: AuthService, 
    private userService: UserFacadeService,
    private router: Router) { 
    this.socialAuthService.authState.subscribe((user: SocialUser) => { 
      if (!user) {
        return
      }
      this.authService.login(user.idToken)
      .pipe(
        tap(user => {
        this.userService.loggedIn(user);
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

  loginWithGoogle(){
    this.socialAuthService.signIn(GoogleLoginProvider.PROVIDER_ID);
  }
}
