from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post,Logement, Transport, Stage, Evenement, Recommandation, Commentaire, Like

from django.shortcuts import render, redirect
from .forms import LogementForm, TransportForm, StageForm, EvenementForm, RecommandationForm

def create_post(request):
    if request.method == 'POST':
        # Check for hidden form field indicating post type
        if 'logement' in request.POST:
            form = LogementForm(request.POST)
        elif 'transport' in request.POST:
            form = TransportForm(request.POST)
        elif 'stage' in request.POST:
            form = StageForm(request.POST)
        elif 'evenement' in request.POST:
            form = EvenementForm(request.POST)
        elif 'recommandation' in request.POST:
            form = RecommandationForm(request.POST)
        else:
            # Handle invalid or missing form type
            return render(request, 'components/create_post.html', {'error': 'Invalid form type'})

        if form.is_valid():
            # Save the form data to the database (common for all types)
            post = form.save(commit=False)
            post.creator = request.user  # Assuming user is authenticated
            post.save()

            # Additional logic for specific post types (optional)
            if isinstance(post, Logement):
                # Do something specific for Logement posts
                pass
            elif isinstance(post, Transport):
                # Do something specific for Transport posts
                pass
            elif isinstance(post, stage):
                # Do something specific for Transport posts
                pass
            elif isinstance(post, evenement):
                # Do something specific for Transport posts
                pass
            elif isinstance(post, recommandation):
                # Do something specific for Transport posts
                pass
            return redirect('home')  #replace this with a notification in the headaer
        else:
            return render(request, 'components/create_post.html', {'form': form})

    form_dict = {'logement': LogementForm(), 'transport': TransportForm(),
                 'stage': StageForm(), 'evenement': EvenementForm(),
                 'recommandation': RecommandationForm()}
    form = form_dict.get(request.GET.get('type'))  # Allow GET param to pre-select form type (optional)
    if not form:
        form = "null"  # Set default form (optional)
    return render(request, 'components/create_post.html', {'form': form})


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

