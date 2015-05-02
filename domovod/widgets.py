from kivy.core.image import Image
from kivy.properties import (
    BooleanProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.relativelayout import RelativeLayout


class Dimmer(RelativeLayout):
    image = ObjectProperty()
    label = StringProperty()
    slider = ObjectProperty()
    value = NumericProperty()

    def __init__(self, label, value=None, callback=None,
                 min_value=0, max_value=255, step=1,
                 bottom=None, top=None):
        super(Dimmer, self).__init__()
        if bottom is None:
            bottom = min_value
        if top is None:
            top = max_value
        self.textures = {
            key: Image('data/bulb/{0:03d}.png'.format(value)).texture
            for key, value in [
                (v, int(float(v) / (top - bottom) * 100))
                for v in range(min_value, max_value, step) + [max_value]
            ]
        }
        self.label = label
        self.old_value = max_value
        self.min = min_value
        self.max = max_value
        self.value = min_value if value is None else value
        self.image.texture = self.textures[self.value]
        self.slider.min = min_value
        self.slider.max = max_value
        self.slider.step = step
        if callback is not None:
            self.callback = callback

    def callback(self, value):
        print value

    def on_press(self):
        if self.image.state == 'down':
            value = self.old_value
        else:
            self.old_value = self.value
            value = self.min
        self.value = value
        self.callback(value)

    def on_slider_value(self):
        old_value = self.value
        value = int(self.slider.value)
        self.value = value
        if value != old_value:
            self.callback(value)

    def on_value(self, _, value):
        self.image.state = 'normal' if value == self.min else 'down'
        self.image.texture = self.textures[value]
        self.slider.value = value


class Relay(RelativeLayout):
    image = ObjectProperty()
    label = StringProperty()
    value = BooleanProperty()

    def __init__(self, label, value=False, callback=None):
        super(Relay, self).__init__()
        self.textures = {
            key: Image('data/bulb/{0:03d}.png'.format(value)).texture
            for key, value in ((False, 0), (True, 100))
        }
        self.label = label
        self.value = value
        if callback is not None:
            self.callback = callback

    def callback(self, value):
        pass

    def on_press(self):
        value = not self.value
        self.value = value
        self.callback(value)

    def on_value(self, _, value):
        self.image.texture = self.textures[value]
