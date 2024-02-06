from django.shortcuts import render

# Create your views here.
def index(request):
    context={"var1":"this is value for var1","var2":"this is value for var2",}
    template_path= 'apps/app1/index.html'
    return render(request=request,
                  template_name=template_path,
                  context=context)
    
    
def form(request): 
    template_path= 'apps/app1/form.html'
    return render(request=request,
                  template_name=template_path)
 