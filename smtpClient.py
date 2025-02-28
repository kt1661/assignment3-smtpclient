from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # This is the servers reponse to the client, acknowledging that it is ready to recieve mail - STATUS CODE 220
    recv = clientSocket.recv(1024).decode()
    # print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #     print('220 reply not received from server.')

    # Send HELO command and print server response.
    # This is the servers reponse to the client, acknowledging that it has recognized the client - STATUS CODE 250
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1) 
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # This is the servers reponse to the client, acknowledging that it has understood the mail from address - STATUS CODE 250
    mailFromCommand = 'MAIL FROM:<alice@stmpClient.com>\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2) 

    # Send RCPT TO command and handle server response.
    # This is the servers reponse to the client, acknowledging that it has understood the mail to address and confirms it can send emails to that address - STATUS CODE 250
    rcptCommand = 'RCPT TO:<alice2@smtpClient.com>\r\n'
    clientSocket.send(rcptCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3) 

    # Send DATA command and handle server response.
    # This is the servers reponse to the client, acknowledging that it has understood the client is about to send the email message data and is ready to recieve it - STATUS CODE 354
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4) 
    

    # Client sends message data.
    clientSocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    # This is the servers reponse to the client, acknowledging that the client had send the end of the message - STATUS CODE 250
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv5) 


    # Send QUIT command and handle server response.
    # This is the servers reponse to the client, acknowledging that the client had sent the whole message the quits the process - STATUS CODE 221
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv6)


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')