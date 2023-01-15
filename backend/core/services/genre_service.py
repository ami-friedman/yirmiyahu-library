from typing import Dict, List

from core.decorators import api_interface
from core.exceptions import Conflict, NotFound
from db.book_models import Genre
from db.db_actions import save_to_db
from logger import get_logger


class GenreService:

    def __init__(self):
        self.logger = get_logger()

    def add_genre(self, name: str) -> int:
        self.logger.info(f'About to add genre: {name=}')
        genre = Genre(name=name)
        try:
            save_to_db(genre)
        except Conflict:
            raise Conflict(f'{genre=} already exists')

        self.logger.info(f'{genre=} added! ID={genre.id}')
        return genre.id

    def get_genre(self, genre_id: int) -> Dict:
        self.logger.info(f'About to get genre {genre_id=}')
        genre = Genre.query.get(genre_id)

        if not genre:
            raise NotFound('Genre was not found')

        return genre.json

    def get_genres(self) -> List[Dict]:
        self.logger.info(f'About to get all genres')
        genres = Genre.query.all()

        return [genre.json for genre in genres]

    def update_genre(self, genre_id: int, updated_genre: Dict) -> Dict:
        self.logger.info(f'About to update {genre_id=}')
        genre = Genre.query.get(genre_id)

        if name := updated_genre.get('name'):
            genre.name = name

        save_to_db(genre)

        return genre.json


genre_svc = GenreService()
