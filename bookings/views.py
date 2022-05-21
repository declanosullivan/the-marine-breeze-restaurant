from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from tables.models import TableAvail
from tables.models import Tables
from bookings.models import Bookings
import random

def bookings(request):
    '''
    View to search for available tables
    '''
    selected_date = request.GET.get('date')
    if selected_date:
        selected_date = request.GET.get("date")
        request.session['selected_date'] = selected_date
        num_seats = request.GET.get("num_seats")
        request.session['num_seats'] = num_seats
        print(selected_date, num_seats)
        results = TableAvail.objects.filter(table_date=selected_date, table_no__table_seats=num_seats, is_booked=False)
        return render(request, 'bookings/bookings.html', {"available_tables": results, "selected_date" : selected_date})
    return render(request, 'bookings/bookings.html')


@login_required
def bookings_now(request):
    '''
    Book available table
    '''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    selected_date = request.session['selected_date']
    pk = request.POST.get('table_no')
    ta = TableAvail.objects.get(pk=pk)
    confirm = request.POST.get('confirm')

    if confirm:
        ref = []
        for i in range(8):
            letter = random.choice(letters)
            ref.append(letter)
        ref = "".join(ref)

        Bookings.objects.create(booking_ref=ref, booking_date=selected_date,
            booking_start=ta.table_start, booking_end=ta.table_end,
            table=ta.table_no, customer=request.user,
            booked_by=""
        )

        ta.is_booked = True
        ta.save()

        return render(request, 'bookings/bookings_now.html')

    return render(request, 'bookings/bookings_now.html', {'ta': ta, 'selected_date': selected_date});

def confirmation(request):
    '''
    
    '''
    return render(request, 'bookings/booking_confirmed.html')
