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

def note_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content)
        
    # ✅ Add 'notes:' before the name
    return redirect('notes:note_list')

def note_edit(request, pk):
    # 1. Define 'note' at the very top so both IF and ELSE can see it!
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes:note_list")
    else:
        # 2. This is where the yellow line was likely complaining
        form = NoteForm(instance=note) 

    return render(request, "notes/note_edit.html", {"form": form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        # ❌ You had: redirect("note_list")
        # ✅ Must be:
        return redirect("notes:note_list") 

    return render(request, "notes/note_delete.html", {"note": note})

