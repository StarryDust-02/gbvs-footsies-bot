import pyautogui, random, time, keyboard


PREVIOUS_HEALTH = 10000.0
ACTION = False

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
    global PREVIOUS_HEALTH, ACTION
    
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
    
    if not keyboard.is_pressed("j") and not ACTION:
        footsies_bot(xp, yp, xb, yb, hp, hb, rad, pattern, combo, PREVIOUS_HEALTH)
        time.sleep(0.01)
        PREVIOUS_HEALTH = prev_player_health(hp)


def prev_player_health(health: float) -> float:
    return health


##################################################################
#                          AI ACTIONS                            #
##################################################################

REACTION_TIME = random.choice([0.12, 0.15, 0.17, 0.22])

def move_left() -> None:
    pyautogui.keyDown('a')
    time.sleep(0.15)
    pyautogui.keyUp('a')

def move_right() -> None:
    pyautogui.keyDown('d')
    time.sleep(0.15)
    pyautogui.keyUp('d')

def down_poke(button: str='i') -> None:
    pyautogui.keyDown('s')
    pyautogui.keyDown(button)
    time.sleep(0.15)
    pyautogui.keyUp(button)
    pyautogui.keyUp('s')

def stand_poke(strength: str='l') -> str:
    pyautogui.keyDown(strength)
    time.sleep(0.15)
    pyautogui.keyUp(strength)
    return strength

def down_guard() -> None:
    pyautogui.keyDown('s')
    pyautogui.keyDown(';')
    time.sleep(random.choice([0.35, 0.45, 0.55]))
    pyautogui.keyUp(';')
    pyautogui.keyUp('s')

def stand_guard() -> None:
    pyautogui.keyDown(';')
    time.sleep(random.choice([0.35, 0.45, 0.55]))
    pyautogui.keyUp(';')

def on_right_dp() -> None:
    pyautogui.keyDown('a')
    pyautogui.keyDown('i')
    pyautogui.keyDown('p')
    time.sleep(0.15)
    pyautogui.keyUp('p')
    pyautogui.keyUp('i')
    pyautogui.keyUp('a')

def on_left_dp() -> None:
    pyautogui.keyDown('d')
    pyautogui.keyDown('i')
    pyautogui.keyDown('p')
    time.sleep(0.15)
    pyautogui.keyUp('p')
    pyautogui.keyUp('i')
    pyautogui.keyUp('d')

def on_right_enchant(strength: str='i') -> None:
    pyautogui.keyDown('d')
    pyautogui.keyDown(strength)
    pyautogui.keyDown('p')
    time.sleep(0.15)
    pyautogui.keyUp('p')
    pyautogui.keyUp(strength)
    pyautogui.keyUp('d')

def on_left_enchant(strength: str='i') -> None:
    pyautogui.keyDown('a')
    pyautogui.keyDown(strength)
    pyautogui.keyDown('p')
    time.sleep(0.15)
    pyautogui.keyUp('p')
    pyautogui.keyUp(strength)
    pyautogui.keyUp('a')

def fireball(strength: str='i') -> None:
    pyautogui.keyDown(strength)
    pyautogui.keyDown('p')
    time.sleep(0.15)
    pyautogui.keyUp('p')
    pyautogui.keyUp(strength)

def run_left_pressure() -> None:
    pyautogui.keyDown('a')
    time.sleep(0.01)
    pyautogui.keyUp('a')
    pyautogui.keyDown('a')
    time.sleep(1.05)
    pyautogui.keyUp('a')
    pyautogui.keyDown('d')
    time.sleep(0.85)
    pyautogui.keyUp('d')
    down_poke(random.choice(['i', 'i', 'u']))

def run_right_pressure() -> None:
    pyautogui.keyDown('d')
    time.sleep(0.01)
    pyautogui.keyUp('d')
    pyautogui.keyDown('d')
    time.sleep(1.05)
    pyautogui.keyUp('d')
    pyautogui.keyDown('a')
    time.sleep(0.85)
    pyautogui.keyUp('a')
    down_poke(random.choice(['i', 'i', 'u']))


##################################################################
#                         MAIN FUNCTION                          #
##################################################################

def footsies_bot(xp: float, yp: float, xb: float, yb: float, \
    hp: float, hb: float, attack_rad: float, strike_pattern: list[bool], combo, prev_health: int=10000) -> None:

    dm_range = 1.0              # placeholder
    m_range = 1.0               # placeholder
    h_distance = abs(xb - xp)
    v_distance = abs(yb - yp)   # not yet implimented

    global ACTION
    poke_strength = None

    if attack_rad <= 0.04 and hb < 3500:

            # become defensive upon low health in higher accuracy settings
            strike_pattern = [True, True, False, False, False, False, False]


    pyautogui.keyUp('s')
    pyautogui.keyUp(';')
    ACTION = True
            

    # walk forward when player is out of range
    if h_distance > (m_range + m_range * attack_rad):

        zoning = random.choice([False, False, False, True])

        if xp < xb:
            if zoning:
                move_right()
                fireball()
            else:
                move_left()
        else:
            if zoning:
                move_left()
                fireball()
            else:
                move_right()

    
    # choose to poke or not poke when player is in range
    elif m_range - m_range * attack_rad <= h_distance <= (m_range + m_range * attack_rad):

        strike = random.choice(strike_pattern)

        # choose to use 2m or 5m if player in 2m range
        if strike and h_distance <= (dm_range + dm_range * attack_rad):
            use_dm = [True, False]
            if use_dm:
                down_poke()
            else:
                poke_strength = stand_poke(random.choice['l', 'm'])

        elif strike:
            poke_strength = stand_poke(random.choice['l', 'm'])
        
        elif not strike:
            guard = random.choice([True, False])
            if guard:
                random.choice([down_guard(), stand_guard()])
                random.choice([down_poke(), None, None])
            else:
                if xp < xb:
                    move_right()
                else:
                    move_left()


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
                on_right_dp()

            else:
                on_left_dp()


        if strike and use_skill:
            if xp < xb:
                on_right_enchant()

            elif xp > xb:
                on_left_enchant()
        
        elif strike:
            low = random.choice([True, False, True])
            if low:
                down_poke()

            elif attack_rad <= 0.04:
                stand_u = random.choice([True, False, False])
                if stand_u:
                    pyautogui.keyDown('j')
                    time.sleep(random.choice([0.5, 0.7, 0.9, 1.1, 1.3, 1.5]))
                    pyautogui.keyUp('j')
            else:
                poke_strength = stand_poke(random.choice['l', 'm'])


        # defend if choose not to strike
        else:
            low_defen = random.choice([True, False, False, False, False])
            away = random.choice([True, True, True, True, False])
            if low_defen:
                down_guard()

            elif away and xp < xb:
                move_right()
            elif away and xp > xb:
                move_left()

            else:
                dodge = random.choice([True, False])
                if dodge:
                    direction = random.choice(['a', 'd'])
                    pyautogui.keyDown(direction)
                    pyautogui.keyDown(';')
                    time.sleep(0.15)
                    pyautogui.keyUp(';')
                    pyautogui.keyUp(direction)
                else:
                    stand_guard()

        
    # hit confirm into 214X
    if combo and hp < prev_health - 200 and not anti_air and poke_strength == 'l':
        if xp < xb:
            on_right_enchant('h')
            run_left_pressure()

        elif xp > xb:
            on_left_enchant('h')
            run_right_pressure()


    ACTION = False
    pyautogui.keyDown('s')
    pyautogui.keyDown(';')
    time.sleep(0.15)
