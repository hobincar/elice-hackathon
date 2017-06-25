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


def test(request):
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi",
             "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('test.html', data)