from django.shortcuts import render, redirect, get_object_or_404
from .models import Widget
from .forms import WidgetForm
from .tasks import rename_widget
# Create your views here.
def widget_list(request):
    widgets = Widget.objects.all()
    return render(request, 'widget_list.html', {'widgets': widgets})

def create_widget(request):
    if request.method == 'POST':
        form = WidgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('widget_list')
    else:
        form = WidgetForm()
    return render(request, 'create_widget.html', {'form': form})

def update_widget(request, widget_id):
    widget = get_object_or_404(Widget, pk=widget_id)

    if request.method == 'POST':
        form = WidgetForm(request.POST, instance=widget)
        if form.is_valid():
            name = form.cleaned_data['name']
            rename_widget.delay(widget_id, name)
            return redirect('widget_list')
    else:
        form = WidgetForm(instance=widget)

    return render(request, 'update_widget.html', {'form': form, 'widget': widget})