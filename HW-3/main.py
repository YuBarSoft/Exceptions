from my_functools.input_data import *
from my_functools.myexceptions import *

if __name__ == "__main__":
    while True:
        try:
            SaveToFile()
        except LenException as ex:
            print(ex)
        except OnlyAlpha as ex:
            print(ex)
        except ValidBirthDay as ex:
            print(ex)
        except PhoneNumException as ex:
            print(ex)
        except GenderException as ex:
            print(ex)
        except SaveToFileException as ex:
            print(ex)
