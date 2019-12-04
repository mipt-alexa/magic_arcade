def read_message(who):  # who - кто сообщение вызывает
    # принимает значения: "client", "server" 
    """
    Отвечает за чтение сообщения
    """
    other = return_other(who)
    file_for_reading = open("{}_message.txt".format(other),'r',encoding = 'utf-8')
    message = file_for_reading.readlines()
    clining = open("{}_message.txt".format(other),'w')
    file_for_reading.close()
    clining.close()
    return message


def write_message(who, message):  # message - сообщение, которое необходимо передать клиенту, who - кто сообщение вызывает
    # принимает значения: "client", "server" 
    """
    Отвечает за создание сообщения
    """
    file_for_write = open("{}_message.txt".format(who),'a')
    file_for_write.write(str(message) + '\n')
    file_for_write.close
    

def return_other(who):
    if who == "client":
        return "server"
    else:
        return "client"
