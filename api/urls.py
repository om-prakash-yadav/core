from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import *


urlpatterns = [

	re_path("OfferLetter/((?P<pk>\d+)/)?", csrf_exempt(OfferLetterView.as_view())),

]