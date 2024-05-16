import datetime
import time

from utils import get_weather_data
from database import data_base_update, create_data_base
from config import CITIES


def main():
    create_data_base()
    while True:
        current_time = datetime.datetime.now()

        for city in CITIES:
            weather_data = get_weather_data(city)
            if weather_data:
                data_base_update(weather_data)

        time.sleep(3600)  # Сбор данных каждые 60 минут


if __name__ == "__main__":
    main()

