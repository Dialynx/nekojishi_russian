screen language(isClick):
    modal True

    window:
        style "gm_root"
        style_group "empty"

        python:
            button_xysize = (76,25)
            text_size = 16

        frame:
            align (0.5,0.4)
            xysize (400,160)


            add Frame("ui/frame_h01.png", left=20, top=20, tile=True) alpha 0.75


            text "Выберите язык" size 22 color title_color align (0.5,0.2)

            grid 2 2:
                align (0.5, 0.8)
                spacing 7.5
                default hover = 0

                button:
                    xysize button_xysize
                    if isClick:
                        action [Function(language.change, index = 0), Hide('language'), Return()]
                    hovered SetScreenVariable("hover", 1)
                    unhovered SetScreenVariable("hover", 0)
                    add ConditionSwitch( hover == 1 , "ui/frame_dlg01tch.png",
                        True, im.MatrixColor("ui/frame_dlg01tch.png",im.matrix.opacity(0)) ) xalign 0.5 ypos 1
                    text "繁體中文" size text_size xalign 0.5


                button:
                    xysize button_xysize
                    if isClick:
                        action [Function(language.change, index = 1), Hide('language'), Return()]
                    hovered SetScreenVariable("hover", 4)
                    unhovered SetScreenVariable("hover", 0)
                    add ConditionSwitch( hover == 4 , "ui/frame_dlg01tch.png",
                        True, im.MatrixColor("ui/frame_dlg01tch.png",im.matrix.opacity(0)) ) xalign 0.5 ypos 1
                    text "简体中文" size text_size xalign 0.5


                button:
                    xysize button_xysize
                    if isClick:
                        action [Function(language.change, index = 2), Hide('language'), Return()]
                    hovered SetScreenVariable("hover", 2)
                    unhovered SetScreenVariable("hover", 0)
                    add ConditionSwitch( hover == 2 , "ui/frame_dlg02en.png",
                        True, im.MatrixColor("ui/frame_dlg01tch.png",im.matrix.opacity(0)) ) xalign 0.5 ypos 1
                    text "English" size text_size xalign 0.5


                button:
                    xysize button_xysize
                    if isClick:
                        action [Function(language.change, index = 4), Hide('language'), Return()]
                    hovered SetScreenVariable("hover", 3)
                    unhovered SetScreenVariable("hover", 0)
                    add ConditionSwitch( hover == 3 , "ui/frame_dlg02en.png",
                        True, im.MatrixColor("ui/frame_dlg02en.png",im.matrix.opacity(0)) ) xalign 0.5 ypos 1
                    text "Русский" size text_size xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
