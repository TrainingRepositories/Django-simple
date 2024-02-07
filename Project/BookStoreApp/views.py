from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Authors , Books , Shelves
from .forms import AuthorsForm , BooksForm , ShelvesForm

# Create your views here.
def index(request): 
    template_path= 'apps/BookStoreApp/index.html'
    data = Authors.objects.all()
    return render(request, template_path, {'data': data})  

if True : # Authors
    def add_Author(request): 
        template_path= 'apps/BookStoreApp/Authors/add.html'
        
        if request.method=='POST':
            form = AuthorsForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return index(request)
            else:
                print('ERROR AuthorsForm INVALID')
                
        form1 = AuthorsForm()
        return render(request=request,
                        template_name=template_path ,
                        context={'form':form1})  
        
    def list_Authors(request): 
        template_path= 'apps/BookStoreApp/Authors/list2.html'
        data = Authors.objects.all()
        return render(request, template_path, {'data': data}) 
                 
if True : # Shelves 
    def add_Shelve(request): 
        template_path= 'apps/BookStoreApp/Shelves/add.html'
        
        if request.method=='POST':
            form = ShelvesForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return index(request)
            else:
                print('ERROR ShelvesForm INVALID')
                
        form1 = ShelvesForm()
        return render(request=request,
                        template_name=template_path ,
                        context={'form':form1})   
        
    def list_Shelves(request): 
        template_path= 'apps/BookStoreApp/Shelves/list.html'
        data = Shelves.objects.all()
        return render(request, template_path, {'data': data}) 

if True : # Books
    def add_Book(request): 
        template_path= 'apps/BookStoreApp/Books/add.html'
        
        if request.method=='POST':
            form = BooksForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return index(request)
            else:
                print('ERROR BooksForm INVALID')
                
        form1 = BooksForm()
        return render(request=request,
                        template_name=template_path ,
                        context={'form':form1}) 
        
    def list_Books(request): 
        template_path= 'apps/BookStoreApp/Books/list.html' 
        data = Books.objects.all()
        return render(request, template_path, {'data': data})
 
        