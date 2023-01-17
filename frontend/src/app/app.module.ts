import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RootModule } from './components/root/root.module';
import { AuthModule } from './components/auth/auth.module';
import { StoreModule } from '@ngrx/store';
import { authReducer } from './components/auth/auth.reducer';
import { EffectsModule } from '@ngrx/effects';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';
import { environment } from 'src/environments/environment.prod';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { HttpInterceptorService } from './http-interceptor.service';
import { EntityDataModule } from '@ngrx/data';
import { RootComponent } from './components/root/root.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    RootModule,
    AuthModule.forRoot(),
    StoreModule.forRoot({auth: authReducer}),
    EffectsModule.forRoot([]),
    EntityDataModule.forRoot({}),
    StoreDevtoolsModule.instrument({maxAge: 25, logOnly: environment.production})
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: HttpInterceptorService, multi: true },
  ],
  bootstrap: [RootComponent]
})
export class AppModule {}
