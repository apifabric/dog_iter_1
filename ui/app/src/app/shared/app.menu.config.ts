import { MenuRootItem } from 'ontimize-web-ngx';

import { DogCardComponent } from './Dog-card/Dog-card.component';

import { LocationCardComponent } from './Location-card/Location-card.component';

import { OwnerCardComponent } from './Owner-card/Owner-card.component';

import { PackageCardComponent } from './Package-card/Package-card.component';

import { ReviewCardComponent } from './Review-card/Review-card.component';

import { ScheduleCardComponent } from './Schedule-card/Schedule-card.component';

import { ServiceCardComponent } from './Service-card/Service-card.component';

import { SubscriptionCardComponent } from './Subscription-card/Subscription-card.component';

import { WalkCardComponent } from './Walk-card/Walk-card.component';

import { WalkerCardComponent } from './Walker-card/Walker-card.component';

import { WalkerPackageCardComponent } from './WalkerPackage-card/WalkerPackage-card.component';

import { WalkerServiceCardComponent } from './WalkerService-card/WalkerService-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Dog', name: 'DOG', icon: 'view_list', route: '/main/Dog' }
    
        ,{ id: 'Location', name: 'LOCATION', icon: 'view_list', route: '/main/Location' }
    
        ,{ id: 'Owner', name: 'OWNER', icon: 'view_list', route: '/main/Owner' }
    
        ,{ id: 'Package', name: 'PACKAGE', icon: 'view_list', route: '/main/Package' }
    
        ,{ id: 'Review', name: 'REVIEW', icon: 'view_list', route: '/main/Review' }
    
        ,{ id: 'Schedule', name: 'SCHEDULE', icon: 'view_list', route: '/main/Schedule' }
    
        ,{ id: 'Service', name: 'SERVICE', icon: 'view_list', route: '/main/Service' }
    
        ,{ id: 'Subscription', name: 'SUBSCRIPTION', icon: 'view_list', route: '/main/Subscription' }
    
        ,{ id: 'Walk', name: 'WALK', icon: 'view_list', route: '/main/Walk' }
    
        ,{ id: 'Walker', name: 'WALKER', icon: 'view_list', route: '/main/Walker' }
    
        ,{ id: 'WalkerPackage', name: 'WALKERPACKAGE', icon: 'view_list', route: '/main/WalkerPackage' }
    
        ,{ id: 'WalkerService', name: 'WALKERSERVICE', icon: 'view_list', route: '/main/WalkerService' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    DogCardComponent

    ,LocationCardComponent

    ,OwnerCardComponent

    ,PackageCardComponent

    ,ReviewCardComponent

    ,ScheduleCardComponent

    ,ServiceCardComponent

    ,SubscriptionCardComponent

    ,WalkCardComponent

    ,WalkerCardComponent

    ,WalkerPackageCardComponent

    ,WalkerServiceCardComponent

];