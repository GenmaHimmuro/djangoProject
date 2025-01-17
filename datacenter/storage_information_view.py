from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datacenter.time_info import format_duration


def storage_information_view(request):
    visits_with_no_leaving = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visit in visits_with_no_leaving:
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': format_duration(visit.get_duration()),
            'is_strange': visit.count_delayed(minutes=15)
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)