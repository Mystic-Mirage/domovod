from __future__ import division

from kivy.core.image import Image as CoreImage
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.slider import Slider


class ImageButton(ButtonBehavior, Image):
    pass


class Dimmer(RelativeLayout):

    def __init__(self, label, value=0):
        super(Dimmer, self).__init__()
        self.textures = {k: CoreImage('data/bulb/%03d.png' % k).texture
                         for k in range(0, 101, 5)}
        self.slider = Slider(min=0, max=100, step=1, orientation='vertical')
        self.slider.size_hint = (.2, None)
        self.image = ImageButton(allow_stretch=True)
        self.image.pos_hint = {'center_x': .5, 'center_y': .6}
        self.image.size_hint_y = .8
        self.image.on_press = self.on_image_press
        self.image.bind(size=self.on_image_size)
        self.slider.bind(value=self.on_slider_value)
        self.change(value)
        self.label = Label(text=label)
        self.label.pos_hint = {'center_x': .5, 'center_y': .1}
        self.label.size_hint_y = .2
        self.add_widget(self.image)
        self.add_widget(self.slider)
        self.add_widget(self.label)
        self.saved_state = 75

    def change(self, value):
        self.image.texture = self.textures[int(value // 5 * 5)]

    def on_image_press(self):
        if self.slider.value == 0:
            self.slider.value = self.saved_state
            self.change(self.saved_state)
        else:
            self.saved_state = self.slider.value
            self.slider.value = 0
            self.change(0)

    def on_image_size(self, _, value):
        self.slider.height = .9 * value[1]
        ratio = value[0] / value[1]
        pos = .9 if ratio < 1 else .5 + .4 / ratio
        self.slider.pos_hint = {'center_x': pos, 'center_y': .6}

    def on_slider_value(self, _, value):
        self.change(value)
