from rest_framework import serializers
from article.models import *
import datetime

class ArticleSerializer(serializers.ModelSerializer):
    # username = serializers.SerializerMethodField()
    create_time = serializers.SerializerMethodField()
    class Meta:
        model = Artical
        fields = ('user_id','artical_title','artical_content','create_time','artical_views','artical_comment_count',
                  'artical_like_count')
        read_only_fields = ('artical_views','artical_comment_count','artical_like_count')

    # def get_username(self,obj):
    #     return obj.user_id

    def get_create_time(self,obj):
        return datetime.datetime.strftime(datetime.datetime.now(),"%Y.%m.%d %H.%M.%S")

class ArticalLabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticalLabel
        fields = '__all__'

class ArticalSortSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticalSort
        fields = '__all__'

class LabelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Labels
        fields = '__all__'