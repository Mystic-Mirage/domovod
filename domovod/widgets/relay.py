from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.core.image import Image as CoreImage
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image


class Relay(ToggleButtonBehavior, AnchorLayout):

    def __init__(self, value=False):
        super(Relay, self).__init__()
        self.textures = {bool(k): CoreImage('data/bulb/%03d.png' % k).texture
                         for k in range(0, 101, 100)}
        self.image = Image(allow_stretch=True)
        self.change(value)
        self.add_widget(self.image)

    def change(self, value):
        self.image.texture = self.textures[bool(value)]

    def on_press(self):
        self.change(self.state == 'down')
