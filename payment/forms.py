from django import forms
from payment.models import PaymentDetail, PaymentCategory, PaymentChart, BankDetail

# INLINE FORM STUFF
from django import forms
from django.forms.models import formset_factory
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div
from crispy_forms.layout import Layout
from crispy_forms import bootstrap, layout


class PaymentChartForm(forms.ModelForm):
    """
    TODO: Extend CompanyModel into Form
    :returns: TODO
    """
    def __init__(self, *args, **kwargs):
        super(PaymentChartForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.method = "POST"
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_action = "payment:payment-chart"

        self.helper.layout = Layout(
        Div(
            Div('name', css_class="col-sm-2"),
            Div('payment_cat', css_class="col-sm-2"),
            Div('session', css_class="col-sm-2"),
            Div('term', css_class="col-sm-2"),
            Div('amount_due', css_class="col-sm-2"),
            bootstrap.FormActions(
                layout.Submit('submit', 'Add', css_class='btn btn-primary')),
            css_class='row',
        )
    )

    class Meta:
        model = PaymentChart
        fields = ["name", "payment_cat", "session", "term", "amount_due"]



class PaymentCreateForm(forms.ModelForm):
        
        class Meta:
            model = PaymentDetail
            fields = '__all__'
            exclude = ('confirmed', 'discount', 'file', 'student_id', 'student_detail',)

            widgets = {
            'payment_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
        }
                        #Note that i removed user because it is an instance in the view already
class PaymentForm(forms.ModelForm):
        
        class Meta:
            model = PaymentDetail
            fields = '__all__'
            exclude = ('confirmed', 'file',)

            widgets = {
            'payment_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
        }
                        #Note that i removed user because it is an instance in the view already



          
class PaymentCatForm(forms.ModelForm):
        
        class Meta:
            model = PaymentCategory
            fields = '__all__'
           

class BankRegisterForm(forms.ModelForm):
        
        class Meta:
            model = BankDetail
            fields = '__all__'
           



