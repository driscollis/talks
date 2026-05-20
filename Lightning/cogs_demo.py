from textual.app import App
from textual.app import App, ComposeResult

from textual_cogs.dialogs import MessageDialog
from textual_cogs import icons


class DialogApp(App):
    def on_mount(self) -> ComposeResult:
        def my_callback(value: None | bool) -> None:
            self.exit()

        self.push_screen(
            MessageDialog(
                "What is your favorite language?",
                icon=icons.ICON_QUESTION,
                title="Warning",
                ),
            my_callback,
        )


if __name__ == "__main__":
    app = DialogApp()
    app.run()