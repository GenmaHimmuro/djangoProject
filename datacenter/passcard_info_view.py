from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
from datacenter.time_info import format_duration


def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)

    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        is_strange = visit.count_delayed(minutes=60)
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.get_duration()),
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)