from django.contrib import admin

from customer.models import Customer, Package, Word, Union
from bill.models import Bill, Invoice, BillHistory
from  user.models import CustomUser


admin.site.register(Customer)
admin.site.register(CustomUser)
admin.site.register(Bill)
admin.site.register(Invoice)
admin.site.register(Package)
admin.site.register(Word)
admin.site.register(Union)
admin.site.register(BillHistory)
