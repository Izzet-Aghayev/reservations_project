from django import forms

from reservations.models import(
    Service,
    Reservation,
)



class CreateReservationForms(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('service', 'datetime')
