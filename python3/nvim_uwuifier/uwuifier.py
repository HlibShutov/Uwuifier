import pynvim
import uwuipy

@pynvim.plugin
class Uwuifier:
    def __init__(self, nvim):
        self.nvim = nvim
        self.uwuifier = uwuipy.uwuipy()

    def uwuify_range(self, start_line, end_line):
        buffer = self.nvim.current.buffer
        filetype = self.nvim.eval('&filetype')

        if filetype == 'python' or filetype == 'sh' or filetype == 'nasm' or filetype == 'gas' or filetype == 'tasm':
            comment_char = '#'
        elif filetype == 'c' or filetype == 'cpp':
            comment_char = '//'
        else:
            self.nvim.out_write('Unsupported filetype\n')
            return

        for i in range(start_line, end_line):
            line = buffer[i]
            comment_index = line.find(comment_char)
            if comment_index != -1:
                comment = line[comment_index + len(comment_char):]
                uwuified_comment = self.uwuifier.uwuify(comment)
                buffer[i] = line[:comment_index + len(comment_char)] + uwuified_comment
