from django.shortcuts import render,redirect
from decouple import config
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.http import HttpResponse
from io import BytesIO
from xhtml2pdf import pisa
from cgi import escape
from parking_data.models import parking_daily_history as pdh
import pygal
from django.contrib.auth.decorators import login_required


def render_to_pdf(template_src, context_dict,to):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    email = EmailMessage(
    'Daily Parking History',
    'The attached pdf contains the detial',
    config("EMAIL_HOST_USER"),
    [to,],
    reply_to=['another@example.com'],
    headers={'Message-ID': 'foo'},
)
    if not pdf.err:
        email.attach('my_pdf.pdf', result.getvalue(), 'application/pdf')
        email.content_subtype = "html"
        email.send()
        return redirect("/")
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


@login_required(login_url='/accounts/login')
def pdfview(request):
    cars = pdh.objects.all()
    cars_no = cars.count()
    c_car = 0
    c_car = cars.filter(reserved=False).count()
    r_car = cars_no - c_car
    chrg = cars.filter(charged=True,reserved=False).count()
    unchrg = c_car - chrg
    if request.GET:
        to = ""
    elif request.POST:
        to = request.POST.get("to_email")
    print(to)
    template="pd/history.html"
    context={"cars":cars,"Unchrg":unchrg,
              "Chrg":chrg,"r_car":r_car,"total":cars_no,"c_car":c_car,"pagesize":'A4'}
    return render_to_pdf(template,context,to)


def signup(request):
    pass
    '''if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            print(form)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()

            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/registration.html', {'form': form})'''


def charts(request):    
    pass
    '''fw = fbp.objects.filter(status='waiting').count()
    fp = fbp.objects.filter(status='in progress').count()
    fc = fbp.objects.filter(status='completed').count()
    bw = bbp.objects.filter(status='waiting').count()
    bp = bbp.objects.filter(status='in progress').count()
    bc = bbp.objects.filter(status='completed').count()
    pie_chart1 = pygal.Pie(inner_radius=.4,print_values=True)
    pie_chart1.title = 'Bugs'
    pie_chart1.add('waiting', bw)
    pie_chart1.add('in progress', bp)
    pie_chart1.add('completed', bc)
    pie_chart2 = pygal.Pie(inner_radius=.4,print_values=True)
    pie_chart2.title = 'features'
    pie_chart2.add('waiting', fw)
    pie_chart2.add('in progress', fp)
    pie_chart2.add('completed', fc)
    feature = pie_chart2.render()
    bugs = pie_chart1.render()
    context = {"fc":feature,'bc':bugs}
    return render(request,"charts.html",context)'''

