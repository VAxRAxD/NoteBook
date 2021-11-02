import tkinter as tk
from tkinter import Label, Variable, ttk, font,colorchooser,filedialog, messagebox
import os,sys
from tkinter.constants import ANCHOR, NONE

main = tk.Tk()
main.state('zoomed')
main.title('Untitled - Notebook')
main.wm_iconbitmap('media/main/Notebook.ico')

# Main menu:
main_menu=tk.Menu()

# Edit Menu
file_menu=tk.Menu(main_menu,tearoff=0)

new_file_icon=tk.PhotoImage(file='media/File/new_file.png')
open_file_icon=tk.PhotoImage(file='media/File/open_file.png')
save_file_icon=tk.PhotoImage(file='media/File/save_file.png')
saveas_file_icon=tk.PhotoImage(file='media/File/saveas_file.png')
exit_file_icon=tk.PhotoImage(file='media/File/exit_file.png')

#Edit Menu
edit_menu=tk.Menu(main_menu,tearoff=0)

copy_edit_icon=tk.PhotoImage(file='media/Edit/copy_edit.png')
paste_edit_icon=tk.PhotoImage(file='media/Edit/paste_edit.png')
cut_edit_icon=tk.PhotoImage(file='media/Edit/cut_edit.png')
clear_edit_icon=tk.PhotoImage(file='media/Edit/clear_edit.png')
find_edit_icon=tk.PhotoImage(file='media/Edit/find_edit.png')
undo_icon=tk.PhotoImage(file='media/Edit/undo.png')
redo_icon=tk.PhotoImage(file='media/Edit/redo.png')

#View menu
tools_menu=tk.Menu(main_menu,tearoff=0)

statusbar_view_icon=tk.PhotoImage(file='media/Tools/statusbar_view.png')
toolbar_view_icon=tk.PhotoImage(file='media/Tools/toolbar_view.png')

#Color Theme Menu
view_menu=tk.Menu(main_menu,tearoff=0)

light_colortheme_icon=tk.PhotoImage(file='media/View/light_colortheme.png')
dark_colortheme_icon=tk.PhotoImage(file='media/View/dark_colortheme.png')
zoom_in_icon=tk.PhotoImage(file='media/View/zoom_in.png')
zoom_out_icon=tk.PhotoImage(file='media/View/zoom_out.png')
reset_icon=tk.PhotoImage(file='media/View/reset.png')
appearance_icon=tk.PhotoImage(file='media/View/appearance.png')

theme_choice=tk.StringVar()
color_icon=(light_colortheme_icon,dark_colortheme_icon)
color_dictionary={
    'Light':('#000000','#ffffff'),
    'Dark':('#c4c4c4','#2d2d2d')
}

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="Tools", menu=tools_menu)
main_menu.add_cascade(label="View", menu=view_menu)

# Tool Bar:
tool_bar=ttk.Label(main)
tool_bar.pack(side=tk.TOP,fill=tk.X)

#Font
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5,pady=2)

#Size
size_variable=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=15,textvariable=size_variable,state='readonly')
font_size['value']=tuple(range(8,150,2))
font_size.current(3)
font_size.grid(row=0,column=1,padx=5,pady=2)

#Bold Button
bold_icon=tk.PhotoImage(file='media/ToolBar/bold.png')
bold_button=ttk.Button(tool_bar,image=bold_icon)
bold_button.grid(row=0,column=2,padx=5,pady=2)

#Italic Button
italic_icon=tk.PhotoImage(file='media/ToolBar/italic.png')
italic_button=ttk.Button(tool_bar,image=italic_icon)
italic_button.grid(row=0,column=3,padx=5,pady=2)

#Underline Button
underline_icon=tk.PhotoImage(file='media/ToolBar/underline.png')
underline_button=ttk.Button(tool_bar,image=underline_icon)
underline_button.grid(row=0,column=4,padx=5,pady=2)

# Font Color
font_color_icon=tk.PhotoImage(file='media/ToolBar/font_color.png')
font_color_button=ttk.Button(tool_bar,image=font_color_icon)
font_color_button.grid(row=0,column=5,padx=5,pady=2)

