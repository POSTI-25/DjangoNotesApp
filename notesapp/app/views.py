from django.shortcuts import render
from .models import Notes

# Create your views here.
def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'app/notes_list.html', {'app': all_notes})

def detail(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'app/notes_detail.html', {'note': note})