from .exceptions import ValidationError

def validate_length(field_name: str, value: str, max_length: int):
    if len(value) > max_length:
        raise ValidationError(f"{field_name} exceeds max length of {max_length}")
