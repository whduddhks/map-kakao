from django.shortcuts import render, redirect

# Create your views here.
def map(request):
    findloc = "서울 성북구"
    loclist = ["서울 성북구 보문로30길 46 3층", "서울 성북구 성북로 156", "서울 성북구 동소문로22길 57-4"]
    namelist = ["카페매니플리즈", "블랑제메종북악", "카페 원오프"]
    return render(request, 'map2.html', {'loclist':loclist, 'namelist':namelist, 'findloc':findloc})