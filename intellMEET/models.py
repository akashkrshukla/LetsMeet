from django.db import models


class Candidate(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    resume = models.CharField(db_column='Resume', max_length=250)  # Field name made lowercase.
    email = models.CharField(max_length=100)
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    lastmodifed = models.DateTimeField(db_column='LastModifed')  # Field name made lowercase.
    candidate_image = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    mobileno = models.CharField(max_length=100, blank=True, null=True)
    current_company = models.CharField(max_length=100, blank=True, null=True)
    current_position = models.CharField(max_length=100, blank=True, null=True)
    total_experience = models.IntegerField(blank=True, null=True)
    current_salary = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    expected_salary = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    notice_period_days = models.IntegerField(blank=True, null=True)
    job_type = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    fkcandidatesource = models.ForeignKey('Candidatesource', models.DO_NOTHING, db_column='fkCandidateSource',
                                          blank=True, null=True)  # Field name made lowercase.
    fkcity = models.ForeignKey('City', models.DO_NOTHING, db_column='fkCity', blank=True,
                               null=True)  # Field name made lowercase.
    fkcountry = models.ForeignKey('Country', models.DO_NOTHING, db_column='fkCountry', blank=True,
                                  null=True)  # Field name made lowercase.
    street_name = models.CharField(max_length=30, blank=True, null=True)
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate'


class Candidateexperience(models.Model):
    company = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    current_employer = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    job_type = models.CharField(max_length=1, blank=True, null=True)
    salary = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    fkcandidate = models.ForeignKey(Candidate, models.DO_NOTHING, db_column='fkCandidate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'candidateexperience'


class Candidateskill(models.Model):
    skill = models.CharField(db_column='Skill', max_length=30)  # Field name made lowercase.
    fkcandidate = models.ForeignKey('Candidate', models.DO_NOTHING,
                                    db_column='fkCandidate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'candidateskill'


class Candidatesource(models.Model):
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'candidatesource'


class City(models.Model):
    id = models.CharField(primary_key=True, max_length=11)
    cityname = models.CharField(db_column='CityName', max_length=30)  # Field name made lowercase.
    fkcountry = models.ForeignKey('Country', models.DO_NOTHING, db_column='fkCountry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    countryname = models.CharField(db_column='CountryName', primary_key=True,
                                   max_length=100)  # Field name made lowercase.
    lastmodifed = models.DateTimeField(db_column='LastModifed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    companyno = models.CharField(db_column='CompanyNo', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=250, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fkcountry = models.ForeignKey(Country, models.DO_NOTHING, db_column='fkCountry')  # Field name made lowercase.
    postcode = models.CharField(db_column='Postcode', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'


class Department(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=30)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    fkcustomer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='fkCustomer')  # Field name made lowercase.
    departmentowner = models.CharField(db_column='DepartmentOwner', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Department'


class Jobposition(models.Model):
    positioncode = models.CharField(db_column='PositionCode', primary_key=True,
                                    max_length=30)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=30)  # Field name made lowercase.
    jobdecription = models.TextField(db_column='JobDecription')  # Field name made lowercase.
    posteddate = models.DateField(db_column='PostedDate')  # Field name made lowercase.
    closedate = models.DateField(db_column='CloseDate')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    fkcustomer = models.ForeignKey('Customer', models.DO_NOTHING, db_column='fkCustomer')  # Field name made lowercase.
    fkdepartment = models.ForeignKey('Department', models.DO_NOTHING,
                                     db_column='fkDepartment')  # Field name made lowercase.
    fkcountry = models.ForeignKey('Country', models.DO_NOTHING, db_column='fkCountry')  # Field name made lowercase.
    fkcity = models.ForeignKey('City', models.DO_NOTHING, db_column='fkCity',
                               max_length=30)  # Field name made lowercase.
    lastmodifed = models.DateTimeField(db_column='LastModifed')  # Field name made lowercase.
    companydepartmentname = models.CharField(db_column='CompanyDepartmentName', max_length=100, blank=True,
                                             null=True)  # Field name made lowercase.
    attachfile = models.CharField(db_column='attachFile', max_length=70)  # Field name made lowercase.
    keyskills = models.CharField(max_length=70)
    jobtype = models.CharField(db_column='jobType', max_length=70)  # Field name made lowercase.
    fkacademicqualification = models.ForeignKey('Academicqualification', models.DO_NOTHING,
                                                db_column='fkacademicqualification',
                                                max_length=30)  # Field name made lowercase.
    minexperience = models.IntegerField()
    maxexperience = models.IntegerField()
    minpackage = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    maxpackage = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    certification = models.CharField(max_length=70)
    otherinfo = models.CharField(db_column='otherInfo', max_length=70)  # Field name made lowercase.
    created_by = models.CharField(max_length=150, blank=True, null=True)
    fkRoleUser = models.ForeignKey('Roleuser', db_column='fkRoleUser', on_delete=models.DO_NOTHING)
    openings = models.IntegerField(db_column='openings', null=True)
    interviewers = models.CharField(max_length=300, db_column="interviewers", null=True, blank=True)
    slottype = models.IntegerField(db_column='slottype', null=False, blank=False, default=1)

    class Meta:
        managed = True
        db_table = 'Jobposition'


class Jobapplication(models.Model):
    fkcandidate = models.ForeignKey(Candidate, models.DO_NOTHING, db_column='fkCandidate')  # Field name made lowercase.
    fkjobposition = models.ForeignKey(Jobposition, models.DO_NOTHING,
                                      db_column='fkJobPosition')  # Field name made lowercase.
    applieddate = models.DateField(db_column='AppliedDate')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30)  # Field name made lowercase.
    lastmodifed = models.DateTimeField(db_column='LastModifed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Jobapplication'


class Recruitmentprocess(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    processtitle = models.CharField(db_column='ProcessTitle', max_length=100)  # Field name made lowercase.
    processdecription = models.CharField(db_column='ProcessDecription', max_length=255)  # Field name made lowercase.
    processtype = models.CharField(db_column='ProcessType', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    processorder = models.IntegerField(db_column='ProcessOrder', blank=True, null=True)  # Field name made lowercase.
    fkjobposition = models.CharField(db_column='fkJobPosition', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recruitmentprocess'


class Interview(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    interviewdate = models.DateTimeField(db_column='InterviewDate')  # Field name made lowercase.
    interviewtype = models.CharField(db_column='InterviewType', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    fkjobapplication = models.ForeignKey('Jobapplication', models.DO_NOTHING,
                                         db_column='fkJobApplication')  # Field name made lowercase.
    fkrecruitmentprocess = models.ForeignKey('Recruitmentprocess', models.DO_NOTHING, db_column='fkRecruitmentProcess',
                                             blank=True, null=True)  # Field name made lowercase.
    lastmodifed = models.DateTimeField(db_column='LastModifed')  # Field name made lowercase.
    created_by = models.CharField(max_length=150, blank=True, null=True)
    fkinterviewslot = models.ForeignKey('InterviewSlot', models.DO_NOTHING, db_column='fkInterviewslot',
                                        blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Interview'


class Interviewpack(models.Model):
    fkjobposition = models.ForeignKey('Jobposition', models.DO_NOTHING,
                                      db_column='fkJobPosition')  # Field name made lowercase.
    interviewtotaltime = models.IntegerField(db_column='InterviewTotalTime')  # Field name made lowercase.
    lastmodifed = models.DateTimeField(db_column='LastModifed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InterviewPack'


class Academicqualification(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AcademicQualification'


class Role(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=1)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class Roleuser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=150)
    profilepicture = models.ImageField(upload_to='userprofile/')
    description = models.CharField(max_length=250)
    fkrole = models.ForeignKey(Role, models.DO_NOTHING, db_column='fkRole')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roleuser'


class Interviewer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    fkcustomer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='fkCustomer')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    designation = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    interviewerimage = models.CharField(db_column='interviewerImage', max_length=100, blank=True,
                                        null=True)  # Field name made lowercase.
    fkuser = models.CharField(db_column='fkUser', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lastmodifed = models.DateTimeField(db_column='LastModifed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Interviewer'


class Interviewpanel(models.Model):
    fkinterviewer = models.ForeignKey('Interviewer', models.DO_NOTHING,
                                      db_column='fkInterviewer')  # Field name made lowercase.
    fkJobPosition = models.ForeignKey(Jobposition, models.DO_NOTHING,
                                      db_column='fkJobPosition')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InterviewPanel'


class Brand(models.Model):
    logofilepath = models.CharField(db_column='LogoFilePath', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    bannerfilepath = models.CharField(db_column='BannerFilePath', max_length=100, blank=True,
                                      null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, blank=True,
                                   null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fkcustomer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='fkCustomer')  # Field name made lowercase.
    fkbrandingTemplate = models.ForeignKey("BrandingTemplate", models.DO_NOTHING, db_column='fkbrandingTemplate',
                                           null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'brand'

class Brandsection(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    titlecolor = models.CharField(max_length=6, blank=True, null=True)
    textcolor = models.CharField(max_length=6, blank=True, null=True)
    fkbrand = models.ForeignKey(Brand, models.DO_NOTHING, db_column='fkbrand')
    # position = models.IntegerField(null=True, blank = True)

    class Meta:
        managed = False
        db_table = 'brandsection'


class Sectionmedia(models.Model):
    mediapatch = models.IntegerField()
    fksection = models.ForeignKey(Brandsection, models.DO_NOTHING, db_column='fksection')

    class Meta:
        managed = False
        db_table = 'sectionmedia'

class Socialmedialink(models.Model):
    url = models.CharField(max_length=100)
    fkbrand = models.ForeignKey(Brand, db_column='fkBrand', on_delete=models.DO_NOTHING, max_length=30)  # Field name made lowercase.
    fkmediasite = models.ForeignKey('Socialmediasite', models.DO_NOTHING, db_column='fkmediasite')

    class Meta:
        managed = False
        db_table = 'socialmedialink'


class Socialmediasite(models.Model):
    sitelabel = models.CharField(db_column='SiteLabel', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    sitelogo = models.CharField(db_column='SiteLogo', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'socialmediasite'


class NewsFeed(models.Model):
    date = models.DateTimeField(db_column='date')  # Field name made lowercase.
    news_feed = models.CharField(db_column='news_feed', max_length=1500,)
    created_by = models.CharField(max_length=50, )

    class Meta:
        managed = True
        db_table = 'newsfeed'


class InterviewSlot(models.Model):
    starttime = models.TimeField(db_column='starttime', null=False)
    endtime = models.TimeField(db_column='endtime', null=False)
    slottype = models.IntegerField(db_column="slottype", null=False, blank=False, default=1)

    class Meta:
        managed = True
        db_table = 'interviewslot'


class BrandingTemplate(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30, null=False, blank=False)
    thumbnailpath = models.CharField(max_length=50, null=True, blank=True)
    cssfilepath = models.CharField(max_length=50, null=True, blank=True)
    status = models.IntegerField(default=1, null=True)

    class Meta:
        managed = True
        db_table = 'brandingtemplate'


class Interviewrole(models.Model):
    status = models.CharField(max_length=1, blank=True, null=True)
    fkroleuser = models.IntegerField(db_column='fkRoleUser')  # Field name made lowercase.
    fkinterview = models.IntegerField(db_column='fkInterview')  # Field name made lowercase.
    fktransferroleuser = models.IntegerField(db_column='fkTransferRoleUser', blank=True, null=True)  # Field name made lowercase.
    fkproposedinterviewslot = models.IntegerField(db_column='fkProposedInterviewslot', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InterviewRole'
