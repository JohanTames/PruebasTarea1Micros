flowchart TD
    inicio(( )) --> IDLE

    IDLE((IDLE <br> Espera botón START))
    IDLE -- start_pulse --> NEW_STEP

    NEW_STEP((NEW_STEP <br> Agrega nuevo color <br> add_step = 1))
    NEW_STEP --> SHOW_LED_ON

    SHOW_LED_ON((SHOW_LED_ON <br> Enciende LED actual <br> leds_enable = 1))
    SHOW_LED_ON -- enable_halfsec --> SHOW_LED_OFF

    SHOW_LED_OFF((SHOW_LED_OFF <br> LEDs apagados))
    SHOW_LED_OFF -- enable_halfsec --> NEXT_SHOW

    NEXT_SHOW((NEXT_SHOW <br> Decide siguiente LED))
    NEXT_SHOW -- "show_index < sequence_length - 1" --> SHOW_LED_ON
    NEXT_SHOW -- "show_index == sequence_length - 1" --> WAIT_PLAYER

    WAIT_PLAYER((WAIT_PLAYER <br> Espera entrada jugador))
    WAIT_PLAYER -- button_pulse --> CHECK_INPUT

    CHECK_INPUT((CHECK_INPUT <br> Compara botón jugador<br>vs secuencia))
    CHECK_INPUT -- "player_button != sequence_color" --> LOSE_STATE
    CHECK_INPUT -- "player_button == sequence_color" --> NEXT_INPUT

    NEXT_INPUT((NEXT_INPUT <br> Decide progreso juego))
    NEXT_INPUT -- "input_index == 9" --> WIN_STATE
    NEXT_INPUT -- "input_index == sequence_length - 1" --> NEW_STEP
    NEXT_INPUT -- "otro caso" --> WAIT_PLAYER

    WIN_STATE((WIN_STATE <br> Victoria<br>win = 1))
    WIN_STATE -- start_pulse --> NEW_STEP

    LOSE_STATE((LOSE_STATE <br> Derrota<br>lose = 1))
    LOSE_STATE -- start_pulse --> NEW_STEP
