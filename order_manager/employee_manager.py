from django.contrib.auth.base_user import BaseUserManager


class EmployeeManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
            self,
            username: str,
            password: str,
            probation: bool = None,
            position: str = None,
            email: str = None,
            **extra_fields
    ):
        if not username:
            raise ValueError("Username field required")

        if not password:
            raise ValueError("Password field required")

        user = self.model(
            username=username,
            **extra_fields
        )

        if email:
            user.email = self.normalize_email(email)
        if probation:
            user.probation = probation
        if position:
            user.position = position

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(
            self,
            username: str,
            password: str,
            probation: bool = None,
            position: str = None,
            email: str = None,
            **extra_fields
    ):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(
            username=username,
            password=password,
            probation=probation,
            position=position,
            email=email,
            **extra_fields
        )

    def create_superuser(
            self,
            username: str,
            password: str,
            **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            username=username,
            password=password,
            position=self.model.PositionChoices.SENIOR,
            probation=False,
            **extra_fields
        )
