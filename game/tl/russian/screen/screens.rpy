


init -2:
    style empty_button:
        background None
        xpadding 0
        ypadding 0
        xmargin 0
        ymargin 0

    style empty_frame:
        background None
        xpadding 0
        ypadding 0
        xmargin 0
        ymargin 0

init -2 python:
    title_color = "#FF9900"
    content_normal_color = "#CCCCCC"
    content_selected_color = "#FFFFFF"







init python:
    use_corner_button = True

screen say:
    key "rollback" action ShowMenu('myHistory')
    on "show" action [Hide('tooltip')]


    default side_image = None
    default two_window = False


    if not two_window:


        window:
            if 'lpdcat_vision' in globals() and lpdcat_vision:
                background Frame(im.MatrixColor("extra/image/frame_b04.png",im.matrix.opacity(0.75)), 12, 12)

            id "window"

            vbox:
                style "say_vbox"

                if who:
                    text who id "who"

                text what id "what"

    else:


        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"


    if side_image:
        add side_image
    else:
        add SideImage() xanchor 1.0 yanchor 1.0 xpos style.window.left_margin-15 ypos config.screen_height-15



    use quick_menu


    if _in_replay or not use_corner_button:
        key "game_menu" action NullAction()

    else:
        use corner_button






screen choice_background:
    default question = None
    window:
        style "gm_root"
        background Frame(Solid(Color("#000000",alpha=0.4)))
        if question is not None:
            text question align (0.5,0.5)







screen choice:

    key "rollback" action ShowMenu('myHistory')
    on "show" action [Hide('tooltip')]

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.75

        has vbox:
            style "menu"
            spacing 5

        for caption, action, chosen in items:

            if action:

                button:
                    action [action]
                    style "menu_choice_button"
                    text caption style "menu_choice"

            else:
                text caption style "menu_caption"

    use corner_button


init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text clear


    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)









screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu
    use corner_button









screen main_menu:
    tag menu


    add im.Scale("bg/bg.jpg",1200,900)
    if ending.is_tig_true_end():
        add "bg/bg_tig.png"
    if ending.is_lpd_true_end():
        add "bg/bg_lpd.png"
    if ending.is_lpdcat_true_end():
        add "bg/bg_lpdcat.png"


    if language.is_chinese_logo() or language.get_label() == 'japanese':
        add "bg/bigcat_logo_ch_s.png" xanchor 0.5 xpos 593 ypos 65 zoom 0.84
    else:
        add "bg/bigcat_logo_en_s.png" xanchor 0.5 xpos 593 ypos 65 zoom 0.84


    imagebutton:
        idle "ui/frame_a01.png"
        hover "ui/frame_a01-1.png"
        xpos 510 ypos 503
        focus_mask True


    imagebutton:
        idle "ui/aico_clocka.png"
        hover "ui/aico_clockb.png"
        xpos 523 ypos 568
        focus_mask None
        action [Hide("tooltip"), ShowMenu("save_load")]
        hovered [Show("tooltip", tip = __("Загрузить") )]
        unhovered [Hide("tooltip")]


    imagebutton:
        idle "ui/aico_photoa.png"
        hover "ui/aico_photob.png"
        xpos 565 ypos 522
        focus_mask None
        action [Function(store_gallery_viewport_yvalue, y=0), ShowMenu("myGallery"), Hide("tooltip")]
        hovered [Show("tooltip", tip= __("Галерея") )]
        unhovered [Hide("tooltip")]


    imagebutton:
        idle "ui/aico_geara.png"
        hover "ui/aico_gearb.png"
        xpos 623 ypos 523
        focus_mask None
        action [ShowMenu("preferences"), Hide("tooltip")]
        hovered [Show("tooltip", tip= __("Настройки") )]
        unhovered [Hide("tooltip")]


    imagebutton:
        idle "ui/aico_infoa.png"
        hover "ui/aico_infob.png"
        xpos 661 ypos 573
        focus_mask None
        action [ShowMenu("information"), Hide("tooltip")]
        hovered [Show("tooltip", tip= __("Глоссарий") )]
        unhovered [Hide("tooltip")]


    imagebutton:
        idle "ui/aico_quita.png"
        hover "ui/aico_quitb.png"
        xpos 659 ypos 683
        focus_mask None
        action [With(Dissolve(0.3)) ,Quit(confirm=True)]
        hovered [Show("tooltip", tip= __("Выйти") )]
        unhovered [Hide("tooltip")]


    default start_hover = False
    button:
        background None
        xysize (80,50)
        pos (562,605)
        hovered SetScreenVariable("start_hover", True)
        unhovered SetScreenVariable("start_hover", False)
        add ConditionSwitch( start_hover, "ui/aico_startc.png",
                        True, "ui/aico_starta.png") align (0.5,0.5)
        action [Preference("auto-forward", "disable"), Function(reset_main_menu_music), With(Fade(1,0,1)), Start()]

    if extra_enable and ending.is_tig_true_end() and ending.is_lpd_true_end() and ending.is_lpdcat_true_end():
        imagebutton:
            idle "extra/image/picture.png"
            xpos 930
            ypos 28
            hovered [Show("tooltip", tip=__("Эпилог"))]
            unhovered [Hide("tooltip")]
            action [With(Fade(1,0,1)),Start("furry_con"), Hide("tooltip")]


    if adult_enable:
        if persistent.r18_flag:
            imagebutton:
                idle "adult/ui/L.png"
                pos (810, 350)
                hovered [Show("tooltip", tip=__("Версия для взрослых"))]
                unhovered [Hide("tooltip")]
                action [Function(unsetR18Flag), Show("tooltip", tip=__("Обычная версия"))]
        else:
            imagebutton:
                idle "adult/ui/S.png"
                pos (810, 350)
                hovered [Show("tooltip", tip=__("Обычная версия"))]
                unhovered [Hide("tooltip")]
                action [Function(setR18Flag), Show("tooltip", tip=__("Версия для взрослых"))]

    use DescriptionBar()

