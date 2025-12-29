from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from django.forms import ModelForm

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]

def note_list(request):
    notes = Note.objects.all().order_by("-created_at")
    return render(request, "notes/note_list.html", {"notes": notes})

def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")  # 👈 this makes notes page appear after save
    else:
        form = NoteForm()

    return render(request, "notes/create_note.html", {"form": form})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/note_edit.html", {"form": form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")

    return render(request, "notes/note_delete.html", {"note": note})

