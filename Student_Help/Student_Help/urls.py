from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_view

from core.views import home,Dashboard,layout,profile,register,login,create_post,PostListView,PostDeleteView,PostUpdateView,like_post,get_liked_status, create_comment, PostWithCommentDetailView, PostDetailView, fetch_notifications,report_post, modcp_dashboard,update_report_status, modcp_reports, modcp_users, user_update, mark_all_notifications_as_read,profile_view, update_profile
from django.conf import settings
from django.conf.urls.static import static
# from core.views import PostListView

urlpatterns = [
    path('',home, name='home'), # Default view when accessing root of site
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    #path('dashboar/',Dashboard, name='dashboard'),
    path('t/',layout),
    path('profile/',profile, name='profile'),
    path('register/',register, name='register'),
    #path('login/',login, name='login'),
    path('login/', auth_view.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
    # path('posts/', PostListView.as_view(), name='post_list'),
    #path('api/',include('api.urls')),
    path('newpost/',create_post,name='create_post'),
    path('dashboard/', PostListView.as_view(), name='dashboard'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    #path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('like/', like_post, name='like_post'),
    path('get-liked-status/<int:post_id>/', get_liked_status, name='get_liked_status'),
    path('post/<int:post_id>/comment/', create_comment, name='create_comment'),
    path('post/<int:pk>/comment/<int:comment_id>/', PostWithCommentDetailView.as_view(), name='post_with_comment'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('fetch-notifications/', fetch_notifications, name='fetch_notifications'),
    path('report-post/<int:post_id>/', report_post, name='report_post'),
    path('modcp/', modcp_dashboard, name='modcp_dashboard'), 
    path('modcp/update_report_status/<int:report_id>/', update_report_status, name='update_report_status'),
    path('modcp/reports/', modcp_reports, name='modcp_reports'), 
    path('modcp/users/', modcp_users, name='modcp_users'), 
    path('modcp/users/user/<int:user_id>/update/', user_update, name='user_update'),
    path('mark-all-notifications-as-read/', mark_all_notifications_as_read, name='mark_all_notifications_as_read'),
    path('profile/<str:username>/', profile_view, name='profile'),
    path('settings/update/', update_profile, name='update_profile'),



    





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

