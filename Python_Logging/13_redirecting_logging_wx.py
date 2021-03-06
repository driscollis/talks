import logging
import logging.config
import wx

class CustomConsoleHandler(logging.StreamHandler):
    """"""

    def __init__(self, textctrl):
        """"""
        logging.StreamHandler.__init__(self)
        self.textctrl = textctrl

    def emit(self, record):
        """Constructor"""
        msg = self.format(record)
        self.textctrl.WriteText(msg + "\n")
        self.flush()


class MyPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        super().__init__(parent)
        self.logger = logging.getLogger("wxApp")

        self.logger.info("Test from MyPanel __init__")

        logText = wx.TextCtrl(self,
                              style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)

        btn = wx.Button(self, label="Press Me")
        btn.Bind(wx.EVT_BUTTON, self.on_press)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(logText, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(btn, 0, wx.ALL, 5)
        self.SetSizer(sizer)

        txtHandler = CustomConsoleHandler(logText)
        self.logger.addHandler(txtHandler)

    def on_press(self, event):
        self.logger.error("Error Will Robinson!")
        self.logger.info("Informational message")


class MyFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        super().__init__(None, title="Logging test")
        panel = MyPanel(self)
        self.logger = logging.getLogger("wxApp")
        self.Show()


def main():
    """
    """
    dictLogConfig = {
        "version":1,
        "handlers":{
                    "fileHandler":{
                        "class":"logging.FileHandler",
                        "formatter":"myFormatter",
                        "filename":"wx_test.log"
                        },
                    "consoleHandler":{
                        "class":"logging.StreamHandler",
                        "formatter":"myFormatter"
                        }
                    },
        "loggers":{
            "wxApp":{
                "handlers":["fileHandler", "consoleHandler"],
                "level":"INFO",
                }
            },

        "formatters":{
            "myFormatter":{
                "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                }
            }
        }
    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger("wxApp")

    logger.info("This message came from main!")

    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()

if __name__ == "__main__":
    main()