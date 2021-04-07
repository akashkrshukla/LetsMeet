import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas
from django.db import models
from django.forms import forms
from django.http import HttpResponse, Http404
from django.shortcuts import render

from intellMEET import settings
from intellMEET.constants import CANDIDATE_IMAGE_PLACE_HOLDER
from intellMEET.models import Country, City, Academicqualification, Department, Customer, Socialmediasite


def get_salary(lakhs: int, thousands: int):
    if lakhs or thousands:
        return int(lakhs) * 100000 + int(thousands) * 10000
    else:

        return 0


def not_found_404(request: object):
    return render(request, 'errors/not_found_404.html')


def get_all_countries():
    return Country.objects.all()


def split_total_experience(total_experience: int):
    if total_experience is not None:
        return total_experience // 12, total_experience % 12
    else:
        return 1, 1


def handle_uploaded_file(file: models.FileField, folder: str, rel_path: str):
    if file is None:
        return ""
    full_path = os.path.join(os.getcwd(), folder)
    if os.path.exists(full_path):
        pass
    else:
        os.makedirs(full_path)
    destination = open(os.path.join(full_path, file.name), 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()
    return os.path.join(rel_path, file.name)


def split_salary_amount(salary: int):
    if salary is not None:
        return int(salary // 100000), int((salary % 100000) / 10000)
    else:
        return 0, 0


def get_total_experience(tot_exp_yr, tot_exp_month):
    return int(tot_exp_yr) * 12 + int(tot_exp_month)


def read_excel(file):
    data = list()
    df = pandas.read_excel(file)
    # df.shape[0] returns rows and df.shape[1] returns columns in the excel
    for row in range(0, df.shape[0]):
        data.insert(len(data), df.values[row])
    return data


def get_job_type(job_type: str):
    if job_type.__eq__("Permanent") or job_type.__eq__('0'):
        return 0
    elif job_type.__eq__("Part-time") or job_type.__eq__('1'):
        return 1
    elif job_type.__eq__("Contract") or job_type.__eq__('2'):
        return 2
    elif job_type.__eq__("Freelancer") or job_type.__eq__('3'):
        return 3
    else:
        return 0


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def get_all_cities():
    return City.objects.all()


def get_academic_qualifications():
    return Academicqualification.objects.all()


def get_all_department():
    return Department.objects.all()


def get_all_customers():
    return Customer.objects.all()


def get_job_stage(job_stage: str):
    if job_stage.__eq__('0'):
        return 0
    elif job_stage.__eq__('1'):
        return 1
    elif job_stage.__eq__('2'):
        return 2
    elif job_stage.__eq__('3'):
        return 3
    elif job_stage.__eq__('4'):
        return 4
    elif job_stage.__eq__('5'):
        return 5
    elif job_stage.__eq__('6'):
        return 6


def get_form_errors(request):
    try:
        errors = request.form_errors
        return errors
    except:
        return None


def get_relative_change(cr_value, pr_value):
    # cr_value: current value
    # pr_value: previous value (provided as per business logic to find change)
    if pr_value == 0:
        if cr_value == 0:
            return 0
        else:
            return 100
    else:
        return ((cr_value - pr_value) / pr_value) * 100


def get_social_media():
    return Socialmediasite.objects.all()


def send_mail(receiver: list, content: str, file):
    try:
        EMAIL_HOST = 'gsgpm1014.siteground.biz'
        EMAIL_HOST_USER = 'development@intellworx.com'
        EMAIL_HOST_PASSWORD = 'Dev@intellworx'
        port = 465  # for tls it's 465 else 587
        smtp_server = EMAIL_HOST
        sender_email = EMAIL_HOST_USER  # Host address for from in the email
        receiver_email = receiver  # receiver address
        password = EMAIL_HOST_PASSWORD
        message = MIMEMultipart('alternative')
        message['From'] = sender_email
        message['To'] = receiver
        message['Subject'] = 'Test email.'
        content = content
        message.attach(MIMEText(content, 'plaintext'))
        message.attach(MIMEText(content, 'html'))
        payload = MIMEBase('application', 'octet-stream')
        if file is None:
            pass
        else:
            payload.set_payload(open(file, 'rb').read())
            encoders.encode_base64(payload)  # encode the attachment
            payload.add_header('Content-Disposition', 'attachment', filename=file)
            message.attach(payload)
        text = message.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
        return
    except Exception as e:
        pass


def clean_date(self):
    cleaned_data = super().clean()
    start_date = cleaned_data.get("start_date")
    end_date = cleaned_data.get("end_date")
    if end_date < start_date:
        raise forms.ValidationError("End date should be greater than start date.")


def create_news_feed(initiator: str, initiator_detail: str, action: str, action_object: str,
                     action_object_details: str, feed_image_path=CANDIDATE_IMAGE_PLACE_HOLDER):
    # initiator : who
    # initiator_detail : link for initiator
    # action : created, joined as
    # action_object : Jobposition
    # action_object details
    # feed_image_path: Path for image to be shown by side of feed description.
    return initiator + "__" + initiator_detail + "__" + action + "__" + action_object + "__" + action_object_details + "__" + feed_image_path
    # "Akash" + "__" + "candidate_detail?cnd_id=" + "1" + "created" + "__" + "UI Developer" + "applicant_list?job_id=" + "1"
