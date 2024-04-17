from django.shortcuts import render
from .models import Mesures
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import Datafile

def index(request):

    data = Mesures.objects.all().values().first()
    files = Datafile.objects.all()

    return render(request, 'appAquaponie/index.html', {
        'data': data,
        'files': files
    })



def download_datafile(request, datafile_id):
    datafile = get_object_or_404(Datafile, pk=datafile_id)
    file_path = datafile.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{datafile.title}"'
    return response


