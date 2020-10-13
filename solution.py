from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    mailserver = (mailserver,port)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')
    # Send HELO command and print server response.
    hellocommand = 'HELO Alice\r\n'
    clientSocket.send(hellocommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print("resonse 1 is " +recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfromcommand="MAIL FROM: <bc2968@nyu.edu>\r\n"
    clientSocket.send(mailfromcommand.encode())
    server_response=clientSocket.recv(1024).decode()
    #print("response from mail from command " + server_response)

    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptmsg="RCPT TO: bc2968@nyu.edu\r\n"
    clientSocket.send(rcptmsg.encode())
    recv2 = clientSocket.recv(1024)
    #print("response from recpt command" + recv2.decode())
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    datacommand='DATA\r\n'
    clientSocket.send(datacommand.encode())
    recv3= clientSocket.recv(1024).decode()
    #print("data command response: " +recv3)
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv4= clientSocket.recv(1024).decode()
    #print("after sending message body" + recv4)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitmsg="QUIT\r\n"
    clientSocket.send(quitmsg.encode())
    recv5= clientSocket.recv(1024).decode()
    #print(recv5)
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
