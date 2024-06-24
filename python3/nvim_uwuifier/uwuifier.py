import pynvim
import uwuipy

@pynvim.plugin
class Uwuifier:
    """
    A plugin to uwuify comments in a buffer based on filetype.
    """
    comment_symbol_lang: dict[str, list[str]] = {
        '#': ['python', 'sh', 'nasm', 'gas', 'tasm'],
        '//': ['c', 'cpp', 'go'],
        '--': ['lua']
    }

    def __init__(self, nvim):
        self.nvim = nvim
        self.uwuifier = uwuipy.uwuipy()

    def uwuify_range(self, start_line, end_line):
        """
        Uwuify the comments in a given range of lines in the current buffer.
        """
        buffer = self.nvim.current.buffer
        filetype = self.nvim.eval('&filetype')

        comment_char = ''
        for symbol, languages in self.comment_symbol_lang.items():
            if filetype in languages:
                comment_char = symbol
                break

        if not comment_char:
            self.nvim.out_write(f"Filetype: {filetype} is not supported, you can add it manually though.\n")
            return

        for i in range(start_line, end_line):
            line = buffer[i]
            comment_index = line.find(comment_char)
            if comment_index != -1:
                comment = line[comment_index + len(comment_char):]
                uwuified_comment = self.uwuifier.uwuify(comment)
                buffer[i] = line[:comment_index + len(comment_char)] + uwuified_comment

