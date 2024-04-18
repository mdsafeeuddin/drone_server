from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from drone.models import Visa, VisaForm, UmraMonth, UmraPackage, UmraForm, CustomUmraForm, Holidays, HolidayForm, ContactForm
from drone.serializers import UmraFormSerializer, UmraMonthSerializer, VisaSerializer, VisaFormSerializer, UmraPackageSerializer, CustomUmraFormSerializer, HolidayFormSerializer, HolidaysSerializer, ContactFormSerializer

class VisaListView(generics.ListAPIView):
	permission_classes = [HasAPIKey]
	queryset = Visa.objects.all().order_by('name')
	serializer_class = VisaSerializer

class VisaTypesView(generics.RetrieveAPIView):
	queryset = Visa.objects.all()
	serializer_class = VisaSerializer
	lookup_field = 'id'

	def get(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		return Response(serializer.data, status=status.HTTP_200_OK)
    
class VisaFormView(generics.CreateAPIView):
	queryset = VisaForm.objects.all()
	serializer_class = VisaFormSerializer

class UmraMonthView(generics.ListAPIView):
	queryset = UmraMonth.objects.all()
	serializer_class = UmraMonthSerializer

class UmraPackagesView(generics.RetrieveAPIView):
	queryset = UmraMonth.objects.all()
	serializer_class = UmraMonthSerializer
	lookup_field = 'id'

	def get(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		return Response(serializer.data, status=status.HTTP_200_OK)

class UmraFormView(generics.CreateAPIView):
	queryset = UmraForm.objects.all()
	serializer_class = UmraFormSerializer

class CustomUmraFormView(generics.CreateAPIView):
	queryset = CustomUmraForm.objects.all()
	serializer_class = CustomUmraFormSerializer

class HolidaysView(generics.ListAPIView):
	queryset = Holidays.objects.all().order_by('name')
	serializer_class = HolidaysSerializer

class HolidayDetailsView(generics.ListAPIView):
	serializer_class = HolidaysSerializer
	def get_queryset(self):
		pkg_id = self.kwargs['id']
		queryset = Holidays.objects.filter(id=pkg_id)
		return queryset

class HolidayFormView(generics.CreateAPIView):
	queryset = HolidayForm.objects.all()
	serializer_class = HolidayFormSerializer

class ContactFormCreateView(generics.CreateAPIView):
	queryset = ContactForm.objects.all
	serializer_class = ContactFormSerializer