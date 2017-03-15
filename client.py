#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Σε αυτό το παράδειγμα δημιουργούμε τη σύνδεση του Client στο localhost και σε ένα καθορισμένο port(θύρα),
# τα δεδομένα στέλνονται στον Server, στη συνέχεια τα ληφθέντα δεδομένα γράφονται στο standard out. 
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Εισαγωγή απαιτούμενων βιβλιοθηκών, (libraries).
#-----------------------------------------------------------------------------
# Aπαιτείται η χρήση του socket library.
import socket


#-----------------------------------------------------------------------------
# Το κύριο πρόγραμμα.
#-----------------------------------------------------------------------------

# Δημιουργούμε ένα νέο socket και καθορίζουμε με ποιά host και port θα συνδέεται.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 80

# Σύνδεση με host και port.
sock.connect((host, port))

# Αποστολή δεδομένων στον server.
send = "Sending some data..."
print("Sending -> %s")% (send)
sock.send(send)

# Λήψη δεδομένων από τον server.Η έξοδος αυτών γίνεται στο standard out.
data = sock.recv(1024)
print("Received -> %s")% (data)