screen DescriptionBar():
    frame:
        yalign 1.0
        xysize (config.screen_width, 34)
        if not persistent.hide_description:
            background Frame(Solid(Color("#000000",alpha=0.75)))
        else:
            background None

        textbutton "©":
            background None
            yalign 0.5
            xpos 0
            margin (0,0)
            padding (0,0)
            action [ShowMenu("myAbout"), Hide("tooltip")]
            hovered [Show("tooltip", tip=__("О нас"), x_flipped=False, y_flipped=True)]
            unhovered [Hide("tooltip")]

        imagebutton:
            xanchor 1.0
            xpos config.screen_width-12
            idle "ui/ico_hide_a.png"
            hover "ui/ico_hide_a.png"
            action [Function(toggleDescriptionBar), Hide("tooltip")]
            if not persistent.hide_description:
                hovered [Show("tooltip", tip=__("Скрыть"), x_flipped=True, y_flipped=True)]
            else:
                hovered [Show("tooltip", tip=__("Инфо"), x_flipped=True, y_flipped=True)]
            unhovered [Hide("tooltip")]

        if not persistent.hide_description:
            hbox:
                spacing 40
                align (0.5, 0.5)
                text _("Левая кнопка мыши: выбрать/прокрутка") size 16
                text _("Колесико мыши: показать/спрятать") size 16
                text _("Пробел: прокрутка") size 16
                text _("Ctrl: быстрая перемотка") size 16

init python:
    def setR18Flag():
        persistent.r18_flag = True
    def unsetR18Flag():
        persistent.r18_flag = False
    def toggleDescriptionBar():
        if not persistent.hide_description:
            persistent.hide_description = True
        else:
            persistent.hide_description = False







