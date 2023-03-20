from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import os

ALLOWED_FORMATS = ('.jpg','.png','.jpeg')

UPLOAD_FILE_MAX_SIZE = 1048576
# UPLOAD_FILE_MIN_SIZE = 

def is_image(file):
    file_format = os.path.splitext(file.name)[1]
  
    if file_format not in ALLOWED_FORMATS:
        raise ValidationError(_('invalid file format'))
    
    return file


def check_size(file):
    if file.size> UPLOAD_FILE_MAX_SIZE:
        raise ValidationError(_('file too large expecting 1mb at most'))
    return file