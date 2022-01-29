from django.shortcuts import render
from django.http import HttpResponse
from .models import BaseStation
from .genmap import gen
import os

# Create your views here.
def usermode(request):
    if request.method == "POST":
        key = str(request.POST.get('inputkey'))
        if key != '' and key != None:
            if (stations := BaseStation.objects.filter(secret_key = key)).exists():
                data = stations[0].data
                drones = [list(map(float,i.split(','))) for i in list(data.split(';'))]
                print(drones)
                zoom = 12
                if max(drones, key = lambda x:x[0])[0] - min(drones, key = lambda x:x[0])[0] <= 5:
                    zoom += 1
                gen(drones, '{}.html'.format(key), zoom)
                with open('{}.html'.format(key), 'r') as file:
                    text = file.read()
                    text = (text[:text.find('</body>')] + '<script type="text/javascript">function start(){initialize();setTimeout(function(){document.querySelectorAll("#map_canvas > div")[1].style.display = "none";}, 300);setTimeout(function(){location.reload();}, 5000);}</script>' + text[text.find('</body>'):]).replace('onload="initialize()"','onload="start()"')
                    # print(text)
                os.remove('{}.html'.format(key))

                return HttpResponse(text)
            else:
                return render(request, 'main/main.html', {'placeholder' : 'Неверный ключ'})
    return render(request, 'main/main.html', {'placeholder' : 'Введите здесь'})

def send(request):
    key = request.GET.get('key')
    # add key validation
    data = request.GET.get('data')
    if (old := BaseStation.objects.filter(secret_key = key)).exists():
        old = old[0]
        if old.data != data:
            old.data = data
            old.save()
    else:
        new = BaseStation(secret_key = key, data = data)
        new.save()
    return HttpResponse()

def about(request):
    return render(request, 'main/about.html')

def abouteng(request):
    return render(request, 'main/abouteng.html')
