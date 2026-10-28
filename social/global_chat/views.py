from django.shortcuts import render
from .models import Global_Chat
from .forms import GlobalChatForm
# Create your views here.
def global_chat(req):
    if req.method == 'POST':
        form = GlobalChatForm(req.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = req.user
            message.save()
    return render(req, 'global_chat.html', {
        'global_chat_form': GlobalChatForm(),
        'global_chat': Global_Chat.objects.all()
    })