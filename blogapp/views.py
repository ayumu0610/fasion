"""from .models import Article, Comment

from .froms import CommentForm

from django.shortcuts import redirect, get_absolute_or_404"""

from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView

from .models import BlogPost

from django.views.generic import FormView

from django.urls import reverse_lazy

from .forms import ContactForm

from django.contrib import messages

from django.core.mail import EmailMessage
"""
class DetailView(generic.DetailView):
    model = Article
    def get_context_data(self,**kwargs):
        context['comment_form']= CommentForm
        return context

class CommentView(LoginRequiredMixin, generic.edit.CreateView):
    model = Comment
    form_class = CommentForm

    def from_vaild(self,form):
        form.instance.author = self.request.user
        article_pk = self.kwargs.get('pk')
        Article = get_absolute_or_404(Article, pk=article_pk)

        comment = form.save(commit=False)
        comment.target = Article
        comment.save()

        return redirect('blogapp:detail',pk=article_pk)
"""
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('blogapp:contact')

    def form_vaild(self,form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名:{0}\nメールアドレス:{1}\n タイトル:{2}\n メッセージ:\n{3}'\
            .format(name,email,title,message)
        from_email = 'admin@example.com'
        to_list = ['admin@example.com']
        message = EmailMessage(subject=subject,
                                body=massage,
                                from_email=from_email,
                                to=to_list,
                                )
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        return super().form_vaild(form)

class IndexView(ListView):
    '''トップページのビュー
    
    投稿記事を一覧表示するのでListViewを継承する
    
    Attributes:
      template_name: レンダリングするテンプレート
      context_object_name: object_listキーの別名を設定
      queryset: データベースのクエリ
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    # object_listキーの別名を設定
    context_object_name = 'orderby_records'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並べ替える
    queryset = BlogPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数を設定
    paginate_by = 4

class BlogDetail(DetailView):
    '''詳細ページのビュー
    
    投稿記事の詳細を表示するのでDetailViewを継承する
     Attributes:
      template_name: レンダリングするテンプレート
      Model: モデルのクラス
    '''
    # post.htmlをレンダリングする
    template_name ='post.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost

class NaturalView(ListView):
    template_name ='natural_list.html'
    model = BlogPost
    context_object_name = 'natural_records'
    queryset = BlogPost.objects.filter(
        category='natural').order_by('-posted_at')
    paginate_by = 2

class BeautifulView(ListView):
    template_name ='beautiful_list.html'
    model = BlogPost
    context_object_name = 'beautiful_records'
    queryset = BlogPost.objects.filter(
        category='beautiful').order_by('-posted_at')
    paginate_by = 2

class CasualView(ListView):
    template_name ='casual_list.html'
    model = BlogPost
    context_object_name = 'casual_records'
    queryset = BlogPost.objects.filter(
        category='casual').order_by('-posted_at')
    paginate_by = 2

class CuteView(ListView):
    template_name ='cute_list.html'
    model = BlogPost
    context_object_name = 'cute_records'
    queryset = BlogPost.objects.filter(
        category='cute').order_by('-posted_at')
    paginate_by = 2

class CoolView(ListView):
    template_name ='cool_list.html'
    model = BlogPost
    context_object_name = 'cool_records'
    queryset = BlogPost.objects.filter(
        category='cool').order_by('-posted_at')
    paginate_by = 2

class ModeView(ListView):
    template_name ='mode_list.html'
    model = BlogPost
    context_object_name = 'mode_records'
    queryset = BlogPost.objects.filter(
        category='mode').order_by('-posted_at')
    paginate_by = 2