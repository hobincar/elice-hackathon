from django import forms


class UserInputForm(forms.Form):
    age = forms.CharField()
    sex = forms.ChoiceField(
        choices=([
            ('1', 'Male'),
            ('2', 'Female'),
        ])
    )
    hospital_treatment = forms.CharField()
    disease = forms.ChoiceField(
        choices=([
            ('E119', '합병증을 동반하지 않은 2형 당뇨병'),
            ('I100', '심장침범에 대한 언급이 없는 류마티스열'),
            ('I109', '기타 및 상세불명의 원발성 고혈압'),
            ('J00', '급성 비인두염[감기]'),
            ('J029', '상세불명의 급성 인두염'),
            ('J060', '급성 후두인두염'),
            ('J069', '상세불명의 급성 상기도감염'),
            ('J209', '상세불명의 급성 기관지염'),
            ('J304', '상세불명의 앨러지비염'),
            ('J0390', '재발성으로 명시되어 있지 않은 상세불명의 급성 편도염'),
            ('K021', '상아질의 우식'),
            ('K0401', '비가역적 치수염'),
            ('K0530', '만성 단순치주염'),
            ('K0531', '만성 복합치주염'),
            ('L239', '상세불명 원인의 앨러지성 접촉피부염'),
            ('M170', '양쪽 원발성 무릎관절증'),
            ('M511', '신경뿌리병증을 동반한 요추 및 기타 추간판장애'),
            ('M4806', '척추협착, 요추부'),
            ('M5456', '요통, 요추부'),
            ('N185', '만성 신장병(5기)'),
            ('S3350', '요추의 염좌 및 긴장'),
        ])
    )
    start_month = forms.ChoiceField(
        choices=([
            ('2015-01-01', '1월'),
            ('2015-02-01', '2월'),
            ('2015-03-01', '3월'),
            ('2015-04-01', '4월'),
            ('2015-05-01', '5월'),
            ('2015-06-01', '6월'),
            ('2015-07-01', '7월'),
            ('2015-08-01', '8월'),
            ('2015-09-01', '9월'),
            ('2015-10-01', '10월'),
            ('2015-11-01', '11월'),
            ('2015-12-01', '12월'),
        ]),
        required=False
    )
    show_result = forms.ChoiceField(
        choices=([
            ('C', 'Cost'),
            ('P', 'Period'),
        ])
    )