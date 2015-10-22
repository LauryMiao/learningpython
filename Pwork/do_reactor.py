from twisted.internet import reactor
# import traceback


def Echo():
    print('the reactor is running')
    print('++++++++++++++++++++++')
# traceback.print_stack()

reactor.callWhenRunning(Echo)
print('Hello')
reactor.run()
