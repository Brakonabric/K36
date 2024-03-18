from tkinter import *
from algorithm.play_game import Game
from data.player import WhoPlayFirst
from data.alg import UsingAlgorithm


# Функция закрытия приложения
def on_click_exit():
    # Уничтожение главного окна, это вызовет выключение приложения без ошибок.
    root.destroy()


# Функция отображения окна "О программе"
def about(src):
    # Внутренняя функция для закрытия окна "О программе"
    def close_about():
        # Уничтожение кнопки
        about_fake_button.destroy()

    # Создание полноэкранной кнопки для отображения окна "О программе"
    about_fake_button = Button(root, width=800, height=600, command=close_about, border=0, relief='sunken')

    # Проверка источника вызова функции
    if src == "main":
        # Если источник главное меню, установить изображения "О программе"
        about_fake_button.config(image=Assets.main_about_preview_img)
    else:
        # Если источник меню настройки игры, установить изображения "Правила игры"
        about_fake_button.config(image=Assets.main_about_preview_img)

    # Размещение полноэкранной кнопки на экране
    about_fake_button.place(x=-1.5, y=-1.5)


# Функция отображения окна игры
def game_menu(turn, mode, start_score):
    play = Game(turn, mode, start_score, root)

    def play_game(mult):
        def check_game_state():
            if gm_sc >= 1000:
                if hm_sc < ai_sc:
                    finish_menu("human", hm_sc, gm_sc, ai_sc)
                elif hm_sc > ai_sc:
                    finish_menu("ai", hm_sc, gm_sc, ai_sc)
                else:
                    finish_menu("draw", hm_sc, gm_sc, ai_sc)
                destroy()
                return False
            else:
                print(hm_sc, gm_sc, ai_sc)
                print("its okay")
                return True

        def update_game_stats():
            human_score.config(text=f"{hm_sc}")
            ai_score.config(text=f"{ai_sc}")
            game_score.config(text=f"{gm_sc}")

        def destroy():
            human_score.destroy()
            game_score.destroy()
            ai_score.destroy()
            info_bar.destroy()
            x2_button.destroy()
            x3_button.destroy()

        if mult is None:
            play.ai_turn()
            gm_sc, hm_sc, ai_sc = play.get_data("ai")
            update_game_stats()
            background.create_image(0, 0, image=Assets.in_game_human_bg, anchor=NW)

        else:
            if turn == "human":
                play.human_turn(mult)
                gm_sc, hm_sc, ai_sc = play.get_data("human")
                update_game_stats()
                if check_game_state():
                    ai_img = background.create_image(0, 0, image=Assets.in_game_ai_bg, anchor=NW)
                    play.ai_turn()
                    gm_sc, hm_sc, ai_sc = play.get_data("ai")
                    update_game_stats()
                    check_game_state()
                    background.delete(ai_img)
            else:
                ai_img = background.create_image(0, 0, image=Assets.in_game_ai_bg, anchor=NW)
                play.ai_turn()
                gm_sc, hm_sc, ai_sc = play.get_data("ai")
                update_game_stats()
                background.delete(ai_img)
                if check_game_state():
                    play.human_turn(mult)
                    gm_sc, hm_sc, ai_sc = play.get_data("human")
                    update_game_stats()
                    check_game_state()

    info_bar = Canvas(root, width=400, height=64, highlightthickness=0, border=0)
    info_bar.create_image(0, 0, image=Assets.in_game_window, anchor=NW)

    info_bar.place(x=200, y=264)

    human_score = Label(text="0", font=('Terminal', 23, 'bold'), justify="center", width=2, background="white")
    game_score = Label(text=f"{start_score}", font=('Terminal', 23, 'bold'), justify="center", width=4,
                       background="white")
    ai_score = Label(text="0", font=('Terminal', 23, 'bold'), justify="center", width=2, background="white")

    human_score.place(x=224, y=278)
    game_score.place(x=350, y=278)
    ai_score.place(x=520, y=278)

    x3_button = Button(root, image=Assets.in_game_x3, border=0, command=lambda: play_game(3))  # finish("human")
    x2_button = Button(root, image=Assets.in_game_x2, border=0, command=lambda: play_game(2))  # finish("ai")

    x3_button.place(x=412, y=349)
    x2_button.place(x=286, y=349)

    if turn == 'human':
        background.create_image(0, 0, image=Assets.in_game_human_bg, anchor=NW)
    else:
        background.create_image(0, 0, image=Assets.in_game_ai_bg, anchor=NW)
        play_game(None)
    print(turn, mode, start_score)


