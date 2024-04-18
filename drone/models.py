from django.db import models

# Create your models here
class Visa(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  details = models.CharField(max_length=255)
  documents = models.TextField()
  special_note = models.TextField()
  start_price = models.CharField(max_length=255)
  currency = models.CharField(max_length=255)
  flag_image = models.CharField(max_length=255)

  class Meta:
    managed = False
    db_table = 'visa'

  def __str__(self):
    return self.name

class VisaTypes(models.Model):
  id = models.AutoField(primary_key=True)
  visa_id = models.IntegerField(primary_key=False)
  name = models.CharField(max_length=255)
  start_price = models.CharField(max_length=255)
  currency = models.CharField(max_length=255)
  proc_time = models.CharField(max_length=255)
  stay_period = models.CharField(max_length=255)
  visa_cat = models.CharField(max_length=255)
  entry = models.CharField(max_length=255)
  validity = models.CharField(max_length=255)

  class Meta:
    managed = False
    db_table = 'visa_type'

  def __str__(self):
    return self.name

class VisaForm(models.Model):
  fname = models.CharField(max_length=255)
  lname = models.CharField(max_length=255)
  mobile = models.CharField(max_length=255)
  email = models.EmailField()
  nationality = models.CharField(max_length=255)
  visa_qty = models.IntegerField(primary_key=False)
  visa_country = models.CharField(max_length=255)
  visa_type = models.CharField(max_length=255)
  message = models.TextField()
  created_at = models.DateTimeField()

  class Meta:
    managed = False
    db_table = 'visa_form'
  
  def __str__(self):
    return self.fname

class UmraMonth(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  start_date = models.DateField()
  end_date = models.DateField()
  hotel = models.CharField(max_length=255)
  airlines = models.CharField(max_length=255)
  start_price = models.CharField(max_length=255)

  class Meta:
    managed = False
    db_table = 'umra_month'

  def __str__(self):
    return self.name

class UmraPackage(models.Model):
  id = models.AutoField(primary_key=True)
  umra_month = models.ForeignKey(UmraMonth, on_delete=models.CASCADE)
  departure = models.DateField()
  arrival = models.DateField()
  airlines = models.CharField(max_length=255)
  hotel_makkah = models.CharField(max_length=255)
  hotel_makkah_dist = models.CharField(max_length=255)
  hotel_madina = models.CharField(max_length=255)
  hotel_madina_dist = models.CharField(max_length=255)
  price = models.CharField(max_length=255)

  class Meta:
    managed = False
    db_table = 'umrah_packages'

  def __str__(self):
    return self.id

class UmraForm(models.Model):
  fname = models.CharField(max_length=255)
  lname = models.CharField(max_length=255)
  mobile = models.CharField(max_length=255)
  email = models.EmailField()
  month = models.CharField(max_length=255)
  departure = models.CharField(max_length=255)
  total_people = models.CharField(max_length=255)
  message = models.TextField()
  created_at = models.DateTimeField()

  class Meta:
    managed = False
    db_table = 'umra_form'
  
  def __str__(self):
    return self.fname
    
class CustomUmraForm(models.Model):
  name = models.CharField(max_length=255)
  mobile = models.CharField(max_length=255)
  email = models.EmailField()
  total_persons = models.CharField(max_length=255)
  total_days = models.CharField(max_length=255)
  created_at = models.DateTimeField()

  class Meta:
    managed = False
    db_table = 'custom_umra_form'

  def __str__(self):
    return self.name
  
class Holidays(models.Model):
  id = models.AutoField(primary_key=True)
  country = models.CharField(max_length=255)
  region = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  price = models.CharField(max_length=255)
  duration_days = models.CharField(max_length=255)
  duration_nights = models.CharField(max_length=255)
  inclusion = models.TextField()
  room_sharing = models.CharField(max_length=255)
  cities = models.CharField(max_length=255)
  image1 = models.CharField(max_length=255)

  class Meta:
    managed = False
    db_table = 'packages'
  
  def __str__(self):
    return self.name

class HolidayForm(models.Model):
  fname = models.CharField(max_length=255)
  lname = models.CharField(max_length=255)
  mobile = models.CharField(max_length=255)
  email = models.EmailField()
  total_persons = models.IntegerField(primary_key=False)
  childrens = models.IntegerField(primary_key=False)
  travel_start = models.DateTimeField()
  travel_end = models.DateTimeField()
  created_at = models.DateTimeField()
  package_name = models.CharField(max_length=255)
  message = models.TextField()

  class Meta:
    managed = False
    db_table = 'package_form'
  
  def __str__(self):
    return self.fname

class ContactForm(models.Model):
  fname = models.CharField(max_length=255)
  lname = models.CharField(max_length=255)
  mobile = models.CharField(max_length=255)
  email = models.EmailField()
  message = models.TextField()
  created_at = models.DateTimeField()

  class Meta:
    managed = False
    db_table = 'contact_form'

  def __str__(self):
    return self.fname
