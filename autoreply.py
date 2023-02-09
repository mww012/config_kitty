from typing import List
from kitty.boss import Boss
from kitty import remote_control


def main(args: List[str]) -> str:
    # this is the main entry point of the kitten, it will be executed in
    # the overlay window when the kitten is
    try:
        remote_control.main(
            ["", "resize-window", "--self", "--axis=vertical", "--increment", "-100"]
        )
    except:
        pass
    answer = input("Enter some text: ")
    # whatever this function returns will be available in the
    # handle_result() function
    return answer


def handle_result(
    args: List[str], answer: str, target_window_id: int, boss: Boss
) -> None:
    # get the kitty window into which to paste answer
    w = boss.window_id_map.get(target_window_id)
    if w is not None:
        w.paste_text(answer)

