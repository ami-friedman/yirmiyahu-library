import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Store } from '@ngrx/store';
import { GoogleLoginProvider, SocialAuthService, SocialUser } from 'angularx-social-login';
import { noop, tap } from 'rxjs';
import { AppState } from 'src/app/app.state'; 
import { User } from 'src/app/models/user.model';
import * as AuthActions from '../auth.actions'
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  socialUser!: SocialUser;


  constructor(private socialAuthService: SocialAuthService,  
    private router: Router, 
    private store: Store<AppState>,
    private authService: AuthService) { }

  ngOnInit(): void {}

  loginWithGoogle(){
    this.socialAuthService.signIn(GoogleLoginProvider.PROVIDER_ID);
  }
}
