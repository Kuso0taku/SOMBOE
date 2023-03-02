from deepface import DeepFace
import json
import cv2
import tkinter
from PIL import Image, ImageTk


class App:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        self.root = tkinter.Tk()

        self.lblF = tkinter.LabelFrame(bg='red')
        self.lbl = tkinter.Label(self.lblF)
        self.btn = tkinter.Button(self.root, text='Emotion', fg='red', bg='black', font=('Arial', 30))
        self.lbl_res = tkinter.Label(self.root, text='', fg='blue', bg='black', font=('Cooky Chooky', 35))

    def main_window(self):
        root = self.root
        root.geometry('750x750')
        root['bg'] = 'black'
        root.title('Emotion')

    def pack(self):
        tkinter.Label(text='Camera:', font=('Times New Roman', 25), bg='black', fg='red').pack()
        self.lblF.pack()
        self.lbl.pack()
        self.btn.pack()
        self.lbl_res.pack()

    def face_analyze(self, img):
        try:
            result_dict = DeepFace.analyze(img_path=img, actions=['emotion'])

            with open('result.json', 'w') as file:
                json.dump(result_dict, file, indent=4, ensure_ascii=False)

            return result_dict[0]["dominant_emotion"]

        except Exception as _ex:
            return _ex

    def Emote(self):
        while True:
            ret, img = self.cap.read()

            def click():
                result = self.face_analyze(img)
                self.lbl_res.configure(text=result)

            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img1 = ImageTk.PhotoImage(Image.fromarray(img1))
            self.lbl['image'] = img1
            self.btn.configure(command=click)
            self.root.update()

    def main(self):
        self.main_window()
        self.pack()

        self.Emote()
        self.root.mainloop()


if __name__ == '__main__':
    App().main()
