from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.views.generic import ListView
from django.views.generic import View
# Import forms and models
from uploads.models import Product
from .forms import UploadForm

class ProductList(ListView):
    model = Product

#std form view
class MyFormView(View):
    form_class = UploadForm
    initial = {'key': 'value'}
    template_name = 'upload_form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect('/products/')

        return render(request, self.template_name, {'form': form})