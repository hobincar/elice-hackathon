from django.shortcuts import render
from django.template.context_processors import csrf
from sklearn.externals import joblib

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

            AGG = float(form.cleaned_data['age']) // 5 + 1
            SEX_TP_CD = float(form.cleaned_data['sex'])
            SOPR_YN = float(form.cleaned_data['hospital_treatment'])
            DUMMY_DATA = 1.0

            # Linear Regression
            if form.cleaned_data['show_result'] == 'C':
                model = joblib.load("Demo/static/models/%s_LINEAR_REGR_COST.model" % form.cleaned_data['disease'])
                cost = model.predict([[AGG, SEX_TP_CD, DUMMY_DATA, SOPR_YN, DUMMY_DATA]])
                result['cost'] = cost
            else:
                model = joblib.load("Demo/static/models/%s_LINEAR_REGR_PERIOD.model" % form.cleaned_data['disease'])
                period = model.predict([[AGG, SEX_TP_CD, DUMMY_DATA, SOPR_YN, DUMMY_DATA]])
                result['period'] = period

    else:
        form = UserInputForm

    args = {
        'form': form,
        'result': result
    }
    args.update(csrf(request))
    return render(request, "main.html", args)
