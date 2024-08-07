from datetime import timedelta
from tire_info import tire_info

def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    minutes, seconds = divmod(total_seconds, 60)
    milliseconds = td.microseconds // 1000
    return f"{minutes:02}:{seconds:02}.{milliseconds:03}"


def deg():
    lap_time = tire_info["Belgium"]["soft"]["lap_times"][0]
    print(lap_time)

def deg_laptimes(tire_choice, deg):
    # laps
    laps = 71

    # list to hold laps times
    lap_times = []

    # calculate a new lap time with deg factored in
    def calc_laptime_w_deg(tire, tire_deg):
        new_lap_time = tire + tire_deg
        return new_lap_time

    # how many total seconds the tire is degraded by (linearly)
    current_deg = timedelta(milliseconds=0)
    i = 1
    while i <= laps:
        current_deg += deg  # Increase the degradation for each lap
        lap_time = calc_laptime_w_deg(tire_choice, current_deg)
        lap_times.append({f"lap {i}": lap_time}) # append lap and time to list as value pair
        i += 1

    for lap in lap_times:
        for lap_num, lap_time in lap.items():
            print(f"{lap_num}: {format_timedelta(lap_time)}")

# Example usage
# deg_laptimes(timedelta(minutes=1, seconds=52, milliseconds=800), timedelta(milliseconds=400))

deg()