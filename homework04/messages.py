from collections import Counter
import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from typing import List, Tuple

from api import messages_get_history
from api_models import Message
import config


Dates = List[datetime.date]
Frequencies = List[int]


plotly.tools.set_credentials_file(
    username=config.PLOTLY_CONFIG['username'],
    api_key=config.PLOTLY_CONFIG['api_key']
)


def fromtimestamp(ts: int) -> datetime.date:
    return datetime.datetime.fromtimestamp(ts).date()


def count_dates_from_messages(messages: List[Message]) -> Tuple[Dates, Frequencies]:
    """ Получить список дат и их частот

    :param messages: список сообщений
    """
    dates = [fromtimestamp(c.get('date')) for c in messages.get('response').get('items')]
    count = list(dict(Counter(dates)).values())
    dates = list(set(dates))
    #freq = list(count.values())
    a = (dates, count)
    return a

def plotly_messages_freq(dates: Dates, freq: Frequencies) -> None:
    """ Построение графика с помощью Plot.ly

    :param date: список дат
    :param freq: число сообщений в соответствующую дату
    """
    trace0 = go.Scatter(
        x=dates,
        y=freq
    )
    data = [trace0]

    py.plot(data, filename = 'messages', auto_open=True)

plotly_messages_freq(count_dates_from_messages(messages_get_history(59027965, offset=0, count=200))[0], count_dates_from_messages(messages_get_history(59027965, offset=0, count=200))[1])