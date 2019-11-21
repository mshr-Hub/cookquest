from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .models import CustomUser, Quest, Message

# Create your views here.

def toppage(request):
    """
    トップページ
    """
    return render(request, 'toppage.html')


@login_required
def quest_index(request):
    """
    クエスト一覧
    """
    quests = Quest.objects.order_by("-created_at")
    page_quests = paginate_query(request, quests, settings.PAGE_PER_ITEM)
    return render(request, 'quest/index.html', {'quests': quests, 'page_quests': page_quests})


def paginate_query(request, queryset, count):
    """
    ページネーション用に、Pageオブジェクトを返す。
    """
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


@login_required
def quest_create(request):
    """
    クエスト依頼
    """
    if request.method == 'POST':
        quest_title = request.POST['quest_title']
        quest_memo = request.POST['quest_memo']
        quest_text = request.POST['quest_text']
        quest_image = request.FILES.get('quest_image', '')
        customuser_name = request.POST['author']
        author = CustomUser.objects.get(username=customuser_name)
        """
        クエスト依頼のバリデーション
        """
        if quest_title == '':
            return render(request, 'quest/create.html', {'title_validate': 'Please input Quest title'})
        if quest_memo == '':
            return render(request, 'quest/create.html', {'memo_validate': 'Please input Quest memo'})
        if quest_text == '':
            return render(request, 'quest/create.html', {'text_validate': 'Please input Quest text'})
        Quest.objects.create(title=quest_title, memo=quest_memo, text=quest_text, image=quest_image, author=author)
        return redirect('index')
    return render(request, 'quest/create.html')


@login_required
def quest_detail(request, pk):
    """
    クエスト詳細
    """
    quest = Quest.objects.get(pk=pk)
    return render(request, 'quest/detail.html', {'quest': quest})


@login_required
def quest_delete(request, pk):
    """
    クエスト削除確認画面
    """
    quest = Quest.objects.get(pk=pk)
    if request.method == 'POST':
        quest.delete()
        return redirect('index')
    return render(request, 'quest/delete.html', {'quest': quest})


@login_required
def quest_update(request, pk):
    """
    クエスト情報更新
    """
    quest = Quest.objects.get(pk=pk)
    if request.method == 'POST':
        quest_title = request.POST['quest_title']
        quest_memo = request.POST['quest_memo']
        quest_text = request.POST['quest_text']
        quest_image = request.FILES.get('quest_image', quest.image)
        customuser_name = request.POST['author']
        author = CustomUser.objects.get(username=customuser_name)
        """
        クエスト情報更新のバリデーション
        """
        if quest_title == '':
            return render(request, 'quest/update.html', {'title_validate': 'Please input Quest title'})
        if quest_memo == '':
            return render(request, 'quest/update.html', {'memo_validate': 'Please input Quest memo'})
        if quest_text == '':
            return render(request, 'quest/update.html', {'text_validate': 'Please input Quest text'})
        Quest.objects.filter(pk=pk).update_or_create(defaults={'title': quest_title, 'memo': quest_memo, 'text': quest_text, 'image': quest_image, 'author': author})
        return redirect('index')
    return render(request, 'quest/update.html', {'quest': quest})


@login_required
def quest_search(request):
    """
    クエスト検索
    """
    if request.method == 'POST':
        quest_title = request.POST['quest_title']
        quests = Quest.objects.filter(title__icontains=quest_title).order_by("-created_at")
        page_quests = paginate_query(request, quests, settings.PAGE_PER_ITEM)
        """
        クエスト検索のバリデーション
        """
        if quest_title == '':
            return render(request, 'quest/search.html', {'title_validate': 'Please input Quest title'})
        return render(request, 'quest/search_result.html', {'quests': quests, 'page_quests': page_quests})
    return render(request, 'quest/search.html')


def app_login(request):
    """
    ログイン機能
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    if request.user.is_authenticated:
        return render(request,'toppage.html', {'error': 'You are already logged in!'})
    return render(request, 'login.html')


def app_signup(request):
    """
    ユーザー登録機能
    """
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            CustomUser.objects.get(username=username)
            return render(request, 'signup.html', {'error':'This user is already registered!'})
        except:
            user = CustomUser.objects.create_user(username, email, password)
            return redirect('index')
    if request.user.is_authenticated:
        return render(request,'toppage.html', {'error': 'You are already logged in!'})
    return render(request, 'signup.html')


def app_logout(request):
    """
    ログアウト機能
    """
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


@login_required
def mypage(request, pk):
    """
    マイページ
    """
    user = CustomUser.objects.get(pk=pk)
    quests = user.create_quest.filter(author=user).order_by("-created_at")[0:3]
    return render(request, 'mypage.html', {'user': user, 'quests': quests})


@login_required
def message_index(request, pk):
    """
    メッセージ画面
    """
    quest = Quest.objects.get(pk=pk)
    messages = quest.quest_message.filter(quest=quest).order_by("created_at")
    """
    同期通信でのメッセージ送信
    """
    # if request.method == 'POST':
    #     quest = Quest.objects.get(pk=pk)
    #     customuser_name = request.POST['author']
    #     author = CustomUser.objects.get(username=customuser_name)
    #     message_text = request.POST['message_text']
    #     message_image = request.FILES.get('message_image', '')
    #     if message_text == '' and message_image == '':
    #         return render(request, 'message/index.html', {'quest': quest, 'messages': messages, 'message_validate': 'Please input message!'})
    #     Message.objects.create(text=message_text, image=message_image, author=author, quest=quest)
    #     return redirect('message_index', pk=pk)
    return render(request, 'message/index.html', {'quest': quest, 'messages': messages})

