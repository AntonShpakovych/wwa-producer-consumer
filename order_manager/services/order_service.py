from __future__ import annotations
from typing import Dict
from uuid import uuid4, UUID
from random import choice

from faker import Faker

from django.contrib.auth import get_user_model

from order_manager.models import Order


class OrderService:
    @classmethod
    def produce_order(cls) -> None:
        Order.objects.create(
            employee=cls.__generate_random_employee(),
            **cls.__generate_random_order_data()
        )

    @staticmethod
    def __generate_random_employee() -> get_user_model:
        return choice(get_user_model().objects.all())

    @staticmethod
    def __generate_random_order_data() -> Dict[str, str | UUID]:
        faker = Faker()

        return {
            "task_id": uuid4(),
            "name": faker.paragraph(nb_sentences=1),
            "description": faker.paragraph(nb_sentences=5)
        }
