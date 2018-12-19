import datetime
from statistics import median
from typing import Optional

from api import get_friends
from api_models import User


def age_predict(user_id: int) -> Optional[float]:
    """ Наивный прогноз возраста по возрасту друзей

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: идентификатор пользователя
    :return: медианный возраст пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    
    friends = get_friends(user_id, 'bdate')
    bdates = [c.get('bdate') for c in friends.get('response').get('items')]
    fdates = []
    now = datetime.datetime.now()
    
    for date in bdates:
    	if date != None:
    	    if len(date) >= 8:
    		    d = date.split('.')
    		    da = datetime.datetime(int(d[2]), int(d[1]), int(d[0]))
    		    delta = now - da
    		    fdates.append(delta.days)
    return (median(fdates) / 365.25)   
