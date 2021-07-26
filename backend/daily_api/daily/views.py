#JSONを返す処理

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters

from .models import Daily


class ListDaily(APIView):
    def get(self, request):
        try:
            daily = Daily.objects.filter(isOpen=True).order_by('-date') #設定が公開になってるものだけを抽出
            res_list =[
                {
                    'id': d.id,
                    'date': d.date,
                    'evaluation': d.evaluation.evaluation,
                }
                for d in daily
            ]

            return Response(res_list)
        except:
            error_msg = "予期せぬエラーが起こってる気がするよ。"
            return Response(error_msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DailyDetail(APIView):
    def get(self, request, pk):
        try:
            try:
                daily = Daily.objects.get(id=pk)
            except:
                error_msg = "ソンナidノニッポーハナイヨ"
                return Response(error_msg, status=status.HTTP_404_NOT_FOUND)
            res = {
                'id': daily.id,
                'date': daily.date,
                'study': daily.study,
                'other': daily.other,
                'first_meet': daily.first_meet,
                'wanna_do': daily.wanna_do,
                'summary': daily.summary,
            }
            return Response(res)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Category(APIView):
    def get(self, request, cat):
        try:
            try:
                daily = Daily.objects.filter(isOpen=True).values_list('date', cat).order_by('-date') #タプル形式でdateと指定したcatの内容だけが取り出される
            except:
                error_msg = "そないカテゴリはなかよ"
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            #一つの要素にidとcontent
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
