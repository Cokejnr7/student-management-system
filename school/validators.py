from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


    
def valid_level(level):
    if level > 6:
        raise ValidationError(_("No level higher than 6"))
    
    elif level<1:
        raise ValidationError(_("No level less than 1"))
    
    
def valid_unit(unit):
    if unit > 6 :
        raise ValidationError(_("No unit higher than 6"))
    
    elif unit<1:
        raise ValidationError(_("No unit less than 1"))