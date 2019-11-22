from celery.schedules import crontab
from celery.task import periodic_task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from bill.models import Bill
from django.utils import timezone


@periodic_task(run_every=crontab(hour=0, minute=1))
def every_hour_work(request):
    bills = Bill.objects.all()
    for bill in bills:
        bill.celery_update = 10
        bill.save()

    return HttpResponseRedirect(reverse('customer:customer_list'))
