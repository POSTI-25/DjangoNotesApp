from django.shortcuts import render
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/smart/app/'
    template_name = 'app/notes_delete.html'
    login_url = "/admin/login/"

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/smart/app/'
    form_class = NotesForm
    login_url = "/admin/login/"

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    # fields = ['title' , 'text']
    success_url = '/smart/app/'
    form_class = NotesForm
    login_url = "/admin/login/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    login_url = "/admin/login/"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = 'note'
    login_url = "/admin/login/"

    def get_queryset(self):
        return self.request.user.notes.all()


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'app/notes_list.html', {'app': all_notes})

# def detail(request, pk):
#     note = Notes.objects.get(pk=pk)
#     return render(request, 'app/notes_detail.html', {'note': note})