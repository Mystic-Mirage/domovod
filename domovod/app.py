from kivy.app import App

from domovod.widgets import Dimmer, Relay


class DomoVodApp(App):

    use_kivy_settings = False

    def build(self):
        self.root.prev.title = 'Room 1'
        relay = Relay('Relay 1')
        dimmer = Dimmer('Dimmer 1')
        self.root.grid.add_widget(relay)
        self.root.grid.add_widget(dimmer)

    def on_pause(self):
        return True

    def on_resume(self):
        pass

    def open_settings(self, *_):
        pass
