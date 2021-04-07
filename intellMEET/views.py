from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.db.models import Count, Max, F, Q
from django.shortcuts import render
from django.template.response import TemplateResponse

from intellMEET.constants import LIMITED_DATA_DISPLAY_COUNT, job_position
from intellMEET.models import Interview, Jobposition, Jobapplication, Interviewpanel, NewsFeed
from intellMEET.utils import get_all_department


@login_required
def home(request):
    next_seven_days = datetime.today() + timedelta(days=7)
    # showing the top 7 results
    interviews = Interview.objects.filter(interviewdate__lte=next_seven_days,
                                          created_by=request.user)[:LIMITED_DATA_DISPLAY_COUNT]

    # aCount: Application count
    trend_job_application = Jobapplication.objects.values(
        'fkjobposition', 'fkjobposition__positioncode', 'fkjobposition__created_by',
        'fkjobposition__status', 'fkjobposition__jobtitle'
        ).annotate(
        aCount=Count(F('fkjobposition'))).all().order_by('-aCount')

    # ivCount: interviewer Count
    top_interviewers = Interviewpanel.objects.values(
        'fkinterviewer', 'fkinterviewer__email', 'fkinterviewer__name', 'fkinterviewer__designation').annotate(
        ivCount=Count(F('fkinterviewer'))).all().order_by('-ivCount')
    total_jobs = Jobposition.objects.all().count()
    closed_jobs = Jobposition.objects.filter(status=job_position.get('CLOSED_CODE')).count()
    under_process_jobs = Jobposition.objects.filter(
        ~Q(status__in=(job_position.get('CLOSED_CODE'), job_position.get('ARCHIVED_CODE')))).count()
    onhold_jobs = Jobposition.objects.filter(status=job_position.get('ON_HOLD')).count()
    action_required = Jobposition.objects.filter(
        ~Q(status=job_position.get('ARCHIVED_CODE')), jobapplication__isnull=True).count()
    # get department data
    departments = get_all_department()
    for item in departments:
        item.total_jobs, item.completed_jobs = Jobposition.objects.filter(fkdepartment=item).count(), \
                                               Jobposition.objects.filter(status=job_position.get('CLOSED_CODE'),
                                                                          fkdepartment=item).count()
    if request.method == 'POST':
        return TemplateResponse(request, 'index.html', {'interviews': interviews,
                                                        'top_jobs': trend_job_application,
                                                        'top_interviewers': top_interviewers,
                                                        'total_jobs': total_jobs,
                                                        'closed_jobs_count': closed_jobs,
                                                        'under_process_jobs': under_process_jobs,
                                                        'onhold_jobs': onhold_jobs,
                                                        'action_required': action_required,
                                                        'departments': departments,
                                                        })
    return TemplateResponse(request, 'index.html', {'interviews': interviews,
                                                    'top_jobs': trend_job_application,
                                                    'top_interviewers': top_interviewers,
                                                    'total_jobs': total_jobs,
                                                    'closed_jobs_count': closed_jobs,
                                                    'under_process_jobs': under_process_jobs,
                                                    'onhold_jobs': onhold_jobs,
                                                    'action_required': action_required,
                                                    'departments': departments,
                                                    })


def get_news_feed(request):
    news_feeds = NewsFeed.objects.all().order_by("-id")
    for feed in news_feeds:
        attributes = feed.news_feed.split("__")
        feed.attribute = attributes
    return render(request, 'news_feed_list.html', {'news_feeds': news_feeds})