screen yesno_prompt:
    default yes_hover = False
    default no_hover = False
    modal True

    window:
        style "gm_root"
        if not main_menu:
            background Frame(Solid(Color("#000000",alpha=0.4)))

    python:

        if language.get_label() == 'zhHant' or language.get_label() == 'zhHans':
            message_text_size = 20
            yesno_text_size = 20
            yes_img_size = (53,27)
            yes_img = "ui/frame_d02.png"
            no_img_size = (53,27)
            no_img = "ui/frame_d02.png"

        elif language.get_label() == 'english':
            message_text_size = 20
            yesno_text_size = 20
            yes_img_size = (53,27)
            yes_img = "ui/frame_d02.png"
            no_img_size = (53,27)
            no_img = "ui/frame_d02.png"

        elif language.get_label() == 'japanese':
            message_text_size = 20
            yesno_text_size = 20
            yes_img_size = (53,27)
            yes_img = "ui/frame_d02.png"
            no_img_size = (53,27)
            no_img = "ui/frame_d02.png"

        else:
            message_text_size = 20
            yesno_text_size = 20
            yes_img_size = (53,27)
            yes_img = "ui/frame_d02.png"
            no_img_size = (53,27)
            no_img = "ui/frame_d02.png"

    frame:
        style_group "yesno"

        xysize (500,160)
        align (0.5,0.5)

        add im.MatrixColor("ui/frame_h01.png",im.matrix.opacity(0.75)) zoom 1.25

        vbox:
            xalign .5
            yalign .2
            spacing 30

            label _(message):
                xalign 0.5
                text_color title_color
                text_size message_text_size


        hbox:
            align (0.5, 0.8)
            spacing 100
            frame:
                xysize yes_img_size
                if yes_hover:
                    add yes_img zoom 1.2
                textbutton _("Да"):
                    align (0.5,0.5)
                    text_size yesno_text_size
                    action [yes_action, SetScreenVariable("yes_hover", False)]
                    hovered [SetScreenVariable("yes_hover", True)]
                    unhovered SetScreenVariable("yes_hover", False)
            frame:
                xysize no_img_size
                if no_hover:
                    add no_img zoom 1.2
                textbutton _("Нет"):
                    align (0.5,0.5)
                    text_size yesno_text_size
                    action [no_action, SetScreenVariable("no_hover", False)]
                    hovered [SetScreenVariable("no_hover", True)]
                    unhovered SetScreenVariable("no_hover", False)


    key "game_menu" action no_action

    key "hide_windows" action NullAction()

init -2:
    style yesno_button:
        background None
        xpadding 0
        ypadding 0
        xmargin 0
        ymargin 0

    style yesno_frame:
        background None
        xpadding 0
        ypadding 0
        xmargin 0
        ymargin 0

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"










screen quick_menu:


    hbox:
        style_group "quick"
        spacing 12
        xanchor 1.0
        xpos .97
        ypos 800-style.window.yminimum+135


        imagebutton:
            idle "ui/ico_hide_a.png"
            hover "ui/ico_hide_b.png"
            action [Preference("auto-forward", "disable"), HideInterface(), Hide("tooltip")]
            hovered [Show("tooltip", tip=__("Скрыть") )]
            unhovered [Hide("tooltip")]


        imagebutton:

            if _preferences.afm_enable:
                idle DynamicDisplayable(auto_forward_displayable)
            else:
                idle "ui/ico_auto_forward_a.png"
            hover "ui/ico_auto_forward_b.png"
            action [Preference("auto-forward", "toggle"), Hide("tooltip")]
            hovered [Show("tooltip", tip=__("Авто") )]
            unhovered [Hide("tooltip")]


        imagebutton:
            idle "ui/ico_speedup_a.png"
            hover "ui/ico_speedup_b.png"
            action [Preference("auto-forward", "disable"), Skip(fast=False, confirm=False), Hide("tooltip")]
            hovered [Show("tooltip", tip=__("Пропуск"), x_flipped=True)]
            unhovered [Hide("tooltip")]


    if info.has_new():
        $ import time
        imagebutton:
            idle "ui/ico_infonews_w.png"
            action [Preference("auto-forward", "disable"), ShowMenu("information", page= info.get_current_index_page(), choice_index= info.get_current_index() ), Hide("tooltip"), Function(info.reset_has_new)]
            hovered [Show("tooltip", tip=__("Статья") ), Function(info.extend_has_new_time)]
            unhovered [Hide("tooltip")]
            if time.time() - info.has_new_time() < 0.1:
                at info_zoom
            else:
                at info_normal
            anchor (0.5,0.5)
            xpos 1054
            ypos 800-style.window.yminimum + 146

init python:

    def auto_forward_displayable(st, at):
        import time
        refresh_time = 0.1
        cur = time.time() % 1
        if cur > 0.5:
            return "ui/ico_auto_forward_b.png", refresh_time
        else:
            return "ui/ico_auto_forward_a.png", refresh_time

transform info_zoom:
    alpha 0.0 zoom 3.0
    linear 0.3 alpha 1.0 zoom 1.0

transform info_normal:
    zoom 1.0

init -2:
    style quick_button is default:

        background None
        xpadding 5







screen corner_button:

    imagebutton:

        idle im.Composite(
        (45, 53),
        (0, 0), im.MatrixColor("ui/frame_b01.png",im.matrix.opacity(0.75)),
        (14, 15), "ui/ico_item_a.png"
        )
        hover im.Composite(
        (45, 53),
        (0, 0), im.MatrixColor("ui/frame_b01.png",im.matrix.opacity(0.75)),
        (14, 15), "ui/ico_item_b.png"
        )

        action [Preference("auto-forward", "disable"), Hide("tooltip"), ShowMenu("corner_menu2")]
        xanchor 1.0
        xpos config.screen_width-style.window.right_margin
        ypos style.window.right_margin

        hovered [Show("tooltip", tip=__("Меню"), x_flipped=True)]
        unhovered [Hide("tooltip")]

        focus_mask None








screen corner_menu2:
    tag menu

    style_group "empty"
    window:
        style "mm_root"
        if not main_menu:
            background Frame(Solid(Color("#000000",alpha=0.4)))

    imagebutton:



        idle im.Composite(
        (165, 240),
        (0, 0), im.MatrixColor("ui/frame_b02.png",im.matrix.opacity(0.75)),
       (134, 15), "ui/ico_item_a.png"
        )
        hover im.Composite(
        (165, 240),
        (0, 0), im.MatrixColor("ui/frame_b02.png",im.matrix.opacity(0.75)),
       (134, 15), "ui/ico_item_b.png"
        )
        action [Return()]
        xanchor 1.0
        xpos config.screen_width-style.window.right_margin
        ypos style.window.right_margin
        focus_mask True

    python:
        image_ypos = 6
        text_size = 19

    vbox:
        xpos config.screen_width-style.window.right_margin - 150
        ypos style.window.right_margin + 63
        spacing 14

        default clock_hover = False
        button:
            xysize (150,30)
            action [Hide("corner_button"), ShowMenu("save_load")]
            hovered SetScreenVariable("clock_hover", True)
            unhovered SetScreenVariable("clock_hover", False)

            has hbox:
                spacing 6
            if clock_hover:
                add "ui/ico_clock_b.png" ypos image_ypos zoom 0.7
                text _("Сохранения") color content_selected_color size text_size yalign 0.5
            if not clock_hover:
                add "ui/ico_clock_a.png" ypos image_ypos zoom 0.7
                text _("Сохранения") color content_normal_color size text_size yalign 0.5

        default info_hover = False
        button:
            xysize (150,30)
            action [Hide("corner_button"), ShowMenu("information")]
            hovered SetScreenVariable("info_hover", True)
            unhovered SetScreenVariable("info_hover", False)

            has hbox:
                spacing 6
            if info_hover:
                add "ui/ico_info_b.png" ypos image_ypos zoom 0.7
                text _("Глоссарий") color content_selected_color size text_size yalign 0.5
            if not info_hover:
                add "ui/ico_info_a.png" ypos image_ypos zoom 0.7
                text _("Глоссарий") color content_normal_color size text_size yalign 0.5

        default gear_hover = False
        button:
            xysize (150,30)
            action [Hide("corner_button"), ShowMenu("preferences")]
            hovered SetScreenVariable("gear_hover", True)
            unhovered SetScreenVariable("gear_hover", False)

            has hbox:
                spacing 8
            if gear_hover:
                add "ui/ico_gear_b.png" ypos image_ypos zoom 0.7
                text _("Настройки") color content_selected_color size text_size yalign 0.5
            if not gear_hover:
                add "ui/ico_gear_a.png" ypos image_ypos zoom 0.7
                text _("Настройки") color content_normal_color size text_size yalign 0.5

        default home_hover = False
        button:
            xysize (150,30)
            action [With(Dissolve(0.3)),MainMenu()]
            hovered SetScreenVariable("home_hover", True)
            unhovered SetScreenVariable("home_hover", False)

            has hbox:
                spacing 8
            if home_hover:
                add "ui/ico_home_b.png" ypos image_ypos zoom 0.7
                text _("Выйти") color content_selected_color size text_size ypos -1
            if not home_hover:
                add "ui/ico_home_a.png" ypos image_ypos zoom 0.7
                text _("Выйти") color content_normal_color size text_size ypos -1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
