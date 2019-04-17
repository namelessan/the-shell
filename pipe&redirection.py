from subprocess import Popen
from subprocess import PIPE


def split_to_list(elem, punc):
    j = len(punc)
    i = 0
    part = ''
    res = []
    while i < len(elem):
        if elem[i:i+j] == punc:
            if part:
                res.extend([part, punc])
            part = ''
            i += j
        else:
            part += elem[i]
            i += 1
    return res


def devide_to_pieces(user_input):
    delimiter = ['|', '<', '<<', '>', '>>', '&&', '||']
    pieces = []
    for elem in user_input:
        for punc in delimiter:
            if punc in elem:
                devided = split_to_list(elem, punc)
                if devided:
                    pieces.extend(devided)
    pass


def get_pipe_part(user_input):
    delimiter = ['|']
    res = []
    part = []
    for elem in user_input:
        if any(x in elem for x in delimiter):
            if part:
                res.append(part)
            part = []
        else:
            part.append(elem)
    return res


def pipe(inp):
    inputs = inp.split('|')
    for i, command in enumerate(inputs):
        cmd = command.strip().split()
        p = Popen(cmd, stdout=PIPE, stdin=p.stdout if i != 0 else None)
    return p.communicate()[0].decode()


if __name__ == '__main__':
    # print(pipe('ls -l| grep a| echo 3333333'))
    print(pipe('ls -l | grep a | wc'))