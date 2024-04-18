from django.contrib import admin
from drone.models import Visa
from drone.models import VisaTypes
from drone.models import VisaForm
from drone.models import UmraMonth
from drone.models import UmraPackage
from drone.models import UmraForm
from drone.models import CustomUmraForm
from drone.models import Holidays
from drone.models import HolidayForm
from drone.models import ContactForm

# Register your models here.
@admin.register(Visa)
class VisaAdmin(admin.ModelAdmin):
  list_display = [field.name for field in Visa._meta.fields]

@admin.register(VisaTypes)
class VisaTypesAdmin(admin.ModelAdmin):
  list_display = [field.name for field in VisaTypes._meta.fields]

@admin.register(VisaForm)
class VisaFormAdmin(admin.ModelAdmin):
  list_display = [field.name for field in VisaForm._meta.fields]

@admin.register(UmraMonth)
class UmraMonthsAdmin(admin.ModelAdmin):
  list_display = [field.name for field in UmraMonth._meta.fields]

@admin.register(UmraPackage)
class UmraPackageAdmin(admin.ModelAdmin):
  list_display = [field.name for field in UmraPackage._meta.fields]

@admin.register(UmraForm)
class UmraFormAdmin(admin.ModelAdmin):
  list_display = [field.name for field in UmraForm._meta.fields]

@admin.register(CustomUmraForm)
class CustomUmraFormAdmin(admin.ModelAdmin):
  list_display = [field.name for field in CustomUmraForm._meta.fields]

@admin.register(Holidays)
class PackagesmAdmin(admin.ModelAdmin):
  list_display = [field.name for field in Holidays._meta.fields]

@admin.register(HolidayForm)
class PackageFormAdmin(admin.ModelAdmin):
  list_display = [field.name for field in HolidayForm._meta.fields]

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
  list_display = [field.name for field in ContactForm._meta.fields]