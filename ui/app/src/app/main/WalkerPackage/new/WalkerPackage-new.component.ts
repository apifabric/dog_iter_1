import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'WalkerPackage-new',
  templateUrl: './WalkerPackage-new.component.html',
  styleUrls: ['./WalkerPackage-new.component.scss']
})
export class WalkerPackageNewComponent {
  @ViewChild("WalkerPackageForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}