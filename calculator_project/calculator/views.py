from django.shortcuts import render

def calculator_view(request):
    result = None
    if request.method == "POST":
        expression = request.POST.get('expression')
        try:
            
            result = eval(expression)
        except ZeroDivisionError:
            result = 'Error (Division by 0)'
        except Exception:
            result = 'Invalid Expression'

    return render(request, 'calculator/calculator.html', {'result': result})
