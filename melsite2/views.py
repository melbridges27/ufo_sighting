from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import FreqList
from .forms import FreqForm

def home(request):
    return render(request, 'melsite2/index.html', {})

def preds(request):  
    form = FreqForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        freq_id = request.POST.get("city-year-select")
        # if freq_id is none or empty then render error
        if (freq_id is None) or (freq_id == ""):
            messages.error(request, "Error")
            return render(request, "melsite2/projects/dtsc691/error.html", messages)
        else:
            # get the item row in the db with the city_val that matches freq_id
            item_db = FreqList.objects.get(city_val=freq_id)
            # get the actual freq
            actual_freq = item_db.freq_val
            # get the pred freq
            pred_freq = item_db.rf_pred
            # assign these values to the context dict
            context = {"city_val": item_db, "freq_val": actual_freq, "rf_pred": pred_freq}
            #print(context)  # for debugging
            return render(request, "melsite2/projects/dtsc691/preds_result.html", context)           
    else:
        form = FreqForm()
        return render(request, "melsite2/projects/dtsc691/preds.html", {"form":form})

def preds_result(request, context):
    return render(request, "melsite2/projects/dtsc691/preds_result.html", context)

def error(request):
    return render(request, "melsite2/projects/dtsc691/error.html", messages)

def index(request):
    return render(request, 'melsite2/index.html')

def about(response):
    return render(response, "melsite2/about.html", {})

def projects(response):
    return render(response, "melsite2/projectmenu.html", {})

def resume(response):
    return render(response, "melsite2/resume.html", {})

def test(response):
    return render(response, "melsite2/test.html", {})

def projectmenu(response):
    return render(response, "melsite2/projectmenu.html", {})

def dtsc691menu(response):
    return render(response, "melsite2/projects/dtsc691menu.html", {})

def dtsc691_jupyter_notebook(response):
    return render(response, "melsite2/projects/dtsc691/DTSC691ProjectJupyterNotebook.html", {})

def project_analyses(response):
    return render(response, "melsite2/projects/dtsc691/DTSC691ProjectAnalyses.html", {})

def state_heatmap(response):
    return render(response, "melsite2/projects/dtsc691/state_heatmap.html", {})

def us_cities_map(response):
    return render(response, "melsite2/projects/dtsc691/us_cities_map.html", {})

def world_cities_map(response):
    return render(response, "melsite2/projects/dtsc691/world_cities_map.html", {})

def fars(response):
    return render(response, "melsite2/projects/fars.html", {})

def fethealth(response):
    return render(response, "melsite2/projects/fethealth.html", {})


