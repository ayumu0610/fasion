from django.db import models
"""from django.urls import reverse

class Article(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('blogapp:detail',kwargs={'pk': self.pk})

class Comment(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    target = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )
    content = models.TextField('コメント')
    created_at = models.DateTimeField(auto_now_add=True)
"""
class BlogPost(models.Model):
    '''モデルクラス
    '''
    # カテゴリに設定する項目を入れ子のタプルとして定義
    # タプルの第1要素はモデルが使用する値、
    # 第2要素は管理サイトの選択メニューに表示する文字列
    CATEGORY = (('natural','ナチュラル'),
                ('beautiful','きれいめ'),
                ('casual','カジュアル'),
                ('cute', '可愛い系'),
                ('cool', 'クール系'),
                ('mode', 'モード系'),)

    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル', # フィールドのタイトル
        max_length=200        # 最大文字数は200
        )
    # 本文用のフィールド
    content = models.TextField(
        verbose_name='本文'   # フィールドのタイトル
        )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', # フィールドのタイトル
        auto_now_add=True       # 日時を自動追加
        )
    # カテゴリのフィールド
    category = models.CharField(
        verbose_name='カテゴリ', # フィールドのタイトル
        max_length=50,        # 最大文字数は50
        choices=CATEGORY # categoryフィールドにはCATEGORYの要素のみを登録
        )
    
    def __str__(self):
        '''Django管理サイトでデータを表示する際に識別名として
           投稿記事のタイトル(titleフィールドの値を表示するために必要
        
        Returns(str):投稿記事のタイトル
        '''
        return self.title
    
