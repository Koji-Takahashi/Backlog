from django.shortcuts import render
from django.http import HttpResponse
from backlog.models import Issue


def issue_list(request):
    """課題の一覧"""
    # return HttpResponse('課題の一覧')
    # issues = Issue.objects.all().order_by('id')
    issues = []
    # names = Issue.objects.values('name').order_by('name').distinct()
    names = ['岩崎　月斗', '日壁　博之', '服部 幹太', '葛山']
    for name in names:
        issuebyname = Issue.objects.filter(name=name)
        for issue in issuebyname:
            issue.summary = issue.summary[:12]
        issues.append(issuebyname)

    return render(request,
                  'backlog/issue_list.html',  # 使用するテンプレート
                  {'issues': issues})  # テンプレートに渡すデータ
