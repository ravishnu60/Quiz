from tkinter import*
import openpyxl

root=Tk()
root.title('QUIZ')
root.iconbitmap('__func/logo.ico')
root.state('zoomed')

start=PhotoImage(file='__func/b1.png')

#start bg image 
bg=Label(root,image=start)
bg.place(x=1,y=1) 

def create(src,anx):


    midle=PhotoImage(file=src+'/b2.png')

    #read and write in excel 
    path=src+'/answer.xlsx'
    wb=openpyxl.load_workbook(path)
    sheet=wb.active

    #for opening and ending
    tq=PhotoImage(file=src+'/b3.png')
    #question image
    img1=PhotoImage(file=src+'/img1.png')
    img2=PhotoImage(file=src+'/img2.png')
    img3=PhotoImage(file=src+'/img3.png')
    img4=PhotoImage(file=src+'/img4.png')
    img5=PhotoImage(file=src+'/img5.png')
    img6=PhotoImage(file=src+'/img6.png')
    img7=PhotoImage(file=src+'/img7.png')
    img8=PhotoImage(file=src+'/img8.png')
    img9=PhotoImage(file=src+'/img9.png')
    img10=PhotoImage(file=src+'/img10.png')
    img11=PhotoImage(file=src+'/img11.png')
    img12=PhotoImage(file=src+'/img12.png')
    img13=PhotoImage(file=src+'/img13.png')
    img14=PhotoImage(file=src+'/img14.png')
    img15=PhotoImage(file=src+'/img15.png')
    img16=PhotoImage(file=src+'/img16.png')
    img17=PhotoImage(file=src+'/img17.png')
    img18=PhotoImage(file=src+'/img18.png')
    img19=PhotoImage(file=src+'/img19.png')
    img20=PhotoImage(file=src+'/img20.png')

    
    #label for  text and images
    bg=Label(root)
    tim=Label(root,font=('Impact', 18),bg='white')
    lab_img = Label(root)
    lab_img1 = Label(root)
    no=Label(root)


    nxt=Button(root)
    ans=Button(root)

    #function loop
    def change(i=1):

        bg.config(image=midle)
        bg.place(x=1,y=1)

        #after the quiz
        def end():

            #restart function
            def rst():

                nxt.destroy()
                
                bg.config(image=start)

                #logo button
                rs.config(text='Logo finder',width=10,height=1,bg='lightblue',font=('Impact',22),command=loif)
                rs.place(x=500,y=400) 

                #tech word button
                ans.config(text='Technical word finder',width=20,height=1,bg='lightblue',font=('Impact',22),command=techfi)
                ans.place(x=700,y=400)

            bg.config(image=tq)
            #lab_img.place(x=0,y=0)
            
            rs=Button(root,text="Retry",width=10,height=1,bg='green',font=('Impact',22),command=rst)
            rs.place(x=580,y=350)

            nxt.config(text="Exit",width=10,height=1,bg="red",font=('Impact',22),command=quit)
            nxt.place(x=770,y=350)


        #timer label
        tim.config(text='Timer')    
        tim.place(x=1150,y=80)

        #timer
        def count(t=30):
            
            if t>=0:
                sec.config(text=str(t)+' Sec left' , font=('Impact', 18))
                sec.place(x=1130,y=125)
                
                if(t<=10):
                    sec.config(fg='red')
                elif(t<=20):
                    sec.config(fg='blue')                 


                root.after(1000, count, t - 1)
            else:

                tim.config(text="Times up!",fg="red") 
                sec.destroy()    
        
            
        #answer button
        def answer():

            #show answer
            show.config(text='Answer : '+cell.value,font=('Impact',22))
            show.place(x=anx,y=530)
            tim.place_forget()
            sec.destroy()

        #function for next button
        def next():

            show.destroy()
            sec.destroy()
            root.after(0,change,i+1) 

        #label for timer
        sec = Label(root, text='', fg='green', bg='white', font=('Impact', 18))
        count()    

        #label for answer
        show=Label(root,text='',fg='darkgreen',bg='white',font=('Roman Italic',18))

        #button name change
        nt='Next'
        
        #choose a particular image and text
        if(i==1):
            pic=img1
            pic1=img2 
        elif(i==2):
            pic=img3
            pic1=img4
        elif(i==3):
            pic=img5
            pic1=img6
        elif(i==4):
            pic=img7
            pic1=img8
        elif(i==5):
            pic=img9
            pic1=img10
        elif(i==6):       
            pic=img11
            pic1=img12
        elif(i==7):
            pic=img13
            pic1=img14 
        elif(i==8):
            pic=img15
            pic1=img16
        elif(i==9):
            pic=img17
            pic1=img18
        elif(i==10):
            nt='Finish'
            pic=img19
            pic1=img20
        else:
            lab_img.destroy()
            lab_img1.destroy()
            nxt.place_forget()
            show.destroy() 
            sec.destroy()
            tim.destroy()
            ans.place_forget()
            no.destroy()
            end()       
            
        #get answer
        cell=sheet.cell(row=i,column=1)


        #display count of quiz
        no.config(text=str(i)+'.',fg='brown',bg='lightblue',font=('Roman Italic',18))
        no.place(x=170,y=200)

        #load first image           
        lab_img.config(image=pic)   
        lab_img.place(x=230,y=200)

        #load second image           
        lab_img1.config(image=pic1)   
        lab_img1.place(x=700,y=200)


        #next button
        nxt.config(text=nt,width=8,height=1,bg='red',font=('Times New Roman',20),command=next)
        nxt.place(x=700,y=610)

        #answer button
        ans.config(text='Answer',width=8,height=1,bg='lightgreen',font=('Times New Roman',20),command=answer)
        ans.place(x=550,y=610) 

    #start the program by calling change function
    change() 
    st.destroy()   


def loif():
    bg.destroy()
    create("__func","600")

def techfi():  
    bg.destroy()      
    create("__func1","570")

#logo button
st=Button(root,text='Logo finder',width=10,height=1,bg='lightblue',font=('Impact',22),command=loif)
st.place(x=500,y=400) 

#tech word button
st1=Button(root,text='Technical word finder',width=20,height=1,bg='lightblue',font=('Impact',22),command=techfi)
st1.place(x=700,y=400)   

    
root.mainloop()