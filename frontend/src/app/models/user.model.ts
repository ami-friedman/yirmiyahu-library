export enum Role {
    admin = 'admin',
    subscriber = 'subscriber'
  }

export interface User {
    name: string,
    email: string,
    id?: number,
    role: Role 
  }