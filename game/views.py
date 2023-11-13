from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line2 = '<img src="https://pic2.zhimg.com/v2-41a37d8e2bbcf61c5805a308debb4dfd_r.jpg?source=1940ef5c">'
    line3 = '<hr>'
    line4 = '<a href="/play/">进入游戏</a>'
    return HttpResponse(line1 + line4 + line3 + line2)

def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line2 = '<img src="https://ts1.cn.mm.bing.net/th/id/R-C.06a209f100a18ee1ef662a63aefbe39c?rik=fWBqdQMxDysJCA&riu=http%3a%2f%2fi2.sinaimg.cn%2fgm%2fj%2fi%2f2009-03-17%2fU1850P115T41D162079F756DT20090317125238.jpg&ehk=38Fe6i4Jq7PhjbY8uqPzK4ZkPkNqj%2biGp25vDy7Jbkw%3d&risl=&pid=ImgRaw&r=0">'
    line3 = '<a href="/">返回主页面</a>'
    return HttpResponse(line1 + line3 +line2)

