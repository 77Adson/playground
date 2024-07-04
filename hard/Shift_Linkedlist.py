class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    current = current2 = head
    count = 0
    k = k % count

    #Dla k=0 bez zmian
    if k == 0:
        return head
    else:
        #Ile elementow ma lista
        while current.next:
            count += 1
            current = current.next
        count += 1  #Dodatkowy element bo warunek ucinal 1

        current.next = head     #laczymy listy

        #Pentla bedzie wyznaczac gdzie przerwac 
        for i in range(count - k - 1):
            current2 = current2.next

        head = current2.next    #nowy poczatek
        current2.next = None    #nowy koniec
    return head
