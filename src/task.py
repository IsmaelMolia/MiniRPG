import time


class Task:
    tasks: dict[str, 'Task'] = {}

    @classmethod
    def get(cls, title: str, start: float | None = None, title_len: int = 20, bar_len: int = 20):
        task = cls.tasks.get(title)
        if task is None:
            task = Task(title=title, start=start, title_len=title_len, bar_len=bar_len)
        return task

    def __init__(self, title: str, start: float | None = None, title_len: int = 20, bar_len: int = 20):
        if title in Task.tasks:
            self = Task.tasks.get(title)
            return

        self.title = title
        self.start = start if start is not None else time.time()
        self.progress: float = 0.0

        self.title_len = title_len
        self.bar_len = bar_len

        Task.tasks[self.title] = self

    def get_ellapsed_time(self):
        return round((time.time() - self.start) * 1000, 2)

    def set_progess(self, progress: float):
        self.progress = progress
        return self

    def print_loading_bar(self):
        print(f"\r>>> Loading {self.title + ' :':{self.title_len + 1}} [{'#' * int(self.progress * self.bar_len):-<{self.bar_len}}] {round(self.progress * 100, 2):.2f} %   time : {str(self.get_ellapsed_time()) + ' ms':12}", end="", flush=True)
        if self.progress >= 1:
            print("\tDone !")
            Task.tasks.pop(self.title, None)
