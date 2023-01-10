import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconRegistry } from '@angular/material/icon';
import { DomSanitizer } from '@angular/platform-browser';
import { SharedModule } from '../../shared/shared.module';
import { RootComponent } from './root.component';
import { AuthModule } from '../auth/auth.module';
import { LeftNavComponent } from '../left-nav/left-nav.component';
import { RouterModule, Routes } from '@angular/router';


@NgModule({
  declarations: [
    RootComponent,
    LeftNavComponent
  ],
  imports: [
    RouterModule,
    CommonModule,
    SharedModule,
  ]
})
export class RootModule { 
  constructor(private matIconRegistry: MatIconRegistry, private domSanitizer: DomSanitizer) {
    this.matIconRegistry.addSvgIcon('google_logo', this.domSanitizer.bypassSecurityTrustResourceUrl("../assets/google_logo.svg"));

  }
}
