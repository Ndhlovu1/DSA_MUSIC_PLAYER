from platform import node

"""
STUDENT NAMES

218122187 - Tinomudaishe Ndhlovu
221026916 - Kelvin Gora
220076618 - Tashinga Mataranyika
222048212 - Nathan Diambomba


"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 


class playlist_Items:
    def __init__(self):
        self.head = None
        self.tail = None

    #ADD SONGS TO THE FILE
    def push(self, newSong):
        newSong = Node(newSong)
        newSong.next = self.head
        if self.head is not None:
            self.head.prev = newSong
        self.head = newSong 

    #ADDED ITEMS FOR SEARCH
    def pushSearch(self, song):
        newSong = Node(song)
        if (self.head == None):
            self.head = self.tail = newSong
            self.head.previous = None
            self.tail.next = None

        else:
            self.tail.next = newSong
            newSong.previous = self.tail
            self.tail = newSong
            self.tail.next = None

    #PRINT ITEMS SEARCHED
    def print_Searched_Item(self):
        current = self.head
        if self.head == None:
            print("NO SONGS")
            return
        print("ITEMS SAVED ARE :\n")
        while current != None:
            print(current.data)
            current = current.next

    #SEARCH FOR AN ELEMENT SAVED
    def searchSong(self, seachSong):
        item = 1
        flag_value = False
        current = self.head

        if self.head == None:
            print("Empty Playlist")
            return
        while current !=None :
            if current.data == seachSong:
                flag_value = True 
                break
            current = current.next
            item = item + 1

        if flag_value :
            print("SONG FOUND!")
            print("Position : " + item )
        else:
            print("Song isn't found in the list")
        
    #ADD ITEMS TO THE END OF THE EXISTING LIST
    def append(self, new_Song):
        new_Song = Node(new_Song)
        new_Song.next = None

        if self.head is None:
            new_Song.prev = None
            self.head = new_Song
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = new_Song
        new_Song.prev = last
        return

    #DELETE THE ITEM IN THE LIST
    def deleteSong(self, del_song):
        firstSong = self.head
        
        if (firstSong is not None):
            if (firstSong.data == del_song):
                self.head = firstSong.next
                firstSong = None
                return
            
        while (firstSong is not None):
            if firstSong.data == del_song:
                break
            prev = firstSong
            firstSong = firstSong.next

        if firstSong == None :
            print("Not Found")
            return
        
        prev.next = firstSong.next
        firstSong = None

    


  
    #SHOW DELETED ITEMS LEFT LIST 
    def printSongsLeft(self):
        print("SONGS LEFT")
        val = self.head
        while val:    
            print(val.data)
            val = val.next



    #VIEW NEW LIST OF ADDED SONGS
    def appendedSongs(self, song):
        while (song is not None):
            print(song.data)
            last = song
            song = song.next


    #Show the songs in the linked list
    def listSongsDoubly(self, pos):
        while (pos is not None):
            print(pos.data),
            last = pos
            pos = pos.next

    #The Circular Linked List
    def playSongsCircular(self):
        top = self.head
        while(top):
            print("TOP",top.data)
            top = top.next

    
    
## ------------------------------------------- ##
#       UNCOMMENT TO TEST EACH CASE SCENARIO    #   
## ------------------------------------------- ##


# d_list = playlist_Items()

# d_list.push(11)
# d_list.push(8)
# d_list.push(62)

# d_list.playSongsCircular()
#print(" ---- SUCCESSFULL ADDITION ---- ")
# d_list.listSongsDoubly(d_list.head)

"""
TEST FOR THE ADDING OF NEW SONGS
"""
# d_list.append(9)
# d_list.append(45)
#print(" ---- SUCCESSFULL ADDING ON TOP OF EXISTSING LIST ---- ")
# d_list.appendedSongs(d_list.head)

"""
TEST FOR THE DELETING OF NEW SONGS
"""
# d_list.deleteSong(8)

#print(" ---- SUCCESSFULL DELETED ---- ")
# d_list.printSongsLeft()
        
"""
TEST FOR THE SEARCHING OF NEW SONGS
"""
# d_list.pushSearch(11)
# d_list.pushSearch(8)
# d_list.pushSearch(62)
# d_list.pushSearch(32)
# d_list.pushSearch(44)

# #Print the Values
#print(" ---- SUCCESSFULL SEARCH ---- ")
# #Search
# d_list.searchSong(8)
# d_list.searchSong(44)


