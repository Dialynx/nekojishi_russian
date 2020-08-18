init -2:
    style my_about_button:
        background None
        xpadding 0
        ypadding 0
        xmargin 0
        ymargin 0

    style my_about_frame:
        background None
        xpadding 0
        ypadding 0
        xmargin 0
        ymargin 0

    style my_about_vbox:
        background None
        xpadding 0
        ypadding 0
        xmargin 0
        ymargin 0

    style my_about_text:
        size 16

screen myAbout():
    tag menu
    modal True
    style_group "my_about"

    window:
        style "mm_root"
        if not main_menu:
            background Frame(Solid(Color("#000000",alpha=0.4)))

    python:
        background_size = (800, 700)

    frame:
        background Frame(im.MatrixColor("ui/frame_g01.png",im.matrix.opacity(0.75)), 10, 10)

        xysize background_size
        align (0.5, 0.5)


        imagebutton:
            idle "ui/item_x_a.png"
            hover "ui/item_x_b.png"
            xanchor 1.0
            pos (background_size[0]-20, 20)
            action Return()

        frame:
            ypos 50
            xpadding 50
            has vbox
            text "О нас" color title_color size 24 xalign 0.5
            text ("Nekojishi %s" % config.version)
            text "Ren'Py 6.99.14"
            text ""
            text "Эта программа содержит бесплатное программное обеспечение по ряду лицензий, включая лицензию MIT и GNU Lesser General Public License. Полный список программного обеспечения, включая ссылки на полный исходный код, можно найти здесь: https://www.renpy.org/l/license"
            text "Звуковые эффекты, используемые в этой программе, кроме выпущенных Lightrain Music (www.lightrain.com.cn), являются бесплатными треками, разрешёнными для использования в коммерческих проектах. Авторские права на эти треки принадлежат их соответствующим правообладателям: © Taira Komori (http://taira-komori.jpn.org)"
            text "Авторские права на историю, дизайн персонажей, художественные работы, дизайн интерфейса и оригинальный звуковой трек Nekojishi принадлежат команде Nekojishi и Orange Juice Dog."
            text "©  Team Nekojishi"
            text "©  Orange Juice Dog"
            text ""
            text "На русский язык игру перевели:  dmitrykotov93,  Furainguari,  Hades,  JackMantel,  Kareolis,  Mr.Ghost,  Nafarrry,  Pam8wlkr,  Shaopard  и  Vincent Grey."
            text ""
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
