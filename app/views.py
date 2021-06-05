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

    @staticmethod
    def calculate_fib(number):

        if number in [1,2]:
            return 1 
        
        first = 1 
        second = 1 
        for i in range(2,number):
            second += first 
            first = second - first 

        return second


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            time1 = perf_counter()
            answer = FiboView.calculate_fib(form.cleaned_data['n'])
            time2 = perf_counter()

            return render(request, self.template_name, {'answer': f'{answer}\n calculated in {(time2 - time1)*1000:0.10f} milliseconds', 'form': form})
        else: 
            return render(request, self.template_name, {'form': form})  


class AckermanView(View):
    form_class = AckermanForm
    template_name = 'ack.html'

    @staticmethod
    def calculate_ackerman(m, n):
  
        cache = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for rows in range(m + 1):
            for cols in range(n + 1):
                if rows == 0:       
                    cache[rows][cols] = cols + 1

                elif cols == 0:
                    cache[rows][cols] = cache[rows-1][1]
                else:

                    r = rows - 1
                    c = cache[rows][cols-1]

                    if r == 0:    
                        ans = c + 1
                    elif c <= n:
                        ans = cache[rows-1][cache[rows][cols-1]]
                    else:
                        ans = (c-n)*(r) + cache[r][n]
    
                    cache[rows][cols] = ans
    
        return cache[m][n]


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            time1 = perf_counter()
            answer = AckermanView.calculate_ackerman(form.cleaned_data['m'], form.cleaned_data['n'])
            time2 = perf_counter()

            return render(request, self.template_name, {'answer': f'{answer}\n calculated in {(time2 - time1)*1000:0.10f} milliseconds', 'form': form})
        else: 
            return render(request, self.template_name, {'form': form})  


class FactView(View):
    form_class = FactForm
    template_name = 'fact.html'

    @staticmethod
    def fact(n):
        out = 1 
        for i in range(1,n+1):
            out *= i

        return out


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            time1 = perf_counter()
            answer = FactView.fact(form.cleaned_data['n'])
            time2 = perf_counter()

            return render(request, self.template_name, {'answer': f'{answer}\n calculated in {(time2 - time1)*1000:0.10f} milliseconds', 'form': form})
        else: 
            return render(request, self.template_name, {'form': form})  