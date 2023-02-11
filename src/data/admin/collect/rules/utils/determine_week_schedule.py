import pdfplumber

def charsRepresentDays(chars, idx):
    if(chars[idx]['text'] == 'P' and \
       chars[idx + 1]['text'] == 'U' and \
       chars[idx + 2]['text'] == 'S' and \
       chars[idx + 3]['text'] == 'Č' and \
       chars[idx + 4]['text'] == 'P' and \
       chars[idx + 5]['text'] == 'S' and \
       chars[idx + 6]['text'] == 'N'):
        return True
    else:
        return False

def determineWeekSchedule(page, weekSchedule):
    # pdlplumber se gubi kada rect nije obojan u smislu
    # da izbacuje cudne atribute pozicija i velicina
    # program se pouzdava da se ne gubi kada je rect obojan
    weekScheduleDefault = True
    rects = page.rects
    chars = page.chars

    message0 = '0$Raspored službi uobičajen.\n'
    message1 = '1$Raspored službi neuobičajen.\n'
    nonDefaultDays = dict()
    days = ['Ponedjeljak', 'Utorak', 'Srijeda', \
            'Četvrtak', 'Petak', 'Subota', 'Nedjelja']
            
    fileW = open('data/data/warnings.txt', 'w', encoding='utf-8')
    for idx in range(len(chars)):
        if charsRepresentDays(chars, idx):
            for day in range(0,7):
                charTop = chars[idx + day]['top']
                charBottom = chars[idx + day]['bottom']
                charLeft = chars[idx + day]['x0']
                charRight = chars[idx + day]['x1']
                for rect in rects:
                    rectTop = rect['top']
                    rectBottom = rect['bottom']
                    rectLeft = rect['x0']
                    rectRight = rect['x1']
                    if(charTop > rectTop and charBottom < rectBottom and
                       charLeft > rectLeft and charRight < rectRight):
                        color = rect['non_stroking_color']
                        if color[1] >= 0.9 and color != (1,1,1): # green
                            nonDefaultDays[days[day]] = 'Subota'
                            weekSchedule[day] = 'St'
                            break
                        elif color[0] >= 0.9 and color != (1,1,1): # red
                            nonDefaultDays[days[day]] = 'Nedjelja'
                            weekSchedule[day] = 'Sn'
                            break
           
            if nonDefaultDays['Subota'] == 'Subota':
                del nonDefaultDays['Subota']
            if nonDefaultDays['Nedjelja'] == 'Nedjelja':
                del nonDefaultDays['Nedjelja']
            
            if not nonDefaultDays:
                fileW.write(message0)
            else:
                fileW.write(message1)
                for key,value in nonDefaultDays.items():
                    fileW.write('{0} se uzima kao {1}.\n'.format(key, value))
            fileW.close()
            return
