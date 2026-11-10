from django.shortcuts import redirect, render
from catalogo.forms.libro_form import Libroform
from catalogo.models.libro import Libro

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo/libros/libro_list.html', {'libros': libros})

def create_libro(request):
    if request.method == 'POST':
        form = Libroform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = Libroform()
    return render(request, 'catalogo/libros/libro_form.html', {'form': form})

def update_libro(request, pk):
    libro = Libro.objects.get(pk=pk)
    if request.method == 'POST':
        form = Libroform(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = Libroform(instance=libro)
    return render(request, 'catalogo/libros/libro_form.html', {'form': form})

def delete_libro(request, pk):
    libro = Libro.objects.get(pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request, 'catalogo/libros/libro_confirm_delete.html', {'libro': libro})
    