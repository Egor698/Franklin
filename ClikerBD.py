import flet as ft
import sqlite3
import random
import asyncio


def main(page: ft.Page):

    page.window.height = 900
    page.window.width = 400
    page.theme = ft.Theme(hint_color=ft.Colors.WHITE)
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
    

    #БД создание
    
    db = sqlite3.connect("Orange4.db")

    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY,
                name TEXT,
                token TEXT,
                lvl INTEGER,
                score INTEGER,
                EXP INTEGER,
                cookci INTEGER,
                cookciau INTEGER
                )""")
    
    db.commit()
    db.close()
    #вход

    #БД
    def basareg(e):
        db = sqlite3.connect("Orange4.db")

        cur = db.cursor()

        cur.execute(f"INSERT INTO user VALUES(NULL, '{field1.value}', '{field2.value}', 1, 0, 0, 0, 0)")

        db.commit()
        db.close()
    
    def basavh(e):
        db = sqlite3.connect("Orange4.db")

        cur = db.cursor()

        cur.execute(f"SELECT * FROM user WHERE name = '{field1.value}' AND token = '{field2.value}'")
        data = cur.fetchone()

        #передаем данные в UI
        
        if data != None:
        
            for el in data:
                print(el)
                star.value = data[4]
                lvl.value = data[3]
                upcookci.value = data[6]
                upaucookci.value = data[7]

                page.clean() 
                page.add(playUI)
                page.update()
        else:
            basareg(e)

        db.commit()
        db.close()




    field1 = ft.TextField(hint_text="Имя", width=200, border_color=ft.Colors.ORANGE, border_radius=10)
    field2 = ft.TextField(hint_text="Ваш токен", width=200, border_color=ft.Colors.ORANGE, border_radius=10)
    button = ft.ElevatedButton(text="Вход", bgcolor=ft.Colors.BLACK,width=200, on_click=basavh)
    register = ft.Column([
        ft.Image(src="https://github.com/Egor698/Orange/blob/main/2025-03-07_10-53-34%201%20(1).png?raw=true"),
        ft.Row([field1], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([field2], alignment=ft.MainAxisAlignment.CENTER),
        button
        
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
   

    #механника подарков
    #точка возврата 
    def UIRem(e):
        page.clean()
        page.add(playUI)
        page.update()

    #подарки
    def gife2(e):
         text = ft.Text("Вам выпала печенька", weight=ft.FontWeight.W_500)
         gifeimage = ft.Image(src="https://cdn-icons-png.flaticon.com/128/164/164659.png", scale=1)
         gife1 = ft.Container(bgcolor="#0f0d0d",border_radius=15,width=350, height=400, content=ft.Column([
            ft.Row([gifeimage], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([text], alignment=ft.MainAxisAlignment.CENTER)
         ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER), alignment=ft.alignment.center, on_click=UIRem )
         
    
         gife1content = ft.Column(
            [gife1],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True, 
        )
         page.clean()
         page.add(gife1content)
         page.update()

    def gife1(e):
        text = ft.Text("Вам выпала золотая печенька", weight=ft.FontWeight.W_500)
        gifeimage = ft.Image(src="https://cdn-icons-png.flaticon.com/128/1375/1375198.png", scale=1)
        gife1 = ft.Container(bgcolor="#0f0d0d",border_radius=15,width=350, height=400, content=ft.Column([
            ft.Row([gifeimage], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([text], alignment=ft.MainAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER), alignment=ft.alignment.center, on_click=UIRem )
         
    
        gife1content = ft.Column(
            [gife1],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True, 
        )
        page.clean()
        page.add(gife1content)
        page.update()




    #открытие подарков
    def opengife(e):
        events = [1, 2]
        probabalities_persent = [20, 80]

        probabilities = [p / 100 for p in probabalities_persent]

        chosen_event = random.choices(events, probabilities, k=1)[0]

        if chosen_event == 1:
            print(chosen_event)
            gife1(e)
            upaucookci.data += 1
            upaucookci.value = str(upaucookci.data)
            remcoockiau(e)


        elif chosen_event == 2:
            gife2(e)
            upcookci.data += 1
            upcookci.value = str(upcookci.data)
            remcoocki(e)
    

    def gifesmex(e):
        page.clean()
        page.add(centered_content)
        page.update()

    text = ft.Text("Нажмите чтобы открыть!", weight=ft.FontWeight.W_500)
    gifeimage = ft.Image(src="https://cdn-icons-png.flaticon.com/128/8146/8146553.png", scale=1)
    gifeconteiner = ft.Container(bgcolor="#0f0d0d",border_radius=15,width=350, height=400, content=ft.Column([
            ft.Row([gifeimage], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([text], alignment=ft.MainAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER), alignment=ft.alignment.center, on_click=opengife)
    
    centered_content = ft.Column(
            [gifeconteiner],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True, 
        )
    #обновление счета в БД
    #обновление печенек в БД
    def remcoocki(e):
        db = sqlite3.connect("Orange4.db")
        
        cur = db.cursor()

        cur.execute(f"UPDATE user SET cookci = cookci + 1 WHERE name = '{field1.value}' AND token = '{field2.value}'")
        
        db.commit()
        db.close()

    def remcoockiau(e):
        db = sqlite3.connect("Orange4.db")
        
        cur = db.cursor()

        cur.execute(f"UPDATE user SET cookciau = cookciau + 1 WHERE name = '{field1.value}' AND token = '{field2.value}'")
        
        db.commit()
        db.close()
    
    def score_upBD(e):

        db = sqlite3.connect("Orange4.db")

        cur= db.cursor()
        
        cur.execute(f"UPDATE user SET score = score + 10 WHERE name = '{field1.value}' AND token = '{field2.value}' ")

        db.commit()
        db.close()
    #мехфника lvlbar 
    def mexlvlbar(e):
       if lvlbar.value >= 1:
            gifesmex(e)
            lvlbar.value = 0
            db = sqlite3.connect("Orange4.db")

            cur = db.cursor()

            cur.execute(f"UPDATE user SET lvl = lvl + 1 WHERE name = '{field1.value}' AND token = '{field2.value}'")
            db.commit()
            db.close()
            lvl.value += 1
            page.update()
    #механика
    async def score_up(e):
        n = score.data / 100
        image.scale = 0.9 #анимация
        score.data += 1 #логика очков
        score.value = str(score.data)
        progressBar.value += 0.1
        if score.data % 10 == 0: #and score.data / 10 < 10:
            snackBar10 = ft.SnackBar(content=ft.Row([ft.Text("🍪 +10", size=20, color=ft.Colors.BROWN_800, weight=ft.FontWeight.W_500)], alignment=ft.MainAxisAlignment.CENTER), bgcolor=ft.Colors.BLACK26)
            progressBar.value = 0
            lvlbar.value += 0.1
            mexlvlbar(e)
            score_upBD(e)
            page.open(snackBar10)
        elif n.is_integer() and n != 0:
            snackBar100 = ft.SnackBar(content=ft.Row([ft.Text("🍪 +100", size=20, color=ft.Colors.BROWN_800, weight=ft.FontWeight.W_500)], alignment=ft.MainAxisAlignment.CENTER), bgcolor=ft.Colors.BLACK26)
            progressBar.value = 0
            lvlbar.value += 0.2
            mexlvlbar(e)
            page.open(snackBar100)
        page.update()
        await asyncio.sleep(0.1) #анимация
        image.scale = 1
        page.update()
   
                 
        
    #UI 

    #инвентарь
    upcookci = ft.Text(value="", weight=ft.FontWeight.W_600, data=0)
    upaucookci = ft.Text(value="", weight=ft.FontWeight.W_600, data=0)
    buttoninvent = ft.IconButton(content=ft.Image(src="https://cdn-icons-png.flaticon.com/128/3916/3916912.png", width=20, height=20), icon_size=7, on_click=UIRem)

    image1 = ft.Image(src="https://cdn-icons-png.flaticon.com/128/164/164659.png",width=120,height=120, fit = ft.ImageFit.CONTAIN)
    coocki = ft.Column([
            ft.Row([image1], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([upcookci], alignment=ft.MainAxisAlignment.CENTER)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER, expand=True)
         
        
        # золотая печенька
    image2 = ft.Image(src="https://cdn-icons-png.flaticon.com/128/1375/1375198.png",width=120,height=120, fit = ft.ImageFit.CONTAIN)
    coockiau = ft.Column([
            ft.Row([image2], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([upaucookci], alignment=ft.MainAxisAlignment.CENTER)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER, expand=True)
       
    def inventarmec(e):
        container1 = ft.Container(width=180, height=180, bgcolor=ft.Colors.BLACK,border_radius=10, content=ft.Row([coocki]), alignment=ft.alignment.center)
        container2 = ft.Container(width=180, height=180, bgcolor=ft.Colors.BLACK,border_radius=10, content=ft.Row([coockiau]), alignment=ft.alignment.center)
       
        grid = ft.Row([container1, container2], alignment=ft.MainAxisAlignment.CENTER)
        
        page.clean()
        page.add(buttoninvent,grid)
        page.update()

   
    star = ft.Text(value="", weight=ft.FontWeight.W_500)
    #контейнер с прогрессом

    #lvl.value - левел, lvlbar.value, gifebocks
   
    lvl = ft.Text(value="1", weight=ft.FontWeight.W_700)
    lvlbar = ft.ProgressBar(color=ft.Colors.BROWN_300, width=200, value=0, border_radius=20, height=15)
    gifebocks = ft.Image(src="https://cdn-icons-png.flaticon.com/128/8146/8146553.png", width=40, height=40, fit=ft.ImageFit.CONTAIN)
    inventar = ft.Container(
        width=40,
        height=40,
        border_radius=5,
        content=ft.Image(src="https://cdn-icons-png.flaticon.com/128/4670/4670588.png", width=40, height=40, fit=ft.ImageFit.CONTAIN), 
        on_click=inventarmec)
    lvlcontainer = ft.Container(
        width=40, 
        height=40, 
        border_radius=20, 
        content=lvl, 
        alignment=ft.alignment.center, 
        border=ft.border.all(1.5, ft.colors.BROWN_900))
    
    progress = ft.Container(
        width=400, 
        height=45, 
        bgcolor=ft.colors.BLACK,
        border_radius=20, 
        content=ft.Row([inventar, lvlcontainer,lvlbar, gifebocks], alignment=ft.MainAxisAlignment.CENTER))
    
        
    progressBar = ft.ProgressBar(color=ft.Colors.BROWN_300, value=0, width=page.window.width - 60, height=20, border_radius=10)
    image = ft.Image(src="https://github.com/Egor698/Orange/blob/main/808851%201.png?raw=true")
    score = ft.Text("0", weight=ft.FontWeight.W_500, size=100, data=0)
    playUI = ft.Column([
    progress,
    ft.Row([score], alignment=ft.MainAxisAlignment.CENTER),
    ft.Container(content=image, alignment=ft.alignment.center, on_click=score_up),
        
    ft.Row([progressBar], alignment=ft.MainAxisAlignment.CENTER)
        ])
    


    #панельуправления

    #UIbottomBar = ft.BottomAppBar(bgcolor=ft.Colors.BLACK12, content=
        
            #ft.Row([
            #ft.IconButton(content=ft.Image(src="https://cdn-icons-png.flaticon.com/128/686/686589.png"), on_click=UI),
            #ft.VerticalDivider(thickness=2),
            #ft.IconButton(content=ft.Image(src="https://cdn-icons-png.flaticon.com/128/2948/2948037.png"), on_click=menu),
            #ft.VerticalDivider(thickness=2),
            #ft.IconButton(content=ft.Image(src="https://cdn-icons-png.flaticon.com/128/3094/3094830.png"), on_click=competition),
            #ft.VerticalDivider(thickness=2),
            #ft.IconButton(content=ft.Image(src="https://cdn-icons-png.flaticon.com/128/2976/2976215.png"), on_click=setting)
            #], alignment=ft.MainAxisAlignment.SPACE_AROUND)
            
            
    #)



    
    page.add(register)









ft.app(target=main)
