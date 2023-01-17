import { Injectable } from "@angular/core";
import { EntityCollectionServiceBase, EntityCollectionServiceElementsFactory } from "@ngrx/data";
import { Author } from "src/app/models/book.model";



@Injectable()
export class AuthorEntityService extends EntityCollectionServiceBase<Author>{
    constructor(serviceElementFactory: EntityCollectionServiceElementsFactory) {
        super('Author', serviceElementFactory)
    }

}