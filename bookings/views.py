from django.shortcuts import render
from tables.models import TableAvail
from tables.models import Tables

def bookings(request):
    '''
    View to search for available tables
    '''
    if request.method == "POST":
        selected_date = request.POST.get("date")
        request.session['selected_date'] = selected_date
        num_seats = request.POST.get("num_seats")
        request.session['num_seats'] = num_seats
        print(selected_date, num_seats)
        results = TableAvail.objects.filter(table_date=selected_date, table_no__table_seats=num_seats, is_booked=False)
        return render(request, 'bookings/bookings.html', {"available_tables": results})
    return render(request, 'bookings/bookings.html')


def bookings_now(request, id):
    '''
    Book available table
    '''
    selected_date = request.session['selected_date']
    request.session[table_no] 


