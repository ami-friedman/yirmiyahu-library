import { HttpErrorResponse } from '@angular/common/http';
import { AfterViewInit, Component } from '@angular/core';
import { Router } from '@angular/router';
import { noop, tap } from 'rxjs';
import { AuthService } from '../auth.service';
import { UserFacadeService } from '../user-facade.service';

declare var google: any;

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements AfterViewInit {

  constructor(
    private authService: AuthService, 
    private userService: UserFacadeService,
    private router: Router) { 
    

  }

  loginWithGoogle(response){
    this.authService.login(response.credential)
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
    
  }

  ngAfterViewInit(): void {
    google.accounts.id.initialize({
      client_id: "389702736477-p3c32j84usecie7o3ubfnqd2nh7rkic1.apps.googleusercontent.com",
      callback: (response: any) => this.loginWithGoogle(response)
    });
    google.accounts.id.renderButton(
      document.getElementById("buttonDiv"),
      { size: "large", type: "standard", shape: "pill" }  // customization attributes
    );
  }
}
