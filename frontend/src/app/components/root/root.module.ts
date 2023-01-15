import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconRegistry } from '@angular/material/icon';
import { DomSanitizer } from '@angular/platform-browser';
import { SharedModule } from '../../shared/shared.module';
import { RootComponent } from './root.component';
import { TopNavComponent } from '../left-nav/top-nav.component';
import { RouterModule, Routes } from '@angular/router';
import { EntityDataService, EntityDefinitionService } from '@ngrx/data';
import { entityMetadata as BookEntityMetadata } from '../catalog/book/book-metadata';
import { BookDataService } from '../catalog/book/book-data.service';
import { AuthGuardService } from '../auth/auth.guard';
import { CatalogComponent } from '../catalog/catalog.component';
import { BookEntityService } from '../catalog/book/book-entity.service';


const routes: Routes = [
  {
    path: 'catalog',
    component: CatalogComponent,
    canActivate: [AuthGuardService]
  }
];


@NgModule({
  declarations: [
    RootComponent,
    TopNavComponent
  ],
  imports: [
    RouterModule,
    CommonModule,
    SharedModule,
    [RouterModule.forChild(routes)],
  ],
  exports: [RouterModule],
  providers: [
    BookDataService,
    BookEntityService
  ]
})
export class RootModule { 
  constructor(
    private matIconRegistry: MatIconRegistry, 
    private domSanitizer: DomSanitizer,
    private eds: EntityDefinitionService,
    private entityDataService: EntityDataService, 
    private bookDataService: BookDataService
    ) {
    this.matIconRegistry.addSvgIcon('google_logo', this.domSanitizer.bypassSecurityTrustResourceUrl("../assets/google_logo.svg"));
    this.matIconRegistry.addSvgIcon('catalog', this.domSanitizer.bypassSecurityTrustResourceUrl("../assets/catalog.svg"));

    this.eds.registerMetadataMap(BookEntityMetadata);
    this.entityDataService.registerService('Book', this.bookDataService);

  }
}
