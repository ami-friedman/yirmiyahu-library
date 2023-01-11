import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Store } from '@ngrx/store';
import { GoogleLoginProvider, SocialAuthService, SocialUser } from 'angularx-social-login';
import { AppState } from 'src/app/app.state'; 
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  socialUser!: SocialUser;


  constructor(private socialAuthService: SocialAuthService) { }

  loginWithGoogle(){
    this.socialAuthService.signIn(GoogleLoginProvider.PROVIDER_ID);
  }
}
