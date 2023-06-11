import textwrap

def wrap(string, max_width):
    final_string = textwrap.fill(string, max_width)
    return final_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)