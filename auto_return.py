import inspect
import re


RETURN_REGEX = re.compile('\s*return[[(\'" ]')
LEFT_SPACES_REGEX = re.compile('\s*.')


def auto_return(func):
    source_lines = inspect.getsourcelines(func)[0]
    for line_num, line in enumerate(source_lines):
        if line.strip() == '@auto_return':
            auto_return_line = line_num
            break
    else:
        auto_return_line = None
    if auto_return_line is not None:
        del source_lines[auto_return_line]
    last_line = source_lines[-1]
    if RETURN_REGEX.match(last_line) is None:
        try:
            eval(last_line)
        except SyntaxError:
            return func
        except NameError:
            pass
        indentation = LEFT_SPACES_REGEX.match(last_line).span()[1] - 1
        last_line = indentation * ' ' + 'return ' + last_line.lstrip()
        source_lines = source_lines[:-1] + [last_line]

        base_indentation = LEFT_SPACES_REGEX.match(source_lines[0]).span()[1] - 1
        source_lines = [line[base_indentation:] for line in source_lines]

        exec(''.join(source_lines))

        local_vars = list(vars().items())
        new_func = local_vars[-1][1]
        return new_func
    return func