from django.urls import path
from rest_framework import routers
from .views import BoardViewSet, BoardListViewSet, BoardCardViewSet, BoardMemberViewSet, CardCommentViewSet
from . import views


urlpatterns = [
    # boards
    path('boards/', BoardViewSet.as_view({'get': 'board_list','post':'board_create'})),
    path('boards/<int:id>/', BoardViewSet.as_view({'get': 'board_detail', 'delete': 'board_delete'})),
    # boardlists
    path('boards/<int:board_id>/lists/', BoardListViewSet.as_view({'get': 'boardlist_list','post':'boardlist_create'})),
    path('boards/<int:board_id>/lists/<int:list_id>/', BoardListViewSet.as_view({'get': 'boardlist_detail','post':'boardlist_delete'})),
    # cards
    path('boards/<int:board_id>/lists/<int:list_id>/cards/', BoardCardViewSet.as_view({'get': 'card_list','post':'card_create'})),
    path('boards/<int:board_id>/lists/<int:list_id>/cards/<int:card_id>/', BoardCardViewSet.as_view({'get': 'card_detail','post':'card_delete'})),

    # cardcomment
    path('boards/<int:board_id>/lists/<int:list_id>/cards/<int:card_id>/comments/', CardCommentViewSet.as_view({'get': 'comment_list', 'post':'comment_create'})),
    path('boards/<int:board_id>/lists/<int:list_id>/cards/<int:card_id>/comments/<int:comment_id>/', CardCommentViewSet.as_view({'delete': 'comment_delete'})),
    # boardmember
    path('boards/<int:board_id>/members/', BoardMemberViewSet.as_view({'get': 'boardmember_list'})),
    path('boards/<int:board_id>/members/<int:member_id>/', BoardMemberViewSet.as_view({'get': 'boardmember_list'})),
]