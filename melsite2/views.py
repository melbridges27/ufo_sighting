from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404
from .models import toDoList, Item

# Create your views here.
#def index(response, name):
#    ls = toDoList.objects.get(name=name)
#    items = ls.item_set.get(id=1)
#    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(Item.text)))

def home(request):
    return render(request, 'melsite2/index.html')

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
    return render(response, "melsite2/projects/dtsc691/dtsc691_jupnotebook.html", {})

def project_analyses(response):
    return render(response, "melsite2/projects/dtsc691/project_analyses.docx", {})

def state_heatmap(response):
    return render(response, "melsite2/projects/dtsc691/state_heatmap.html", {})

def us_cities_map(response):
    return render(response, "melsite2/projects/dtsc691/us_cities_map.html", {})

def world_cities_map(response):
    return render(response, "melsite2/projects/dtsc691/world_cities_map.html", {})

def project_analyses(response):
    return render(response, "melsite2/projects/dtsc691/DTSC691ProjectAnalysis.html", {})

def preds(response):
    return render(response, "melsite2/projects/dtsc691/preds.html", {})

def json(response):
    return render(response, "melsite2/projects/dtsc691/nuforc_reports.json", {})

def fars(response):
    return render(response, "melsite2/projects/fars.html", {})

def fethealth(response):
    return render(response, "melsite2/projects/fethealth.html", {})

def pdf_view(request): 
    try: return FileResponse(open("melsite2/projects/dtsc691/DTSC691ProjectAnalysis.pdf", "rb"), content_type="application/pdf") 
    except FileNotFoundError: raise Http404()

