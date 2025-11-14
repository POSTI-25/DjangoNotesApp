from django.shortcuts import render
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView
from .forms import NotesForm

# Create your views here.

class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title' , 'text']
    success_url = '/smart/app/'
    form_class = NotesForm

class NotesListView(ListView):
    model = Notes
    context_object_name = 'app'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'app/notes_list.html', {'app': all_notes})

# def detail(request, pk):
#     note = Notes.objects.get(pk=pk)
#     return render(request, 'app/notes_detail.html', {'note': note})