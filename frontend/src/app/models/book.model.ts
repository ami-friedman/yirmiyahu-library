
export enum BookAvailability {
  Available = 'available',
  OnLoan = 'on_loan',
  Reserved = 'reserved'
}

export interface Author {
  first_name: string,
  last_name: string,
  id?: number
}

export interface Genre {
  name: string,
  id?: number
}

export interface BookType {
  name: string,
  loan_duration: number,
  extension_duration: string,
  id?: number
}


export interface Book {
    title: string,
    author: Author,
    genre: Genre,
    type: BookType,
    availability: BookAvailability,
    id?: number,
  }
