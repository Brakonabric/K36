from tkinter import *


class LoadAssets:
    main_menu_bg_img = PhotoImage(file='assets/img/main/main_menu_background.png')
    main_menu_start_img = PhotoImage(file='assets/img/main/main_menu_start.png')
    main_menu_exit_img = PhotoImage(file='assets/img/main/main_menu_exit.png')
    main_menu_about_img = PhotoImage(file='assets/img/main/main_menu_about.png')

    preset_back_img = PhotoImage(file='assets/img/preset/preset_background.png')
    preset_number_img = PhotoImage(file='assets/img/preset/preset_number.png')
    preset_who_starts_img = PhotoImage(file='assets/img/preset/preset_who_starts.png')
    preset_human_img = PhotoImage(file='assets/img/preset/preset_who_starts_human.png')
    preset_ai_img = PhotoImage(file='assets/img/preset/preset_who_starts_ai.png')

    preset_plus = PhotoImage(file='assets/img/preset/preset_number_plus.png')
    preset_minus = PhotoImage(file='assets/img/preset/preset_number_minus.png')

    preset_algorithm_img = PhotoImage(file='assets/img/preset/preset_alg.png')
    preset_alg_ab_img = PhotoImage(file='assets/img/preset/preset_alg_alpha_beta.png')
    preset_alg_mm_img = PhotoImage(file='assets/img/preset/preset_alg_minimax.png')
    preset_alg_hf_img = PhotoImage(file='assets/img/preset/preset_alg_hf.png')

    in_game_human_bg = PhotoImage(file='assets/img/game/game_human_background.png')
    in_game_ai_bg = PhotoImage(file='assets/img/game/game_computer_background.png')
    in_game_window = PhotoImage(file='assets/img/game/game_window.png')
    in_game_x3 = PhotoImage(file='assets/img/game/game_x3.png')
    in_game_x2 = PhotoImage(file='assets/img/game/game_x2.png')

    final_defeat_bg_img = PhotoImage(file='assets/img/final/final_defeat_background.png')
    final_draw_bg_img = PhotoImage(file='assets/img/final/final_draw_background.png')
    final_victory_bg_img = PhotoImage(file='assets/img/final/final_victory_background.png')
    final_menu_img = PhotoImage(file='assets/img/final/final_menu.png')
    final_start_img = PhotoImage(file='assets/img/final/final_start_again.png')
    final_exit_img = PhotoImage(file='assets/img/final/final_exit.png')

    about_game_img = PhotoImage(file='assets/img/about_game.png')
    about_rules_img = PhotoImage(file='assets/img/about_rule.png')
    authors_img = PhotoImage(file='assets/img/authors.png')
    icon = 'assets/img/icon.ico'

    mute_w = PhotoImage(file='assets/img/mute_w.png')
    unmute_w = PhotoImage(file='assets/img/unmute_w.png')
    mute = PhotoImage(file='assets/img/mute.png')
    unmute = PhotoImage(file='assets/img/unmute.png')

    sheet = """
    \u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c
    \u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u005b\u0035\u002c\u0020\u0048\u0075\u006d\u0061\u006e\u002c\u0020\u0033\u0033\u0033\u005d\u007c\u007c\u005b\u0036\u002c\u0020\u0041\u0049\u002c\u0020\u0032\u0033\u0033\u005d\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c
    \u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c
    \u007c\u007c\u007c\u007c\u005b\u0037\u002c\u0020\u0048\u0075\u006d\u0061\u006e\u002c\u0020\u0033\u0033\u0033\u005d\u007c\u007c\u005b\u0031\u0034\u002c\u0020\u0041\u0049\u002c\u0033\u0033\u0033\u005d\u007c\u007c\u005b\u0031\u0031\u002c\u0020\u0048\u0075\u006d\u0061\u006e\u002c\u0020\u0033\u0033\u0032\u005d\u007c\u007c\u007c\u007c
    \u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c
    \u007c\u007c\u007c\u007c\u005b\u0031\u0031\u002c\u0020\u0048\u0075\u006d\u0061\u006e\u002c\u0020\u0033\u0033\u0033\u005d\u007c\u007c\u005b\u0039\u002c\u0020\u0048\u0075\u006d\u0061\u006e\u002c\u0020\u0033\u0033\u0033\u005d\u007c\u007c\u005b\u0036\u002c\u0020\u0041\u0049\u002c\u0020\u0032\u0033\u0032\u005d\u007c\u007c\u007c\u007c
    \u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c
    \u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u005b\u0031\u0034\u002c\u0020\u0041\u0049\u002c\u0020\u0033\u0033\u0032\u005d\u007c\u007c\u005b\u0036\u002c\u0020\u0041\u0049\u002c\u0020\u0032\u0032\u0033\u005d\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c
    \u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c\u007c
    """
