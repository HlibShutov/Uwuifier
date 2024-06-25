import pynvim
import uwuipy

@pynvim.plugin
class Uwuifier:
    """
    A plugin to uwuify comments in a buffer based on filetype.
    """

    """ test comment """ 
    # test comment 
    comment_symbol_lang = {
        "python": {"comment_char": "#", "multi_line_comment_start": '"""', "multi_line_comment_end": '"""'},
        "c": {"comment_char": "//", "multi_line_comment_start": "/*", "multi_line_comment_end": "*/"},
        "cpp": {"comment_char": "//", "multi_line_comment_start": "/*", "multi_line_comment_end": "*/"},
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

        comment_char = ""
        multi_line_comment_start = ""
        multi_line_comment_end = ""
        for language in self.comment_symbol_lang.keys():
            if filetype == language:
                language_settings = self.comment_symbol_lang[language]
                comment_char = language_settings["comment_char"]
                multi_line_comment_start = language_settings["multi_line_comment_start"]
                multi_line_comment_end = language_settings["multi_line_comment_end"]
                break

        if not comment_char:
            self.nvim.out_write(f"Filetype: {filetype} is not supported, you can add it manually though.\n")
            return
        
        inside_multi_comment = False

        for i in range(start_line, end_line):
            line = buffer[i]
            comment_index = line.find(comment_char)
            if multi_line_comment_start == multi_line_comment_end:
                start_index = line.find(multi_line_comment_start) if inside_multi_comment == False else -1
                if start_index != -1:
                    end_index = line.find(multi_line_comment_end, start_index+len(multi_line_comment_end))
                else:
                    end_index = line.find(multi_line_comment_end) if inside_multi_comment == True else -1
            else:
                start_index = line.find(multi_line_comment_start)
                end_index = line.find(multi_line_comment_end)
           
            if inside_multi_comment:
                if end_index != -1:
                    inside_multi_comment = False
                    comment = line[:end_index + len(multi_line_comment_end)]
                    uwuified_comment = self.uwuifier.uwuify(comment)
                    buffer[i] = uwuified_comment + line[end_index + len(multi_line_comment_end):]
                else:
                    comment = line
                    uwuified_comment = self.uwuifier.uwuify(comment)
                    buffer[i] = uwuified_comment
            elif start_index != -1 and end_index != -1:
                comment = line[start_index + len(multi_line_comment_start):end_index]
                uwuified_comment = self.uwuifier.uwuify(comment)
                buffer[i] = line[:start_index + len(multi_line_comment_start)] + uwuified_comment + line[end_index:]
            elif start_index != -1:
                inside_multi_comment = True
                comment = line[start_index + len(multi_line_comment_start):]
                uwuified_comment = self.uwuifier.uwuify(comment)
                buffer[i] = line[:start_index + len(multi_line_comment_start)] + uwuified_comment
            elif comment_index != -1:
                comment = line[comment_index + len(comment_char):]
                uwuified_comment = self.uwuifier.uwuify(comment)
                buffer[i] = line[:comment_index + len(comment_char)] + uwuified_comment
