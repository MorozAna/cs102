import requests
import config
import telebot
from bs4 import BeautifulSoup
import datetime


bot = telebot.TeleBot(config.access_token)
week = {1:'Понедельник', 2:'Вторник', 3:'Среда', 4:'Четверг', 5:'Пятница', 6:'Суббота', 7:'Воскресенье'}


def get_page(group, week=''):
    if week:
        week = str(week) + '/'
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain=config.domain,
        week=week,
        group=group)
    response = requests.get(url)
    web_page = response.text
    return web_page


def parse_schedule_for_a_day(web_page, week_day):
    soup = BeautifulSoup(web_page, "html5lib")
    
    # Получаем таблицу с расписанием на понедельник
    schedule_table = soup.find("table", attrs={"id": "{}day".format(week_day)})

    # Время проведения занятий
    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text for room in locations_list]

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
    lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]

    return times_list, locations_list, lessons_list


'''@bot.message_handler(commands=['monday'])
def get_monday(message):
    """ Получить расписание на понедельник """
    _, group = message.text.split()
    web_page = get_page(group)
    times_lst, locations_lst, lessons_lst = \
        parse_schedule_for_a_day(web_page)
    resp = ''
    for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
        resp += '<b>{}</b>, {}, {}\n'.format(time, location, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')'''


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
def get_schedule(message):
    """ Получить расписание на указанный день """
    mes = str(message)
    if 'monday' in mes:
        week_day = 1
    if 'tuesday' in mes:
        week_day = 2
    if 'wednesday' in mes:
        week_day = 3
    if 'thursday' in mes:
        week_day = 4
    if 'friday' in mes:
        week_day = 5
    if 'saturday' in mes:
        week_day = 6
    if 'sunday' in mes:
        week_day = 7
    _, group = message.text.split()
    web_page = get_page(group)
    times_lst, locations_lst, lessons_lst = \
        parse_schedule_for_a_day(web_page, week_day)
    resp = ''
    for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
        resp += '<b>{}</b>, {}, {}\n'.format(time, location, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['near'])
def get_near_lesson(message):
    """ Получить ближайшее занятие """
    # PUT YOUR CODE HERE
    pass


@bot.message_handler(commands=['tommorow'])
def get_tommorow(message):
    """ Получить расписание на следующий день """
    _, group = message.text.split()
    today = datetime.datetime.now()
    tommorow = today
    if (today.weekday() == 5):
        tommorow += datetime.timedelta(days=2)
    else:
        tommorow += datetime.timedelta(days=1)

    week_number = datetime.date(tommorow.year, tommorow.month, tommorow.day).isocalendar()[1]
    if week_number % 2 == 0:
        week_number = 1
    else:
        week_number = 2

    tommorow_day = tommorow.weekday()
    web_page = get_page(group, week_number)
    times_lst, locations_lst, lessons_lst = \
        parse_schedule_for_a_day(web_page, tommorow_day + 1)
    resp = ''
    for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
        resp += '<b>{}</b>, {}, {}\n'.format(time, location, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['all'])
def get_all_schedule(message):
    """ Получить расписание на всю неделю для указанной группы """
    week_day = 0
    resp = ''
    _, group = message.text.split()
    web_page = get_page(group)

    for d in range(6):
        week_day += 1
        times_lst, locations_lst, lessons_lst = \
            parse_schedule_for_a_day(web_page, week_day)
        
        for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
            resp += '<b>{}\n {}</b> {} {}\n'.format(week[week_day], time, location, lession)
    
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


if __name__ == '__main__':
    bot.polling(none_stop=True)

