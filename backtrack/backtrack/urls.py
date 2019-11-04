from django.urls import path
from django.conf.urls import url
from .views import PBIviews, projectViews
from django.shortcuts import redirect

urlpatterns = [
    # path('', lambda x: redirect('1/'),name='home'),
    path('', PBIviews.HomeView.as_view(), name='home'),
    path('<int:pk>/pb/', PBIviews.ProductBacklogView.as_view(), name='pb'),
    path('<int:pk>/pb/add/', PBIviews.AddPBI.as_view(), name='add-pbi'),
    path('<int:pk>/pb/<int:pbipk>/update',
         PBIviews.updatePBI.as_view(), name='detail-pbi'),
    path('<int:pk>/pb/<int:pbipk>/delete',
         PBIviews.DeletePBI.as_view(), name='delete-pbi'),
    path('project/create', projectViews.CreateProject.as_view(),
         name='create-project'),
    path('project/create/<int:pk>/inviteList', projectViews.InviteMember.as_view(),
         name='invite-project-members'),
         path('<int:pk>/inviteAccept', projectViews.EmailMember.as_view(),
         name='email-member'),
    path('project/create/<int:pk>/add/developer', projectViews.AddDeveloper.as_view(),
         name='add-project-developer')
]
