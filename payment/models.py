from django.db import models
from django.contrib.auth.models import User
from curriculum.models import Session
from students.models import StudentDetail
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator 
from django.db.models import F, Sum, Q


class BankDetail(models.Model):
    acc_name = models.CharField(max_length=150, blank=False)
    acc_number = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=150, blank=False, verbose_name='Bank Name')

    def __str__(self):
        return f'{self.acc_name}'

    class Meta:
        ordering:['acc_number']


class PaymentCategory(models.Model):
    name = models.CharField(max_length=150, blank=True, unique=True)
    description = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Payment Category'
        verbose_name_plural = 'Payment Categories'


class PaymentChart(models.Model):
    name = models.CharField(max_length=150, blank=True)
    payment_cat = models.ForeignKey(PaymentCategory, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    first_term = 'First Term'
    second_term = 'Second Term'
    third_term = 'Third Term'
    others = 'Others'

    term = [
        (first_term, 'First Term'),
        (second_term, 'Second Term'),
        (third_term, 'Third Term'),
        (others, 'Others'),
    ]
    term = models.CharField(max_length=50, choices=term, blank=True) 
    amount_due = models.DecimalField(max_digits=15, decimal_places=2, default=0.0) 
    
    def __str__ (self):
        return f'{self.name}' 

    class Meta:
        ordering:['-session']
    

class PaymentDetail(models.Model):
    student_detail = models.ForeignKey(StudentDetail, on_delete=models.CASCADE, default=None, null=True)
    payment_name = models.ForeignKey(PaymentChart, on_delete=models.CASCADE, default= None, related_name='payment_name')
    amount_paid_a = models.DecimalField(max_digits=15, decimal_places=2, default=0.0, null=True)
    bank_name_a = models.ForeignKey(BankDetail, on_delete=models.CASCADE, default=None, null=True, related_name='bank_name_a')   
    payment_date_a = models.DateField()
    other_details_a = models.CharField(max_length=200, blank=True, verbose_name='description(if any)')

    amount_paid_b = models.DecimalField(max_digits=15, decimal_places=2, default=0.0, null=True)
    bank_name_b = models.ForeignKey(BankDetail, on_delete=models.CASCADE, default=None, null=True, related_name='bank_name_b')   
    payment_date_b = models.DateField()
    other_details_b = models.CharField(max_length=200, blank=True, verbose_name='description(if any)')

    amount_paid_c = models.DecimalField(max_digits=15, decimal_places=2, default=0.0, null=True)
    bank_name_c = models.ForeignKey(BankDetail, on_delete=models.CASCADE, default=None, null=True)   
    payment_date_c = models.DateField()
    other_details_c = models.CharField(max_length=200, blank=True, verbose_name='description(if any)')

    discount = models.DecimalField(help_text='enter in %', max_digits=3, decimal_places=0, blank=True, null=True, verbose_name='TOTAL DISCOUNT(if any)', default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]) 
    # payment confirmation
    confirmed_a = models.BooleanField(default=False) 
    confirmed_b = models.BooleanField(default=False) 
    confirmed_c = models.BooleanField(default=False) 

    payment_updated_date = models.DateField(auto_now_add=True)     

    class Meta:
        ordering = ['-student_detail' ]

    #def __str__ (self):
    #    return f'{self.payee}'

    def get_absolute_url(self):
        return reverse('payment:payment_detail', kwargs={'id':self.id})

    @property
    def balance_pay(self):
       return self.payment_name.amount_due - (self.amount_paid_a + self.amount_paid_b + self.amount_paid_c)

    @property
    def discounted_amount_due(self):
       return self.payment_name.amount_due - (self.discount/100 * self.payment_name.amount_due)

    @property
    def discounted_balance_pay(self):
        #return self.discounted_amount_due - self.amount_paid
        return self.discounted_amount_due - self.balance_pay


    # for getting total number of payments a student made
    @property
    def no_of_payments(request):
      return PaymentDetail.objects.filter(student_detail = request.student_detail).count()

       
    