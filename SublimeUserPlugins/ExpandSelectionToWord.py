import sublime
import sublime_plugin
import re


class ExpandSelectionToWordCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selections = self.view.sel()
		new_selections = list(self.getwordwithdots(selections))
		if new_selections:
			selections.add_all(new_selections)

	def getwordwithdots(self, selections):
		for region in selections:
			lines = self.view.lines(region)
			if len(lines) != 1:
				continue

			line_contents = self.view.substr(lines[0])
			rowcols = map(self.view.rowcol, (region.begin(), region.end()))
			(row, begin), (row, end) = rowcols

			pattern = re.compile(r"[\w\.]+", flags=re.ASCII)
			matches = filter(
				lambda match: (
					(match.start() <= begin <= match.end())
					or (match.start() <= end <= match.end())
				),
				re.finditer(pattern, line_contents),
			)
			word = sublime.Region(
				*[self.view.text_point(row, col) for col in next(matches).span()]
			)
			yield region.cover(word)
