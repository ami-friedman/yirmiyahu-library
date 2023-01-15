from typing import Dict, List

from core.decorators import api_interface
from core.exceptions import Conflict, NotFound
from db.book_models import Category
from db.db_actions import save_to_db
from logger import get_logger


class CategoryService:

    def __init__(self):
        self.logger = get_logger()

    def add_category(self, name: str) -> int:
        self.logger.info(f'About to add category: {name=}')
        category = Category(name=name)
        try:
            save_to_db(category)
        except Conflict:
            raise Conflict(f'{category=} already exists')

        self.logger.info(f'{category=} added! ID={category.id}')
        return category.id

    def get_category(self, category_id: int) -> Dict:
        self.logger.info(f'About to get category {category_id=}')
        category = Category.query.get(category_id)

        if not category:
            raise NotFound('Category was not found')

        return category.json

    def get_categories(self) -> List[Dict]:
        self.logger.info(f'About to get all categories')
        categories = Category.query.all()

        return [category.json for category in categories]

    def update_category(self, category_id: int, updated_category: Dict) -> Dict:
        self.logger.info(f'About to update {category_id=}')
        category = Category.query.get(category_id)

        if name := updated_category.get('name'):
            category.name = name

        save_to_db(category)

        return category.json


category_svc = CategoryService()
