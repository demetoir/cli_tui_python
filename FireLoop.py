import traceback
import fire


# simple easy but need tab completion
class FireLoop:
    def __init__(self, component):
        self.log = None
        self.os = None
        self.component = component
        self.component_functions = None
        self.getch = self._getch_anywhere()

    def start(self):
        while True:
            print('(fire loop)', end='')
            try:
                arg = input()
                # log here

                if arg == "exit":
                    print("exit fire loop")
                    # log here
                    break

                ret = fire.Fire(self.component, arg)
            except fire.core.FireExit as e:
                # catch FireExit exception
                # log here
                pass
            except EOFError as e:
                print('eof error')
                exit()

            except KeyboardInterrupt as e:
                print(" keyboard interrupt")
                break

            except BaseException as e:
                traceback.print_exc()
                # log here
                pass

    def input_(self):
        # cursor 처리해야하네..
        # need "argcomplete" module ?
        # deal input and tab completion
        token = ""

        while True:
            byte_ = self.getch()

            if "enter":
                break
            elif "tab":
                # tab completion
                pass

            elif "del char":
                pass

            elif "space":
                token
                ""
            elif "arrow key":
                pass
            elif "other chars":
                token += byte_.decode("utf-8")
                # just push it

        return buf + token

    @staticmethod
    def _getch_anywhere():
        """
        find getch function equivalent of c getch
        if msvcrt module can load than return msvcrt.getch
        else return getch.getch
        windows env use msvcrt.getch
        linux env use getch.getch

        :return: getch func
        """
        import importlib

        try:
            module_ = importlib.import_module("msvcrt")

        except ModuleNotFoundError as e:
            print("msvcrt not found")

            try:
                module_ = importlib.import_module("getch")
            except ModuleNotFoundError as e:
                raise ModuleNotFoundError("getch module not found.\n this will help you 'pip install getch' ")
        del importlib

        return module_.getch
