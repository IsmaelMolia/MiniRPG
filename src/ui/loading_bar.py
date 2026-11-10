import time

def loading_bar_console(progress:float, title: str, wait=False):
    progress_bar = "#" * int(20 * progress) + "-" * (20 - int(20 * progress))
    added_space = 20 - len(title) # this allows multiple loading_bars to be centered, as long as their title length is less than 20 characters

    print(f"\r>>> Loading {title} : {' '*added_space} [{progress_bar}] {round((progress) * 100, 2)} % ", end="", flush=True)

    if wait:
        time.sleep(0.01)
    if progress >= 1:
        print("\tDone !")
