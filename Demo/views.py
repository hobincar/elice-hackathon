from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from sklearn.externals import joblib
import pandas as pd
import numpy as np
import random
from collections import Counter
import json
from django.core.serializers.json import DjangoJSONEncoder

from .forms import UserInputForm


def LR_3in(request):
    result = {}
    scatter_data_json = {}
    line_data_json = {}
    xlabel = None
    ylabel = None
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            AGG = float(form.cleaned_data['age']) // 5 + 1
            SEX_TP_CD = float(form.cleaned_data['sex'])
            SOPR_YN = float(form.cleaned_data['hospital_treatment'])

            model = joblib.load("Demo/static/models/%s_LINEAR_REGR_COST.model" % form.cleaned_data['disease'])
            cost = model.predict([[AGG, SEX_TP_CD, SOPR_YN]])[0][0]

            model = joblib.load("Demo/static/models/%s_LINEAR_REGR_PERIOD.model" % form.cleaned_data['disease'])
            period = model.predict([[AGG, SEX_TP_CD, SOPR_YN]])[0][0]
            if cost < 0:
                cost = 0.01
            result['cost'] = format(cost, ".2f")
            if period < 0:
                period = 0.01
            result['period'] = format(period, ".2f")



            disease_code_map = {
                'E119': '합병증을 동반하지 않은 2형 당뇨병',
                'I00': '심장침범에 대한 언급이 없는 류마티스열',
                'I109': '기타 및 상세불명의 원발성 고혈압',
                'J00': '급성 비인두염[감기]',
                'J029': '상세불명의 급성 인두염',
                'J0390': '재발성으로 명시되어 있지 않은 상세불명의 급성 편도염',
                'J060': '급성 후두인두염',
                'J069': '상세불명의 급성 상기도감염',
                'J209': '상세불명의 급성 기관지염',
                'J304': '상세불명의 앨러지비염',
                'K021': '상아질의 우식',
                'K0401': '비가역적 치수염',
                'K0530': '만성 단순치주염',
                'K0531': '만성 복합치주염',
                'L239': '상세불명 원인의 앨러지성 접촉피부염',
                'M170': '양쪽 원발성 무릎관절증',
                'M4806': '척추협착, 요추부',
                'M511': '신경뿌리병증을 동반한 요추 및 기타 추간판장애',
                'M5456': '요통, 요추부',
                'N185': '만성 신장병(5기)',
                'S3350': '요추의 염좌 및 긴장'
            }

            mean_line_data = np.array(pd.read_csv("Demo/static/mean_line/line_%s.csv" % form.cleaned_data['disease']).values)
            mean_line_period = mean_line_data[:, 1]
            mean_line_cost = mean_line_data[:, 2]

            if form.cleaned_data['show_result'] == 'C':
                scatter_data = [{"x": period, "y": cost, "shape": "square", "size": 50},]
                line_data = [{"x": period, "y": cost} for period, cost in zip(mean_line_period, mean_line_cost)]
                xlabel = "진료 기간(일)"
                ylabel = "비용(원)"
            else:
                sorted_period = [x for (y, x) in sorted(zip(mean_line_cost, mean_line_period))]
                sorted_cost = sorted(mean_line_cost)
                scatter_data = [{"x": cost, "y": period, "shape": "square", "size": 50},]
                line_data = [{"x": cost, "y": period} for period, cost in zip(sorted_period, sorted_cost)]
                xlabel = "비용(원)"
                ylabel = "진료 기간(일)"

            scatter_data_json = json.dumps(list(scatter_data), cls=DjangoJSONEncoder)
            line_data_json = json.dumps(list(line_data), cls=DjangoJSONEncoder)

    else:
        form = UserInputForm


    args = {
        'form': form,
        'result': result,
        'scatter_data': scatter_data_json,
        'line_data': line_data_json,
        'xlabel': xlabel,
        'ylabel': ylabel
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
    """
    scatterchart page
    """
    nb_element = 50
    _xdata = [i + random.randint(1, 10) for i in range(nb_element)]
    _xdata_cnt = Counter(_xdata)
    xdata = list(_xdata_cnt.keys())
    size = list(_xdata_cnt.values())
    ydata1 = [i * random.randint(1, 10) for i in range(len(xdata))]

    kwargs1 = {'shape': 'circle', 'size': size}

    extra_serie1 = {"tooltip": {"y_start": "", "y_end": " balls"}}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata1, 'kwargs1': kwargs1, 'extra1': extra_serie1,
    }
    charttype = "scatterChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render_to_response('test.html', data)