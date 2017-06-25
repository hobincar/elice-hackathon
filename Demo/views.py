from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from sklearn.externals import joblib

from .forms import UserInputForm


def LR_3in(request):
    result = {}
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            AGG = float(form.cleaned_data['age']) // 5 + 1
            SEX_TP_CD = float(form.cleaned_data['sex'])
            SOPR_YN = float(form.cleaned_data['hospital_treatment'])

            # Linear Regression
            if form.cleaned_data['show_result'] == 'C':
                model = joblib.load("Demo/static/models/%s_LINEAR_REGR_COST.model" % form.cleaned_data['disease'])
                cost = model.predict([[AGG, SEX_TP_CD, SOPR_YN]])[0][0]
                if cost < 0:
                    cost = 0.01
                result['cost'] = format(cost, ".2f")
            else:
                model = joblib.load("Demo/static/models/%s_LINEAR_REGR_PERIOD.model" % form.cleaned_data['disease'])
                period = model.predict([[AGG, SEX_TP_CD, SOPR_YN]])[0][0]
                if period < 0:
                    period = 0.01
                result['period'] = format(period, ".2f")

    else:
        form = UserInputForm

    args = {
        'form': form,
        'result': result
    }
    args.update(csrf(request))
    return render(request, "LR_3in.html", args)


def LR_4in(request):
    result = {}
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            AGG = float(form.cleaned_data['age']) // 5 + 1
            SEX_TP_CD = float(form.cleaned_data['sex'])
            SOPR_YN = float(form.cleaned_data['hospital_treatment'])

            # Linear Regression
            if form.cleaned_data['show_result'] == 'C':
                model = joblib.load("Demo/static/models/%s_LINEAR_REGR_COST.model" % form.cleaned_data['disease'])
                cost = model.predict([[AGG, SEX_TP_CD, SOPR_YN]])[0][0]
                if cost < 0:
                    cost = 0.01
                result['cost'] = format(cost, ".2f")
            else:
                model = joblib.load("Demo/static/models/%s_LINEAR_REGR_PERIOD.model" % form.cleaned_data['disease'])
                period = model.predict([[AGG, SEX_TP_CD, SOPR_YN]])[0][0]
                if period < 0:
                    period = 0.01
                result['period'] = format(period, ".2f")

    else:
        form = UserInputForm

    args = {
        'form': form,
        'result': result
    }
    args.update(csrf(request))
    return render(request, "LR_4in.html", args)


import time
import datetime
import random
def test(request):
    """
    scatterchart page
    """
    nb_element = 50
    xdata = [i + random.randint(1, 10) for i in range(nb_element)] + [10] * 100
    ydata1 = [i * random.randint(1, 10) for i in range(nb_element)] + [800] * 100
    # xdata = [i + random.randint(1, 10) for i in range(nb_element)]
    # ydata1 = [i * random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata1)
    ydata3 = map(lambda x: x * 5, ydata1)

    kwargs1 = {'shape': 'circle'}
    kwargs2 = {'shape': 'cross'}
    kwargs3 = {'shape': 'triangle-up'}

    extra_serie1 = {"tooltip": {"y_start": "", "y_end": " balls"}}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata1, 'kwargs1': kwargs1, 'extra1': extra_serie1,
        'name2': 'series 2', 'y2': ydata2, 'kwargs2': kwargs2, 'extra2': extra_serie1,
        'name3': 'series 3', 'y3': ydata3, 'kwargs3': kwargs3, 'extra3': extra_serie1
    }
    charttype = "scatterChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render_to_response('test.html', data)