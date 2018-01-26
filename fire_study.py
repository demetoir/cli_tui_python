from FireLoop import FireLoop
import fire


class Manager:
    def __init__(self):
        self.count = 0
        pass

    def __repr__(self):
        return self.__class__.__name__

    def say(self):
        print('hello word')
        return 'i just print "hello world"'

    def info(self):
        self.count += 1
        print('info count %d' % self.count)

    def num_catch(self, num):
        return 'i catch %d' % num

    def help(self):
        return 'help docs ...'

    def exit(self):
        exit()

    def error(self):
        return


if __name__ == '__main__':
    fire.Fire(Manager)
    # FireLoop(Manager()).start()
