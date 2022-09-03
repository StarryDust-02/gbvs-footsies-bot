import pyautogui, random, time, keyboard


PREVIOUS_HEALTH = 10000.0

def run_footsies_bot(xp: float, yp: float, xb: float, yb: float, \
    hp: float=10000.0, hb: float=10000.0, level: str='normal', mode: str='balance') -> None:
    '''
    Parameters (from game)
        - xp: the x position of the player.
        - yp: the y position of the player (*).
        - xb: the x position of the bot.
        - yb: the y position of the bot (*).
        - hp: the health of the player (#).
        - hb: the health of the bot (#).

    Parameters (from user through ui)
        - level: the intelegence of the bot.
        - mode: the strike mode of the bot.

    (*) not yet implimented.
    (#) if due to time cannot impliment, default it to 10000.
    
    '''
    global PREVIOUS_HEALTH
    
    # strike modes
    pattern = [True, False]
    if mode.lower() == 'offensive':
        pattern = [True, True, True, True, True, False, False]
    elif mode.lower() == 'defensive':
        pattern = [True, True, False, False, False, False, False]      
    
    # ai accuracy levels
    # with hit confirms and adaquately accurate
    rad = 0.08
    combo = True

    if level.lower() == 'easy':

        # without hit confirms and poorly accurate
        rad = 0.12
        combo = False
    
    elif level.lower == 'accurate':

        # with hit confirms and very accurate
        rad = 0.04
        combo = True

    elif level.lower == 'percise':

        # with hit confirms and a percise sense of range
        rad = 0.01
        combo = True
    
    if not keyboard.is_pressed("j"):
        footsies_bot(xp, yp, xb, yb, hp, hb, rad, pattern, combo, PREVIOUS_HEALTH)
        time.sleep(0.01)
        PREVIOUS_HEALTH = prev_player_health(hp)


def prev_player_health(health: float) -> float:
    return health


def footsies_bot(xp: float, yp: float, xb: float, yb: float, \
    hp: float, hb: float, attack_rad: float, strike_pattern: list[bool], combo, prev_health: int=10000) -> None:

    dm_range = 1.0              # placeholder
    m_range = 1.0               # placeholder
    h_distance = abs(xb - xp)
    v_distance = abs(yb - yp)   # not yet implimented


    if attack_rad <= 0.04 and hb < 3500:

            # become defensive upon low health in higher accuracy settings
            strike_pattern = [True, True, False, False, False, False, False]
            

    # walk forward when player is out of range
    if h_distance > (m_range + m_range * attack_rad):

        if xp < xb:
            pyautogui.press('a')
        else:
            pyautogui.press('d')

    
    # choose to poke or not poke when player is in range
    elif m_range - m_range * attack_rad <= h_distance <= (m_range + m_range * attack_rad):

        strike = random.choice(strike_pattern)

        # choose to use 2m or 5m if player in 2m range
        if strike and h_distance <= (dm_range + dm_range * attack_rad):
            use_dm = [True, False]
            if use_dm:
                pyautogui.keyDown('s')
                pyautogui.press('i')
                pyautogui.keyUp('s')
            else:
                pyautogui.press('i')

        elif strike:
            pyautogui.press('i')
        
        elif not strike:
            guard = random.choice([True, False])
            if guard:
                pyautogui.keyDown('s')
                pyautogui.press(';')
                pyautogui.keyUp('s')
            else:
                if xp < xb:
                    pyautogui.press('d')
                else:
                    pyautogui.press('a')

    # poke or defense if player gets too close
    elif h_distance < m_range - (m_range * attack_rad):

        strike = random.choice(strike_pattern)

        # choose if or not poke with 214X
        use_skill = random.choice([True, False])

        # choose if or not perform an anti-air when applicable.
        anti_air = random.choice([True, True, False, False, False])

        # if the bot is at a higher accuracy and has decent health,
        # it will choose to anti-air more often.
        if attack_rad <= 0.04 and hb > 6500:
            anti_air = random.choice([True, True, False])

        # detect player's jump-in and choose weather or not to DP 
        if attack_rad <= 0.08 and v_distance > 0 and anti_air and hb > 4000:
            if xp < xb:
                pyautogui.keyDown('a')
                pyautogui.keyDown('i')
                pyautogui.press('p')
                pyautogui.keyUp('i')
                pyautogui.keyUp('a')

            elif xb < xp:
                pyautogui.keyDown('d')
                pyautogui.keyDown('i')
                pyautogui.press('p')
                pyautogui.keyUp('i')
                pyautogui.keyUp('d')


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
                    pyautogui.keyDown('j')
                    time.sleep(random.choice([0.5, 0.7, 0.9, 1.1, 1.3, 1.5]))
                    pyautogui.keyUp
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
    if combo and hp < prev_health - 500 and not anti_air:
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

