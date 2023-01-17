from typing import Dict, List

from core.decorators import api_interface
from core.exceptions import Conflict, NotFound
from db.book_models import Author
from db.db_actions import save_to_db
from logger import get_logger


class AuthorService:

    def __init__(self):
        self.logger = get_logger()

    def add_author(self, first_name: str, last_name: str) -> int:
        self.logger.info(f'About to add author: {first_name=} {last_name=}')
        author = Author(first_name=first_name, last_name=last_name)
        try:
            save_to_db(author)
        except Conflict:
            raise Conflict(f'{author} already exists')

        self.logger.info(f'{author=} added! ID={author.id}')
        return author.id

    def get_author(self, author_id: int) -> Dict:
        self.logger.info(f'About to get author {author_id=}')
        author = Author.query.get(author_id)

        if not author:
            raise NotFound('Author was not found')

        return author.json

    def get_authors(self) -> List[Dict]:
        self.logger.info(f'About to get all authors')
        authors = Author.query.all()

        return [author.json for author in authors]

    def update_author(self, author_id: int, updated_author: Dict) -> Dict:
        self.logger.info(f'About to update {author_id=}')
        author = Author.query.get(author_id)

        if first_name := updated_author.get('first_name'):
            author.first_name = first_name
        if last_name := updated_author.get('last_name'):
            author.last_name = last_name

        save_to_db(author)

        return author.json


author_svc = AuthorService()
