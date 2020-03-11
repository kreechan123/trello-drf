from django.urls import path
from rest_framework import routers
from . import views
from .views import BoardViewSet, BoardListViewSet, BoardCardViewSet, BoardMemberViewSet, CardCommentViewSet


urlpatterns = [
    # boards
    path('', BoardViewSet.as_view({'get': 'board_list','post':'board_create'})),
    path('<int:id>/', BoardViewSet.as_view({'get': 'board_detail', 'delete': 'board_delete'})),
    # boardlists
    path('<int:board_id>/lists/', BoardListViewSet.as_view({'get': 'boardlist_list','post':'boardlist_create'})),
    path('<int:board_id>/lists/<int:list_id>/', BoardListViewSet.as_view({'get': 'boardlist_detail','post':'boardlist_delete'})),
    # cards
    path('<int:board_id>/lists/<int:list_id>/cards/', BoardCardViewSet.as_view({'get': 'card_list','post':'card_create'})),
    path('<int:board_id>/lists/<int:list_id>/cards/<int:card_id>/', BoardCardViewSet.as_view({'get': 'card_detail','post':'card_delete'})),

    # cardcomment
    path('<int:board_id>/lists/<int:list_id>/cards/<int:card_id>/comments/', CardCommentViewSet.as_view({'get': 'comment_list', 'post':'comment_create'})),
    path('<int:board_id>/lists/<int:list_id>/cards/<int:card_id>/comments/<int:comment_id>/', CardCommentViewSet.as_view({'delete': 'comment_delete'})),
    # boardmember
    path('<int:board_id>/members/', BoardMemberViewSet.as_view({'get': 'boardmember_list'})),
    path('<int:board_id>/members/<int:member_id>/', BoardMemberViewSet.as_view({'get': 'boardmember_list'})),
]