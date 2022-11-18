from typing import List


class DirtyClass:

    def __init__(self, name: str, glob_state: List = []):
        self.name = name
        self.glob_state = glob_state


if __name__ == "__main__":
    dirty_1 = DirtyClass("Dan")
    dirty_1.glob_state.append(1)
    dirty_2 = DirtyClass("Jojo")
    print("dirty_2 already have state from dirty_1")
    print(dirty_2.glob_state)
    dirty_2.glob_state.append(2)
    print("dirty_1 will take this also")
    print(dirty_1.glob_state)

    dirty_3 = DirtyClass("kek")
    print("new dirty_3 also get glob_state :)")

    dirty_4 = DirtyClass("no_glob", [])
    print("however dirty_4 has not glob, because we give new list")
    print(dirty_4.glob_state)
