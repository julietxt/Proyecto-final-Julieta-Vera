from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from VentaLibre.models import Articulo, Profile, Mensaje
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "VentaLibre/index.html")

def about(request):
    return render(request, "VentaLibre/about.html")


class ArticuloList(ListView):
    model = Articulo
    context_object_name = "articulos"

class ArticuloMineList(ArticuloList):

    def get_queryset(self):
        return Articulo.objects.filter(propietario=self.request.user.id).all()

class ArticuloDetail(DetailView):
    model = Articulo
    context_object_name = "articulo"


class ArticuloUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    success_url = reverse_lazy("articulo-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        articulo_id = self.kwargs.get("pk")
        return Articulo.objects.filter(propietario=user_id,id=articulo_id).exists()


class ArticuloDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    context_object_name = "articulo"
    success_url = reverse_lazy("articulo-list")

    def test_func(self):
        user_id = self.request.user.id
        articulo_id = self.kwargs.get("pk")
        return Articulo.objects.filter(propietario=user_id,id=articulo_id).exists()


class ArticuloCreate(LoginRequiredMixin, CreateView):
    model = Articulo
    success_url = reverse_lazy("articulo-list")
    fields = '__all__'

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)


class ArticuloSearch(ListView):
    model = Articulo
    context_object_name = "articulos"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Articulo.objects.filter(titulo=criterio).all()
        return result

class Login(LoginView):
    next_page = reverse_lazy("index")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('articulo-list')


class Logout(LogoutView):
    template_name = "registration/logout.html"
    
    
class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("articulo-list")
    fields = ['avatar',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    success_url = reverse_lazy("articulo-list")
    fields = ['avatar',]

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()
    
class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-create')
    fields = '__all__'


class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        return Mensaje.objects.filter(destinatario=self.request.user).exists()
    

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        import pdb; pdb.set_trace
        return Mensaje.objects.filter(destinatario=self.request.user).all()