from django import forms


class JobPositionDto(forms.Form):
    job_code = forms.CharField(max_length=30, required=True)
    job_title = forms.CharField(max_length=30, required=True)
    created_date = forms.DateField(required=True)
    closed_date = forms.DateField(required=True),
    client = forms.CharField(max_length=30, required=True)
    department = forms.CharField(max_length=20, required=True)
    description = forms.CharField(max_length=50, required=True)
    attachfile = forms.CharField(max_length=20, required=False)
    min_ctc = forms.IntegerField( required=True)
    max_ctc = forms.IntegerField(required=True)
    prim_recruiter = forms.CharField(max_length=50, required=True)
    interviewers = forms.CharField(max_length=50, required=False)
    min_education = forms.CharField(max_length=30, required=False)
