from django.urls import path
from users import views
from .forms import UserForm
from .models import Profile


urlpatterns = [
    path('users/', views.myaccount, name='myaccount'),
    path('view_myaccount/', views.view_myaccount, name='view_myaccount'),
]

def myaccount(request):
    if request.method == 'POST':
        form = UserFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myaccount')
    else:
        form = UserForm()
    return render(request, 'myaccount.html', {'form': form})

def view_myaccount(request):
    user = user.objects.get(user=request.user)  # Assuming user is authenticated
    return render(request, 'view_myaccount.html', {'user': user})
