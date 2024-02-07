from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import FormName
from .models import User
# Create your views here.
def index(request):
    context={"var1":"this is value for var1","var2":"this is value for var2",}
    template_path= 'apps/app1/index.html'
    return render(request=request,
                  template_name=template_path,
                  context=context)
    
    
def form(request): 
    template_path= 'apps/app1/form.html'
    
    if request.method=='POST':
        form = FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    form1 = FormName()
    return render(request=request,
                  template_name=template_path ,
                  context={'form':form1})
 
def list_users(request):
    users_list = User.objects.order_by('first_name')
    paginator = Paginator(users_list, 5)  # Show 10 users per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'apps/app1/table.html', {'page_obj': page_obj})

        
# def list_users(request):
    
#     users_list = User.objects.all()

#     paginator = Paginator(users_list, 10)  # Show 10 users per page

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'apps/app1/table.html', {'page_obj': page_obj})
