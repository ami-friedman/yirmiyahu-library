import { Component } from '@angular/core';
import { UserFacadeService } from '../auth/user-facade.service';


@Component({
  selector: 'app-root',
  templateUrl: './root.component.html',
  styleUrls: ['./root.component.css']
})
export class RootComponent {

  constructor(private userService: UserFacadeService) {
    const user = localStorage.getItem('user');
    if (user) {
      this.userService.loggedIn(JSON.parse(user))
    }
   
  }
}
