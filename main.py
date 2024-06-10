import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.clock import Clock
from datetime import datetime

class CameraApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = Image()
        layout = BoxLayout(orientation='vertical')

        layout.add_widget(self.my_camera)

        btn = Button(text="Take Picture")
        btn.bind(on_press=self.take_picture)
        layout.add_widget(btn)

        Clock.schedule_interval(self.update, 1.0 / 30.0)
        return layout

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.my_camera.texture = image_texture

    def take_picture(self, *args):
        ret, frame = self.capture.read()
        if ret:
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"IMG_{current_time}.png"
            cv2.imwrite(filename, frame)
            print(f"Picture saved as {filename}")

    def on_stop(self):
        self.capture.release()

if __name__ == '__main__':
    CameraApp().run()
