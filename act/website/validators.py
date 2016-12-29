# act_project/act/website/validators.py
def top_event_validator(top_event, events):
    '''
    Validator makes sure that selected top event is in
    the list of events related to the current centre.
    '''
    if top_event and not events.filter(pk=top_event.id):
        return "Вказана головна подія не має відношення до даного центру"

    return False


def problem_description_validator(problem, problem_description):
    '''
    Validator makes sure that problem description field
    linked to a problem boolean field would raise error,
    if boolean is set to `True` and description is blank.
    '''
    if problem and not problem_description:
        return "Будь ласка, опишіть проблему."

    return False


def activity_description_validator(activity, activity_description):
    '''
    Validator makes sure that activity description field
    linked to a activity boolean field would raise error,
    if boolean is set to `True` and description is blank.
    '''
    if activity and not activity_description:
        return "Будь ласка, опишіть діяльність."

    return False
