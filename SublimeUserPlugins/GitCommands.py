import sublime
import sublime_plugin
from os.path import split as splitpath


class GitStageSelfCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		_, name = splitpath(self.view.file_name())
		stage = 'wsl git add "' + name + '"'
		self.view.window().run_command(
			"exec", {
				"shell_cmd": stage,
				"show_panel": False
				}
			)


class GitStageSelfDirCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		stage = 'wsl git add .'
		self.view.window().run_command(
			"exec", {
				"shell_cmd": stage,
				"show_panel": False
				}
			)


class GitCommitCommand(sublime_plugin.TextCommand):

	def run(self, edit, name):
		commit = 'wsl git commit -m "' + name + '"'
		self.view.window().run_command(
			"exec", {
				"shell_cmd": commit,
				"show_panel": False
				}
			)

	def input(self, args):
		if "name" not in args:
			return NameInputHandler(self.view)
		else:
			return None


class NameInputHandler(sublime_plugin.TextInputHandler):

	def initial_text(self):
		return "--unspecified user commit"
