from django.urls import path
# views.py를 사용할 수 있게 가져오라는 뜻
from . import views

urlpatterns = {
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    #path('<int:pk>/', views.single_post_page),
    # 입력된 URL이 "blog/"로 끝난다면 임포트한 views.py에
    # 정의되어 있는 index() 함수를 실행
    #path('', views.index)
}