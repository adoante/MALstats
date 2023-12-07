import requests
import time

File_object = open(r"mal_reddit_user_list.txt", "r")
user_list = File_object.readlines()
File_object.close()

counts = {'days_watched': 0, 'mean_score': 0, 'watching': 0, 'completed': 0, 'on_hold': 0, 'dropped': 0, 'plan_to_watch': 0, 'total_entries': 0, 'rewatched': 0, 'episodes_watched': 0}

# fail one
counts = {'days_watched': 98835.19999999991, 'mean_score': 8008.869999999998, 'watching': 15668, 'completed': 343050, 'on_hold': 15298, 'dropped': 29185, 'plan_to_watch': 131376, 'total_entries': 534577, 'rewatched': 16278, 'episodes_watched': 5996659}

#fail two
counts = {'days_watched': 580909.4999999993, 'mean_score': 46744.1700000001, 'watching': 102323, 'completed': 2026789, 'on_hold': 93141, 'dropped': 177821, 'plan_to_watch': 780179, 'total_entries': 3180253, 'rewatched': 94278, 'episodes_watched': 35169050}

cnt = 0;

for users in user_list:
	api_url = "https://api.jikan.moe/v4/users/" +  users.strip() +  "/statistics"

	print(str(cnt) + ": " + api_url)

	response = requests.get(api_url)
	data = response.json()
	
	try:
		anime_data = data['data']['anime']

		File_object = open(r"all_data.txt", "a")

		File_object.write(str(cnt) + ": " + users.strip() + ": ")

		File_object.write(str(anime_data) + "\n")
		File_object.close()

		counts['days_watched'] = counts['days_watched'] + anime_data['days_watched']
		counts['mean_score'] = counts['mean_score'] + anime_data['mean_score']
		counts['watching'] = counts['watching'] + anime_data['watching']
		counts['completed'] = counts['completed'] + anime_data['completed']
		counts['on_hold'] = counts['on_hold'] + anime_data['on_hold']
		counts['dropped'] = counts['dropped'] + anime_data['dropped']
		counts['plan_to_watch'] = counts['plan_to_watch'] + anime_data['plan_to_watch']
		counts['total_entries'] = counts['total_entries'] + anime_data['total_entries']
		counts['rewatched'] = counts['rewatched'] + anime_data['rewatched']
		counts['episodes_watched'] = counts['episodes_watched'] + anime_data['episodes_watched']

		file_obj = open(r"data_counts.txt", "w")
		file_obj.write(str(counts))
		file_obj.close()

		cnt = cnt+1
	except:
		print ("Bad Status: " + str(response.status_code) + ", User: " + users)
		continue

	time.sleep(0.5)

