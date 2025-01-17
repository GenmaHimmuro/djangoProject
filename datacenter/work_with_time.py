SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60


def format_duration(duration):

    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, SECONDS_PER_HOUR)

    minutes, seconds = divmod(remainder, SECONDS_PER_MINUTE)
    return f'{hours}ч {minutes}мин'