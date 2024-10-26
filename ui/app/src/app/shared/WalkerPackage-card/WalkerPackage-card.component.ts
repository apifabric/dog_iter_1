import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WalkerPackage-card.component.html',
  styleUrls: ['./WalkerPackage-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WalkerPackage-card]': 'true'
  }
})

export class WalkerPackageCardComponent {


}