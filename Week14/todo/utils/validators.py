from django.core.exceptions import ValidationError
import os

ALLOWED_EXTENSIONS = ['.jpg', '.png']
MAZ_SIZE = 1024000000000000000000000000000000000000000000000000000000000


def validate_file_size(value):
    if value.size > MAZ_SIZE:
        raise ValidationError('Photo can not be so big')


def validate_extension(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if not ext.lower() in ALLOWED_EXTENSIONS:
            raise ValidationError(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')
