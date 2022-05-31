from datetime import datetime
from datetime import timedelta
from tracemalloc import start
from django.db import transaction
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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


@login_required(login_url='/login/')
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
            booked_by=request.user,
            table_avail_id=ta.id,
        )

        ta.is_booked = True
        ta.save()

        return redirect("profile")
        #return render(request, 'registration/profile.html')

    return render(request, 'bookings/bookings_now.html', {'ta': ta, 'selected_date': selected_date});

def confirmation(request):
    '''
    
    '''
    return render(request, 'bookings/booking_confirmed.html')

@transaction.atomic
def booking_cancel(request, booking_id):
    '''
    Cancel reservation
    '''
    userbooking = Bookings.objects.get(id=booking_id)
    ta = Bookings.table_avail
    tablerelease = TableAvail.objects.get(id=ta)
  
    confirm = request.POST.get('confirm')
    if confirm:
        
        tablerelease.table_avail.is_booked = False
        tablerelease.table_avail.save()
        userbooking.delete()

        return redirect('profile')

    return render(request, 'bookings/booking_cancel.html', {"userbooking": userbooking})


def create_availability(request):
    try:
        start_date = datetime.today()
        start_time = '9:00'
        end_time = '22:00'
        time_slots = []
        s_time = datetime.strptime(start_time, '%H:%M')
        e_time = datetime.strptime(end_time, '%H:%M')
        while s_time <= e_time:
            _e_time = s_time + timedelta(minutes=120)
            time_slots.append((s_time, _e_time))
            s_time += timedelta(minutes=120)
        # print(start_date, end_date)
        # loop every day for the next 30 days
        # get all table objects
        # loop over every table object
        # loop over each slot
        # create TableAvail objects for each table

        for i, x in enumerate(range(0, 4)):
            if i == 0:
                start_date = start_date
            else:
                start_date = start_date + timedelta(days=1)
            tables = Tables.objects.all()
            for table in tables:
                for time_slot in time_slots:
                    TableAvail.objects.create(table_no=table, table_date=start_date, table_start=time_slot[0], table_end=time_slot[1])
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False})



def create_availability_daily(request):
    try:
        start_time = '9:00'
        end_time = '22:00'
        time_slots = []
        s_time = datetime.strptime(start_time, '%H:%M')
        e_time = datetime.strptime(end_time, '%H:%M')
        while s_time <= e_time:
            _e_time = s_time + timedelta(minutes=120)
            time_slots.append((s_time, _e_time))
            s_time += timedelta(minutes=120)

        max_avail = TableAvail.objects.last()
        print(max_avail.table_date)
        start_date = max_avail.table_date + timedelta(days=1)
        print(start_date)
        tables = Tables.objects.all()
        for table in tables:
            for time_slot in time_slots:
                TableAvail.objects.create(table_no=table, table_date=start_date, table_start=time_slot[0], table_end=time_slot[1])
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False})



