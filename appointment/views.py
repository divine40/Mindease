from django.shortcuts import render
from .models import Appointment
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


@csrf_exempt
@login_required
def appointment(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        date = request.POST.get('date')
        purpose = request.POST.get('purpose')
        message = request.POST.get('message')

        try:
            appointment = Appointment(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email=email,
                date=date,
                purpose=purpose,
                message=message
            )
            appointment.save()

            messages.success(request, "Appointment Booked Successfully")
            return render(
                request,
                'core/appointment.html',
            )
        except Exception as e:
            messages.error(request, "Failed to book appointment")
            return render(
                request,
                'core/appointment.html',
                {'error': str(e)}
            )


    return render(request, 'core/appointment.html')
