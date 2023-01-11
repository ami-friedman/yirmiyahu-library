import {Directive, Input, TemplateRef, ViewContainerRef} from '@angular/core';
import { UserFacadeService } from '../components/auth/user-facade.service';
import { Role, User } from '../models/user.model';


@Directive({selector: '[hasRole]'})
export class RolesCheckDirective {

	currentUser: User;

	@Input() set hasRole(role: Role) {
		if (!role || (role && role.length > 0 && this.userService.hasRole(role))) {
			this.viewContainer.createEmbeddedView(this.templateRef);
		} else {
			this.viewContainer.clear();
		}
	}

	constructor(private templateRef: TemplateRef<any>,
		private viewContainer: ViewContainerRef, private userService: UserFacadeService) {
			
	}
}
