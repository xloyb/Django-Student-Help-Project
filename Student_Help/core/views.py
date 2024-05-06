from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post,Logement, Transport, Stage, Evenement, Recommandation, Commentaire, Like,Notification

from django.shortcuts import render, redirect
from .forms import LogementForm, TransportForm, StageForm, EvenementForm, RecommandationForm,CommentForm


from django.views.generic import ListView,DeleteView,UpdateView,DetailView


from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render, redirect
from .forms import CommentForm


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'  
    context_object_name = 'post'


class PostWithCommentDetailView(DetailView):
    model = Post
    template_name = 'components/postwithcomment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_id = self.kwargs.get('comment_id')
        context['comment'] = Commentaire.objects.get(id=comment_id)
        return context



# class PostWithCommentDetailView(DetailView):
#     model = Commentaire
#     template_name = 'components/post.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post_id = self.kwargs.get('post_id')
#         comment_id = self.kwargs.get('comment_id')
#         comment = Commentaire.objects.get(id=comment_id)
#         context['post'] = comment.post
#         context['comment'] = comment
#         return context

# def create_comment(request, post_id):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.post_id = post_id
#             comment.save()
#             return redirect('dashboard')  


def create_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = post_id
            comment.save()
            cid = comment.id
            post = Post.objects.get(pk=post_id)
            commenter = request.user
            message = f"{commenter.username} commented on your post: {comment.content}"
            create_notification_for_comment(post, commenter, message,cid)
            
            return redirect('dashboard')

def create_notification_for_Like(post, commenter, message):
    Notification.objects.create(
        user=post.creator, 
        message=message, 
        link=f"/post/{post.id}/"
    )

def create_notification_for_comment(post, commenter,message,cid):
    #if commenter != post.creator:  # Disabled for now 
        Notification.objects.create(user=post.creator, message=message, link=f"/post/{post.id}/comment/{cid}")



@csrf_exempt
def like_post(request):
    if request.method == 'POST' and request.user.is_authenticated:
        post_id = request.POST.get('post_id')
        user = request.user
        try:
            like = Like.objects.get(user=user, post_id=post_id)
            like.delete()
            return JsonResponse({'success': True, 'action': 'unliked'})
        except Like.DoesNotExist:
            Like.objects.create(user=user, post_id=post_id)
            post = Post.objects.get(id=post_id)
            create_notification_for_Like(post, user, f"{user.username} liked your post.")
            return JsonResponse({'success': True, 'action': 'liked'})
    return JsonResponse({'success': False})

# @csrf_exempt
# def like_post(request):
#     if request.method == 'POST' and request.user.is_authenticated:
#         post_id = request.POST.get('post_id')
#         user = request.user        
#         try:
#             like = Like.objects.get(user=user, post_id=post_id)
#             like.delete()
            


#             return JsonResponse({'success': True, 'action': 'unliked'})
#         except Like.DoesNotExist:
#             Like.objects.create(user=user, post_id=post_id)

#             return JsonResponse({'success': True, 'action': 'liked'})
#     return JsonResponse({'success': False})

# def like_post(request):
#     if request.method == 'POST':
#         post_id = request.POST.get('post_id')
#         post = get_object_or_404(Post, pk=post_id)
#         user = request.user
#         # Check if the user has already liked the post
#         already_liked = Like.objects.filter(user=user, post=post).exists()
#         if already_liked:
#             # Unlike the post
#             Like.objects.filter(user=user, post=post).delete()
#         else:
#             # Like the post
#             Like.objects.create(user=user, post=post)
#         # Get the updated like count for the post
#         likes_count = post.likes.count()
#         return JsonResponse({'success': True, 'likes_count': likes_count})
#     else:
#         return JsonResponse({'success': False})


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    success_url = reverse_lazy('dashboard')  

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if hasattr(post, 'recommandation'):
            return post.recommandation
        elif hasattr(post, 'transport'):
            return post.transport
        elif hasattr(post, 'stage'):
            return post.stage
        elif hasattr(post, 'evenement'):
            return post.evenement
        elif hasattr(post, 'logement'):
            return post.logement
        else:
            return None

    def get_form_class(self):
        post = self.object
        if hasattr(post, 'recommandation'):
            return RecommandationForm
        elif hasattr(post, 'transport'):
            return TransportForm
        elif hasattr(post, 'stage'):
            return StageForm
        elif hasattr(post, 'evenement'):
            return EvenementForm
        elif hasattr(post, 'logement'):
            return LogementForm
        else:
            return None


    # def get_object(self, queryset=None):
    #     post = super().get_object(queryset)
    #     if post.recommandation:
    #         return post.recommandation
    #     elif post.transport:
    #         return post.transport
    #     elif post.stage:
    #         return post.stage
    #     elif post.evenement:
    #         return post.evenement
    #     elif post.logement:
    #         return post.logement
    #     else:
    #         return None

    # def get_form_class(self):
    #     post = self.object
    #     if post.recommandation:
    #         return RecommandationForm
    #     elif post.transport:
    #         return TransportForm
    #     elif post.stage:
    #         return StageForm
    #     elif post.evenement:
    #         return EvenementForm
    #     elif post.logement:
    #         return LogementForm
    #     else:
    #         return None

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)


# class PostUpdateView(LoginRequiredMixin, UpdateView):
#     model = Post
#     fields = ['title', 'description', 'image']  # Specify the fields you want to allow users to edit
#     success_url = reverse_lazy('dashboard')  # URL to redirect after successful update

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         if self.object.creator == self.request.user:
#             return super().get(request, *args, **kwargs)
#         else:
#             return HttpResponseForbidden("You are not allowed to edit this post.")

#     def form_valid(self, form):
#         form.instance.creator = self.request.user  # Set the creator of the post to the current user
#         return super().form_valid(form)



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



class PostListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard.html'
    context_object_name = 'posts'
    form_class = CommentForm  


    def get_queryset(self):
        queryset = Post.objects.select_related('logement', 'transport', 'stage', 'evenement', 'recommandation').order_by('-created_at')
        user = self.request.user
        for post in queryset:
            post.is_liked = post.is_liked_by_user(user)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = self.form_class()  
        return context

def get_liked_status(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(pk=post_id)
            user = request.user
            if user.is_authenticated:
                is_liked = post.is_liked_by_user(user)
                return JsonResponse({'success': True, 'is_liked': is_liked})
            else:
                return JsonResponse({'success': False, 'error': 'User not authenticated'})
        except Post.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Post not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


# class PostListView(ListView):
#     template_name = 'dashboard.html'
#     context_object_name = 'posts'

#     def get_queryset(self):

#         #return Post.objects.select_related('logement', 'transport', 'stage', 'evenement', 'recommandation').all()
#         return Post.objects.select_related('logement', 'transport', 'stage', 'evenement', 'recommandation').order_by('-created_at')


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
            return redirect('dashboard')
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

