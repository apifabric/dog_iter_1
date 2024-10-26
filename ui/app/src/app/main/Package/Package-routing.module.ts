import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PackageHomeComponent } from './home/Package-home.component';
import { PackageNewComponent } from './new/Package-new.component';
import { PackageDetailComponent } from './detail/Package-detail.component';

const routes: Routes = [
  {path: '', component: PackageHomeComponent},
  { path: 'new', component: PackageNewComponent },
  { path: ':id', component: PackageDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Package-detail-permissions'
      }
    }
  },{
    path: ':package_id/Subscription', loadChildren: () => import('../Subscription/Subscription.module').then(m => m.SubscriptionModule),
    data: {
        oPermission: {
            permissionId: 'Subscription-detail-permissions'
        }
    }
},{
    path: ':package_id/WalkerPackage', loadChildren: () => import('../WalkerPackage/WalkerPackage.module').then(m => m.WalkerPackageModule),
    data: {
        oPermission: {
            permissionId: 'WalkerPackage-detail-permissions'
        }
    }
}
];

export const PACKAGE_MODULE_DECLARATIONS = [
    PackageHomeComponent,
    PackageNewComponent,
    PackageDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PackageRoutingModule { }