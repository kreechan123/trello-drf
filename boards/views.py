# from boards.models import Board
# from rest_framework import viewsets
# from rest_framework.response import Response
# from boards.serializers import BoardSerializer


# class BoardViewSet(viewsets.ModelViewSet):
#     serializer = BoardSerializer

#     def board_list(self, request, **kwargs):
#         board_list = Board.objects.all()
#         serializer = self.serializer(board_list, many=True)
#         import pdb; pdb.set_trace()
#         return Response(serializer.data, status=200)

from .models import Board
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from boards.serializers import BoardSerializer
from django.shortcuts import get_object_or_404


class BoardViewSet(viewsets.ViewSet):
    serializer = BoardSerializer

    def board_list(self, request, **kwargs):
        board_list = Board.objects.all()
        serializer = self.serializer(board_list, many=True)
        return Response(serializer.data, status=200)

    def board_create(self, request, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer = serializer.save()
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