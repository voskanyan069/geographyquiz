# Imports
from tkinter import *
from datetime import datetime
from tkinter.messagebox import *
from tkinter import simpledialog
import pyglet


# Scores array
scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

font = "Arial"
btn_background = "#919cb5"
btn_foreground = "#28385c"

# Alert Links and Copy it to Clipboard
def Alert(title, text):
    alert = Tk()

    alert.geometry("300x100")
    alert.resizable(False, False)
    alert.title(title)

    link = Button(alert, text=text, width=35, height=5)
    link.configure(borderwidth=0)
    link.grid(row=0, column=0)

    text = text
    alert.clipboard_clear()
    alert.clipboard_append(text)
    clip_text = alert.clipboard_get()

    alert.mainloop()


# Menu of the Game Start
def Menu():
    # Window settings
    menu = Tk()

    menu.geometry("900x600")
    menu.resizable(False, False)
    menu.title("Աշխարհագրութեան Հացաշար")

    def btn_start_func(event):
        menu.destroy()
        Questions()

    def btn_info_func(event):
        showinfo('Խաղի մասին', '1. Խաղը աշխարհագրութիւն առարկայի մասին է\n'
                        '2. «Համաշխարհային տրանսպորտ» թեմայով\n'
                        '3. Բոլոր թուերը գրել թուերով\n'
                        '4. Սկսել մեծատառով\n'
                        '5․ Վերջակէտ չդնել')

    def btn_feedback_func(event):
        showinfo('Յետադարձ կապ', 'Խաղի ստեղծողը։ Անդրանիկ Ոսկանեան\n'
                        'Հարցերի եւ առաջարկների համար\n'
                        'կարող էք կապուել այս էլ․ հասցէին\n'
                        'andranik.voskanyan@realschool.am')

    mini_title = Button(menu, text="Աշխարհագրութիւն", width=40, height=2, background="#0e263d", foreground="#fff",
                        font=(font, 30))
    mini_title.place(relx=0, rely=0)

    btn_start = Button(menu, text="Սկսել", width=15, height=2, background="#1d2228", foreground="#fb8122",
                       font=(font, 16))
    btn_start.place(relx=.38, rely=.35)
    btn_start.bind("<Button-1>", btn_start_func)

    btn_info = Button(menu, text="Ինֆորմացիայ", width=20, height=2, background="#1d2228", foreground="#fb8122",
                      font=(font, 16))
    btn_info.place(relx=.35, rely=.48)
    btn_info.bind("<Button-1>", btn_info_func)

    btn_feedback = Button(menu, text="Յետադարձ կապ", width=25, height=2, background="#1d2228", foreground="#fb8122",
                          font=(font, 16))
    btn_feedback.place(relx=.32, rely=.61)
    btn_feedback.bind("<Button-1>", btn_feedback_func)

    # # YouTube Alert
    # def yt(event):
    #     Alert("YouTube", "https://youtube.com\n"
    #                      "Link are copied to clipboard")

    # YouTube button
    # try:
    #     ytPhotoOriginal = PhotoImage(file=r"res/yt.png")
    #     ytPhoto = ytPhotoOriginal.subsample(5)
    #     ytImgBtn = Button(menu, image=ytPhoto)
    #     ytImgBtn.place(relx=.93, rely=.9)
    #     ytImgBtn.bind("<Button-1>", yt)
    # except Exception as e:
    #     showwarning(title='Files and folders', message='Please don\'t touch files and folders')  # , **options)


    # Menu Window Launch
    menu.mainloop()


