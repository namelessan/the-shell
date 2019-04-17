from subprocess import run

def find_parenth(raw_input):
    try:
        i = raw_input.index('(')
        j = raw_input.index(')')
        while j < i:
            try:
                j = raw_input[j+1:].index(')') + (j + 1)
                if i < j:
                    break
            except ValueError:
                break
        return i, j
    except Exception as e:
        raise e # test
        return 'Not found bracket'


def get_subcmd(raw_input):
    res = []
    i, j = find_parenth(raw_input)
    res.append(raw_input[i+1:j].strip().split())
    rem_string = raw_input[j+1:]
    if '(' in rem_string:
        res.extend(get_subcmd(rem_string))
    return res


def subshell(raw_input):
    sub_cmd = get_subcmd(raw_input)
    for cmd in sub_cmd:
        try:
            exit_code = run(cmd).returncode
        except FileNotFoundError:
            print('intek-sh: %s: command not found' % cmd[0])
            exit_code = 127
        # catch if PATH variable doesn't exist
        except KeyError:
            print('intek-sh: %s: No such file or directory' % cmd[0])
            exit_code = 127
        # catch if no execute permission on the command
        except PermissionError:
            print('intek-sh: %s: Permission denied' % cmd[0])
            exit_code = 126


if __name__ == '__main__':
    print(subshell('(hsahk jksaldl) (ls -l) (cat bloble)'))
    # print(get_subcmd('(hsahk jksaldl) (ls -l) (cat bloble)'))