from kivy.core.image import Image as CoreImage
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout


class Relay(ToggleButtonBehavior, RelativeLayout):

    def __init__(self, label, value=False):
        super(Relay, self).__init__()
        self.textures = {bool(k): CoreImage('data/bulb/%03d.png' % k).texture
                         for k in range(0, 101, 100)}
        self.image = Image(allow_stretch=True)
        self.image.pos_hint = {'center_x': .5, 'center_y': .6}
        self.image.size_hint_y = .8
        self.change(value)
        self.label = Label(text=label)
        self.label.pos_hint = {'center_x': .5, 'center_y': .1}
        self.label.size_hint_y = .2
        self.add_widget(self.image)
        self.add_widget(self.label)

    def change(self, value):
        self.image.texture = self.textures[bool(value)]

    def on_press(self):
        self.change(self.state == 'down')
