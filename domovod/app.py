from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from domovod.widgets.dimmer import Dimmer
from domovod.widgets.relay import Relay


class DomoVodApp(App):

    def build(self):
        layout = GridLayout(cols=2)
        dimmer1 = Dimmer()
        dimmer2 = Dimmer()
        dimmer3 = Dimmer()
        relay1 = Relay()
        layout.add_widget(dimmer1)
        layout.add_widget(dimmer2)
        layout.add_widget(dimmer3)
        layout.add_widget(relay1)
        return layout

    def on_pause(self):
        return True

    def on_resume(self):
        pass
