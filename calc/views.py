from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, "calc/index.html")

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

        return JsonResponse({"result": result})
