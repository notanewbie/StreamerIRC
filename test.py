import ctypes as ct
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
def dark_title_bar(window):
    """
    MORE INFO:
    https://docs.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
    window.configure(background='black')
    window.withdraw()
    window.deiconify()

root = Tk()

dark_title_bar(root)

root.attributes('-topmost',True)

chatWin = ttk.Notebook(root)
chatWin.pack(fill=BOTH, expand=1)

Tabs = [];

def newTab(tabName):
    myFrame = LabelFrame(chatWin)
    myFrame.pack(fill=BOTH, expand=1, padx=0, pady=0)
    chatWin.add(myFrame, text = tabName)
    FrameText = ScrolledText(myFrame, wrap=WORD)
    FrameText.pack(fill=BOTH, expand=1)
    FrameText.config(state=DISABLED)
    return FrameText;

ChatEntryLabel = LabelFrame(root)
ChatEntryLabel.pack(fill=X, expand=0, padx=0, pady=0)
T = ScrolledText(ChatEntryLabel, height=2)
T.pack(fill=BOTH, expand=1, side="bottom")

#root.mainloop()

def addContent(content, ti):
    Tabs[ti].config(state=NORMAL)
    Tabs[ti].insert("insert", content + "\n")
    Tabs[ti].config(state=DISABLED)
    root.update()

Tabs.append(newTab("New Tab"))
addContent("Amar: hello", 0)
addContent("Amar: hello", 0)
Tabs.append(newTab("New Tab 2"))
addContent("Amar's enemy: homeboy", 1)
addContent("Amar's enemy: get back here", 1)

def newMSG():
    addContent(T.get("1.0", END), 0)

root.bind('<Return>', newMSG())
