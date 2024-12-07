from .fetch_g_events import execute as fetch_g_events_execute

class APIExecutors:
    fetch_g_events = fetch_g_events_execute

__all__ = ['APIExecutors']