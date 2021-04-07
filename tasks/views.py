from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render
from intellMEET.models import Interview


def task_list(request):
    next_seven_days = datetime.today() + timedelta(days=7)
    interviews = Interview.objects.filter(interviewdate__lte=next_seven_days, created_by=request.user)

    for interview in interviews:
        interview.starttime = interview.interviewdate.replace(hour=interview.fkinterviewslot.starttime.hour,
                                                              minute=interview.fkinterviewslot.starttime.minute).timestamp()
        interview.endtime = interview.interviewdate.replace(hour=interview.fkinterviewslot.endtime.hour,
                                                            minute=interview.fkinterviewslot.endtime.minute).timestamp()
    return render(request, "task/tasks.html", {"interviews": interviews})
