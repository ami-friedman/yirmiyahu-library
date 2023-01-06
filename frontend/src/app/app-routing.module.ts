import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RootComponent } from './components/root/root.component';

const routes: Routes = [
  {
    path: 'auth',
    loadChildren: () => import('src/app/components/auth/auth.module').then(m => m.AuthModule)
  },
  {
    path: '',
    component: RootComponent

  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
