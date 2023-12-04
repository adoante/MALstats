getCompletedAnime().catch(error => {
	console.log(error);
	console.error(error);
});

async function getCompletedAnime(userName) {
	const response = await fetch("https://api.jikan.moe/v4/users/" + userName + "/statistics");
	const data = await response.json();
	//console.log(userName, data.data.anime.completed);
	return (data.data.anime.completed);
}

  (async () => {
	const response = await fetch("mal_reddit_user_list.txt");
	const data = await response.text();
	const lines = data.split("\n");

	let cnt = 3073354;
	for (let i = 9671; i < lines.length; i++) {
		const storedPromise = getCompletedAnime(lines[i]);
		storedPromise.then(function(result) {
			cnt = cnt + result;
		})
		await new Promise(r => setTimeout(r, 1500));
		
		console.log("Users: " + i + ", Completed Anime: " + cnt + ", AVG Completed Anime: " + Math.floor(cnt/i));
	}

  })();