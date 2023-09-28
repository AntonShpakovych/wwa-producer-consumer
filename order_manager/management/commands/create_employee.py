from django.core.management.base import BaseCommand
from order_manager.services.employee_service import EmployeeService


class Command(BaseCommand):
    help = "Create three records in Employee if they do not exist"

    def handle(self, *args, **kwargs):
        if EmployeeService.is_already_exists():
            self.stdout.write(self.style.SUCCESS("Employees already exist."))

        EmployeeService.produce_employee()
        self.stdout.write(self.style.SUCCESS("Successfully created records."))
