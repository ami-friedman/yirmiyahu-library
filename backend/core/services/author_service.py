from core.decorators import api_interface
from core.exceptions import Conflict
from db.db_models import Author, save_to_db
from logger import get_logger


class AuthorService:

    def __init__(self):
        self.logger = get_logger()

    @api_interface
    def add_author(self, first_name: str, last_name: str) -> int:
        self.logger.info(f'About to add author: {first_name=} {last_name=}')
        author = Author(first_name=first_name, last_name=last_name)
        try:
            save_to_db(author)
        except Conflict:
            self.logger.error(f'{author} already exists')
            raise

        self.logger.info(f'{author=} added! ID={author.id}')
        return author.id


author_svc = AuthorService()
