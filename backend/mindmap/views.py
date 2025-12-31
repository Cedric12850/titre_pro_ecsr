# mindmap/views.py
import json
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MindMap


class MindMapListView(ListView):
    model = MindMap
    template_name = "mindmap/list.html"
    context_object_name = "mindmaps"


class MindMapCreateView(CreateView):
    model = MindMap
    fields = ["title"]
    template_name = "mindmap/editor.html"
    success_url = reverse_lazy("mindmap:mindmap-list")

    def form_valid(self, form):
        data = self.request.POST.get("data")
        if data:
            form.instance.data = json.loads(data)
        return super().form_valid(form)


class MindMapUpdateView(UpdateView):
    model = MindMap
    fields = ["title"]
    template_name = "mindmap/editor.html"
    success_url = reverse_lazy("mindmap:mindmap-list")

    def form_valid(self, form):
        data = self.request.POST.get("data")
        if data:
            form.instance.data = json.loads(data)
        return super().form_valid(form)


class MindMapDeleteView(DeleteView):
    model = MindMap
    template_name = "mindmap/confirm_delete.html"
    success_url = reverse_lazy("mindmap:mindmap-list")
