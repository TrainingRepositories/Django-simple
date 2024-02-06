from django.shortcuts import render

# Create your views here.
def index(request): 
    template_path= 'main/index.html'
    return render(request=request,
                  template_name=template_path)