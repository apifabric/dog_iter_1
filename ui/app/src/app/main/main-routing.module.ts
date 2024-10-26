import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Dog', loadChildren: () => import('./Dog/Dog.module').then(m => m.DogModule) },
    
        { path: 'Location', loadChildren: () => import('./Location/Location.module').then(m => m.LocationModule) },
    
        { path: 'Owner', loadChildren: () => import('./Owner/Owner.module').then(m => m.OwnerModule) },
    
        { path: 'Package', loadChildren: () => import('./Package/Package.module').then(m => m.PackageModule) },
    
        { path: 'Review', loadChildren: () => import('./Review/Review.module').then(m => m.ReviewModule) },
    
        { path: 'Schedule', loadChildren: () => import('./Schedule/Schedule.module').then(m => m.ScheduleModule) },
    
        { path: 'Service', loadChildren: () => import('./Service/Service.module').then(m => m.ServiceModule) },
    
        { path: 'Subscription', loadChildren: () => import('./Subscription/Subscription.module').then(m => m.SubscriptionModule) },
    
        { path: 'Walk', loadChildren: () => import('./Walk/Walk.module').then(m => m.WalkModule) },
    
        { path: 'Walker', loadChildren: () => import('./Walker/Walker.module').then(m => m.WalkerModule) },
    
        { path: 'WalkerPackage', loadChildren: () => import('./WalkerPackage/WalkerPackage.module').then(m => m.WalkerPackageModule) },
    
        { path: 'WalkerService', loadChildren: () => import('./WalkerService/WalkerService.module').then(m => m.WalkerServiceModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }