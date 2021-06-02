# import sublime
import sublime_plugin
from os.path import split as splitpath
from glob import glob


class ZipThisDirectoryCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		view = self.view
		path, _ = splitpath(view.file_name())
		dirpath, dirname = splitpath(path)
		command = (
			"zip ../{name} -u -9 -r *"
			if not glob(dirpath + "/ZIPS")
			else "zip ../ZIPS/{name} -u -9 -r *"
		)  #yapf: disable
		styles = [
			"BSCS18010_",
			"",
			"BSCS18010_Nawfal_",
			"BSCS18010-",  # "BSCS18010_Nawfal_Ahmed_"
		]
		styles = [style + dirname for style in styles]

		def on_done(index):
			if index != -1:
				self.view.window().run_command(
					"exec",
					{
						"shell_cmd": command.format(name=styles[index]),
						"show_panel": False
					}
				)

		view.window().show_quick_panel(styles, on_done)
