# image_viewer.py

import wx

class ImagePanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        img = wx.Image(400, 400)
        self.image_ctrl = wx.StaticBitmap(self, bitmap=wx.Bitmap(img))
        
        browse_btn = wx.Button(self, label="Browse")
        browse_btn.Bind(wx.EVT_BUTTON, self.on_browse)
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.image_ctrl, 0, wx.ALL, 5)
        main_sizer.Add(browse_btn, 0, wx.ALL, 5)
        
        self.SetSizer(main_sizer)
        main_sizer.Fit(parent)
        self.Layout()
        
    def on_browse(self, event):
        wildcard = "JPEG files (*.jpg)|*.jpg"
        with wx.FileDialog(None, "Choose a file", wildcard=wildcard,
                           style=wx.FD_OPEN) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.load_image(dialog.GetPath())
                
    def load_image(self, image_path):
        img = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
        self.max_size = 400
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            new_w = self.max_size
            new_h = self.max_size * H / W
        else:
            new_h = self.max_size
            new_w = self.max_size * W / H
        img = img.Scale(int(new_w), int(new_h))
        self.image_ctrl.SetBitmap(wx.Bitmap(img))
        self.Refresh()

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Image Viewer")
        panel = ImagePanel(self)
        self.Show()
        
if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()