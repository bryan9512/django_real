from django import forms
from .models import Users
from .models import Apply

class CreateUsers(forms.ModelForm):
    class Meta:
        model = Users

        fields = ['u_name', 'u_school', 'u_major','u_interest']


class CreateApply(forms.ModelForm):
    class Meta:
        model = Apply

        fields = [Users.u_name,'a_company', 'a_interest','a_qone_q', 'a_qone', 'a_qtwo_q','a_qtwo', 'a_qthree_q','a_qthree', 'a_qfour_q' ,'a_four', 'a_qfive_q','a_five']