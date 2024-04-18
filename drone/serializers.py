from rest_framework import serializers
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

class VisaTypesSerializer(serializers.ModelSerializer):
  class Meta:
    model = VisaTypes
    fields = '__all__'

class VisaSerializer(serializers.ModelSerializer):
  visa_types = serializers.SerializerMethodField()
  class Meta:
    model = Visa
    fields = ['id', 'name', 'details', 'documents', 'special_note', 'start_price', 'currency', 'flag_image', 'visa_types']

  def get_visa_types(self, obj):
    visa_types = VisaTypes.objects.filter(visa_id=obj.id)
    return VisaTypesSerializer(visa_types, many=True).data

class VisaFormSerializer(serializers.ModelSerializer):
  class Meta:
    model = VisaForm
    fields = '__all__'

class UmraPackageSerializer(serializers.ModelSerializer):
  class Meta:
    model = UmraPackage
    fields = '__all__'

class UmraMonthSerializer(serializers.ModelSerializer):
  umra_packages = serializers.SerializerMethodField()
  class Meta:
    model = UmraMonth
    fields = [ 'id','name','start_date','end_date','hotel','airlines','start_price', 'umra_packages']

  def get_umra_packages(self, obj):
    umra_packages = UmraPackage.objects.filter(umra_month=obj.id)
    return UmraPackageSerializer(umra_packages, many=True).data

class UmraFormSerializer(serializers.ModelSerializer):
  class Meta:
    model = UmraForm
    fields = '__all__'

class CustomUmraFormSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUmraForm
    fields = '__all__'
    
class HolidaysSerializer(serializers.ModelSerializer):
  class Meta:
    model = Holidays
    fields = '__all__'

class HolidayFormSerializer(serializers.ModelSerializer):
  class Meta:
    model = HolidayForm
    fields = '__all__'
        
class ContactFormSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactForm
    fields = '__all__'