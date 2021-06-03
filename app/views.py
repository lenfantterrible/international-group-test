from django.shortcuts import render

def calculate_fib(number):

    if number in [1,2]:
        return 1 
    
    first = 1 
    second = 1 
    for i in range(2,number):
        second += first 
        first = second - first 

    return second

def fibonacci(request):
    if request.method == 'POST':
        try:
            inp = int(request.POST['inp']) 
        except:
            return render(request, 'fib.html', {'error': 'Please Enter a Valid Number'})
        
        if inp <= 0:
            return render(request, 'fib.html', {'error': 'Please Enter a Positive Integer'})


        return render(request, 'fib.html', {'answer': calculate_fib(inp)})
    else:
        return render(request, 'fib.html', {})
