import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Store } from '@ngrx/store';
import { SocialAuthService } from 'angularx-social-login';
import { noop, tap } from 'rxjs';
import { AppState } from 'src/app/app.state';
import { AuthService } from '../auth/auth.service';
import * as AuthActions from '../auth/auth.actions'
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './root.component.html',
  styleUrls: ['./root.component.css']
})
export class RootComponent {

  constructor() {
    
  }
}