def Questions():
    # Window settings
    root = Tk()

    root.geometry("900x600")
    root.resizable(False, False)
    root.title("Աշխարհագրութեան Հացաշար")

    # Information
    def information(event):
        info = Tk()
        info.geometry("600x400")
        info.resizable(False, False)
        info.title('Ինֆորմացիայ')

        infoInfoTitle = Label(info, text='Ինֆորմացիայ', font=(font, 20))
        infoInfoTitle.place(relx=.33, rely=.05)

        infoCreator = Label(info,
                            text='Խաղի ստեղծողը։ Անդրանիկ Ոսկանյան\nՀարցերի եւ առաջարկների համար\nկարող եք կապուել այս էլ․ հասցէին\nandranik.voskanyan@realschool.am',
                            font=(font, 12))
        infoCreator.place(relx=.2, rely=.15)

        infoGameTitle = Label(info, text='Խաղի մասին', font=(font, 20))
        infoGameTitle.place(relx=.33, rely=.45)

        infoGameText = Label(info,
                             text='1. Խաղը աշխարհագրութիւն առարկայի մասին է\n2. «Համաշխարհային տրանսպորտ» թեմայով\n3. Բոլոր թուերը գրել թուերով\n4. Սկսել մեծատառով\n5․ Վերջակէտ չդնել',
                             font=(font, 12))
        infoGameText.place(relx=.15, rely=.55)

    # Home
    def home(event):
        root.destroy()
        Menu()

    # Questions
    def ask_question1(event):
        master = Tk()
        master.title("Հարց 1")
        master.resizable(False, False)
        master.geometry("500x300")

        def question_right(event):
            scores[0] = 7
            master.destroy()

        def question_wrong(event):
            scores[0] = -1
            master.destroy()
            
        question = Label(master, text="Տրանսպորտը տնտեսութեան առանձին\nճիւղ է, որն սպասարկում է ...", font=(font, 15))
        question.place(relx=.07, rely=.05)

        answer_1 = Button(master, text="զանազան տեսակի փոխադրումներ", width=53, height=2, background=btn_background, foreground=btn_foreground, font=(font, 12))
        answer_1.place(relx=.0, rely=.30)
        answer_1.bind("<Button-1>", question_wrong)

        answer_2 = Button(master, text="հաղորդակցութեան միջոցների ամբողջութիւն", width=53, height=2, background=btn_background, foreground=btn_foreground, font=(font, 12))
        answer_2.place(relx=.0, rely=.45)
        answer_2.bind("<Button-1>", question_wrong)

        answer_3 = Button(master, text="զանազան տեսակի փոխադրումներ, հաղորդակցութեան\nմիջոցների ամբողջութիւն", width=53, height=2, background=btn_background, foreground=btn_foreground, font=(font, 12))
        answer_3.place(relx=.0, rely=.60)
        answer_3.bind("<Button-1>", question_right)
            
        master.mainloop()

    def ask_question2(event):
        answer = simpledialog.askstring("Հարց 2",
                                        "Տրանսպորտի տեսակների թուում են աւդային, ցամաքային եւ ․․․ փոխադրամջոդները")
        if answer == 'ջրային':
            scores[1] = 11
        else:
            scores[1] = -1

    def ask_question3(event):
        master = Tk()
        master.title("Հարց 3")
        master.resizable(False, False)
        master.geometry("500x300")

        def question_right(event):
            scores[2] = 7
            master.destroy()

        def question_wrong(event):
            scores[2] = -1
            master.destroy()
            
        question = Label(master, text="Տրանսպորտը մեծ նշանակութիւն ունի,\nքանի որ թոյլ է տալիս զբաղուել առեւտրով,\nինչը կարեւոր է ․․․ զարգացման համար։", font=(font, 15))
        question.place(relx=.07, rely=.05)

        answer_1 = Button(master, text="քաղաքակրթութիւնների", width=53, height=2, background=btn_background, foreground=btn_foreground, font=(font, 12))
        answer_1.place(relx=.0, rely=.40)
        answer_1.bind("<Button-1>", question_right)

        answer_2 = Button(master, text="գիւղատնտեսութեան", width=53, height=2, background=btn_background, foreground=btn_foreground, font=(font, 12))
        answer_2.place(relx=.0, rely=.60)
        answer_2.bind("<Button-1>", question_wrong)

        master.mainloop()

    def ask_question4(event):
        answer = simpledialog.askstring("Հարց 4",
                                        "Ուղեւորատրանսպորտը լինում է հասարակական, եւ ․․․")
        if answer.lower() == 'անձնական':
            scores[3] = 11
        else:
            scores[3] = -1

    def ask_question5(event):
        answer = askquestion("Հարց 5",
                                        "Փոխադրամիջոցների բազում տեսակներ աղտոտում են աւդը եւ զբաղեցնում մեծ հողատարածքներ")
        if answer == 'yes':
            scores[4] = 5
        else:
            scores[4] = -1

    def ask_question6(event):
        answer = askquestion("Հարց 6",
                                        "Ցամաքային տրանսպորտը ներառում է մարդկանց, ապրանքների եւ ծառայութիւնների շարժն ապահովող ցամաքային բոլոր փոխադրական համակարգերը։")
        if answer == 'yes':
            scores[5] = 5
        else:
            scores[5] = -1

    def ask_question7(event):
        answer = simpledialog.askstring("Հարց 7",
                                        "Քանի՞ անիւանի էր առաջին մեքենան, եւ ո՞վ էր նրա ստեղծողտ։ (թիւ, թուական)")
        if answer.lower() == '3, 1769':
            scores[6] = 11
        else:
            scores[6] = -1

    def ask_question8(event):
        answer = askquestion("Հարց 8",
                                        "Աշխարհի բեռնափոխադրումների 40%-ը կատարուում է ուղաթիռներով, եւ այդ թիւը շարունակում է աճել ամէն տարի:")
        if answer.lower() == 'no':
            scores[7] = 5
        else:
            scores[7] = -1

    def ask_question9(event):
        answer = askquestion("Հարց 9",
                                        "Չարլզ Ֆրուհաուֆը հորինել է առաջին տրակտոր-կցորդը աւելի քան 100 տարի առաջ՝ 1914 թուականին, երբ հաճախորդը ցանկանում էր մեքենայ, որը կարող էր նաւ տեղափոխել:")
        if answer == 'yes':
            scores[8] = 5
        else:
            scores[8] = -1

    def ask_question10(event):
        answer = askquestion("Հարց 10",
                                        "Բրազիլիայի աւդանաւակաեանների քանակը 2000֊ից աւել է։")
        if answer == 'yes':
            scores[9] = 5
        else:
            scores[9] = -1

    def ask_question11(event):
        answer = askquestion("Հարց 11",
                                        "Մոնղոլեաում խցանումների պատճառով մեքենայ վարելու թոյլատուութիւնը կախուած է մեքենայի համարի վերջին թուից")
        if answer == 'yes':
            scores[10] = 5
        else:
            scores[10] = -1

    def ask_question12(event):
        master = Tk()
        master.title("Հարց 12")
        master.resizable(False, False)
        master.geometry("500x300")

        def question_right(event):
            scores[11] = 7
            master.destroy()

        def question_wrong(event):
            scores[11] = -1
            master.destroy()
            
        question = Label(master, text="Մաւտ 1840 թուականից ․․․֊ն աշխարհում\nառաջինն էր արագ եւ հուսալի\nշոգեքարշերի արտադրութեամբ։", font=(font, 15))
        question.place(relx=.07, rely=.05)

        answer_1 = Button(master, text="Հոլանդեան", width=53, height=2, background=btn_background, foreground=btn_foreground, font=(font, 12))
        answer_1.place(relx=.0, rely=.40)
        answer_1.bind("<Button-1>", question_wrong)

        answer_2 = Button(master, text="ԱՄՆ", width=53, height=2, background=btn_background, foreground=btn_foreground, font=(font, 12))
        answer_2.place(relx=.0, rely=.55)
        answer_2.bind("<Button-1>", question_right)

        answer_3 = Button(master, text="Գերմանիան", width=53, height=2, background=btn_background, foreground=btn_foreground, font=(font, 12))
        answer_3.place(relx=.0, rely=.70)
        answer_3.bind("<Button-1>", question_wrong)

        master.mainloop()

    def ask_question13(event):
        answer = askquestion("Հարց 13",
                                        "Առաջին շոգեքարշերը հուսալի չէին եւ շատ ծանր էին։")
        if answer == 'yes':
            scores[12] = 5
        else:
            scores[12] = -1

    def ask_question14(event):
        master = Tk()
        master.title("Հարց 14")
        master.resizable(False, False)
        master.geometry("500x300")

        def question_right(event):
            scores[13] = 7
            master.destroy()

        def question_wrong(event):
            scores[13] = -1
            master.destroy()
            
        question = Label(master, text="Բեռնափոխադրումներ իրականացնող\nարդիւնաբերութիւնը տարեկան\nտեղափոխում է ԱՄՆ տեղափոխուող\nտարեկան բոլոր բեռնափոխադրումնե\nմաւտաւորապէս ...%-ը:", font=(font, 15))
        question.place(relx=.07, rely=.05)

        answer_1 = Button(master, text="35", width=53, height=2, background=btn_background, foreground=btn_foreground, font=(font, 12))
        answer_1.place(relx=.0, rely=.50)
        answer_1.bind("<Button-1>", question_wrong)

        answer_2 = Button(master, text="70", width=53, height=2, background=btn_background, foreground=btn_foreground, font=(font, 12))
        answer_2.place(relx=.0, rely=.65)
        answer_2.bind("<Button-1>", question_right)

        answer_3 = Button(master, text="50", width=53, height=2, background=btn_background, foreground=btn_foreground, font=(font, 12))
        answer_3.place(relx=.0, rely=.80)
        answer_3.bind("<Button-1>", question_wrong)

    def ask_question15(event):
        answer = askquestion("Հարց 15",
                                        "1900-ին ամերիկացիներն ունեին 8000 մեքենայ, 1920-ին՝ նրանց պատկանում էր 8 միլիոն, իսկ 2000-ին՝ աւելի քան 220 միլիոն, աւելի քան մէկ մեքենայ՝ 18 տարեկանից բարձր իւրաքանչիւր անձի համար:")
        if answer == 'yes':
            scores[14] = 4
        else:
            scores[14] = -1

    def facts(event):
        facts = Tk()
        facts.geometry("710x480")
        facts.resizable(False, False)
        facts.title("Հետաքրքիր փաստեր")

        title = Label(facts, text="Հետաքրքիր փաստեր", font=(font, 30))
        title.place(relx=.17, rely=.03)

        text = Label(facts,
                            text="1. Աշխարհը ուղղաթիռով շրջելու համար պահանջուում է 29 աւր:\n"
                                    "2. Առաջին մեքենան աւգտագործում էր լծակ, այլ ոչ թէ ղեկ:\n"
                                    "3. Աշխարհի ամենամեծ աուտոբուսում տեղաւորուում է 300 մարդ:\n"
                                    "4. Ամենակարճ չվերթը գտնուում է Շոտլանդիայի Պապա Ուեսթեյ\nկղզու եւ Ուեսթրի կղզու միջեւ, եւ տեւում է 2 րոպէ:\n"
                                    "5. Մաւտ 100 տարի առաջ մարդկանց մեծամասնութիւնը ծնուել,\nապրել եւ մահացել է 100 մղոնի սահմաններում: Այսաւր մարդիկ\nկարող են ճանապարհորդել ամբողջ աշխարհով մի\nքանի աւրում կամ շաբաթում:\n"
                                    "6. Աշխարհի բոլոր աւդանաւակայանների մէկ երրորդը գտնուում\nէ ԱՄՆ֊ում։"
                                    "7. Աշխարհի ամենաերկար թռիչքը Աուստրալիայի Սիդնեյից մինչեւ\nԴալլաս, Տեխաս է, եւ տեւում է մաւտ 16 ժամ:\n"
                                    "8. Աշխարհի ամենաարագ գնացքը Մագլեւն է` Շանհայում, որը\nկարող է ութ րոպէի ընթացքում 30.5 կմ տարածք հաղթահարել:",
                                    font=(font, 15),
                                    justify=LEFT)
        text.place(relx=.01, rely=.2)

    def check(event):
        # Try sum scores for info
        try:
            # scores_summ = scores[0:20]
            scores_res = sum(scores)
        # if don't working :(
        except Exception as e:
            pass

        # Scores info
        showinfo("Միաւորներ", "Դուք հաւաքել եք " + str(scores_res) + " միաւոր")
        root.destroy()

    # Info button
    try:
        infoPhotoOriginal = PhotoImage(file=r"res/info_2.png")
        infoPhoto = infoPhotoOriginal.subsample(2)
        infoImgBtn = Button(root, image=infoPhoto)
        infoImgBtn.place(relx=.02, rely=.03)
        infoImgBtn.bind("<Button-1>", information)
    except Exception as e:
        showwarning(title='Files and folders', message='Please don\'t touch files and folders')  # , **options)

        infoBtn = Button(root, text='Ինֆորմացիայ')
        infoBtn.place(relx=.01, rely=.03)
        infoBtn.bind("<Button-1>", information)

    # Home button
    try:
        homePhotoOriginal = PhotoImage(file=r"res/home.png")
        homePhoto = homePhotoOriginal.subsample(2)
        homeImgBtn = Button(root, image=homePhoto)
        homeImgBtn.place(relx=.9, rely=.03)
        homeImgBtn.bind("<Button-1>", home)
    except Exception as e:
        showwarning(title='Files and folders', message='Please don\'t touch files and folders')  # , **options)
        homeBtn = Button(root, text='Յետ')
        homeBtn.place(relx=.9, rely=.03)
        homeBtn.bind("<Button-1>", home)

    # Mini title
    label_title = Label(root, text="Աշխարհագրութեան հարցաշար", font=(font, 30))
    label_title.place(relx=.125, rely=.03)

    # Buttons X 1
    btn_question1 = Button(root, text="1", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question1.place(relx=.15, rely=.15)
    btn_question1.bind("<Button-1>", ask_question1)

    btn_question2 = Button(root, text="2", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question2.place(relx=.3, rely=.15)
    btn_question2.bind("<Button-1>", ask_question2)

    btn_question3 = Button(root, text="3", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question3.place(relx=.45, rely=.15)
    btn_question3.bind("<Button-1>", ask_question3)

    btn_question4 = Button(root, text="4", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question4.place(relx=.6, rely=.15)
    btn_question4.bind("<Button-1>", ask_question4)

    btn_question5 = Button(root, text="5", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question5.place(relx=.75, rely=.15)
    btn_question5.bind("<Button-1>", ask_question5)

    # Buttons X 2
    btn_question6 = Button(root, text="6", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question6.place(relx=.15, rely=.35)
    btn_question6.bind("<Button-1>", ask_question6)

    btn_question7 = Button(root, text="7", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question7.place(relx=.3, rely=.35)
    btn_question7.bind("<Button-1>", ask_question7)

    btn_question8 = Button(root, text="8", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question8.place(relx=.45, rely=.35)
    btn_question8.bind("<Button-1>", ask_question8)

    btn_question9 = Button(root, text="9", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question9.place(relx=.6, rely=.35)
    btn_question9.bind("<Button-1>", ask_question9)

    btn_question10 = Button(root, text="10", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question10.place(relx=.75, rely=.35)
    btn_question10.bind("<Button-1>", ask_question10)

    # Buttons X 3
    btn_question11 = Button(root, text="11", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question11.place(relx=.15, rely=.55)
    btn_question11.bind("<Button-1>", ask_question11)

    btn_question12 = Button(root, text="12", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question12.place(relx=.3, rely=.55)
    btn_question12.bind("<Button-1>", ask_question12)

    btn_question13 = Button(root, text="13", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question13.place(relx=.45, rely=.55)
    btn_question13.bind("<Button-1>", ask_question13)

    btn_question14 = Button(root, text="14", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question14.place(relx=.6, rely=.55)
    btn_question14.bind("<Button-1>", ask_question14)

    btn_question15 = Button(root, text="15", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question15.place(relx=.75, rely=.55)
    btn_question15.bind("<Button-1>", ask_question15)

    # Buttons of Bottom (Facts & Check)
    btn_facts = Button(root, text="Հետաքրքիր փաստեր", width=23, height=4, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_facts.place(relx=.15, rely=.75)
    btn_facts.bind("<Button-1>", facts)
    
    btn_check = Button(root, text="Ստուգել", width=23, height=4, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_check.place(relx=.51, rely=.75)
    btn_check.bind("<Button-1>", check)

    # Root Window Launcher
    root.mainloop()


# Launch all app
Menu()
