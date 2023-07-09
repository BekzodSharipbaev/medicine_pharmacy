from django.http import HttpRequest
from django.shortcuts import render

from .models import Medicine, Pharmacy
# Create your views here.
def find_cheapest_price(request: HttpRequest):
    medicines = Medicine.objects.all()
    context = {'medicines': medicines}
    if request.method == 'POST':
        km = int(request.POST.get('kilometer', 0))
        medicine_id = int(request.POST.get('medicine', 0))
        try:
            medicine = Medicine.objects.get(pk=medicine_id)
            cheapest_price = medicine.get_cheapest_price(km)
            context |= {'cheapest_price': cheapest_price}
        except Medicine.DoesNotExist:
            context |= {'error_message': 'Invalid medicine ID.'} 
    return render(request, 'index.html', context)
