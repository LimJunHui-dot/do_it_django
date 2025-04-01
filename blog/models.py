from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    # 문자열의 길이 제한 없이 만든다.
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    # 월, 일, 시, 분, 초까지 기록해줄 수 있는 필드
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #author: 추후 작성 예정

    def __str__(self):
        # 해당 포스트의 pk 값과 title 값
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
