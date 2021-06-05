from django.shortcuts import render
from time import perf_counter
from django.views.generic import TemplateView
from .forms import AckermanForm, FactForm, FiboForm 
from django.views import View

class HomeView(TemplateView):
    template_name = "base.html"

class FiboView(View):
    form_class = FiboForm
    template_name = 'fib.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            time1 = perf_counter()
            answer = calculate_fib(form.cleaned_data['n'])
            time2 = perf_counter()

            return render(request, self.template_name, {'answer': f'{answer}\n calculated in {(time2 - time1)*1000:0.10f} milliseconds', 'form': form})
        else: 
            return render(request, self.template_name, {'form': form})  




def calculate_fib(number):

    if number in [1,2]:
        return 1 
    
    first = 1 
    second = 1 
    for i in range(2,number):
        second += first 
        first = second - first 

    return second

# def fibonacci(request):
#     if request.method == 'POST':
#         try:
#             inp = int(request.POST['inp']) 
#         except:
#             return render(request, 'fib.html', {'error': 'Please Enter a Valid Number'})
        
#         if inp <= 0:
#             return render(request, 'fib.html', {'error': 'Please Enter a Positive Integer'})

#         time1 = perf_counter()
#         answer = calculate_fib(inp)
#         time2 = perf_counter()

#         return render(request, 'fib.html', {'answer': f'{answer}\n calculated in {(time2 - time1)*1000:0.10f} milliseconds' })
#     else:
#         return render(request, 'fib.html', {})

def fibonacci(request):
    if request.method == 'POST':
        form = FiboForm(request.POST)
        
        if form.is_valid():
            time1 = perf_counter()
            answer = calculate_fib(form.cleaned_data['n'])
            time2 = perf_counter()

            return render(request, 'fib.html', {'answer': f'{answer}\n calculated in {(time2 - time1)*1000:0.10f} milliseconds', 'form': form})
        else: 
            return render(request, 'fib.html', {'form': form})  
    else:
        form = FiboForm()
        return render(request,'fib.html', {'form': form})


def calculate_ackerman(m, n):
  
    # creating 2D LIST
    cache = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for rows in range(m + 1):
        for cols in range(n + 1):
            # base case A ( 0, n ) = n + 1
            if rows == 0:       
                cache[rows][cols] = cols + 1
            # base case  A ( m, 0 ) = 
            # A ( m-1, 1) [Computed already]
            elif cols == 0:
                cache[rows][cols] = cache[rows-1][1]
            else:
                # if rows and cols > 0
                # then applying A ( m, n ) = 
                # A ( m-1, A ( m, n-1 ) ) 
                r = rows - 1
                c = cache[rows][cols-1]
                # applying equation (2) 
                # here A ( 0, n ) = n + 1
                if r == 0:    
                    ans = c + 1
                elif c <= n:
                    # using stored value in cache
                    ans = cache[rows-1][cache[rows][cols-1]]
                else:
                    # Using the Derived Formula 
                    # to compute mystery values in O(1) time
                    ans = (c-n)*(r) + cache[r][n]
  
                cache[rows][cols] = ans
  
    return cache[m][n]


# def ackerman(request):
#     if request.method == 'POST':
#         try:
#             m = int(request.POST['m']) 
#             n = int(request.POST['n']) 
#         except:
#             return render(request, 'ack.html', {'error': 'Please Enter a Valid Number'})
        
#         if m <= 0 or n <= 0:
#             return render(request, 'ack.html', {'error': 'Please Enter a Positive Integer'})

#         time1 = perf_counter()
#         answer = calculate_ackerman(m, n)
#         time2 = perf_counter()

#         return render(request, 'ack.html', {'answer': f'{answer}\n calculated in {(time2 - time1)*1000:0.10f} milliseconds' })

#     else:
#         return render(request, 'ack.html', {})

def ackerman(request):
    if request.method == 'POST':

        form = AckermanForm(request.POST)
        
        if form.is_valid():
            time1 = perf_counter()
            answer = calculate_ackerman(form.cleaned_data['m'], form.cleaned_data['n'])
            time2 = perf_counter()

            return render(request, 'ack.html', {'answer': f'{answer}\n calculated in {(time2 - time1)*1000:0.10f} milliseconds', 'form': form})

        else: 
            return render(request, 'ack.html', {'form': form})
    else:
        form = AckermanForm()
        return render(request, 'ack.html', {'form': form})



def fact(n):
    out = 1 
    for i in range(1,n+1):
        out *= i

    return out


def factorial(request):
    if request.method == 'POST':
        
        form = FactForm(request.POST)
        
        if form.is_valid():
            time1 = perf_counter()
            answer = fact(form.cleaned_data['n'])
            time2 = perf_counter()
    
            return render(request, 'fact.html', {'answer': f'{answer},   calculated in {(time2 - time1)*1000:0.10f} milliseconds', 'form': form })

        else:
            return render(request, 'fact.html', {'form': form})

    else:
        form = FactForm()
        return render(request, 'fact.html', {'form': form})