import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkerPackageHomeComponent } from './home/WalkerPackage-home.component';
import { WalkerPackageNewComponent } from './new/WalkerPackage-new.component';
import { WalkerPackageDetailComponent } from './detail/WalkerPackage-detail.component';

const routes: Routes = [
  {path: '', component: WalkerPackageHomeComponent},
  { path: 'new', component: WalkerPackageNewComponent },
  { path: ':id', component: WalkerPackageDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WalkerPackage-detail-permissions'
      }
    }
  }
];

export const WALKERPACKAGE_MODULE_DECLARATIONS = [
    WalkerPackageHomeComponent,
    WalkerPackageNewComponent,
    WalkerPackageDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkerPackageRoutingModule { }