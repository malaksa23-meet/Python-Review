def create_youtube_video(title,description):
	dict1 ={"title":title , "description": description,"likes":0 ,"dislikes":0,"comments":{}}
	return dict1


def like(dict1):
	if "likes" in dict1:
		dict1["likes"] += 1 
	return dict1 


def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username] = comment_text
	return youtubevideo 


dict2 = create_youtube_video("Bnana cake","plaplapal")
for i in range (495):
	like(dict2)
print(dict2)


dict2=dislikes(dicts)






