from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from order_manager.models import Employee, Order


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", "probation")
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position", "probation")}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "position",
                        "probation",
                    )
                },
            ),
        )
    )
    list_filter = UserAdmin.list_filter + ("position", "probation")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ["task_id"]
    list_display = ["task_id", "employee"]
    list_filter = ["employee__username"]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("employee")
