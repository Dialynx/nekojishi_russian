screen r18Warning(isClick):
    python:
        title_text_size = 30
        content_text_size = 20
        bold_font = "tl/None/NotoSansCJKtc-Bold.otf"
        button_xysize = (217, 76)
        button_text_Size = 22
    window:
        style "gm_root"
        style_group "empty"
        background "#000000"

        has frame:
            align (0.5,0.5)
            xmargin 180
        vbox:
            text "ВНИМАНИЕ" color title_color xalign 0.5 size title_text_size font bold_font
            text "PLEASE BE ADVISED" color title_color xalign 0.5 size title_text_size font bold_font

            text ""

            text "Эта программа представляет собой ограниченную по возрасту версию визуальной новеллы «Nekojishi». Игра содержит контент для взрослых, включая изображения и текст, описывающие сексуальные действия." size content_text_size
            text "Нажимая «Я согласен», вы подтверждаете, что:" size content_text_size
            text "- Вам больше 18 лет." size content_text_size
            text "- Вы признаете, что эта программа содержит контент для взрослых, как указано выше." size content_text_size
            text "- Распространение этой программы может нарушать законы в вашей стране/регионе." size content_text_size

            text ""

            text "This program is the age limited version of visual novel \"Nekojishi\". This program contains adult-only contents, including images and text that describe sexual activities." size content_text_size
            text "By clicking \"I confirm\", you confirm that:" size content_text_size
            text "— You are over 18 years old." size content_text_size
            text "— You acknowledge that this program contains adult-only content as mentioned above." size content_text_size
            text "— Unauthorised re-distribution of this program may violate laws in your country/region." size content_text_size

            text ""

            hbox:
                xalign 0.5
                spacing 150

                default yes_hover = False

                button:
                    xysize button_xysize
                    if isClick:
                        action Return()
                    hovered SetScreenVariable("yes_hover", True)
                    unhovered SetScreenVariable("yes_hover", False)
                    if yes_hover:
                        background Frame("ui/r18_button_hovered.png", left=5, top=5, tile=True)
                    else:
                        background Frame("ui/r18_button_unhovered.png", left=5, top=5, tile=True)
                    vbox:
                        align (0.5,0.5)
                        text "Я согласен." size button_text_Size xalign 0.5
                        text "I confirm." size button_text_Size xalign 0.5

                default no_hover = False
                button:
                    xysize button_xysize
                    if isClick:
                        action Function(renpy.quit)
                    hovered SetScreenVariable("no_hover", True)
                    unhovered SetScreenVariable("no_hover", False)
                    if no_hover:
                        background Frame("ui/r18_button_hovered.png", left=5, top=5, tile=True)
                    else:
                        background Frame("ui/r18_button_unhovered.png", left=5, top=5, tile=True)
                    vbox:
                        align (0.5,0.5)
                        text "Закрыть программу" size button_text_Size xalign 0.5
                        text "Close the program." size button_text_Size xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
