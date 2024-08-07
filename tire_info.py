from datetime import timedelta

# data for each tire from specifc country, data taken from fake practice session
tire_info = {
    "Belgium": {
        "soft": {
            "lap_times": [
                {"lap 1": timedelta(minutes=1, seconds=42, milliseconds=500)},
                {"lap 2": timedelta(minutes=1, seconds=42, milliseconds=700)},
                {"lap 3": timedelta(minutes=1, seconds=43, milliseconds=0)},
                {"lap 4": timedelta(minutes=1, seconds=43, milliseconds=200)},
                {"lap 5": timedelta(minutes=1, seconds=43, milliseconds=300)}
            ]
        },
        "medium": {
            "lap_times": [
                {"lap 1": timedelta(minutes=1, seconds=44, milliseconds=0)},
                {"lap 2": timedelta(minutes=1, seconds=44, milliseconds=200)},
                {"lap 3": timedelta(minutes=1, seconds=44, milliseconds=400)},
                {"lap 4": timedelta(minutes=1, seconds=44, milliseconds=600)},
                {"lap 5": timedelta(minutes=1, seconds=44, milliseconds=800)}
            ]
        },
        "hard": {
            "lap_times": [
                {"lap 1": timedelta(minutes=1, seconds=45, milliseconds=0)},
                {"lap 2": timedelta(minutes=1, seconds=45, milliseconds=200)},
                {"lap 3": timedelta(minutes=1, seconds=45, milliseconds=400)},
                {"lap 4": timedelta(minutes=1, seconds=45, milliseconds=600)},
                {"lap 5": timedelta(minutes=1, seconds=45, milliseconds=800)}
            ]
        }
    }
}