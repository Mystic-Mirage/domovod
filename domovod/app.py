from kivy.app import App

from domovod.widgets import Dimmer, Relay


class DomoVodApp(App):

    use_kivy_settings = False

    def build(self):
        self.root.prev.title = 'Room 1'
        for Unit in (Dimmer, Relay):
            for i in range(1, 4):
                self.root.grid.add_widget(Unit('%s %i' % (Unit.__name__, i)))

    def on_pause(self):
        return True

    def on_resume(self):
        pass

    def open_settings(self, *_):
        pass
