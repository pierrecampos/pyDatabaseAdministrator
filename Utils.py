class Utils:
    pass


def set_event_to_buttons(father, type_object, func):
    for item in father.findChildren(type_object):
        item.clicked.connect(func)
