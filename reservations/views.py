from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from reservations.forms import (
    CreateReservationForms,
)
from reservations.models import (
    Service,
    Reservation,
)



class HomeView(View):
    def get(self, request):
        return render(request, 'reservations/home_page.html', {})



class CreateReservationView(LoginRequiredMixin, View):
    def get_user(self, request):
        user = request.user
        return user
    
    def get(self, request):
        form = CreateReservationForms()
        context = {
            'form': form
        }

        return render(request, 'reservations/add_resev.html', context)
    
    def post(self, request):
        user = self.get_user(request)
        form = CreateReservationForms(request.POST)

        if form.is_valid():
            service = form.cleaned_data['service']
            datetime = form.cleaned_data['datetime']

            Reservation.objects.create(user=user, service=service, datetime=datetime)

            messages.success(request, 'Rezervasiya edildi')
            return redirect('home')
        
        else:
            messages.error(request, form.errors)
            return redirect('resev')


# resevleri list et
# tesdiq redd et legv et 
# service yaratma 
