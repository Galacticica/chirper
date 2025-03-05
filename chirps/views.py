from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Chirp
from .forms import ChirpForm


def HomeView(request):
    template = 'chirps/homepage.html'
    chirps = Chirp.objects.order_by('-created_at')
    chirp_form = ChirpForm()
    context = {
        'chirps': chirps,
        'form': chirp_form
    }
    return HttpResponse(template.render(context, request))


