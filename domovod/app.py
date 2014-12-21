from kivy.app import App

from domovod.widgets import Root, Dimmer, Relay


class DomoVodApp(App):

    use_kivy_settings = False

    def build(self):
        layout = Root()
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

    def open_settings(self, *_):
        pass
