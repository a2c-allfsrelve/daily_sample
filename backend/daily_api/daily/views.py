# JSONを返す処理

from dataclasses import field
from pyexpat import model
from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters
from rest_framework import serializers
from rest_framework.parsers import JSONParser

from .models import Daily


class ListDaily(APIView):
    def get(self, request):
        try:
            # 設定が公開になってるものだけを抽出
            daily = Daily.objects.filter(isOpen=True).order_by('-date')
            # QuerySetをJSONにパースして返す
            return Response(daily.values("id", "date", "evaluation"), status.HTTP_200_OK)

        except Exception as ex:
            return Response(ex, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DailyDetail(APIView):
    # 特定の日記取得
    def get(self, request, pk):
        try:
            try:
                daily = Daily.objects.get(id=pk)
                serializer = DailySerializer(daily)  # 　シリアライザバリ便利
            except:
                error_msg = "ソンナidノニッポーハナイヨ"
                return Response(error_msg, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data)

        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# 日記登録
class RegistDaily(APIView):
    def get(self, request):
        return Response(data={
            'data': "あいうえお"
        })

    def post(self, request, *args, **kwargs):
        try:
            # シリアライズ
            serializer = DailySerializer(data=request.data)
            # バリデーション
            serializer.is_valid(raise_exception=True)
            # DB登録
            serializer.save()

            response = "成功"
            return Response(data=response, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response(data=ex, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# カテゴリ検索
class Category(APIView):
    def get(self, request, cat):
        try:
            try:
                # タプル形式でdateと指定したcatの内容だけが取り出される
                daily = Daily.objects.filter(isOpen=True).values_list(
                    'date', cat).order_by('-date')
            except:
                error_msg = "そないカテゴリはなかよ"
                return Response(data=error_msg, status=status.HTTP_404_NOT_FOUND)
            # 一つの要素にidとcontent
            res_list = [
                {
                    'id': d[0],
                    'content': d[1]
                }
                for d in daily
            ]
            return Response(res_list)

        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Dailyモデルのシリアライザ
class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily
        fields = ('date', 'univ', 'study', 'other', 'first_meet',
                  'wanna_do', 'summary', 'evaluation', 'evaluation', 'isOpen')
