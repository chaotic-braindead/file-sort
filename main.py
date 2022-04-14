from cgitb import text
import os
import shutil
from tkinter import *
from tkinter import filedialog


class Move:
    def __init__(self, directory, extract=None):
        self.directory = directory
        self.extract = extract

    def sort_by_extension(self):
        path = os.listdir(self.directory)
        
        for file in path:

            filename, file_extension = os.path.splitext(file)
            
            if file_extension == '':
                continue

            if file_extension == '.ini':
                continue

            if os.path.exists(f'{self.directory}\{file_extension[1:]}'):
                shutil.move(os.path.join(self.directory, f'{filename}{file_extension}'), 
                (os.path.join(self.directory, file_extension[1:])))
                
            else:
                os.makedirs(f'{self.directory}\{file_extension[1:]}')
                shutil.move(os.path.join(self.directory, f'{filename}{file_extension}'),
                (os.path.join(self.directory, file_extension[1:])))

    def sort_by_file_type(directory):
    
        for f in os.listdir(directory):
            filename, file_ext = os.path.splitext(f)
            print(filename, file_ext)

            try:
                if not file_ext:
                    pass

                elif file_ext in ('.jpg', '.png', '.jpeg', '.gif', '.PNG'):
                    shutil.move(
                        os.path.join(directory, f'{filename}{file_ext}'),
                        os.path.join(directory, 'Pictures', f'{filename}{file_ext}'))

                elif file_ext in ('.docx', '.xlsx', '.pptx', '.doc', '.pdf', '.dotx'):
                    shutil.move(
                        os.path.join(directory, f'{filename}{file_ext}'),
                        os.path.join(directory, 'Docs', f'{filename}{file_ext}'))

                elif file_ext in ('.exe', '.msi'):
                    shutil.move(
                        os.path.join(directory, f'{filename}{file_ext}'),
                        os.path.join(directory, 'Executables', f'{filename}{file_ext}'))

                elif file_ext in ('.zip', '.rar', '.7zip'):
                    shutil.move(
                        os.path.join(directory, f'{filename}{file_ext}'),
                        os.path.join(directory, 'Compressed files', f'{filename}{file_ext}'))

                elif file_ext in ('.crdownload'):
                    pass

                else:
                    shutil.move(
                        os.path.join(directory, f'{filename}{file_ext}'),
                        os.path.join(directory, 'Other files', f'{filename}{file_ext}'))

            except (FileNotFoundError, PermissionError):
                print('Error')

    def extension_folder_extract(self):
        extract = self.extract
        for root, dirs, files in os.walk(self.directory):
            try:
                files = [f for f in files if f != 'desktop.ini' and '.qml' not in f and '.qmlc' not in f]
                dirs[:] = [d for d in dirs if d != 'desktop.ini'  and '.qml' not in d and '.qmlc' not in d]
                check = files[0].split('.')[-1]
            except IndexError:
                continue
            if check in root:
                for name in files:
                    dir = name.split('.')[-1]
                    shutil.move(f'{root}\{name}', extract)
                    try:
                        if os.path.exists(f'{self.directory}\{dir}'):
                            os.removedirs(f'{self.directory}\{dir}')
                    except (OSError, shutil.Error):
                        continue
                else:
                    continue

    def folder_extract(self):
        extract = self.extract
        for root, dirs, files in os.walk(self.directory):
            files = [f for f in files if f != 'desktop.ini' and '.qml' not in f and '.qmlc' not in f]
            dirs[:] = [d for d in dirs if d != 'desktop.ini'  and '.qml' not in d and '.qmlc' not in d]
            for name in files:
                shutil.move(f'{root}\{name}', extract)
                try:
                    if os.path.exists(f'{root}'):
                        os.removedirs(f'{root}')
                except (OSError, shutil.Error):
                    continue
    
def clear():
    os.system('cls')

if __name__ == '__main__':
    root = Tk()
    root.title('File Sort')
    root.iconbitmap(r'C:\Users\raf\Desktop\Python\sorter\folders_t9h_icon.ico')
    root.geometry('500x275')
    root.configure(bg='#ffffff')
    my_text = Text(root, width=55, height=1, font=('Segoe', 10))
    my_text.pack(pady=25)
    my_text.configure(state='disabled')

    def getlabel(status):
        my_label.config(text=status, bg='#53fc8e')

    def browse():
        my_text.configure(state='normal')
        path = filedialog.askdirectory(title='Select a directory')
        my_text.delete(1.0, END)
        my_text.insert('1.0', path)
        my_text.configure(state='disabled')
        
    def sort_extension():
        path = my_text.get('1.0', END).rstrip()
        directory = Move(path)
        directory.sort_by_extension()
        getlabel('Files sorted successfully!')

    
    def sort_all():
        path = my_text.get('1.0', END).rstrip()
        directory = Move(path)
        directory.sort_by_file_type()
        getlabel('Files sorted successfully!')

    def extract_extension():
        path = my_text.get('1.0', END).rstrip()
        extract = filedialog.askdirectory(title='Extraction directory')
        directory = Move(path, extract)
        directory.extension_folder_extract()
        getlabel('Files extracted successfully!')

    def extract_all():
        path = my_text.get('1.0', END).rstrip()
        extract = filedialog.askdirectory(title='Extraction directory')
        directory = Move(path, extract)
        directory.folder_extract()
        getlabel('Files extracted successfully!')
        
    def get_text():
        return my_text.get('1.0', END).rstrip()

    def bttn(width, height, x, y, text, bcolor, fcolor, cmd):
        def on_enter(e):
            button['background']=bcolor
            button['foreground']=fcolor
        
        def on_leave(e):
            button['background']=fcolor
            button['foreground']=bcolor


        button = Button(root, width=width, height=height, text=text,
        fg=bcolor, bg=fcolor, border=0, activeforeground=fcolor,
        command=cmd, font=('Helvetica', 10, 'bold'))

        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        button.place(x=x, y=y)

    my_label = Label(root, font=('Segoe', 8))
    my_label.pack(pady=25)

    bttn(62, 2, 0, 50, 'Browse', '#7167fc', '#ffffff', browse)
    bttn(62, 1, 0, 125, 'Sort folder by extension', '#7167fc', '#ffffff', sort_extension)
    bttn(62, 1, 0, 150, 'Sort folder by file type', '#7167fc', '#ffffff', sort_all)
    bttn(62, 1, 0, 175, 'Extract extension folders', '#7167fc', '#ffffff', extract_extension)
    bttn(62, 1, 0, 200, 'Extract all folders', '#7167fc', '#ffffff', extract_all)
   
    root.mainloop()

       