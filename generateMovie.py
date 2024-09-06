import generateStory
import generatePic
import generateKeyword
import clipParagraph
import time
import clipmovie


story=generateStory.generate_sto()
paragraph=clipParagraph.clip_paragraph(story)
c_paragraphs=paragraph.content.split("\n\n")

    
pics=[]

for i in range(len(c_paragraphs)):
        keyword=generateKeyword.generate_keyword(c_paragraphs[i])
        generatePic.generate_pic(keyword.content,str(i))
        pics.append(str(i)+".png")

clipmovie.pics_to_video(pics,10)




        