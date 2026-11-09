import time

def loading_bar_console(progress:float, title: str, wait=False):
    progress_bar = "#" * int(20 * progress) + "-" * (20 - int(20 * progress))
    print(f"\r>>> Loading {title} : [{progress_bar}] {round((progress) * 100, 2)} % ", end="", flush=True)
    if wait:
        time.sleep(0.01)
    if progress >= 1:
        print("")
