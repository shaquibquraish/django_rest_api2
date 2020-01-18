from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
# from polls import views
from polls.apiviews import ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

# urlpatterns = [
#     path('polls/', views.polls_list, name='polls_list'),
#     path('polls/<int:pk>', views.polls_detail, name='polls_detail'),
#
# ]
urlpatterns = [
    # path('polls/', PollList.as_view(), name='polls_list'),
    # path('polls/<int:pk>', PollDetail.as_view(), name='polls_detail'),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),
    # path('login/', views.obtain_auth_token, name='login'), Another way to create this login endpoint is using obtain_auth_token method provide by DRF
    # path('logout/', logout_view, name='logout'),
]

urlpatterns += router.urls

# note:
# We have seen 4 ways to build API views until now
# • Pure Django views in views.py file
# • APIView subclasses
# • generics.* subclasses
# • viewsets.ModelViewSet
# So which one should you use when? My rule of thumb is,
# • Use viewsets.ModelViewSet when you are going to allow all or most of CRUD operations on a model.
# • Use generics.* when you only want to allow some operations on a model
# • Use APIView when you want to completely customize the behaviour.
