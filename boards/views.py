from .models import User, Board, Boardlist, Card, BoardMember, CardComment
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from boards.serializers import BoardSerializer, BoardListSerializer, BoardCardSerializer, BoardMemberSerializer, CardCommentSerializer
from django.shortcuts import get_object_or_404, HttpResponse


class BoardViewSet(viewsets.ViewSet):
    serializer = BoardSerializer

    def board_list(self, request, **kwargs):
        board_list = Board.objects.filter(archive='False')
        serializer = self.serializer(board_list, many=True)
        return Response(serializer.data, status=200)


    def board_create(self, request, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    def board_detail(self, request, **kwargs):
        board = get_object_or_404(Board, id=kwargs.get('id'))
        serializer = self.serializer(board)
        return Response(serializer.data, status=200)


    def board_delete(self, request, **kwargs):
        board = get_object_or_404(Board, id=kwargs.get('id'))
        board.archive = True
        board.save()
        serializer = self.serializer(board)
        return Response(serializer.data, status=200)


class BoardListViewSet(viewsets.ViewSet):
    serializer = BoardListSerializer

    def boardlist_list(self, request, **kwargs):
        board = get_object_or_404(Board, id=kwargs.get('board_id'))
        boardlists = Boardlist.objects.filter(board=board, archive='False')
        serializer = self.serializer(boardlists, many=True)
        return Response(serializer.data, status=200)

        
    def boardlist_create(self, request, **kwargs):
        board = get_object_or_404(Board, id=kwargs.get('board_id'))
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(board=board)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    def boardlist_detail(self, request, **kwargs):
        card = get_object_or_404(Boardlist, id=kwargs.get('list_id'))
        serializer = self.serializer(card)
        return Response(serializer.data, status=200)


    def boardlist_delete(self, request, **kwargs):
        boardlist = get_object_or_404(Boardlist, id=kwargs.get('list_id'))
        boardlist.archive = True
        boardlist.save()
        serializer = self.serializer(boardlist)
        return Response(serializer.data, status=200)


class BoardCardViewSet(viewsets.ViewSet):
    """ Card list and action
    """
    serializer = BoardCardSerializer

    def card_list(self, request, **kwargs):
        boardlist = get_object_or_404(Boardlist, id=kwargs.get('list_id'))
        cards = Card.objects.filter(boardlist=boardlist)
        serializer = self.serializer(cards, many=True)
        return Response(serializer.data, status=200)


    def card_create(self, request, **kwargs):
        boardlist = Boardlist.objects.get(id = kwargs.get('list_id'))
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(boardlist=boardlist)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


    def card_detail(self, request, **kwargs):
        card = get_object_or_404(Card, id=kwargs.get('card_id'))
        serializer = self.serializer(card)
        return Response(serializer.data, status=200)


    def card_delete(self, request, **kwargs):
        card = get_object_or_404(Card, id=kwargs.get('card_id'))
        card.delete()
        return HttpResponse("Deleted")


class BoardMemberViewSet(viewsets.ViewSet):
    """ Boardmember View and action
    """
    serializer = BoardMemberSerializer

    def boardmember_list(self, request, **kwargs):
        board = get_object_or_404(Board, id=kwargs.get('board_id'))
        member = BoardMember.objects.filter(board=board)
        serializer = self.serializer(member, many=True)
        return Response(serializer.data, status=200)


class CardCommentViewSet(viewsets.ViewSet):
    """Card Comment View
    """
    serializer = CardCommentSerializer

    def comment_list(self, request, **kwargs):
        card = get_object_or_404(Card, id=kwargs.get('card_id'))
        comment = CardComment.objects.filter(card=card)
        serializer = self.serializer(comment, many=True)
        return Response(serializer.data, status=200)


    def comment_create(self, request, **kwargs):
        card = Card.objects.get(id = kwargs.get('card_id'))
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(card=card, user=request.user)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
  

    def comment_delete(self, request, **kwargs):
        comment = get_object_or_404(CardComment, id=kwargs.get('comment_id'))
        comment.delete()
        return Response("Deleted")