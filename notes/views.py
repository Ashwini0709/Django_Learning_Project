from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from .forms import NotesForm
from django.views.generic.edit import DeleteView

# Create your views here.

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class DetailListView(DetailView):
    model = Notes
    context_object_name = "note"

class PopularLikesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    queryset = Notes.objects.filter(likes__gte=2)

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_form.html"
    form_class = NotesForm

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_form.html"
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_delete.html"


"""
These are function based views

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})   

def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})

"""