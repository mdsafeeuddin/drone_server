from django.urls import path
from drone.views import UmraMonthView, VisaListView
from drone.views import VisaTypesView
from drone.views import VisaFormView
from drone.views import UmraPackagesView
from drone.views import UmraFormView
from drone.views import CustomUmraFormView
from drone.views import HolidaysView
from drone.views import HolidayDetailsView
from drone.views import HolidayFormView
from drone.views import ContactFormCreateView

urlpatterns = [
  path('visa_list/', VisaListView.as_view(), name='visa-list'),
  path('visa_types/<int:id>/', VisaTypesView.as_view(), name='visa-types'),
  path('visa_form/', VisaFormView.as_view(), name='visa-form'),
  path('umra_months/', UmraMonthView.as_view(), name='umra-month-view'),
  path('umrah_package/<int:id>', UmraPackagesView.as_view(), name='umrah-packages'),
  path('umrah_form/', UmraFormView.as_view(), name='umra-form'),
  path('custom_umra_form/', CustomUmraFormView.as_view(), name='custom-umra-form'),
  path('holidays/', HolidaysView.as_view(), name='holidays'),
  path('holiday_details/<int:id>/', HolidayDetailsView.as_view(), name='holiday-details'),
  path('holiday_form/', HolidayFormView.as_view(), name='holiday-form'),
  path('contact/', ContactFormCreateView.as_view(), name='contact-form')
]