from enum import Enum


class Role(Enum):
    ADMIN = 'Admin'
    SUBSCRIBER = 'Subscriber'


class BookAvailability(Enum):
    AVAILABLE = 'available'
    ON_LOAN = 'on_loan'
    RESERVED = 'reserved'
