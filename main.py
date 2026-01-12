from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.clock import Clock
import requests
from pyzbar import pyzbar
from PIL import Image as PILImage

class ScannerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.cam = Camera(play=True, resolution=(640, 480))
        self.layout.add_widget(self.cam)
        self.label = Label(text="Scanner...", size_hint_y=0.2, color=(0,1,0,1))
        self.layout.add_widget(self.label)
        self.dernier = ""
        Clock.schedule_interval(self.scan, 1.0)
        return self.layout

    def scan(self, dt):
        if self.cam.texture:
            try:
                img = PILImage.frombytes(mode='RGBA', size=self.cam.texture.size, data=self.cam.texture.pixels)
                for code in pyzbar.decode(img):
                    txt = code.data.decode('utf-8')
                    if txt != self.dernier:
                        requests.post("https://xelery.pythonanywhere.com/update", data={'code': txt})
                        self.dernier = txt
                        self.label.text = f"Envoyé: {txt}"
            exceptException:
                pass

if __name__ == '__main__':
    ScannerApp().run()

