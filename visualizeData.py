import numpy as np
import pandas as pd

dict = {
		'days_watched': 1269615.800000005,
		'mean_score': 101966.43000000055,
		'watching': 229042,
		'completed': 4464985,
		'on_hold': 205727,
		'dropped': 438317,
		'plan_to_watch': 1787639,
		'total_entries': 7127692,
		'rewatched': 210902,
		'episodes_watched': 77089149
	}

df = pd.DataFrame ([dict])

print(df)