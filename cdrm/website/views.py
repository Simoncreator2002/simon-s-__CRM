from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import signupform,AddRecordForm
from . models import Record

def home(request):
    records=Record.objects.all()





    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password') 

        if username and password:  
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in successfully")
                return redirect('home')
            else:
                messages.error(request, "There was an error logging in. Please try again.")
                return redirect('home')
        else:
            messages.error(request, "Username and password are required.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out successfully")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('home')
    else:
        form = signupform()
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id =pk)

        return render(request,'record.html',{'customer_record':customer_record})

    else:
          messages.success(request, "you must be logged in to view that page")
          return redirect('home')        
    



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
            if request.method=='POST':
                if form.is_valid():
                    addd_record=form.save()
                    messages.success(request, "your record was successfully added")
                    return redirect('home')
            return render(request,'add_record.html',{'form':form})

    else:
        messages.success(request, "login first plizz")
        return redirect('home')


def update_record(request, pk):
        if request.user.is_authenticated:
            current_record=Record.objects.get(id=pk)
            form=AddRecordForm(request.POST or None,instance=current_record)

            if form.is_valid():
                form.save()
                messages.success(request, "your record was successfully updated")
                return redirect('home')
            return render(request,'update_record.html',{'form':form})
       
        else:
             messages.success(request, "you must login first")
             return redirect('home')
                

                     

     
     