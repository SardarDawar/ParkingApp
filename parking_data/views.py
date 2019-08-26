from django.shortcuts import render,redirect    
from .models import parking_slot as ps,parking_daily_history as pdh
from .forms import CarEnterForm
import pygal
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def uncharged():
    pcs = ps.objects.filter(limit_reached=False,slot_no__icontains="P") ## pc stands for present_car
    for pc in pcs:
        pc.save()
        if pc.due_time() <= pc.updated_tm:
            pc.limit_reached=True
            pc.save()
    unchrg = ps.objects.filter(limit_reached=True,charged=False)
    return unchrg

def charged():
    chrg = ps.objects.filter(limit_reached=True,charged=True)
    return chrg

@login_required(login_url='/accounts/login')
def Front_Page(request):
    template_name = "FPage.html"
    context = {}
    return render(request,template_name,context)
    
#notify
@login_required(login_url='/accounts/login')
def Car_type(request,let):
    template_name = "parkinglist.html"
    C=[]
    j=0
    if let=="R":
        parking = "Reserved"
        for i in range(0,27):
            if i < 9:
                C.append(let+"0"+str(i+1))                
            else:
                C.append(let+str(i+1))
        parked = ps.objects.filter(slot_no__icontains="R").__str__()
    elif let=="P":
        parking = "Public"
        for i in range(0,20):
            j=i+20
            if i < 9:
                C.append((let+"0"+str(i+1),let+str(j+1)))
            else:           
                C.append((let+str(i+1),let+str(j+1)))
        parked = ps.objects.filter(slot_no__icontains="P").__str__()
    unchrg = uncharged()
    chrg = charged()
    context = {"count":C,"type":let,"parking":parking,"parked":parked,"notify":unchrg,
                "notification": chrg.__str__()
              }
    return render(request,template_name,context)

@login_required(login_url='/accounts/login')
def All_Cars(request):
    pcs = ps.objects.all()
    template_name = "all_cars.html"
    context = {"cars":pcs}
    return render(request,template_name,context)

############ This is called via JQUERY AJAX POST REQUEST and also in notifications ############
@login_required(login_url='/accounts/login')
def update_cars(request):
    pcs = ps.objects.filter(limit_reached=False,slot_no__icontains="P") ## pc stands for present_car
    for pc in pcs:
        pc.save()
        if pc.due_time() <= pc.updated_tm:
            pc.limit_reached=True
            pc.save()
    unchrg = ps.objects.filter(limit_reached=True,charged=False)
    context = {"notify":unchrg}
    template_name ="pd/notifications.html"
    return render(request,template_name,context)

@login_required(login_url='/accounts/login')
def car_charge(request,id):
    car=ps.objects.get(slot_no=id)
    car.charged=True
    car.save()
    return redirect("/data/type/"+id[0]+"/")


@login_required(login_url='/accounts/login')
def car_left(request,id):
    car=ps.objects.get(slot_no=id)
    car.save()
    car.delete()
    return redirect("/data/type/"+id[0]+"/")

##################### ENTER FORM PAGE #################### notify
@login_required(login_url='/accounts/login')
def car_entered(request,slot): ### This view loads the car enter form page
    slot_no = slot
    endt=0
    try:             # Checks if any car is already parked or not
        parked = ps.objects.get(slot_no=slot_no)
        endt = ps.due_time
    except:
        parked = 0
    if request.POST:  # POST request is only received from an empty slot
        model = request.POST.get('car_model')
        reg_num = request.POST.get('reg_num')
        slot = request.POST.get('slot_no')
        limit = request.POST.get('limit')
        ps.objects.create(car_model=model,reg_num=reg_num,slot_no=slot,limit=limit)
        return redirect("/data/type/"+slot[0]+"/")
    if slot[0] == "P":   # This check is used to determine whether time input is to be shown or not
        show_time = True
    else: 
        show_time = False
    template_name="enter_page.html"
    context={"slot":slot_no,"filled":parked,"fin":endt,'show_time':show_time}
    return render(request,template_name,context)

########### REMOVE CAR REQUEST ############
@login_required(login_url='/accounts/login')
def car_remove(request):
    template = "pd/remove.html"
    if request.POST:
        reg_num = request.POST.get("reg_num")
        search=ps.objects.filter(reg_num__icontains=reg_num)
        context = {"results":search}
        return render(request,template,context)
    return render(request,template)

############ RENDERS CAR PARKED HISTORY ###########
@login_required(login_url='/accounts/login')
def park_hist(request):
    cars = pdh.objects.all()
    #### charting ####
    cars_no = cars.count()
    c_car = 0
    c_car = cars.filter(reserved=False).count()
    r_car = cars_no - c_car
    chrg = cars.filter(charged=True,reserved=False).count()
    unchrg = c_car - chrg
    pie_chart1 = pygal.Pie(print_values=True)
    pie_chart1.title = 'Summary'    
    pie_chart1.add("Unchrg cstmr",unchrg)
    pie_chart1.add("Chrg cstmr",chrg)
    pie_chart1.add("Reserved",r_car)
    chart = pie_chart1.render()
    context={"cars":cars,"chart":chart,"Unchrg":unchrg,
              "Chrg":chrg,"r_car":r_car,"total":cars_no,"c_car":c_car}
    template="pd/history.html"
    return render(request,template,context)

def charts():
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

