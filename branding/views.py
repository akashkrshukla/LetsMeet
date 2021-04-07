import os

from django.db.models import Q
from django.shortcuts import render, redirect

from intellMEET import settings
from intellMEET.models import Brand, Customer, Socialmedialink, Socialmediasite, Brandsection, \
    BrandingTemplate
from intellMEET.utils import handle_uploaded_file, get_all_customers, get_social_media


def show_branding_customer(request: object):
    brand_templates = BrandingTemplate.objects.filter(~Q(status=0))
    return render(request, 'branding/branding.html', {'clients': get_all_customers(),
                                                      'brand_templates': brand_templates})


# TO DO
# change the customer value & match.
def save_branding(request: object):
    if request.method == 'POST':
        if settings.PRINT_LOG is True:
            print(request.POST)
        customer = Customer.objects.filter(id=request.POST.get('client')).first()

        logo = handle_uploaded_file(request.FILES.get('logo'),
                                    os.path.join('static', 'media', 'branding', str(customer.id)),
                                    os.path.join('media', 'branding', str(customer.id))
                                    )
        banner = handle_uploaded_file(request.FILES.get('banner'),
                                      os.path.join('static', 'media', 'branding', str(customer.id)),
                                      os.path.join('media', 'branding', str(customer.id))
                                      )
        if settings.PRINT_LOG is True:
            print(customer)
        brand = Brand.objects.filter(fkcustomer=customer).first()
        data = request.POST
        if brand is None:
            brand = Brand(logofilepath=logo, bannerfilepath=banner,
                          description=data.get('description'), fkcustomer=customer,
                          website=data.get('company_website'))
        else:
            # file path will always be greater than 2
            if len(logo) > 2:
                brand.logofilepath = logo
            if len(banner) > 2:
                brand.bannerfilepath = banner
            brand.description = data.get('description')
            brand.website = data.get('company_website')

        brand.save()
        links = str(request.POST.get('social_media_link')).split(',')
        Socialmedialink.objects.filter(fkbrand=brand).delete()
        for link in links:
            # links are of the form "url + 'platform'". Hence split on + will return array where first element
            # the content of link and second element is the platform of that link
            link_data = str(link).split('+')
            if len(link_data) > 1:
                label = link_data[1]
                social_media_web = Socialmediasite.objects.filter(sitelabel=label).first()
                social_link, created = Socialmedialink.objects.get_or_create(fkmediasite=social_media_web,
                                                                             fkbrand=brand)
                social_link.url = link_data[0]
                social_link.save()
            else:
                pass
                # social links are not passed/all have been deleted
        return redirect('branding')


def get_branding_data(request: object):
    if settings.PRINT_LOG is True:
        print(request.GET.get('client'))
    customer = Customer.objects.get(id=request.GET.get('client'))
    branding = Brand.objects.filter(fkcustomer=customer).first()
    social_links = Socialmedialink.objects.filter(fkbrand=branding)
    brand_templates = BrandingTemplate.objects.filter(~Q(status=0))
    direc = os.path.join(settings.MEDIA_ROOT, 'branding', customer.id)
    prev_files = list()
    if os.path.exists(direc) and os.path.isdir(direc):
        prev_files = os.listdir(direc)
    brand_sections = Brandsection.objects.filter(fkbrand=branding)
    return render(request, 'branding/branding.html', {'branding': branding,
                                                      'clients': get_all_customers(),
                                                      'sel_customer': customer,
                                                      'social_media_options': get_social_media(),
                                                      'social_links': social_links,
                                                      'brand_templates': brand_templates,
                                                      'prev_files': prev_files,
                                                      'brand_sections': brand_sections})


def show_preview(request: object):
    customer = Customer.objects.get(id=request.GET.get('client'))
    branding = Brand.objects.filter(fkcustomer=customer).first()
    social_links = Socialmedialink.objects.filter(fkbrand=branding)
    brand_sections = Brandsection.objects.filter(fkbrand=branding)
    return render(request, 'branding/company-profile.html', {'branding': branding,
                                                             'client': customer,
                                                             'social_links': social_links,
                                                             'brand_sections': brand_sections})


def add_section(request: object):
    customer = Customer.objects.filter(id=request.GET.get('client')).first()
    if settings.PRINT_LOG is True:
        print(customer)
    if customer is None:
        # do not save and return data since customer is not selected yet.
        # throw error message to choose the customer first
        return show_branding_customer(request)
    else:
        data = request.POST
        brand_section = Brandsection(fkbrand=Brand.objects.filter(fkcustomer=customer).first(),
                                     titlecolor=data.get('section_color')[1:], textcolor=data.get('text_color')[1:],
                                     content=data.get('section_content'), title=data.get('section_title'))
        brand_section.save()
        return redirect('branding')


def save_template(request: object):
    if settings.PRINT_LOG is True:
        print(request.POST)
    template = BrandingTemplate.objects.filter(id=request.POST.get('template')).first()
    brand = Brand.objects.filter(id=request.POST.get('branding')).first()
    brand.fkbrandingTemplate_id = template
    brand.save()
    return redirect('branding')
