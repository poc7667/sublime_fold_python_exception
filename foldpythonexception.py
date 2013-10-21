import sublime, sublime_plugin

class FoldPythonExceptCommand(sublime_plugin.TextCommand):

    def get_text(self, region):

                lines = self.view.lines(region)
                start = lines[0].begin()
                end = lines[-1].end()

                return start, end

    def run(self, edit):
        try:

            for i, region in enumerate( self.view.find_all('except Exception as e',0) ):
                    start, end = self.get_text(region)
                    sub_region = self.view.find_all('raise e', end)[i]
                    sub_start, sub_end = self.get_text(sub_region)
                    # print (start, sub_end)
                    fold_region = sublime.Region( end , sub_end)
                    self.view.fold(fold_region)

        except Exception as e: #2
            print("hihi")
            raise e #2

# '''
class BackgroundFoldPythonExcept(sublime_plugin.EventListener):
    def __init__(self):
        sublime_plugin.EventListener.__init__(self)
        self.last_selected_line = -1
        self.status_active = False

    def _last_selected_lineno(self, view):
        return view.rowcol(view.sel()[0].end())[0]

    def on_post_save(self, view):
            view.run_command('fold_python_except')


def plugin_loaded():
    global pylint_settings
    pylint_settings = sublime.load_settings('FoldPythonExcept.sublime-settings')

# '''