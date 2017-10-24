import random


import tkinter


#creating a function
def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = [ "jack", "queen", "king"]

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for each suit retrieve the image for the cards
    for suit in suits:
        for card in range(1,11):
            name  = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file = name)
            card_images.append((card, image,))

        #face cards
        for card in face_cards:
            name  = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file = name)
            card_images.append((card, image,))


def deal_card(frame):
    next_card= deck.pop(0)
    tkinter.Label(frame, image= next_card[1], relief= 'raised').pack(side='left')
    return next_card
def score_hand(hand):
     #calculate the total score of all cards in the list.
    #only 1 ace can have the value 11, and this will be reduced to 1 if the hand would bust
     score = 0
     ace = False
     for next_card in hand:
         card_value= next_card[0]
         if card_value ==1 and not ace:
            ace= True
            card_value = 11
         score += card_value
        #if we wud bust, check if there is an ace and subtract 10
         if score > 21 and ace:
            score -= 10
            ace = False
     return score



def deal_dealer():
    dealer_hand.append(deal_card(dealercardframe))
    dealer_score = score_hand(dealer_hand)
    dealerscorelabel.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("================== D E A L E R   W I N S!!!!!!!!!!!!!!!!===========================")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("===================P L A Y E R   W I N S!!!!!!!!!!!!!!!!!!!!!===========================")
    elif dealer_score > player_score:
        result_text.set("================== D E A L E R   W I N S!!!!!!!!!!!!!!!!===========================")
    else:
        result_text.set("DRAW")
    deal_card(dealercardframe)

def deal_player():

    player_hand.append(deal_card(playercardframe))
    player_score =score_hand(player_hand)

    playerscorelabel.set(player_score)
    if player_score > 21:
        result_text.set("================== D E A L E R   W I N S===========================")

    # global player_score
    # global player_ace #problem solved by global
    # #player_score = 0 #if we remove this line errors will b there as its not a local variable anymore
    # card_value = deal_card(playercardframe)[0]
    # if card_value == 1 and not player_ace:
    #     card_value = 11
    # player_score += card_value
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace =False
    # playerscorelabel.set(player_score)
    # if player_score > 21:
    #     result_text.set("----DEALER WINS!!!!!!!!!!--------")
    # print(locals())


mainwindow = tkinter.Tk()

#set up the screen and frames for the dealer and player

mainwindow.title("black jack ------a vinayak tiwari creation")
mainwindow.geometry("640x480")
mainwindow.configure(background= "green")

result_text = tkinter.StringVar()
result = tkinter.Label(mainwindow, textvariable= result_text)
result.grid(row= 0, column=  0, columnspan= 3)

card_frame = tkinter.Frame(mainwindow, relief= "sunken", borderwidth=1, background="green" )
card_frame.grid(row=1, column= 0, sticky='ew', columnspan=3, rowspan=2)

dealerscorelabel = tkinter.IntVar()



#player_score = 0
#player_ace = False



tkinter.Label(card_frame, text = 'dealer', background ='green', fg= 'white').grid(row= 0, column= 0)
tkinter.Label(card_frame,textvariable= dealerscorelabel, background= "green",fg = "white").grid(row=1,column= 0)
#embedded frame to hold card images
dealercardframe= tkinter.Frame(card_frame, background= "green")
dealercardframe.grid(row=0, column= 1, sticky= "ew", rowspan= 2)

playerscorelabel = tkinter.IntVar()

tkinter.Label(card_frame, text ="player",background= "green", fg= "white").grid(row= 2, column =0)
tkinter.Label(card_frame, textvariable = playerscorelabel,background= "green", fg= "white").grid(row= 3, column =0)
# embedded frame to hold card images
playercardframe = tkinter.Frame(card_frame, background= "green")
playercardframe.grid(row = 2, column = 1, sticky = 'ew',rowspan= 2)

button_frame= tkinter.Frame(mainwindow)
button_frame.grid(row= 3, column= 0, columnspan= 3, sticky = 'w')

dealer_button = tkinter.Button(button_frame, text= " DEALER", command = deal_dealer)
dealer_button.grid(row= 0, column=0)

player_button = tkinter.Button(button_frame, text ="PLAYER", command= deal_player)
player_button.grid(row= 0, column= 1)




#load cards
cards = []
load_images(cards)
print(cards)


# creste  anew deck of cards and shuffle them
deck =list(cards)
random.shuffle(deck)

# create the list to store the dealer's and player's hands

dealer_hand =[]
player_hand= []
deal_player()
dealer_hand.append(deal_card(dealercardframe))

















mainwindow.mainloop()