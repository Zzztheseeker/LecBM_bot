import telebot
from Video import Video
from Playlist import Playlist
import pickle

with open("coded_list.pkl", "rb") as pp:
    pl_list = pickle.load(pp)

with open("slang_dictionary.pkl", "rb") as sp:
    slang = pickle.load(sp)

token = '5349684609:AAE7SJYilWL1h-75ojIpMK0DTeBjYO6YS1k'
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 
                     'Я на связи. Я бот лектория ФБМФ. ' + 
                     'Для поиска кода напишите команду ' +
                     '/getvideo, для дополнительной информации введите /help')
    
    
    @bot.message_handler(commands = ['help'])
    def help(message):
        bot.send_message(message.chat.id, 'Для поиска видео напиши мне'+
                         ' команду /getvideo, после чего напиши мне предмет'+
                         ' и тему, которую хотелось бы разобрать. '+
                         'Я пришлю тебе все видеоролики, в котором была '+
                         'затронута данная тема с таймкодами, чтобы было '+
                         'удобнее готовиться.'+
                         'Если в поле ничего не ввести мы вернём либо все'+
                         'видео автора, либо будем искать по всем авторам в'+
                         ' записях. Удачи)')


    @bot.message_handler(commands=['getvideo'])
    def getvideo(message):
        mesg = bot.send_message(message.chat.id, 'Напиши мне фамиллию лектора или предмет курса для поиска:')
        bot.register_next_step_handler(mesg, choose_playlist)
        
        
    def choose_playlist(message):
        global fpl
        splt = message.text.lower().strip().strip('.').strip() #searched in playlist text
        cplt = [] #correct playlist text
        for i in splt.split():
            if i.strip(',') in slang:
                cplt.append(slang[i])
            else:   
                cplt.append(i.strip(','))
            
        flag = True
        fpl = set() #found playlist
            
        for i in pl_list:
            if ' '.join(cplt) in i.name:
                fpl.add(i)
                flag = False
                    
                    
        if flag:
            for i in cplt:
                for j in pl_list:
                    if i in j.name:
                        fpl.add(j)
                        flag = False
                            
        if flag:
            bot.send_message(message.chat.id, 'Не удалось найти, попробуй ещё раз...')
        else:
            mesg = bot.send_message(message.chat.id, 'Введите тему, которую хотелось бы разобрать:')
            bot.register_next_step_handler(mesg, send_video)
            
            
def send_video(message):  
    global fpl
    fv = set() #found videos
    flag2 = True
    sv = message.text.lower().strip().strip('.').strip() #search in videos
    csvt = [] #correct search video text
    
    for i in sv.split():
        if i.strip(',') in slang:
            csvt.append(slang[i])
        else:
            csvt.append(i.strip(','))
    
    for i in fpl:
        for j in i.videos:
            #bot.send_message(message.chat.id, j.desc)
            if ' '.join(csvt) in j.desc:
                fv.add(j)
                flag2 = False
                
    if flag2:
        for i in csvt:
            for j in fpl:
                for k in j.videos:
                    if i in k.desc:
                        fv.add(k)
                        flag2 = False                                
            
            
    if flag2:
        bot.send_message(message.chat.id, 'По вашему запросу ничего не найдено( Попробуйте ещё раз')
    
    else: 
        for i in fv:
            bot.send_message(message.chat.id, f'{i.nameU}\n\n{i.url}\n\n{i.descU}')




bot.polling(none_stop=True)