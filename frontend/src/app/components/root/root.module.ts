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
import { entityMetadata as AuthorEntityMetadata } from '../catalog/author/author-metadata';
import { BookDataService } from '../catalog/book/book-data.service';
import { AuthGuardService } from '../auth/auth.guard';
import { CatalogComponent } from '../catalog/catalog.component';
import { BookEntityService } from '../catalog/book/book-entity.service';
import { TitlesComponent } from '../catalog/titles/titles.component';
import { AuthorDataService } from '../catalog/author/author-data.service';
import { AuthorEntityService } from '../catalog/author/author-entity.service';
import { AuthorsComponent } from '../catalog/authors/authors.component';
import { GenresComponent } from '../catalog/genres/genres.component';


const routes: Routes = [
  {
    path: 'catalog',
    component: CatalogComponent,
    canActivate: [AuthGuardService],
    children: [
      {
        path: 'titles',
        component: TitlesComponent,
        canActivate: [AuthGuardService],
      },
      {
        path: 'authors',
        component: AuthorsComponent,
        canActivate: [AuthGuardService],
      },
      {
        path: 'genres',
        component: GenresComponent,
        canActivate: [AuthGuardService],
      }
    ]
  },
  
];


@NgModule({
  declarations: [
    RootComponent,
    TopNavComponent,
    CatalogComponent,
    TitlesComponent,
    AuthorsComponent,
    GenresComponent,
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
    BookEntityService,
    AuthorDataService,
    AuthorEntityService
  ]
})
export class RootModule { 
  constructor(
    private matIconRegistry: MatIconRegistry, 
    private domSanitizer: DomSanitizer,
    private eds: EntityDefinitionService,
    private entityDataService: EntityDataService, 
    private bookDataService: BookDataService,
    private authorDataService: AuthorDataService,
    ) {
    this.matIconRegistry.addSvgIcon('google_logo', this.domSanitizer.bypassSecurityTrustResourceUrl("../assets/google_logo.svg"));
    this.matIconRegistry.addSvgIcon('catalog', this.domSanitizer.bypassSecurityTrustResourceUrl("../assets/catalog.svg"));

    this.eds.registerMetadataMap(BookEntityMetadata);
    this.entityDataService.registerService('Book', this.bookDataService);

    this.eds.registerMetadataMap(AuthorEntityMetadata);
    this.entityDataService.registerService('Author', this.authorDataService);
  }
}
