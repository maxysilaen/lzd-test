from django.conf.urls import url
from .views import (
 CoordinateView,
    
    )

urlpatterns = [

    
    url(r'^$', CoordinateView.as_view(), name='shortest'),
   

]

