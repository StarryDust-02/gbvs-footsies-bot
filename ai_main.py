
import pyautogui, random


def run_footsies_bot(x1: float, y1: float, x2: float, y2: float, level: str='easy', mode: str='balance') -> None:

    
    if level.lower() == 'easy' and mode.lower() == 'balance':

        # strike mode = balance
        strike = [True, True, False, False]
        attack_rad = 0.12
        footsies_bot(x1, y1, x2, y2, attack_rad, strike)


def footsies_bot(x1: float, y1: float, x2: float, y2: float, attack_rad: float, strike: list[bool]) -> None:

    dm_range = 1.0
    m_range = 1.0
    h_distance = abs(x2 - x1)
    v_distance = abs(y2 - y1)

    if h_distance > (m_range + m_range * attack_rad):

        if x1 < x2:
            pyautogui.press('a')
        else:
            pyautogui.press('d')
    
    elif h_distance in range(m_range, m_range + m_range * attack_rad):

        strike = random.choice(strike)
        if strike and h_distance in range(dm_range, dm_range + dm_range * attack_rad):
            use_dm = [True, False]
            if use_dm:
                pyautogui.press('a')
