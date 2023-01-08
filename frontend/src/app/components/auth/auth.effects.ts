import { Injectable } from "@angular/core";
import { Actions, createEffect, ofType } from "@ngrx/effects";
import { tap } from "rxjs/operators";
import * as AuthActions from "./auth.actions";

@Injectable()
export class AuthEffects {
  login$ = createEffect( () => this.action$.pipe(
      ofType(AuthActions.login),
      tap(action => localStorage.setItem('user', JSON.stringify(action.user)))
    ),
  {dispatch: false}
  ) 

  logout$ = createEffect( () => this.action$.pipe(
      ofType(AuthActions.logout),
      tap(action => {
        localStorage.removeItem('user');
      })
    ),
  {dispatch: false}
  ) 

  constructor(private action$: Actions) {}

}