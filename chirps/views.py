from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chirp
from .forms import ChirpForm, LikeForm, ReplyForm
from django.shortcuts import render, redirect
from django.views import View

class HomeView(LoginRequiredMixin, View):
    template_name = 'chirps/homepage.html'
    login_url = '/accounts/login/'  

    def get(self, request):
        return self.render_homepage(request)

    def post(self, request):
        if 'content' in request.POST:
            self.handle_chirp_post(request)
        elif 'chirp_id' in request.POST:
            self.handle_like_post(request)
        
        return self.render_homepage(request)

    def handle_chirp_post(self, request):
        chirp_form = ChirpForm(request.POST)
        if chirp_form.is_valid():
            chirp = chirp_form.save(commit=False)
            chirp.user = request.user  
            chirp.save()
            return redirect('home')

    def handle_like_post(self, request):
        like_form = LikeForm(request.POST)
        if like_form.is_valid():
            chirp_id = like_form.cleaned_data['chirp_id']
            chirp = Chirp.objects.get(id=chirp_id)
            chirp.likes += 1
            chirp.save()
            return redirect('home')

    def render_homepage(self, request):
        chirps = Chirp.objects.order_by('-created_at')
        chirp_form = ChirpForm()
        like_form = LikeForm()
        context = {
            'chirps': chirps,
            'chirp_form': chirp_form,
            'like_form': like_form
        }
        return render(request, self.template_name, context)


class ChirpView(LoginRequiredMixin, View):
    template_name = 'chirps/chirp.html'
    login_url = '/accounts/login/'

    def get(self, request, chirp_id):
        return self.render_chirp_detail(request, chirp_id)

    def post(self, request, chirp_id):
        if 'content' in request.POST:
            self.handle_reply_post(request, chirp_id)
        elif 'chirp_id' in request.POST:
            self.handle_like_post(request, chirp_id)
        
        return self.render_chirp_detail(request, chirp_id)

    def handle_reply_post(self, request, chirp_id):
        chirp = Chirp.objects.get(id=chirp_id)
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.user = request.user
            reply.parent = chirp
            reply.save()
            return redirect('chirp_detail', chirp_id=chirp_id)

    def handle_like_post(self, request, chirp_id):
        like_form = LikeForm(request.POST)
        if like_form.is_valid():
            chirp_id = like_form.cleaned_data['chirp_id']
            chirp_or_reply = Chirp.objects.get(id=chirp_id)
            chirp_or_reply.likes += 1
            chirp_or_reply.save()
            return redirect('chirp_detail', chirp_id=chirp_id)

    def render_chirp_detail(self, request, chirp_id):
        chirp = Chirp.objects.get(id=chirp_id)
        replies = chirp.replies.all()
        reply_form = ReplyForm()
        like_form = LikeForm()
        context = {
            'chirp': chirp,
            'replies': replies,
            'reply_form': reply_form,
            'like_form': like_form
        }
        return render(request, self.template_name, context)