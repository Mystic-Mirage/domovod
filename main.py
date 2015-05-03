import kivy
from kivy.config import Config

from domovod.app import DomoVodApp


kivy.require('1.9.0')


__version__ = '0.1'


if __name__ == '__main__':
    Config.set('graphics', 'width', '240')
    Config.set('graphics', 'height', '400')
    DomoVodApp().run()
