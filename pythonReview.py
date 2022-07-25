def create_youtube_video(title,description,hashtag ):
	dict1 ={"title":title , "description": description,"likes":0 ,"dislikes":0,"comments":{},"hashtag":hashtag}
	return dict1


def like(dict1):
	if "likes" in dict1:
		dict1["likes"] += 1 
	return dict1 

def dislike(dict1):
	if "dislikes" in dict1:
		dict1["dislikes"] += 1 
	return dict1 


def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username] = comment_text
	return youtubevideo 


dict2 = create_youtube_video("Bnana cake","plaplapal",["a1","a2","a3","a4","a5"])
dict3 = create_youtube_video("Bnana cake","plaplapal",["a0","a2","a3","a8","a5"])
dict2= like(dict2)
dict2 = dislike(dict2)
dict2= add_comment(dict2, "username", "comment") 




for i in range (495):
	like(dict2)
print(dict2)

def similarity_to_video(vid1,vid2):
	x=0

	for i in vid1["hashtag"]:
		for k in vid2["hashtag"]:
			if (i==k):
				x+=20 
	print ("They are mach " + str(x) +"%" )
	return x   

vids = similarity_to_video(dict2,dict3)