# Align Center
align_center_icon=tk.PhotoImage(file='media/ToolBar/align_center.png')
align_center_button=ttk.Button(tool_bar,image=align_center_icon)
align_center_button.grid(row=0,column=6,padx=5,pady=2)

# Align Left
align_left_icon=tk.PhotoImage(file='media/ToolBar/align_left.png')
align_left_button=ttk.Button(tool_bar,image=align_left_icon)
align_left_button.grid(row=0,column=7,padx=5,pady=2)

# Align right
align_right_icon=tk.PhotoImage(file='media/ToolBar/align_right.png')
align_right_button=ttk.Button(tool_bar,image=align_right_icon)
align_right_button.grid(row=0,column=8,padx=5,pady=2)

# Status Bar:
status_bar=ttk.Label(main, text="Status Bar")
status_bar.pack(side=tk.BOTTOM)
text_changed=False

# Text Editor:
text_editor=tk.Text(main,undo=True)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Font and Size Functionality
current_font_family='Arial'
current_font_size=14

def change_font_family(event=None):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(event=None):
    global current_font_size,zoom_size
    zoom_size=size_variable.get()
    current_font_size=size_variable.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font_family)
font_size.bind("<<ComboboxSelected>>",change_font_size)

# Bold Button Functionality
bold=0
italic=0
underline=0
def change_bold():
    global bold,italic,underline
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        if (italic==1 and underline==1):
            text_editor.configure(font=(current_font_family,current_font_size,'bold','underline','italic'))
        elif italic==1:
            text_editor.configure(font=(current_font_family,current_font_size,'bold','italic'))
        elif underline==1:
            text_editor.configure(font=(current_font_family,current_font_size,'bold','underline'))
        else:
            text_editor.configure(font=(current_font_family,current_font_size,'bold'))
        bold=1
    if text_property.actual()['weight']=='bold':
        if (italic==1 and underline==1):
            text_editor.configure(font=(current_font_family,current_font_size,'underline','italic'))
        elif italic==1:
            text_editor.configure(font=(current_font_family,current_font_size,'italic'))
        elif underline==1:
            text_editor.configure(font=(current_font_family,current_font_size,'underline'))
        else:
            text_editor.configure(font=(current_font_family,current_font_size,'normal'))
        bold=0

bold_button.configure(command=change_bold)

# Underline button funtionality
def change_underline():
    global bold,italic,underline
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        if(bold==1 and italic==1):
            text_editor.configure(font=(current_font_family,current_font_size,'underline','bold','italic'))
        elif bold==1:
            text_editor.configure(font=(current_font_family,current_font_size,'underline','bold'))
        elif italic==1:
            text_editor.configure(font=(current_font_family,current_font_size,'underline','italic'))
        else:
            text_editor.configure(font=(current_font_family,current_font_size,'underline'))
        underline=1
    if text_property.actual()['underline']==1:
        if(bold==1 and italic==1):
            text_editor.configure(font=(current_font_family,current_font_size,'bold','italic'))
        elif bold==1:
            text_editor.configure(font=(current_font_family,current_font_size,'bold'))
        elif italic==1:
            text_editor.configure(font=(current_font_family,current_font_size,'italic'))
        else:
            text_editor.configure(font=(current_font_family,current_font_size,'normal'))
        underline=0

underline_button.configure(command=change_underline)

# Ittalic button functionality
def change_italic():
    global bold,italic,underline
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        if(bold==1 and underline==1):
            text_editor.configure(font=(current_font_family,current_font_size,'italic','bold','underline'))
        elif bold==1:
            text_editor.configure(font=(current_font_family,current_font_size,'italic','bold'))
        elif underline==1:
            text_editor.configure(font=(current_font_family,current_font_size,'italic','underline'))
        else:
            text_editor.configure(font=(current_font_family,current_font_size,'italic'))
        italic=1
    if text_property.actual()['slant']=='italic':
        if(bold==1 and underline==1):
            text_editor.configure(font=(current_font_family,current_font_size,'bold','underline'))
        elif bold==1:
            text_editor.configure(font=(current_font_family,current_font_size,'bold'))
        elif underline==1:
            text_editor.configure(font=(current_font_family,current_font_size,'underline'))
        else:
            text_editor.configure(font=(current_font_family,current_font_size,'normal'))
        italic=0

