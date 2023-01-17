import { Injectable } from "@angular/core";
import { EntityCollectionServiceBase, EntityCollectionServiceElementsFactory } from "@ngrx/data";
import { Book } from "src/app/models/book.model";


@Injectable()
export class BookEntityService extends EntityCollectionServiceBase<Book>{
    constructor(serviceElementFactory: EntityCollectionServiceElementsFactory) {
        super('Book', serviceElementFactory)
    }

}