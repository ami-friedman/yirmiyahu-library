import { ModuleWithProviders, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedModule } from '../../shared/shared.module';
import { LoginComponent } from './login/login.component';
import { RouterModule } from '@angular/router';
import { environment } from 'src/environments/environment';
import { EffectsModule } from '@ngrx/effects';
import { AuthEffects } from './auth.effects';



@NgModule({
  declarations: [
    LoginComponent
  ],
  imports: [
    RouterModule.forChild([
      {path: 'login', component: LoginComponent},
    ]),
    CommonModule,
    SharedModule,
    EffectsModule.forFeature([AuthEffects]),
  ],
  providers: []

})
export class AuthModule { 
  static forRoot(): ModuleWithProviders<AuthModule> {
    return {
        ngModule: AuthModule,
    }
}
}
