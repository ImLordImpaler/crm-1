from django.forms import ModelForm
from basic.models import Product , Enquiry , Employee



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class EnquiryForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'

class EmployeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'