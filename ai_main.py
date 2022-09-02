
import pyautogui, random, time


def run_footsies_bot(xp: float, yp: float, xb: float, yb: float, \
    hp: float, hb: float, level: str='easy', mode: str='balance') -> None:

    
    # strike modes
    if mode.lower() == 'offensive':
        strike_pattern = [True, True, True, True, True, False, False]
    elif mode.lower() == 'defensive':
        strike_pattern = [True, True, False, False, False, False, False]
    else:
        strike_pattern = [True, False]
    
    # ai accuracy
    if level.lower() == 'easy':

        # without hit confirms
        attack_rad = 0.12
        combo = False

    elif level.lower == 'normal':

        # with hit confirms
        attack_rad = 0.08
        combo = True
    
    elif level.lower == 'accurate':

        attack_rad = 0.04
        combo = True

    elif level.lower == 'percise':

        attack_rad = 0.01
        combo = True

    footsies_bot(xp, yp, xb, yb, hp, hb, attack_rad, strike_pattern, combo)
    time.sleep(0.01)
    prev_player_health(hp)


def prev_player_health(health: float) -> float:
    return health



def footsies_bot(xp: float, yp: float, xb: float, yb: float, \
    hp: float, hb: float, attack_rad: float, strike_pattern: list[bool], combo: bool=False) -> None:

    dm_range = 1.0              # placeholder
    m_range = 1.0               # placeholder
    h_distance = abs(xb - xp)
    v_distance = abs(yb - yp)

    # walk forward when player is out of range
    if h_distance > (m_range + m_range * attack_rad):

        if xp < xb:
            pyautogui.press('a')
        else:
            pyautogui.press('d')

    
    # choose to poke or not poke when player is in range
    elif h_distance in range(m_range, m_range + m_range * attack_rad):

        strike = random.choice(strike_pattern)

        # choose to use 2m or 5m if player in 2m range
        if strike and h_distance in range(dm_range, dm_range + dm_range * attack_rad):
            use_dm = [True, False]
            if use_dm:
                pyautogui.keyDown('s')
                pyautogui.press('i')
                pyautogui.keyUp('s')
            else:
                pyautogui.press('i')

        elif strike:
            pyautogui.press('i')
        
        else:
            pyautogui.keyDown('s')
            pyautogui.press(';')
            pyautogui.keyUp('s')

    # poke or defense if player gets too close
    elif h_distance in range(m_range - m_range * attack_rad, m_range):

        strike = random.choice(strike_pattern)

        # choose if or not poke with 214X
        use_skill = random.choice([True, False])


        if strike and use_skill:
            if xp < xb:
                pyautogui.keyDown('d')
                pyautogui.keyDown('i')
                pyautogui.press('p')
                pyautogui.keyUp('i')
                pyautogui.keyUp('d')

            elif xb < xp:
                pyautogui.keyDown('a')
                pyautogui.keyDown('i')
                pyautogui.press('p')
                pyautogui.keyUp('i')
                pyautogui.keyUp('a')
        
        elif strike:
            low = random.choice([True, False, True])
            if low:
                pyautogui.keyDown('s')
                pyautogui.press('i')
                pyautogui.keyUp('s')

            elif attack_rad <= 0.04:
                stand_u = random.choice([True, False, False])
                if stand_u:
                    pyautogui.press('j')
            else:
                pyautogui.press('i')


        # defend if choose not to strike
        else:
            low_defen = random.choice([True, False, False, False, False])
            away = random.choice([True, True, True, True, False])
            if low_defen:
                pyautogui.keyDown('s')
                pyautogui.press(';')
                pyautogui.keyUp('s')

            elif away and xp < xb:
                pyautogui.press('d')
            elif away and xb < xp:
                pyautogui.press('a')

            else:
                dodge = random.choice([True, False])
                if dodge:
                    direction = random.choice(['a', 'd'])
                    pyautogui.keyDown(direction)
                    pyautogui.press(';')
                    pyautogui.keyUp(direction)
                else:
                    pyautogui.press(';')

        
        # hit confirm into 214X
        if combo and hp < prev_player_health:
            if xp < xb:
                pyautogui.keyDown('d')
                pyautogui.keyDown('i')
                pyautogui.press('p')
                pyautogui.keyUp('i')
                pyautogui.keyUp('d')

            elif xb < xp:
                pyautogui.keyDown('a')
                pyautogui.keyDown('i')
                pyautogui.press('p')
                pyautogui.keyUp('i')
                pyautogui.keyUp('a')

        if attack_rad <= 0.04 and hb < 350:

            # become defensive upon low health in higher accuracy settings
            strike_pattern = [True, True, False, False, False, False, False]


