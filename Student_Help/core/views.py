from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post,Logement, Transport, Stage, Evenement, Recommandation, Commentaire, Like

from django.shortcuts import render, redirect
from .forms import LogementForm, TransportForm, StageForm, EvenementForm, RecommandationForm


from django.views.generic import ListView,DeleteView


from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.creator == self.request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not allowed to delete this post.")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.creator == self.request.user:
            return super().delete(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not allowed to delete this post.")



class PostListView(ListView):
    template_name = 'dashboard.html'
    context_object_name = 'posts'

    def get_queryset(self):

        #return Post.objects.select_related('logement', 'transport', 'stage', 'evenement', 'recommandation').all()
        return Post.objects.select_related('logement', 'transport', 'stage', 'evenement', 'recommandation').order_by('-created_at')


def create_post(request):
    form_type = request.GET.get('type')  # Get the selected form type from the URL parameter

    if request.method == 'POST':
        # Use form_type to determine which form to initialize
        if form_type == 'logement':
            form = LogementForm(request.POST)
        elif form_type == 'transport':
            form = TransportForm(request.POST)
        elif form_type == 'stage':
            form = StageForm(request.POST)
        elif form_type == 'evenement':
            form = EvenementForm(request.POST)
        elif form_type == 'recommandation':
            form = RecommandationForm(request.POST)
        else:
            return render(request, 'components/create_post.html', {'error': 'Invalid form type'})

        if form.is_valid():
            # Save the form data to the database
            post = form.save(commit=False)
            post.creator = request.user
            post.save()

            # Additional logic for specific post types (optional)
            # ...
            return redirect('home')
        else:
            return render(request, 'components/create_post.html', {'form': form})

    # Initialize the form based on the selected form type
    form = {
        'logement': LogementForm(),
        'transport': TransportForm(),
        'stage': StageForm(),
        'evenement': EvenementForm(),
        'recommandation': RecommandationForm()
    }.get(form_type)

    # If form_type is missing or invalid, handle it gracefully
    if not form:
        return render(request, 'components/create_post.html', {'error': 'Please select a form type'})

    return render(request, 'components/create_post.html', {'form': form})


# def create_post(request):
#     if request.method == 'POST':
#         # Check for hidden form field indicating post type
#         if 'logement' in request.POST:
#             form = LogementForm(request.POST)
#         elif 'transport' in request.POST:
#             form = TransportForm(request.POST)
#         elif 'stage' in request.POST:
#             form = StageForm(request.POST)
#         elif 'evenement' in request.POST:
#             form = EvenementForm(request.POST)
#         elif 'recommandation' in request.POST:
#             form = RecommandationForm(request.POST)
#         else:
#             # Handle invalid or missing form type
#             return render(request, 'components/create_post.html', {'error': 'Invalid form type'})

#         if form.is_valid():
#             # Save the form data to the database (common for all types)
#             post = form.save(commit=False)
#             post.creator = request.user  # Assuming user is authenticated
#             post.save()

#             # Additional logic for specific post types (optional)
#             if isinstance(post, Logement):
#                 # Do something specific for Logement posts
#                 pass
#             elif isinstance(post, Transport):
#                 # Do something specific for Transport posts
#                 pass
#             elif isinstance(post, stage):
#                 # Do something specific for Transport posts
#                 pass
#             elif isinstance(post, evenement):
#                 # Do something specific for Transport posts
#                 pass
#             elif isinstance(post, recommandation):
#                 # Do something specific for Transport posts
#                 pass
#             return redirect('home')  #replace this with a notification in the headaer
#         else:
#             return render(request, 'components/create_post.html', {'form': form})

#     form_dict = {'logement': LogementForm(), 'transport': TransportForm(),
#                  'stage': StageForm(), 'evenement': EvenementForm(),
#                  'recommandation': RecommandationForm()}
#     form = form_dict.get(request.GET.get('type'))  # Allow GET param to pre-select form type (optional)
#     if not form:
#         form = "null"  # Set default form (optional)
#     return render(request, 'components/create_post.html', {'form': form})


def  home(request):
    return render (request, 'home.html')

@login_required
def Dashboard(request):
    return render(request, 'dashboard.html')
  

def  layout(request):
    return render (request, 'layout.html')


def  profile(request):
    return render (request, 'pages/profile.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})

def  login(request):
    return render (request, 'registration/login.html')

