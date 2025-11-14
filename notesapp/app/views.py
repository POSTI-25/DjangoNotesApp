from django.shortcuts import render
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/app/'
    template_name = 'app/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/app/'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title' , 'text']
    success_url = '/smart/app/'
    form_class = NotesForm

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    login_url = "/admin/login/"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'app/notes_list.html', {'app': all_notes})

# def detail(request, pk):
#     note = Notes.objects.get(pk=pk)
#     return render(request, 'app/notes_detail.html', {'note': note})