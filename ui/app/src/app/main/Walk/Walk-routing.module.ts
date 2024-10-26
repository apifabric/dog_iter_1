import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkHomeComponent } from './home/Walk-home.component';
import { WalkNewComponent } from './new/Walk-new.component';
import { WalkDetailComponent } from './detail/Walk-detail.component';

const routes: Routes = [
  {path: '', component: WalkHomeComponent},
  { path: 'new', component: WalkNewComponent },
  { path: ':id', component: WalkDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Walk-detail-permissions'
      }
    }
  }
];

export const WALK_MODULE_DECLARATIONS = [
    WalkHomeComponent,
    WalkNewComponent,
    WalkDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkRoutingModule { }