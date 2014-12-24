from kivy.core.image import Image
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout


OFF = 0
ON = 100


class Dimmer(RelativeLayout):
    image = ObjectProperty()
    slider = ObjectProperty()
    label = StringProperty()

    def __init__(self, label, value=OFF):
        super(Dimmer, self).__init__()
        self.textures = {k: Image('data/bulb/%03d.png' % k).texture
                         for k in range(OFF, ON) + [ON]}
        self.label = label
        self.value = value
        self.old_value = ON
        self.image.texture = self.textures[value]

    def on_press(self):
        if self.image.state == 'down':
            self.value = self.old_value
        else:
            self.old_value = self.value
            self.value = OFF

    def on_value(self):
        self.image.state = 'normal' if self.value == OFF else 'down'
        self.image.texture = self.textures[self.value]

    @property
    def value(self):
        return int(self.slider.value)

    @value.setter
    def value(self, value):
        if OFF <= value <= ON:
            self.slider.value = value


class Relay(RelativeLayout):
    image = ObjectProperty()
    label = StringProperty()

    def __init__(self, label, value=OFF):
        super(Relay, self).__init__()
        self.textures = {k: Image('data/bulb/%03d.png' % k).texture
                         for k in (OFF, ON)}
        self.label = label
        self.value = value
        self.image.texture = self.textures[value]

    def on_press(self):
        self.image.texture = self.textures[self.value]

    @property
    def value(self):
        return ON if self.image.state == 'down' else OFF

    @value.setter
    def value(self, value):
        if value in (OFF, ON):
            self.image.state = 'down' if value == ON else 'normal'
