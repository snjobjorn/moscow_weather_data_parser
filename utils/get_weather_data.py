from utils.clean_parsed_text import clean_parsed_text
from utils.parse_dates import parse_russian_dates


def get_weather_from_page(page_soup):
    cols_to_parse = [
        ".cell-forecast-time", ".cell-forecast-main", ".cell-forecast-temp", ".icon-wind",
        ".wind-amount", ".cell-forecast-press", ".cell-forecast-hum", ".cell-forecast-prec"
    ]
    result_cols = [
        "time_day", "sky", "temperature__celsius", "wind_direction", "wind_speed__mps",
        "atmospheric_pressure__mm_Hg", "humidity_%", "precipitation_mm"
    ]
    weather_blocks_mobile = page_soup.select(".table-forecast-mobile > .row-forecast-day-wrap")
    weather_blocks = page_soup.select(".table-forecast > .row-forecast-day-wrap")
    days = list()
    weather_data = list()
    result = dict()
    for block in weather_blocks_mobile:
        day_text = block.select_one(".forecast-day-name").text
        days.append(parse_russian_dates(day_text))
    for block in weather_blocks:
        weather_data_day = list()
        time_day_blocks = block.select(".row-forecast-time-of-day")
        for td_block in time_day_blocks:
            weather_data_time_day = list()
            for col in cols_to_parse:
                col_content = td_block.select_one(col)
                if col_content is None:
                    weather_data_time_day.append(None)
                    continue
                if col_content.name == "img":
                    weather_data_time_day.append(col_content.get("alt"))
                    continue
                weather_data_time_day.append(col_content.text)
            weather_data_day.append(weather_data_time_day)
        weather_data.append(weather_data_day)
    for i in range(len(days)):
        result[days[i]["date"]] = dict()
        result[days[i]["date"]]["weekday"] = days[i]["weekday"]
        result[days[i]["date"]]["data"] = {
            "night": dict(), "morning": dict(), "day": dict(), "evening": dict()
        }
        for time_day_data in weather_data[i]:
            match time_day_data[0]:
                case "ночь":
                    for j in range(len(result_cols)):
                        result[days[i]["date"]]["data"]["night"][result_cols[j]] = clean_parsed_text(time_day_data[j])
                case "утро":
                    for j in range(len(result_cols)):
                        result[days[i]["date"]]["data"]["morning"][result_cols[j]] = clean_parsed_text(time_day_data[j])
                case "день":
                    for j in range(len(result_cols)):
                        result[days[i]["date"]]["data"]["day"][result_cols[j]] = clean_parsed_text(time_day_data[j])
                case "вечер":
                    for j in range(len(result_cols)):
                        result[days[i]["date"]]["data"]["evening"][result_cols[j]] = clean_parsed_text(time_day_data[j])
    return result
