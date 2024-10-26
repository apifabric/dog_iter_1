import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {WALKERPACKAGE_MODULE_DECLARATIONS, WalkerPackageRoutingModule} from  './WalkerPackage-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    WalkerPackageRoutingModule
  ],
  declarations: WALKERPACKAGE_MODULE_DECLARATIONS,
  exports: WALKERPACKAGE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WalkerPackageModule { }