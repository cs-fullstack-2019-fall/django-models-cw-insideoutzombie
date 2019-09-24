from django.contrib import admin

# Register your models here.
from .models import DogData

admin.site.register(DogData)


# from .models import BankUsers
# from .models import BankEmployees
#
# admin.site.register(BankUser)
# admin.site.register(BankEmployees)
