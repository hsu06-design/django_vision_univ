from django.contrib import admin
from django.shortcuts import redirect
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):

    def response_add(self, request, obj, post_url_continue=None):
        """
        After clicking SAVE in admin, redirect to notes list page
        """
        return redirect("note_list")