# Функция отображения меню итогов игры
def finish_menu(mode, hum_sc, game_sc, ai_sc):
    # Внутренняя функция для перехода к меню настройки игры
    def to_preset_menu():
        # Установка фонового изображения и переход к меню настройки игры
        background.create_image(0, 0, image=Assets.preset_back_img, anchor=NW)
        # Уничтожение кнопок и элементов интерфейса текущего меню
        start_again_button.destroy()
        exit_button.destroy()
        menu_bar.destroy()
        # Вызов функции для отображения меню настройки игры
        preset_menu()

    # Внутренняя функция для выхода к главному меню
    def to_main():
        # Уничтожение кнопок и элементов интерфейса текущего меню
        start_again_button.destroy()
        menu_bar.destroy()
        exit_button.destroy()
        # Вызов функции для отображения главного меню
        main_menu()

    # Определение фонового изображения в зависимости от исхода игры
    if mode == "human":
        bg_img = Assets.final_victory_bg_img
    elif mode == "ai":
        bg_img = Assets.final_defeat_bg_img
    else:
        bg_img = Assets.final_draw_bg_img

    # Установка фонового изображения и текстовых элементов для отображения результатов игры
    background.create_image(0, 0, image=bg_img, anchor=NW)
    background.create_text(150, 288, text=f"{game_sc}", font=('Terminal', 23, 'bold'), justify="center",
                           width=200, anchor=NW)
    background.create_text(150, 363, text=f"{hum_sc} : {ai_sc}", font=('Terminal', 23, 'bold'), justify="center",
                           width=200, anchor=NW)
    # Создание кнопок для перехода к различным меню
    exit_button = Button(root, image=Assets.final_exit_img, border=0, command=lambda: on_click_exit())
    start_again_button = Button(root, image=Assets.final_start_img, border=0, command=lambda: to_preset_menu())
    menu_bar = Button(root, image=Assets.final_menu_img, border=0, command=lambda: to_main())

    # Размещение кнопок на экране
    start_again_button.place(x=500, y=270)
    menu_bar.place(x=500, y=330)
    exit_button.place(x=500, y=390)


