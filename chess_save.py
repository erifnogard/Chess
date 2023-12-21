#By: Ilhan Suljic
#TODO: Reverse column and row variable
#Make sure letterToNumber function returns number instead
#check if black piece on spot then remove it


import tkinter as tk

class ChessPiece():
    def __init__(self, piece, position, moved):
        self.piece = piece
        self.position = position
        self.moved = moved

def letterToNumber(letter):
    if letter == "A": 
        return "1"
    if letter == "B": 
        return "2"
    if letter == "C": 
        return "3"
    if letter == "D": 
        return "4"
    if letter == "E": 
        return "5"
    if letter == "F": 
        return "6"
    if letter == "G": 
        return "7"
    if letter == "H": 
        return "8"
    
def numberToLetter(number):
    if number == "1":
        return "A"
    if number == "2":
        return "B"
    if number == "3":
        return "C"
    if number == "4":
        return "D"
    if number == "5":
        return "E"
    if number == "6":
        return "F"
    if number == "7":
        return "G"
    if number == "8":
        return "H"
    
def resetBoard(selectedPiece, wChoiceC, origPos):
    selectedPiece.position = wChoiceC
    selectedPiece.moved = True
    spaces[wChoiceC] = selectedPiece.piece
    spaces[origPos] = " "
    board = f"""
  A B C D E F G H
  _ _ _ _ _ _ _ _
8|{spaces['A8']} {spaces['B8']} {spaces['C8']} {spaces['D8']} {spaces['E8']} {spaces['F8']} {spaces['G8']} {spaces['H8']}
7|{spaces['A7']} {spaces['B7']} {spaces['C7']} {spaces['D7']} {spaces['E7']} {spaces['F7']} {spaces['G7']} {spaces['H7']}
6|{spaces['A6']} {spaces['B6']} {spaces['C6']} {spaces['D6']} {spaces['E6']} {spaces['F6']} {spaces['G6']} {spaces['H6']}
5|{spaces['A5']} {spaces['B5']} {spaces['C5']} {spaces['D5']} {spaces['E5']} {spaces['F5']} {spaces['G5']} {spaces['H5']}
4|{spaces['A4']} {spaces['B4']} {spaces['C4']} {spaces['D4']} {spaces['E4']} {spaces['F4']} {spaces['G4']} {spaces['H4']}
3|{spaces['A3']} {spaces['B3']} {spaces['C3']} {spaces['D3']} {spaces['E3']} {spaces['F3']} {spaces['G3']} {spaces['H3']}
2|{spaces['A2']} {spaces['B2']} {spaces['C2']} {spaces['D2']} {spaces['E2']} {spaces['F2']} {spaces['G2']} {spaces['H2']}
1|{spaces['A1']} {spaces['B1']} {spaces['C1']} {spaces['D1']} {spaces['E1']} {spaces['F1']} {spaces['G1']} {spaces['H1']}

"""
    return board
    
chessBoard = []
capturedPieces = []

wP1 = ChessPiece("P", "A2", False)
wP2 = ChessPiece("P", "B2", False)
wP3 = ChessPiece("P", "C2", False)
wP4 = ChessPiece("P", "D2", False)
wP5 = ChessPiece("P", "E2", False)
wP6 = ChessPiece("P", "F2", False)
wP7 = ChessPiece("P", "G2", False)
wP8 = ChessPiece("P", "H2", False)
wH1 = ChessPiece("H", "B1", False)
wH2 = ChessPiece("H", "G1", False)
wB1 = ChessPiece("B", "C1", False)
wB2 = ChessPiece("B", "F1", False)
wR1 = ChessPiece("R", "A1", False)
wR2 = ChessPiece("R", "H1", False)
wK = ChessPiece("K", "E1", False)
wQ = ChessPiece("Q", "D1", False)

whitePieces = [wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8, wH1, wH2, wB1, wB2, wR1, wR2, wK, wQ]

