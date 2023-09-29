import os
from typing import Dict

from django.contrib.auth import get_user_model

from faker import Faker


class EmployeeService:
    VALID_EMPLOYEE_QUANTITY = 3

    @classmethod
    def produce_employee(cls) -> None:
        num_employees = get_user_model().objects.count()

        for _ in range(cls.VALID_EMPLOYEE_QUANTITY - num_employees):
            get_user_model().objects.create_user(
                **cls.__generate_random_employee_data()
            )

        admin_exist = get_user_model().objects.filter(is_staff=True).count()

        if not admin_exist:
            get_user_model().objects.create_superuser(
                **cls.__generate_static_admin_data()
            )

    @classmethod
    def is_already_exists(cls) -> bool:
        return get_user_model().objects.count() == 3

    @staticmethod
    def __generate_random_employee_data() -> Dict[str, str]:
        faker = Faker()

        return {
            "username": faker.user_name(),
            "password": os.getenv("USER_PASSWORD")
        }

    @staticmethod
    def __generate_static_admin_data() -> Dict[str, str]:
        return {
            "username": os.getenv("ADMIN_USERNAME"),
            "password": os.getenv("ADMIN_PASSWORD"),
        }
