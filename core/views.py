from django.shortcuts import render
import json
from rest_framework import viewsets


from .models import Branch, Sales, Device
from.serializers import DeviceSerializer


def index():
    branches = Branch.objects.all()
    sales = Sales.objects.all()

    sales_list = []
    branch_list = []
    year_set = set()

    for sale in sales:
        year_set.add(sale.year)

    year_list = list(sorted(year_set))
    import pdb;pdb.set_trace()
    for branch in branches:
        sales_list.append(branch.sales_set.all().order_by('year'))
        branch_list.append(branch.name)

    sales_list = [[j.sales_amount for j in i] for i in sales_list]

    branch_dict = dict(zip(branch_list, sales_list))

    return render(request, 'index.html', {
        'year_list': year_list,
        'branch_dict': branch_dict
    })


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save()


class DeviceViewSet(viewsets.ModelViewSet):

    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
