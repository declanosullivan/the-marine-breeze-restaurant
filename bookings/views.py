from django.shortcuts import render
from tables.models import TableAvail

# Create your views here.
def home(request):
    if request.method == "POST":
        selected_date = request.POST.get("date")
        num_seats = request.POST.get("num_seats")
        print(selected_date, num_seats)
        results = TableAvail.objects.filter(table_date=selected_date, table_no__table_seats=num_seats, is_booked=False)
        return render(request, 'base.html', {"available_tables": results})
    return render(request, 'base.html')