bP1 = ChessPiece("P", "A7", False)
bP2 = ChessPiece("P", "B7", False)
bP3 = ChessPiece("P", "C7", False)
bP4 = ChessPiece("P", "D7", False)
bP5 = ChessPiece("P", "E7", False)
bP6 = ChessPiece("P", "F7", False)
bP7 = ChessPiece("P", "G7", False)
bP8 = ChessPiece("P", "H7", False)
bH1 = ChessPiece("H", "B8", False)
bH2 = ChessPiece("H", "G8", False)
bB1 = ChessPiece("B", "C8", False)
bB2 = ChessPiece("B", "F8", False)
bR1 = ChessPiece("R", "A8", False)
bR2 = ChessPiece("R", "H8", False)
bK = ChessPiece("K", "E8", False)
bQ = ChessPiece("Q", "D8", False)

blackPieces = [bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8, bH1, bH2, bB1, bB2, bR1, bR2, bK, bQ]

spaces = {
    "A1": wR1.piece, "B1": wH1.piece, "C1": wB1.piece, "D1": wQ.piece, "E1": wK.piece, "F1": wB2.piece, "G1": wH2.piece, "H1": wR2.piece,
    "A2": wP1.piece, "B2": wP2.piece, "C2": wP3.piece, "D2": wP4.piece, "E2": wP5.piece, "F2": wP6.piece, "G2": wP7.piece, "H2": wP8.piece,
    "A3": " ", "B3": " ", "C3": " ", "D3": " ", "E3": " ", "F3": " ", "G3": " ", "H3": " ",
    "A4": " ", "B4": " ", "C4": " ", "D4": " ", "E4": " ", "F4": " ", "G4": " ", "H4": " ",
    "A5": " ", "B5": " ", "C5": " ", "D5": " ", "E5": " ", "F5": " ", "G5": " ", "H5": " ",
    "A6": " ", "B6": " ", "C6": " ", "D6": " ", "E6": " ", "F6": " ", "G6": " ", "H6": " ",
    "A7": bP1.piece, "B7": bP2.piece, "C7": bP3.piece, "D7": bP4.piece, "E7": bP5.piece, "F7": bP6.piece, "G7": bP7.piece, "H7": bP8.piece,
    "A8": bR1.piece, "B8": bH1.piece, "C8": bB1.piece, "D8": bQ.piece, "E8": bK.piece, "F8": bB2.piece, "G8": bH2.piece, "H8": bR2.piece
    }

