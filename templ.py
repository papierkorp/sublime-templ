import sublime
import sublime_plugin
import re


class TemplCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.templ"):
            return []

        completions = [
            ("templ\tKeyword", "templ ${1:name}($2) {\n\t$0\n}"),
            ("script\tKeyword", "script ${1:name}() {\n\t$0\n}"),
            ("css\tKeyword", "css ${1:name}() {\n\t$0\n}"),
            ("if\tKeyword", "if ${1:condition} {\n\t$0\n}"),
            ("else\tKeyword", "else {\n\t$0\n}"),
            ("for\tKeyword", "for ${1:_, item} := range ${2:items} {\n\t$0\n}"),
            ("switch\tKeyword", "switch ${1:expression} {\n\tcase ${2:value}:\n\t\t$0\n}"),
            ("case\tKeyword", "case ${1:value}:\n\t$0"),
            ("default\tKeyword", "default:\n\t$0"),
            ("@\tImport", "@${1:import}"),
            ("@\tComponent Call", "@${1:componentName}($2)"),
            ("{\tExpression", "{ $0 }"),
            ("{!\tSafe Expression", "{! $0 }"),
            ("package\tKeyword", "package ${1:main}\n"),
            ("import\tKeyword", "import \"${1:package}\"\n"),
            ("func\tKeyword", "func ${1:name}(${2:params}) ${3:returnType} {\n\t$0\n}"),
            ("return\tKeyword", "return ${1:value}\n"),
        ]

        return (completions, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)


class TemplSyntaxListener(sublime_plugin.EventListener):
    def on_load(self, view):
        if view.file_name() and view.file_name().endswith('.templ'):
            view.set_syntax_file('Packages/Templ/Templ.sublime-syntax')


def plugin_loaded():
    sublime.load_settings("Templ.sublime-settings")


def plugin_unloaded():
    sublime.save_settings("Templ.sublime-settings")
