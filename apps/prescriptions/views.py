from django.shortcuts import render, redirect
from .forms import PrescriptionForm

def upload(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prescriptions:thanks')
    else:
        form = PrescriptionForm()
    return render(request, 'prescriptions/upload.html', {'form': form})

def thanks(request):
    return render(request, 'prescriptions/thanks.html')