board = f"""
  A B C D E F G H
  _ _ _ _ _ _ _ _
8|{spaces['A8']} {spaces['B8']} {spaces['C8']} {spaces['D8']} {spaces['E8']} {spaces['F8']} {spaces['G8']} {spaces['H8']}
7|{spaces['A7']} {spaces['B7']} {spaces['C7']} {spaces['D7']} {spaces['E7']} {spaces['F7']} {spaces['G7']} {spaces['H7']}
6|{spaces['A6']} {spaces['B6']} {spaces['C6']} {spaces['D6']} {spaces['E6']} {spaces['F6']} {spaces['G6']} {spaces['H6']}
5|{spaces['A5']} {spaces['B5']} {spaces['C5']} {spaces['D5']} {spaces['E5']} {spaces['F5']} {spaces['G5']} {spaces['H5']}
4|{spaces['A4']} {spaces['B4']} {spaces['C4']} {spaces['D4']} {spaces['E4']} {spaces['F4']} {spaces['G4']} {spaces['H4']}
3|{spaces['A3']} {spaces['B3']} {spaces['C3']} {spaces['D3']} {spaces['E3']} {spaces['F3']} {spaces['G3']} {spaces['H3']}
2|{spaces['A2']} {spaces['B2']} {spaces['C2']} {spaces['D2']} {spaces['E2']} {spaces['F2']} {spaces['G2']} {spaces['H2']}
1|{spaces['A1']} {spaces['B1']} {spaces['C1']} {spaces['D1']} {spaces['E1']} {spaces['F1']} {spaces['G1']} {spaces['H1']}

"""
selectedPiece = ""
while True:
    blocker = 0
    print(board)
    try:
        wChoiceP = input("White: Enter the coordinates of the piece you want to move: ")
        if wChoiceP not in spaces:
            raise Exception()
        for i in whitePieces:
            if wChoiceP == i.position:
                selectedPiece = i
                origPos = i.position
                break
        else:
            print("No valid piece selected.")
            continue
    except Exception:
        print("Enter the coordinate in this form: E4")
        continue
    
    try:
        wChoiceC = input("Enter the coordinates of the place you want the piece to go to: ")
        for i in whitePieces:
            if i.position == wChoiceC:
                raise Exception()
    except Exception:
        print("You have another piece in that spot.")
        continue
    tempList = []
    for i in wChoiceC:
        tempList.append(i)
    wChoiceCRow = tempList[0]
    try:
        wChoiceCColumn = int(tempList[1])
    except ValueError:
        print("Enter the coordinate in this form: E4")
        continue
    tempList2 = []
    for i in origPos:
        tempList2.append(i)
    origPosRow = origPos[0]
    origPosColumn = int(origPos[1])

    if selectedPiece.piece == "P":
        if selectedPiece.moved:
            if origPosColumn - wChoiceCColumn != -1:
                print("Not valid pawn move. ")
                continue
        else:
            if origPosColumn - wChoiceCColumn != -1:
                if origPosColumn - wChoiceCColumn != -2:
                    print("Not valid pawn move. ")
                    continue
        if selectedPiece.moved:
            if wChoiceCRow != origPosRow:
                if spaces[wChoiceC] != "":
                    if int(letterToNumber(origPosRow)) - int(letterToNumber(wChoiceCRow)) != -1:
                        print("Not valid capture.")
                        continue
                else:
                    print("No piece to capture.")
                    continue
        else:
            if wChoiceCRow != origPosRow:
                print("Not a valid pawn move.")
                continue
        board = resetBoard(selectedPiece, wChoiceC, origPos)
    possible_squares = []
    foundBlocker = False
    if selectedPiece.piece == "R":
        if wChoiceCColumn != origPosColumn and wChoiceCRow != origPosRow:
            print("Not valid rook move.")
            break
        for i in range(4):
            foundBlackBlocker = False
            for j in range(8):
                try:
                    if i == 0:
                        if origPosColumn+j > 8:
                            foundBlackBlocker = False
                            break
                        for l in whitePieces:
                            if l.position == origPosRow + str(origPosColumn+j):
                                if origPosRow + str(origPosColumn+j) != origPos:
                                    foundBlackBlocker = False
                                    foundBlocker = True
                                    break
                        if foundBlocker:
                            foundBlocker = False
                            break
                        if spaces[origPosRow + str(origPosColumn+j)] == " ":
                            possible_squares.append(origPosRow + str(origPosColumn+j))
                        if foundBlackBlocker == False:
                            for k in blackPieces:
                                if k.position == origPosRow + str(origPosColumn+j):
                                    print(j)
                                    blackPieces.remove(k)
                                    possible_squares.append(origPosRow + str(origPosColumn+j))
                                    foundBlackBlocker = True
                    if i == 1:
                        if origPosColumn-j <= 0:
                            foundBlackBlocker = False
                            break
                        for l in whitePieces:
                            if l.position == origPosRow + str(origPosColumn-j):
                                if origPosRow + str(origPosColumn-j) != origPos:
                                    foundBlackBlocker = False
                                    foundBlocker = True
                                    break
                        if foundBlocker:
                            foundBlocker = False
                            break
                        if spaces[origPosRow + str(origPosColumn-j)] == " ":
                            possible_squares.append(origPosRow + str(origPosColumn-j))
                        if foundBlackBlocker == False:
                            for k in blackPieces:
                                if k.position == origPosRow + str(origPosColumn-j):
                                    blackPieces.remove(k)
                                    possible_squares.append(origPosRow + str(origPosColumn-j))
                                    foundBlackBlocker = True
                    if i == 2:
                        if int(letterToNumber(origPosRow))-j <= 0:
                            foundBlackBlocker = False
                            break
                        for l in whitePieces:
                            if l.position == numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn):
                                if numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn) != origPos:
                                    foundBlackBlocker = False
                                    foundBlocker = True
                                    break
                        if foundBlocker:
                            foundBlocker = False
                            break
                        if spaces[numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn)] == " ":
                            possible_squares.append(numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn))
                        if foundBlackBlocker == False:
                            for k in blackPieces:
                                if k.position == numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn):
                                    blackPieces.remove(k)
                                    possible_squares.append(numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn))
                                    foundBlackBlocker = True
                    if i == 3:
                        if int(letterToNumber(origPosRow))+j > 8:
                            foundBlackBlocker = False
                            break
                        for l in whitePieces:
                            if l.position == numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn):
                                if numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn) != origPos:
                                    foundBlackBlocker = False
                                    foundBlocker = True
                                    break
                        if foundBlocker:
                            foundBlocker = False
                            break
                        if spaces[numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn)] == " ":
                            possible_squares.append(numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn))
                        if foundBlackBlocker == False:
                            for k in blackPieces:
                                if k.position == numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn):
                                    blackPieces.remove(k)
                                    possible_squares.append(numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn))
                                    foundBlackBlocker = True
                except TypeError or KeyError:
                    foundBlackBlocker = False
                    break
            else:
                foundBlocker = False
                foundBlackBlocker = False
        if wChoiceC in possible_squares:
            board = resetBoard(selectedPiece, wChoiceC, origPos)
        else:
            print("Not valid rook move.")
            continue
    if selectedPiece.piece == "B":
        if wChoiceCRow == origPosRow:
            print(wChoiceCRow, origPosRow)
            print("Not a valid bishop move. 1")
            continue
        if wChoiceCColumn == origPosColumn:
            print("Not a valid bishop move. 2")
            continue
        possible_squares = []
        foundBlocker = False
        foundBlackBlocker = False
        for i in range(4):
            foundBlackBlocker = False
            for j in range(8):
                try:
                    if i == 0:
                        if origPosColumn+j > 8:
                            foundBlackBlocker = False
                            break
                        for l in whitePieces:
                            if l.position == numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn+j):
                                if numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn+j) != origPos:
                                    foundBlackBlocker = False
                                    foundBlocker = True
                        if foundBlocker:
                            foundBlocker = False
                            break
                        if spaces[numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn+j)] == " ":
                            possible_squares.append(numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn+j))
                        if foundBlackBlocker == False:
                            for k in blackPieces:
                                if k.position == numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn+j):
                                    blackPieces.remove(k)
                                    possible_squares.append(numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn+j))
                                    foundBlackBlocker = True
                    elif i == 1:
                        if origPosColumn+j > 8:
                            foundBlackBlocker = False
                            break
                        for l in whitePieces:
                            if l.position == numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn+j):
                                if numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn+j) != origPos:
                                    foundBlackBlocker = False
                                    foundBlocker = True
                        if foundBlocker:
                            foundBlocker = False
                            break
                        if spaces[numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn+j)] == " ":
                            possible_squares.append(numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn+j))
                        if foundBlackBlocker == False:
                            for k in blackPieces:
                                if k.position == numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn+j):
                                    blackPieces.remove(k)
                                    possible_squares.append(numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn+j))
                                    foundBlackBlocker = True
                    elif i == 2:
                        if origPosColumn-j <= 0:
                            foundBlackBlocker = False
                            break
                        for l in whitePieces:
                            if l.position == numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn-j):
                                if numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn-j) != origPos:
                                    foundBlackBlocker = False
                                    foundBlocker = True
                        if foundBlocker:
                            foundBlocker = False
                            break
                        if spaces[numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn-j)] == " ":
                            possible_squares.append(numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn-j))
                        if foundBlackBlocker == False:
                            for k in blackPieces:
                                if k.position == numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn-j):
                                    blackPieces.remove(k)
                                    possible_squares.append(numberToLetter(str(int(letterToNumber(origPosRow))+j)) + str(origPosColumn-j))
                                    foundBlackBlocker = True
                    elif i == 3:
                        if origPosColumn-j <= 0:
                            foundBlackBlocker = False
                            break
                        for l in whitePieces:
                            if l.position == numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn-j):
                                if numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn-j) != origPos:
                                    foundBlackBlocker = False
                                    foundBlocker = True
                        if foundBlocker:
                            foundBlocker = False
                            break
                        if spaces[numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn-j)] == " ":
                            possible_squares.append(numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn-j))
                        if foundBlackBlocker == False:
                            for k in blackPieces:
                                if k.position == numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn-j):
                                    blackPieces.remove(k)
                                    possible_squares.append(numberToLetter(str(int(letterToNumber(origPosRow))-j)) + str(origPosColumn-j))
                                    foundBlackBlocker = True
                except TypeError or KeyError:
                    foundBlackBlocker = False
                    break
            else:
                foundBlocker = False
                foundBlackBlocker = False
        if wChoiceC in possible_squares:
            board = resetBoard(selectedPiece, wChoiceC, origPos)
        else:
            print("Not valid bishop move.")
            continue

                
    if selectedPiece.piece == "K":
        if selectedPiece.moved:
            possible_squares = []
            if abs(wChoiceCColumn - origPosColumn) >= 2:
                print("Not valid king move.")
                continue
            if abs(int(letterToNumber(wChoiceCRow)) - int(letterToNumber(origPosRow))) >= 2:
                print("Not valid king move.")
                continue
            board = resetBoard(selectedPiece, wChoiceC, origPos)
        else:
            possible_squares = []
            if abs(wChoiceCColumn - origPosColumn) >= 2:
                print("Not valid king move.")
                continue
            if abs(int(letterToNumber(wChoiceCRow)) - int(letterToNumber(origPosRow))) >= 2:
                print("Not valid king move.")
                continue
            board = resetBoard(selectedPiece, wChoiceC, origPos)

    if selectedPiece.piece == "Q":
        pass
    if selectedPiece.piece == "H":
        if selectedPiece.moved:
            if abs(wChoiceCColumn - origPosColumn) >= 3:
                print("Not valid knight move.")
                continue
            if abs(int(letterToNumber(wChoiceCRow)) - int(letterToNumber(origPosRow))) >= 3:
                print("Not valid knight move.")
                continue
            if abs(wChoiceCColumn - origPosColumn) == 1:
                if abs(int(letterToNumber(wChoiceCRow)) - int(letterToNumber(origPosRow))) == 2:
                    board = resetBoard(selectedPiece, wChoiceC, origPos)
                else:
                    print("Not valid knight move.")
            else:
                print("Not valid knight move.")
            if abs(wChoiceCColumn - origPosColumn) == 2:
                if abs(int(letterToNumber(wChoiceCRow)) - int(letterToNumber(origPosRow))) == 1:
                    board = resetBoard(selectedPiece, wChoiceC, origPos)
                else:
                    print("Not valid knight move.")
                    continue
            else:
                print("Not valid knight move.")
                continue
            
        else:
            if abs(wChoiceCColumn - origPosColumn) >= 3:
                print("Not valid knight move.")
                continue
            if abs(int(letterToNumber(wChoiceCRow)) - int(letterToNumber(origPosRow))) >= 3:
                print("Not valid knight move.")
                continue
            if abs(wChoiceCColumn - origPosColumn) == 1:
                if abs(int(letterToNumber(wChoiceCRow)) - int(letterToNumber(origPosRow))) == 2:
                    board = resetBoard(selectedPiece, wChoiceC, origPos)
                    continue
            if abs(wChoiceCColumn - origPosColumn) == 2:
                if abs(int(letterToNumber(wChoiceCRow)) - int(letterToNumber(origPosRow))) == 1:
                    board = resetBoard(selectedPiece, wChoiceC, origPos)
                    continue
                else:
                    print("Not valid knight move.")
                    continue
            else:
                print("Not valid knight move.")
                continue
            


        
                
    
