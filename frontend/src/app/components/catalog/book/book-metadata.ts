import { EntityMetadataMap } from "@ngrx/data";
import { Book } from "src/app/models/book.model";


function selectBookId(book: Book) {
  return book.id
}

export const entityMetadata: EntityMetadataMap = {
  Book : {
    selectId: selectBookId
  }
};
