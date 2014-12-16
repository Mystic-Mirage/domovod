from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from domovod.widgets.dimmer import Dimmer
from domovod.widgets.relay import Relay


class DomoVodApp(App):

    def build(self):
        layout = GridLayout(cols=2, padding=10, spacing=10)
        dimmer1 = Dimmer('Dimmer 1')
        dimmer2 = Dimmer('Dimmer 2')
        dimmer3 = Dimmer('Dimmer 3')
        relay1 = Relay('Relay 1')
        layout.add_widget(dimmer1)
        layout.add_widget(dimmer2)
        layout.add_widget(dimmer3)
        layout.add_widget(relay1)
        return layout

    def on_pause(self):
        return True

    def on_resume(self):
        pass
