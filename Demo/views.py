from django.shortcuts import render
from django.template.context_processors import csrf

from .forms import UserInputForm


def main(request):
    result = {}
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            print("age: %s\n" % form.cleaned_data['age'])
            print("sex: %s\n" % form.cleaned_data['sex'])
            print("hospital_treatment: %s\n" % form.cleaned_data['hospital_treatment'])
            print("disease: %s\n" % form.cleaned_data['disease'])
            print("show_result: %s\n" % form.cleaned_data['show_result'])

            # Linear Regression
            cost = 1000000
            period = 30

            if form.cleaned_data['show_result'] == 'C':
                result['cost'] = cost
            else:
                result['period'] = period

    else:
        form = UserInputForm

    args = {
        'form': form,
        'result': result
    }
    args.update(csrf(request))
    return render(request, "main.html", args)
