import { createReducer, on } from "@ngrx/store";
import { User } from "src/app/models/user.model";
import * as AuthActions from "./auth.actions";


export interface AuthState {
    user: User
}

export const authInitialState: AuthState = {
    user: undefined
};


export const authReducer = createReducer(
    authInitialState,
    on(AuthActions.login, (state, {user}) => ({user})),
    on(AuthActions.logout, (state) => authInitialState),
)

