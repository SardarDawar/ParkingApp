from django.db import models
import datetime
from django.db.models.signals import post_save,post_delete,pre_delete
from django.dispatch import receiver
import datetime as dt
# Create your models here.
car_maker_op=(('Acura', 'Acura'), ('Audi', 'Audi'), ('BMW', 'BMW'), ('Buick', 'Buick'), ('Cadillac', 'Cadillac'), ('Chevrolet', 'Chevrolet'), ('Chrysler', 'Chrysler'), ('Dodge', 'Dodge'), ('Ford', 'Ford'), ('GMC', 'GMC'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('Infiniti', 'Infiniti'), ('Jaguar', 'Jaguar'), ('Jeep', 'Jeep'), ('Kia', 'Kia'), ('Land Rover', 'Land Rover'), ('Lexus', 'Lexus'), ('Mazda', 'Mazda'), ('Mercedes Benz', 'Mercedes Benz'), ('Mini', 'Mini'), ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan'), ('Ram', 'Ram'), ('Subaru', 'Subaru'), ('Tesla', 'Tesla'), ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo'))


class parking_slot(models.Model):
    colors_op = (("Black","Black"), ("White","White"),("Green","Green"), ("Grey","Grey"),
     ("Blue","Blue"), ("Red","Red"), ("Yellow","Yellow"),("Beige","Beige"))
    reserved_slot=27
    customer_slots=27
    r_av = 27
    c_av = 27
    car_model = models.CharField(max_length=15)
    car_color = models.CharField(max_length=10,choices=colors_op,default="Black")
    car_maker = models.CharField(max_length=20,choices=car_maker_op,default='Acura')
    reg_num = models.CharField(max_length=10)
    slot_no = models.CharField(max_length=3,unique=True)
    start_tm = models.DateTimeField(auto_now_add=True)
    updated_tm = models.DateTimeField(auto_now=True)
    charged = models.BooleanField(default=False)
    limit = models.PositiveIntegerField(default=7,null=True,blank=True)
    limit_reached = models.BooleanField(default=False)

    class Meta:
        ordering = ('start_tm',)

    def __str__(self):
        return self.slot_no   

    def due_time(self):
        if self.limit==1:
            due = self.start_tm+dt.timedelta(minutes=30)
        elif self.limit==2:
            due = self.start_tm+dt.timedelta(minutes=45)
        elif self.limit==3:
            due = self.start_tm+dt.timedelta(hours=1)
        elif self.limit==4:
            due = self.start_tm+dt.timedelta(hours=1,minutes=30)
        elif self.limit==5:
            due = self.start_tm+dt.timedelta(hours=2)
        elif self.limit==6:
            due = self.start_tm+dt.timedelta(hours=2,minutes=15)
        else:
            due = self.start_tm+dt.timedelta(seconds=10)
        return due
     
class parking_daily_history(models.Model):
    car_model = models.CharField(max_length=15,null=True)
    reg_num = models.CharField(max_length=10,null=True)
    start_tm = models.DateTimeField()
    end_tm = models.DateTimeField()
    charged = models.BooleanField(default=False)
    reserved = models.BooleanField(default=False)

    @receiver(pre_delete, sender=parking_slot)
    def create_history(sender, instance, **kwargs):
        car=instance.car_model
        reg_num=instance.reg_num
        start_tm=instance.start_tm
        end_tm=instance.updated_tm
        charged = instance.charged
        reserved = instance.slot_no.startswith("r")
        parking_daily_history.objects.create(car_model=car,reg_num=reg_num,start_tm=start_tm,end_tm=end_tm,charged=charged)

    def duration(self):
        return self.end_tm-self.start_tm