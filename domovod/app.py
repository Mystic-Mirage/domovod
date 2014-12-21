from kivy.app import App

from domovod.widgets import Dimmer, Relay


class DomoVodApp(App):

    use_kivy_settings = False

    def build(self):
        self.root.prev.title = 'Room 1'
        dimmer1 = Dimmer('Dimmer 1')
        dimmer2 = Dimmer('Dimmer 2')
        dimmer3 = Dimmer('Dimmer 3')
        relay1 = Relay('Relay 1')
        self.root.grid.add_widget(dimmer1)
        self.root.grid.add_widget(dimmer2)
        self.root.grid.add_widget(dimmer3)
        self.root.grid.add_widget(relay1)

    def on_pause(self):
        return True

    def on_resume(self):
        pass

    def open_settings(self, *_):
        pass
