import widgets


class Dimmer(object):

    def __init__(self, label):
        self.widget = widgets.Dimmer(label)


class Relay(object):

    def __init__(self, label):
        self.widget = widgets.Relay(label)
