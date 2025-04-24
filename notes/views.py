from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from .models import Notes
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from .forms import NotesForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()


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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_form.html"
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_delete.html"

def add_like_view(request, pk):
    if request.method == "POST":
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse('notes.detail', args=(pk,)))
    raise Http404



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