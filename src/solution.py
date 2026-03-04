## Student Name: Ashik Acharya
## Student ID: 219611565

"""
Stub file for the meeting slot suggestion exercise.

Implement the function `suggest_slots` to return a list of valid meeting start times
on a given day, taking into account working hours, and possible specific constraints. See the lab handout
for full requirements.
"""
"""
    Suggest possible meeting start times for a given day.

    Args:
        events: List of dicts with keys {"start": "HH:MM", "end": "HH:MM"}
        meeting_duration: Desired meeting length in minutes
        day: Three-letter day abbreviation (e.g., "Mon", "Tue", ... "Fri")

    Returns:
        List of valid start times as "HH:MM" sorted ascending
    """
 
# from typing import List, Dict

# def suggest_slots(
#     events: List[Dict[str, str]],
#     meeting_duration: int,
#     day: str
# ) -> List[str]:

#     WORK_START = 9 * 60
#     WORK_END = 17 * 60
#     LUNCH_START = 12 * 60
#     LUNCH_END = 13 * 60
#     STEP = 15

#     def to_minutes(t: str) -> int:
#         h, m = map(int, t.split(":"))
#         return h * 60 + m

#     def to_time_str(m: int) -> str:
#         return f"{m//60:02d}:{m%60:02d}"

#     # Convert events to minutes and ignore those outside working hours
#     valid_events = []
#     for e in events:
#         start = to_minutes(e["start"])
#         end = to_minutes(e["end"])
#         if end <= WORK_START or start >= WORK_END:
#             continue
#         valid_events.append((start, end))

#     slots = []
#     t = WORK_START

#     while t + meeting_duration <= WORK_END:
#         meeting_end = t + meeting_duration

#         # Block lunch overlap
#         if not (meeting_end <= LUNCH_START or t >= LUNCH_END):
#             t += STEP
#             continue

#         overlap = False
#         for s, e in valid_events:
#             if t < e and meeting_end >= s:
#                 overlap = True
#                 break

#         if not overlap:
#             slots.append(to_time_str(t))

#         t += STEP

#     return sorted(slots)
from typing import List, Dict

def suggest_slots(
    events: List[Dict[str, str]],
    meeting_duration: int,
    day: str
) -> List[str]:

    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m

    def to_time(m: int) -> str:
        return f"{m//60:02d}:{m%60:02d}"

    WORK_START = to_minutes("09:00")
    WORK_END = to_minutes("17:00")
    LUNCH_START = to_minutes("12:00")
    LUNCH_END = to_minutes("13:00")

    # Convert and filter events within working hours
    busy = []
    for e in events:
        start = to_minutes(e["start"])
        end = to_minutes(e["end"])
        if end <= WORK_START or start >= WORK_END:
            continue
        busy.append((start, end))

    # Add lunch break as busy
    busy.append((LUNCH_START, LUNCH_END))

    # Sort events
    busy.sort()

    slots = []
    t = WORK_START

    while t + meeting_duration <= WORK_END:
        meeting_end = t + meeting_duration
        valid = True
        for bstart, bend in busy:
            if t < bend and meeting_end >= bstart:
                valid = False
                break
        if valid:
            slots.append(to_time(t))
        t += 15

    return slots