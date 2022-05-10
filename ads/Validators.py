from django.core.exceptions import ValidationError
from rest_framework import serializers
from datetime import date, timedelta


def check_positive(value: int) -> None:
    if value < 0:
        raise ValidationError(
            f'({value})s should be positive!'
        )


def status(value: str) -> None:
    if value == 'TRUE' or value == 'True':
        raise serializers.ValidationError('This field must be FALSE')


class ADVNotInStatusValidator:
    def __init__(self, statuses):
        if not isinstance(statuses, list):
            statuses = [statuses]

        self.statuses = statuses

    def __call__(self, value) -> None:
        if value in self.statuses:
            raise serializers.ValidationError("Incorrect status. This field must be FALSE")


def UserCreateCheckbirth_date(value: date) -> None:
    age = (date.today() - value) // timedelta(days=365.2425)
    # field_age = User.objects.filter(age__exact=value).exists()
    if age < 9:
        raise ValidationError(
            f'Your age must be more than 9 years old!'
        )


def UserCreateEmailDomen(value: str):
    if '@rambler.ru' in value:
        raise ValidationError(
            f'{value} should be not in domen rambler.ru'
        )


class UserCreateAge:
    def __call__(self, value: int):
        if value < 9:
            raise ValidationError(
                f'Your age must be more than 9 years old!'
            )
