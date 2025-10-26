import rumps
import subprocess

class MyMenuApp(rumps.App):
    def __init__(self):
        super(MyMenuApp, self).__init__("⚡G.V.S")  # Menu bar title
        self.menu = ["Run Script", "Quit"]

    @rumps.clicked("Run Script")
    def run_script(self, _):
        # Replace this with the path to your script
        script_path = "run.sh"
        subprocess.Popen(["/bin/zsh", script_path])
        rumps.notification("Script", "Your script ran!", "")

if __name__ == "__main__":
    MyMenuApp().run()

