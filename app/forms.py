from django import forms 

class FiboForm(forms.Form):
    n = forms.IntegerField(label="")

    def clean(self):
        super().clean()

        n = self.cleaned_data.get('n')

        if n <= 0:
                self._errors['n'] = self.error_class(['Please Enter a positive Integer'])

        return self.cleaned_data    

class AckermanForm(forms.Form):

    m = forms.IntegerField(label="Positive Integer M")
    n = forms.IntegerField(label="Positive Integer N")

    def clean(self):
        super().clean()

        n = self.cleaned_data.get('n')
        m = self.cleaned_data.get('m')

        if n <= 0:
                self._errors['n'] = self.error_class(['Please Enter a positive Integer'])
        
        if m <= 0:
                self._errors['m'] = self.error_class(['Please Enter a positive Integer'])

        return self.cleaned_data    


class FactForm(FiboForm):
    pass
