from django.shortcuts import render
from django.http import JsonResponse
from .models import Calculation

def index(request):
    # Fetch recent history
    history = Calculation.objects.all().order_by('-created_at')[:5]
    return render(request, "calc/index.html", {"history": history})

def calculate(request):
    if request.method == "POST":
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        operation = request.POST.get("operation")

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

        # Save to database
        Calculation.objects.create(
            num1=num1, num2=num2, operation=operation, result=result
        )

        return JsonResponse({"result": result})
