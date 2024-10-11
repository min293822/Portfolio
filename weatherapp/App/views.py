from django.shortcuts import render
import json
import urllib.request

def base(request):
  if request.method == "POST":
    city = request.POST['city']
    res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=10ba81732296874829ba3d24a713d7b0').read()
    data = json.loads(res)
    context = {
      "country_code": str(data['sys']['country']),
      "coordinate": str(data['coor']['lon'])+'   '+str(data['coor']['lat']),
      "temp": str(data['main']['temp']),
      "pressure":str(data['main']['pressure']),
      "humidity": str(data['main']['humidity'])
    }
  else:
    city = ''
    context = {}
  return render(request, 'Base.html', context, {'city':city})
