import clipmovie

pics=[]

for i in range(8):

        pics.append(str(i)+".png")

clipmovie.pics_to_video(pics,10)