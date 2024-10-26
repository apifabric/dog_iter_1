import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkerHomeComponent } from './home/Walker-home.component';
import { WalkerNewComponent } from './new/Walker-new.component';
import { WalkerDetailComponent } from './detail/Walker-detail.component';

const routes: Routes = [
  {path: '', component: WalkerHomeComponent},
  { path: 'new', component: WalkerNewComponent },
  { path: ':id', component: WalkerDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Walker-detail-permissions'
      }
    }
  },{
    path: ':walker_id/Review', loadChildren: () => import('../Review/Review.module').then(m => m.ReviewModule),
    data: {
        oPermission: {
            permissionId: 'Review-detail-permissions'
        }
    }
},{
    path: ':walker_id/Schedule', loadChildren: () => import('../Schedule/Schedule.module').then(m => m.ScheduleModule),
    data: {
        oPermission: {
            permissionId: 'Schedule-detail-permissions'
        }
    }
},{
    path: ':walker_id/Walk', loadChildren: () => import('../Walk/Walk.module').then(m => m.WalkModule),
    data: {
        oPermission: {
            permissionId: 'Walk-detail-permissions'
        }
    }
},{
    path: ':walker_id/WalkerPackage', loadChildren: () => import('../WalkerPackage/WalkerPackage.module').then(m => m.WalkerPackageModule),
    data: {
        oPermission: {
            permissionId: 'WalkerPackage-detail-permissions'
        }
    }
},{
    path: ':walker_id/WalkerService', loadChildren: () => import('../WalkerService/WalkerService.module').then(m => m.WalkerServiceModule),
    data: {
        oPermission: {
            permissionId: 'WalkerService-detail-permissions'
        }
    }
}
];

export const WALKER_MODULE_DECLARATIONS = [
    WalkerHomeComponent,
    WalkerNewComponent,
    WalkerDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkerRoutingModule { }