from deepface import DeepFace
import json
import cv2
import tkinter
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


class App:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        self.EmoteButtonClicked = False
        self.img1 = ''

        self.root = tkinter.Tk()
        self.lblTop = tkinter.Label(text='', font=('Times New Roman', 25), bg='black', fg='red')
        self.lblF = tkinter.LabelFrame(bg='black')
        self.lbl = tkinter.Label(self.lblF, bg='black')

        self.frmBtn = tkinter.Frame(self.root, bg='black')
        self.cam_btn = tkinter.Button(self.frmBtn, command=self.Camera, text='take', fg='red', bg='black', font=('Arial', 15))
        self.emote_btn = tkinter.Button(self.root, command=self.emote, text='Emotion', fg='red', bg='black', font=('Arial', 30))
        self.uploadImage_btn = tkinter.Button(self.frmBtn, command=self.uploadImage, text='upload', fg='red', bg='black', font=('Arial', 15))

        self.lbl_res = tkinter.Label(self.root, text='', fg='blue', bg='black', font=('Cooky Chooky', 35))

    def main_window(self):
        root = self.root
        root.geometry('750x750')
        root['bg'] = 'black'
        root.title('SOMBOE') #suggestion of music based on emotions

    def Pack(self):
        self.lblTop.pack()

        self.lblF.pack()
        self.lbl.pack()

        self.frmBtn.pack(fill='both', pady=10, padx=10)
        self.cam_btn.pack(side='left')
        self.emote_btn.pack()
        self.uploadImage_btn.pack(side='right')

        self.lbl_res.pack()

    def emote(self):
        result = self.face_analyze(img)
        print(result)
        self.lbl_res.configure(text=result)
        self.EmoteButtonClicked = True

    def face_analyze(self, img):
        try:
            result_dict = DeepFace.analyze(img_path=img, actions=['emotion'])

            with open('result.json', 'w') as file:
                json.dump(result_dict, file, indent=4, ensure_ascii=False)

            return result_dict[0]["dominant_emotion"]

        except Exception as _ex:
            return _ex

    def uploadImage(self):
        global img
        f_types = [('Jpg Files', '*.jpg'), ('Png Files', '*.png')]
        filename = tkinter.filedialog.askopenfilename(multiple=False, filetypes=f_types)
        img = cv2.imread(filename)
        img1 = img
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img1 = ImageTk.PhotoImage(Image.fromarray(img1).resize((500, 500)))
        self.lblTop.configure(text='Uploaded file:')
        self.lbl['image'] = img1
        self.img1 = img1

    def Camera(self):
        global img
        while True:
            global img
            ret, img = self.cap.read()
            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img1 = ImageTk.PhotoImage(Image.fromarray(img1).resize((500, 500)))
            self.lblTop.configure(text='Camera:')
            self.lbl['image'] = img1
            self.root.update()
            if self.EmoteButtonClicked:
                self.EmoteButtonClicked = False
                img = img1
                self.img1 = img1
                break

    def main(self):
        self.main_window()
        self.Pack()
        if self.img1:
            self.lbl['image'] = self.img1
        self.root.mainloop()


if __name__ == '__main__':
    App().main()