italic_button.configure(command=change_italic)

# Font Color Functionality
def change_font_color():
    color_variable=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_variable[1])

font_color_button.configure(command=change_font_color)

#Align Left Functionality
def align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_button.configure(command=align_left)

#Align Right Functionality
def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_button.configure(command=align_right)

#Align Center Functionality
def align_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_button.configure(command=align_center)

text_editor.configure(font=('Arial',12))

# Status Bar Functionality
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c').replace(' ',''))
        status_bar.config(text=f'Characters: {characters} | Words: {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)

# Main Menu Functionality
url=''

def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0, tk.END)
    main.title('Untitled - Notebook')

def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File', filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    main.title(os.path.basename(url))

def save_file(event=None):
    global url
    content=str(text_editor.get(1.0,tk.END))
    try:
        if url:
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File','*.txt'),('All Files','*.*')))
            url.write(content)
            url.close()
    except:
        return 

def save_as(event=None):
    global url
    content=str(text_editor.get(1.0,tk.END))
    try:
        url=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return 

def exit(event=None):
    global url, text_changed
    try:
        if text_changed:
            msg_box=messagebox.askyesnocancel("Warning","Do you want yo save this file?")
            if msg_box is True:
                content=str((text_editor.get(1.0,tk.END)))
                if url:
                    with open(url,'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main.destroy()
                else:
                    url=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content)
                    url.close()
                    main.destroy()
            elif msg_box is False:
                main.destroy()
        else:
            main.destroy()
    except:
        return
# File Menu Functionality:
file_menu.add_command(label="New", image=new_file_icon, compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)
file_menu.add_command(label="Open", image=open_file_icon, compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", image=save_file_icon, compound=tk.LEFT,accelerator='Ctrl+S', command=save_file)
file_menu.add_command(label="Save As", image=saveas_file_icon, compound=tk.LEFT,accelerator='Ctrl+Alt+S', command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", image=exit_file_icon, compound=tk.LEFT,accelerator='Ctrl+Q',command=exit)

def find_text(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)
        find_window.destroy()

    find_window = tk.Toplevel()
    find_window.geometry('320x150+500+200')
    find_window.wm_iconbitmap('media/main/find.ico')
    find_window.title('Find')
    find_window.resizable(0,0)

    find_frame = ttk.LabelFrame(find_window, text='Find/Replace')
    find_frame.pack(pady=20)

    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)
    find_button.grid(row=2, column=0, padx=10, pady=4)
    replace_button.grid(row=2, column=1, padx=10, pady=4)


    find_window.mainloop()

#Edit Menu Functionality:
edit_menu.add_command(label="Copy", image=copy_edit_icon, compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate('<Control-c>'))
edit_menu.add_command(label="Paste", image=paste_edit_icon, compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control-v>'))
edit_menu.add_command(label="Cut", image=cut_edit_icon, compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control-x>'))
edit_menu.add_separator()
edit_menu.add_command(label="Clear All", image=clear_edit_icon, compound=tk.LEFT,accelerator='Ctrl+Alt+C',command=lambda:text_editor.delete(1.0,tk.END))
edit_menu.add_separator()
edit_menu.add_command(label="Find/Replace", image=find_edit_icon, compound=tk.LEFT,accelerator='Ctrl+F',command=find_text)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", image=undo_icon, compound=tk.LEFT,accelerator='Ctrl+Z',command=text_editor.edit_undo)
edit_menu.add_command(label="Redo", image=redo_icon, compound=tk.LEFT,accelerator='Ctrl+Y',command=text_editor.edit_redo)

# View Menu Functionality
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

def toolbar_func():
    global show_toolbar,show_statusbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        if show_statusbar:
            status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True 
        text_editor.pack(fill=tk.BOTH, expand=True)

def statusbar_func():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False 
    else :
        text_editor.pack_forget()
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True 
        text_editor.pack(fill=tk.BOTH, expand=True)

tools_menu.add_checkbutton(label="Toolbar",variable=show_toolbar,image=toolbar_view_icon, compound=tk.LEFT,command=toolbar_func)
tools_menu.add_checkbutton(label="Statusbar",variable=show_statusbar,image=statusbar_view_icon, compound=tk.LEFT,command=statusbar_func)


# Zoom functionality

zoom_in_count=0
zoom_in_flag=0
zoom_out_count=0
zoom_out_flag=0
zoom_size=14

def zoom_out(event=None):
    global current_font_family,zoom_out_count,zoom_out_flag,zoom_size,zoom_in_count,zoom_in_flag
    zoom_in_count=0
    zoom_in_flag=0
    font_size_list=list(range(8,150,2))
    if(zoom_out_count==0):
        zoom_out_flag+=font_size_list.index(zoom_size)
        zoom_out_count+=1
    if(font_size_list[zoom_out_flag]>font_size_list[0]):
        content=str(text_editor.get(1.0,tk.END))
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,content.rstrip())
        text_editor.configure(font=(current_font_family,font_size_list[zoom_out_flag-1]))
        zoom_out_flag-=1
        zoom_size-=2
    else:
        content=str(text_editor.get(1.0,tk.END))
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,content.rstrip())
        text_editor.configure(font=(current_font_family,8))
        zoom_out_flag=0
        zoom_size=8

def zoom_in(event=None):
    global current_font_family,zoom_in_count,zoom_in_flag,zoom_size,zoom_out_count,zoom_out_flag
    zoom_out_count=0
    zoom_out_flag=0
    font_size_list=list(range(8,150,2))
    if(zoom_in_count==0):
        zoom_in_flag+=font_size_list.index(zoom_size)
        zoom_in_count+=1
    if(font_size_list[zoom_in_flag]<font_size_list[70]):
        content=str(text_editor.get(1.0,tk.END))
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,content.rstrip())
        text_editor.configure(font=(current_font_family,font_size_list[zoom_in_flag+1]))
        zoom_in_flag+=1
        zoom_size+=2
    else:
        content=str(text_editor.get(1.0,tk.END))
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,content.rstrip())
        text_editor.configure(font=(current_font_family,148))
        zoom_in_flag=70
        zoom_size=148

