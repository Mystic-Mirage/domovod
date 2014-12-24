import kivy
kivy.require('1.8.0')

from kivy.config import Config

from domovod.app import DomoVodApp
import smartbus


__version__ = '0.1'


if __name__ == '__main__':
    Config.set('graphics', 'width', '240')
    Config.set('graphics', 'height', '400')

    smartbus.init()

    DomoVodApp().run()

    smartbus.quit()
