from src.data.read.read_warning_message import readWarningMessage

def getWarningMessageInfo():
    lines = readWarningMessage()
    if(lines == []):
        return
        
    firstMessage = lines[0].split('$')
    message = firstMessage[1]
    if(firstMessage[0] == '0'):
        color = (0.2,0.71,0.13,1)
    else:
        color = (0.96,0.74,0,1)

    for line in lines[1:]:
        color += line

    return {'message': message, 'color': color}

