from django.urls import path
from rest_framework import routers
from .views import BoardViewSet, BoardListViewSet, BoardCardViewSet, BoardMemberViewSet, CardCommentViewSet
from . import views


urlpatterns = [
    # boards
    path('boards/', BoardViewSet.as_view({'get': 'board_list','post':'board_create'})),
    path('boards/<int:id>/detail/', BoardViewSet.as_view({'get': 'board_detail', 'delete': 'board_delete'})),
    # boardlists
    path('list/<int:board_id>/', BoardListViewSet.as_view({'get': 'boardlist_list','post':'boardlist_create'})),
    path('list/<int:list_id>/detail/', BoardListViewSet.as_view({'get': 'boardlist_detail','post':'boardlist_delete'})),
    # cards
    path('card/<int:list_id>/lists/', BoardCardViewSet.as_view({'get': 'card_list','post':'card_create'})),
    # path('card/<int:card_id>/detail', BoardCardViewSet.as_view({'get': 'card_list','post':'card_detail'})),
    # boardmember
    path('member/<int:board_id>/', BoardMemberViewSet.as_view({'get': 'boardmember_list'})),
    # cardcomment
    path('comment/<int:card_id>/', CardCommentViewSet.as_view({'get': 'cardcomment_list'})),
    path('comment/<int:comment_id>/delete/', CardCommentViewSet.as_view({'post': 'cardcomment_delete'})),
]