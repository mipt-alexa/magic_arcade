def read_message(who):  # who - кто сообщение вызывает
    # принимает значения: 2 (client), 1 (server) 
    """
    Отвечает за чтение сообщения
    """
    other = return_other(who)
    file_for_reading = open("{}_message.txt".format(other), 'r', encoding='utf-8')
    message = file_for_reading.readline()
    #file_for_reading.truncate()
    return message


def write_message(who, message):  # message - сообщение, которое необходимо передать клиенту, who - кто сообщение вызывает
    # принимает значения: 2 (client), 1 (server) 
    """
    Отвечает за создание сообщения
    """
    file_for_write = open("{}_message.txt".format(who),'a')
    file_for_write.write(str(message) + '\n')
    
    
def return_other(who):
    if who == "client":
        return "server"
    else:
        return "client"
