from django.conf.urls import url
from basicapp import views
from django.urls import re_path,path
from basicapp.views import booking_charge
#Tis appp name is for TEMPLATE linking
app_name='basicapp'

urlpatterns=[
    url(r'^register/$',views.register,name="register"),
    url(r'^user_login/$',views.user_login,name="user_login"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate,name="activate"),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^profile/update/$',views.update,name='update'),
    url(r'^profile/visited_industries/$', views.visited_industries, name='visited_industries'),
    url(r'^profile/booked_to_visit/$',views.booked_to_visit,name='booked_to_visit'),
    path('profile/cancel_ticket/<industry_id>/', views.cancel_ticket,name='cancel_ticket'),
    path('booking_charge/<industry_id>/',booking_charge.as_view(),name='booking_charge'),
    url(r'^charge1_individual/$',views.charge1,name='charge1'),
    url(r'^charge2_organisation/$',views.charge2,name='charge2'),
]
