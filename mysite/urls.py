
from django.conf.urls import url
from django.contrib import admin
 
from django.urls import path
import mock.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('update', mock.views.update, name="update"),
    path('<par1>', mock.views.index1, name="index1"),
    path('<par1>/<par2>', mock.views.index1, name="index1"),
    path('<par1>/<par2>/<par3>/', mock.views.index1, name="index1"),
    path('<par1>/<par2>/<par3>/<par4>/', mock.views.index1, name="index1"),
    path('<par1>/<par2>/<par3>/<par4>/<par5>/', mock.views.index1, name="index1"),
    path('<par1>/<par2>/<par3>/<par4>/<par5>/<par6>/', mock.views.index1, name="index1"),
    path('<par1>/<par2>/<par3>/<par4>/<par5>/<par6>/<par7>/', mock.views.index1, name="index1"),
    path('<par1>/<par2>/<par3>/<par4>/<par5>/<par6>/<par7>/<par8>/', mock.views.index1, name="index1"),
    path('<par1>/<par2>/<par3>/<par4>/<par5>/<par6>/<par7>/<par8>/<par9>/', mock.views.index1, name="index1"),
    path('<par1>/<par2>/<par3>/<par4>/<par5>/<par6>/<par7>/<par8>/<par9>/<par10>/', mock.views.index1, name="index1"),
    path('<par1>/<par2>/<par3>/<par4>/<par5>/<par6>/<par7>/<par8>/<par9>/<par10>/<par11>/', mock.views.index1, name="index11"),
    path('<par1>/<par2>/<par3>/<par4>/<par5>/<par6>/<par7>/<par8>/<par9>/<par10>/<par11>/<par12>/', mock.views.index1, name="index1"),
    path('<par1>/<par2>/<par3>/<par4>/<par5>/<par6>/<par7>/<par8>/<par9>/<par10>/<par11>/<par12>/<par13>/', mock.views.index1, name="index1"),
    path('<par1>/<par2>/<par3>/<par4>/<par5>/<par6>/<par7>/<par8>/<par9>/<par10>/<par11>/<par12>/<par13>/<par14>/', mock.views.index1, name="index1"),
    path('<par1>/<par2>/<par3>/<par4>/<par5>/<par6>/<par7>/<par8>/<par9>/<par10>/<par11>/<par12>/<par13>/<par14>/<par15>/', mock.views.index1, name="index1"),
]