def zoom_reset(event=None):
    global font_size,current_font_family,zoom_in_count,zoom_in_flag,zoom_out_count,zoom_out_flag,zoom_size
    zoom_in_flag=zoom_in_count=zoom_out_flag=zoom_out_count=0
    font_size_list=list(range(8,150,2))
    zoom_size=font_size_list[font_size.current()]
    text_editor.configure(font=(current_font_family,zoom_size))
    


# Color Theme Functionality
def change_theme():
    choosen_theme=theme_choice.get()
    color_tuple = color_dictionary.get(choosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color) 

appearance_menu=tk.Menu(view_menu,tearoff=0)

count=0
for i in color_dictionary:
    appearance_menu.add_radiobutton(label=i, image=color_icon[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count +=1
view_menu.add_cascade(label="Appearance",image=appearance_icon, compound=tk.LEFT,menu=appearance_menu)
view_menu.add_separator()
view_menu.add_command(label="Zoom In",image=zoom_in_icon, compound=tk.LEFT,accelerator='Ctrl+I',command=zoom_in)
view_menu.add_command(label="Zoom Out",image=zoom_out_icon, compound=tk.LEFT,accelerator='Ctrl+O',command=zoom_out)
view_menu.add_command(label="Zoom Reset",image=reset_icon, compound=tk.LEFT,accelerator='Ctrl+R',command=zoom_reset)

#Bind shortcut keys
main.bind("<Control-n>",new_file)
main.bind("<Control-o>",open_file)
main.bind("<Control-s>",save_file)
main.bind("<Control-Alt-s>",save_as)
main.bind("<Control-q>",exit)
main.bind("<Control-f>",find_text)
main.bind("<Control-o>",zoom_out)
main.bind("<Control-i>",zoom_in)
main.bind("<Control-r>",zoom_reset)

main.config(menu=main_menu)
main.mainloop()