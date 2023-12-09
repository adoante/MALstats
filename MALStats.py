import requests
import time

File_object = open(r"mal_reddit_user_list.txt", "r")
user_list = File_object.readlines()
File_object.close()

counts = {'days_watched': 0, 'mean_score': 0, 'watching': 0, 'completed': 0, 'on_hold': 0, 'dropped': 0, 'plan_to_watch': 0, 'total_entries': 0, 'rewatched': 0, 'episodes_watched': 0}

days_watched = []
mean_score = []
watching = [] 
completed = []
on_hold = []
dropped = []
plan_to_watch = []
total_entries = []
rewatched = []
episodes_watched = []

cnt = 0;

for users in user_list:
	api_url = "https://api.jikan.moe/v4/users/" +  users.strip() +  "/statistics"

	print(str(cnt) + ": " + api_url)

	response = requests.get(api_url)
	data = response.json()
	
	try:
		anime_data = data['data']['anime']

		days_watched.append(anime_data['days_watched'])
		mean_score.append(anime_data['mean_score'])
		watching.append(anime_data['watching'])
		completed.append(anime_data['completed'])
		on_hold.append(anime_data['on_hold'])
		dropped.append(anime_data['dropped'])
		plan_to_watch.append(anime_data['plan_to_watch'])
		total_entries.append(anime_data['total_entries'])
		rewatched.append(anime_data['rewatched'])
		episodes_watched.append(anime_data['episodes_watched'])

		cnt = cnt+1
	except:
		print ("Bad Status: " + str(response.status_code) + ", User: " + users)
		continue

	time.sleep(0.5)

File_object = open(r"all_data_formated.txt", "a")

File_object.write(days_watched)
File_object.write(mean_score)
File_object.write(watching)
File_object.write(completed)
File_object.write(on_hold)
File_object.write(dropped)
File_object.write(plan_to_watch)
File_object.write(total_entries)
File_object.write(rewatched)
File_object.write(episodes_watched)

File_object.close()