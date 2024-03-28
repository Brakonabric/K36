from tkinter import *
from algorithm.play_game import Game
from data.player import WhoPlayFirst
from data.alg import UsingAlgorithm
titleColor = '\x1b[38;5;40m'
defaultColor = '\033[0m'

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
        about_fake_button.config(image=Assets.about_game_img)
    else:
        # Если источник меню настройки игры, установить изображения "Правила игры"
        about_fake_button.config(image=Assets.about_rule_img)

    # Размещение полноэкранной кнопки на экране
    about_fake_button.place(x=-1.5, y=-1.5)


# Функция отображения окна игры
def game_menu(turn, mode, start_score):
    print(f"{titleColor}[ START: {turn} | ALG: {mode} | SCORE: {start_score} ]{defaultColor}")
    # Вызов класса обработки данных с переменными кто начинает, какой алгоритм использовать, с какого числа начинается игра, коренное окно для корректного отображения GUI
    play = Game(turn, mode, start_score, root)

    # Внутренняя функция для обработки действий игрока и ИИ
    def play_game(mult):
        # Внутренняя функция для обновления статуса игры
        def check_game_state():
            # Проверка статуса игры, если очки выше 1000 пунктов
            if gm_sc >= 1000:
                # Если у игрока меньше очков, чем у ИИ:
                if hm_sc < ai_sc:
                    # Закончить игру в пользу игрока
                    finish_menu("human", hm_sc, gm_sc, ai_sc)
                # Если у ИИ меньше очков, чем у игрока:
                elif hm_sc > ai_sc:
                    # Закончить игру в пользу ИИ
                    finish_menu("ai", hm_sc, gm_sc, ai_sc)
                # Если у игрока и ИИ одинаковое кол-во очков:
                else:
                    # Закончить игру в качестве ничьей
                    finish_menu("draw", hm_sc, gm_sc, ai_sc)
                # Вызвать функцию уничтожения элементов окна игры
                destroy()
                return False
            else:
                return True

        # Внутренняя функция для обновления счета в окне интерфейса
        def update_game_stats():
            human_score.config(text=f"{hm_sc}")
            ai_score.config(text=f"{ai_sc}")
            game_score.config(text=f"{gm_sc}")

        # Внутренняя функция уничтожения элементов окна игры
        def destroy():
            # Удаление текста, кнопок и других элементов окна игры используя .destroy()
            human_score.destroy()
            game_score.destroy()
            ai_score.destroy()
            info_bar.destroy()
            x2_button.destroy()
            x3_button.destroy()

        # При вызове функции play_game, когда первым ходит ИИ, мультипликатор игрока (3 или 2) будет None,
        # поэтому происходит проверка для установки корректного порядка ходов.
        # Если первым ходит ИИ, данные о его ходе должны поступить раньше, чем у игрока будет возможность сделать свой ход.
        if mult is None:
            # Сделать ход за ИИ
            play.ai_turn()
            # Получение обновленных данных статуса игры
            gm_sc, hm_sc, ai_sc = play.get_data("ai")
            # Вызов функции обновления данных игры в окне интерфейса
            update_game_stats()
            # Изменение фона игры на фон хода игрока
            background.create_image(0, 0, image=Assets.in_game_human_bg, anchor=NW)
            # Размещение кнопок в окне
            xbutton_place()
        else:  # Если ходит игрок, мультипликатор игрока будет равен 3 или 2
            # Вызов класса игры с аргументов в качестве мультипликатора игрока
            play.human_turn(mult)
            # Получение обновленных данных статуса игры
            gm_sc, hm_sc, ai_sc = play.get_data("human")
            # Вызов функции обновления данных игры в окне интерфейса
            update_game_stats()
            # Проверка условий игры, если счёт меньше 1000, игра продолжается
            if check_game_state():
                # Фон окна меняется на фон хода ИИ
                ai_img = background.create_image(0, 0, image=Assets.in_game_ai_bg, anchor=NW)
                # Вызов класса игры для получения данных хода ИИ
                play.ai_turn()
                # Получение обновленных данных статуса игры
                gm_sc, hm_sc, ai_sc = play.get_data("ai")
                # Вызов функции обновления данных игры в окне интерфейса
                update_game_stats()
                # Размещение кнопок в окне
                xbutton_place()
                # Проверка условий игры, если, после хода ИИ, счёт игры меньше 1000, игра переходит на следующую итерацию
                check_game_state()
                # Удаление изображения фона хода ИИ
                background.delete(ai_img)

    # Создание элемента дизайна, поверх которого размещается счёта участников игры
    info_bar = Canvas(root, width=400, height=64, highlightthickness=0, border=0)
    info_bar.create_image(0, 0, image=Assets.in_game_window, anchor=NW)

    # Размещение элемента в окне
    info_bar.place(x=200, y=264)

    # Создание текстовых элементов, который будет отображать счёт участников игры
    human_score = Label(text="0", font=('Terminal', 23, 'bold'), justify="center", width=2, background="white")
    game_score = Label(text=f"{start_score}", font=('Terminal', 23, 'bold'), justify="center", width=4,
                       background="white")
    ai_score = Label(text="0", font=('Terminal', 23, 'bold'), justify="center", width=2, background="white")

    # Размещение текстовых элементов в окне.
    human_score.place(x=224, y=278)
    game_score.place(x=350, y=278)
    ai_score.place(x=520, y=278)

    # Внутренняя функция для предотвращения спама кнопкой
    def x3():
        # Спрятать кнопки
        x3_button.place_forget()
        x2_button.place_forget()
        # Вызвать функцию игры с мультипликатором 3
        play_game(3)

    # Внутренняя функция для предотвращения спама кнопкой
    def x2():
        # Спрятать кнопки
        x3_button.place_forget()
        x2_button.place_forget()
        # Вызвать функцию игры с мультипликатором 2
        play_game(2)

    # Внутренняя функция для размещения кнопок в окне
    def xbutton_place():
        x3_button.place(x=412, y=349)
        x2_button.place(x=286, y=349)

    # Создание кнопок вызова функции игры, функция вызывается с аргументов в качестве мультипликатора игрока (3 или 2)
    # Если игрок ходит первым, первый вызов функции определит корректный порядок хода игры
    x3_button = Button(root, image=Assets.in_game_x3, border=0, command=x3)
    x2_button = Button(root, image=Assets.in_game_x2, border=0, command=x2)

    # Проверка кто ходит первым:
    if turn == 'human':
        # Установка фона окна на фон хода игрока
        background.create_image(0, 0, image=Assets.in_game_human_bg, anchor=NW)
        # Размещение кнопок в окне
        xbutton_place()
    else:
        # Установка фона окна на фон хода ИИ
        background.create_image(0, 0, image=Assets.in_game_ai_bg, anchor=NW)
        # Вызов функции игры, с аргументом None, для правильного определения порядка ходов
        play_game(None)


# Функция отображения меню итогов игры
def finish_menu(turn, hum_sc, game_sc, ai_sc):
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
    if turn == "human":
        bg_img = Assets.final_victory_bg_img
        print(f"{titleColor}[ WIN: {turn} | {hum_sc} : {ai_sc} | SCORE: {game_sc} ]{defaultColor}")
    elif turn == "ai":
        bg_img = Assets.final_defeat_bg_img
        print(f"{titleColor}[ WIN: {turn} | {hum_sc} : {ai_sc} | SCORE: {game_sc} ]{defaultColor}")
    else:
        bg_img = Assets.final_draw_bg_img
        print(f"{titleColor}[ WIN: DRAW | {hum_sc} : {ai_sc} | SCORE: {game_sc} ]{defaultColor}")
    print("")

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