# Функция отображения меню настройки игры
def preset_menu():
    # Импорт классов для выбора первого игрока и алгоритма ии
    first_player = WhoPlayFirst()
    used_algorithm = UsingAlgorithm()
    start_num = 7  # Начальное значение для очков игры

    # Внутренняя функция для изменения параметра значения начальных очков игры
    def modify(operator):
        nonlocal start_num
        if operator == '+':
            if start_num < 15:
                start_num += 1
        else:
            if start_num > 5:
                start_num -= 1
        start_on.config(text=f"{start_num}")

    # Внутренняя функция для проверки условий перед началом игры и переходом в игровое меню
    def check_rules():
        player_state = first_player.current_player()  # получения информации кто ходит первым
        alg_state = used_algorithm.current_alg()  # получение информации какой алгоритм использовать
        if player_state is not None and alg_state is not None:
            # Удаление элементов интерфейса меню настройки используя .destroy()
            start_button.destroy()
            alg_button.destroy()
            who_starts_button.destroy()
            input_box.destroy()
            start_on.destroy()
            plus_button.destroy()
            minus_button.destroy()
            about_button.destroy()
            # Переход к игровому меню с передачей параметров кто ходит первым, какой алгоритм использовать, с какого числа начать
            game_menu(player_state, alg_state, start_num)
        else:
            pass

    # Внутренняя функция для изменения отображения кнопки кто ходит первым
    def change_player():
        first_player.change_player(False)  # вызов сеттера класса для изменения текущего игрока
        if first_player.current_player() == "human":
            # Изменение изображения кнопки
            who_starts_button.config(image=Assets.preset_human_img)
        elif first_player.current_player() == "ai":
            # Изменение изображения кнопки
            who_starts_button.config(image=Assets.preset_ai_img)
        else:
            return

    # Внутренняя функция для изменения отображения какой алгоритм использовать в игре
    def change_alg():
        used_algorithm.change_alg(False)  # вызов сеттера класса для изменения текущего алгоритма
        if used_algorithm.current_alg() == "Alfa-beta":
            # Изменение изображения кнопки используя метод .config()
            alg_button.config(image=Assets.preset_alg_ab_img)
        elif used_algorithm.current_alg() == "Minimax":
            # Изменение изображения кнопки используя метод .config()
            alg_button.config(image=Assets.preset_alg_mm_img)
        else:
            return

    # Создание кнопок и элементов интерфейса для меню настройки игры используя конструктор Button(параметры)
    start_button = Button(root, image=Assets.main_menu_start_img, border=0, command=lambda: check_rules())
    alg_button = Button(root, image=Assets.preset_algorithm_img, border=0, command=lambda: change_alg())
    who_starts_button = Button(root, image=Assets.preset_who_starts_img, border=0, command=lambda: change_player())
    about_button = Button(root, image=Assets.main_menu_about_img, border=0, background='white',
                          activebackground='white', command=lambda: about("preset"))
    plus_button = Button(root, image=Assets.preset_plus, border=0, command=lambda: modify('+'))
    minus_button = Button(root, image=Assets.preset_minus, border=0, command=lambda: modify('-'))

    # Создание блока для отображения начального числа игры используя конструкторы Canvas и Label
    input_box = Canvas(root, width=76, height=50, highlightthickness=0)
    input_box.create_image(0, 0, image=Assets.preset_number_img, anchor=NW)
    # Создание изменяемой надписи для отображения начального числа игры
    start_on = Label(text=f"{start_num}", font=('Terminal', 23, 'bold'), justify="center", width=2, background="white")

    # Размещение элементов окна настройки игры используя .place(координаты относительно окна)
    input_box.place(x=362, y=350)
    start_button.place(x=275, y=263)
    alg_button.place(x=507, y=349)
    who_starts_button.place(x=145, y=349)
    about_button.place(x=375, y=485)
    minus_button.place(x=303, y=349)
    plus_button.place(x=445, y=349)
    start_on.place(x=370, y=358)


# Функция отображения главного меню
def main_menu():
    # Внутренняя функция, переключающая на меню выбора настройки игры
    def to_preset_menu():
        # Создание фонового изображения для меню выбора настройки игры .create_image(привязка, источник)
        background.create_image(0, 0, image=Assets.preset_back_img, anchor=NW)
        # Уничтожение кнопок главного меню используя .destroy()
        start_button.destroy()
        exit_button.destroy()
        about_button.destroy()
        # Вызов функции для отображения меню выбора настройки
        preset_menu()
    
    # Создание фонового изображения главного меню используя метод .create_image(привязка, источник)
    background.create_image(0, 0, image=Assets.main_menu_bg_img, anchor=NW)

    # Создание кнопки "Начать", "Выход","О программе" с обработчиком события для перехода к меню настройки игры используя конструктор Button(параметры)
    start_button = Button(root, image=Assets.main_menu_start_img, border=0, command=lambda: to_preset_menu())
    exit_button = Button(root, image=Assets.main_menu_exit_img, border=0, command=lambda: on_click_exit())
    about_button = Button(root, image=Assets.main_menu_about_img, border=0, background='white',
                          activebackground='white', command=lambda: about("main"))

    # Размещение кнопки "Начать", "Выход","О программе" на экране используя .place(координаты относительно окна)
    start_button.place(x=275, y=263)
    exit_button.place(x=300, y=350)
    about_button.place(x=375, y=485)


root = Tk()  # Инициализация основного окна
root.title('K36 GAMES')  # Название заголовка окна
root.geometry('800x600')  # Установка размера окна
root.resizable(width=False, height=False)  # Запрет на изменение размера окна
from data.assets import LoadAssets as Assets  # Импорт изображений для GUI

background = Canvas(root, width=800, height=600)  # Создание элемента типа Canvas
background.pack()  # Размещение объекта
main_menu()  # Вызов функции для отображения главного меню
root.mainloop()  # Запуск главного цикла приложения
