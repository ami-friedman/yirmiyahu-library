import { EntityMetadataMap } from "@ngrx/data";
import { Author } from "src/app/models/book.model";



function selectAuthorId(author: Author) {
  return author.id
}

export const entityMetadata: EntityMetadataMap = {
  Author : {
    selectId: selectAuthorId
  }
};
