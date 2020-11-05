def print_msg(msg):
    def printer(ok):
        print(msg)
        print(ok)
    return printer

another = print_msg('Hello')

