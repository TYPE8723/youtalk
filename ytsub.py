from youtube_transcript_api import YouTubeTranscriptApi
import re

class YtScrapper:
    def __init__(self,url):
        self.url = url
         
    def get_id(self):
        try:
            pattern = r'(?:v=|\/|v\/|embed\/|youtu.be\/|\/v\/|\/e\/|watch\?v=)([a-zA-Z0-9_-]{11})'
            video_id = re.search(pattern,self.url).group(1)
            return video_id
        except:
            #dosent match the URL
            return False

    def get_captions(self,vid):
        try:
            titles = YouTubeTranscriptApi.get_transcript(vid)
            video_content = ''
            for verse in titles:
                video_content = video_content+' '+verse['text'].replace('\n',' ')
            return video_content
        except:
            return False
    

# obj = YtScrapper('')
# video_id=obj.get_id()
# if video_id is not False:
#     print(obj.get_captions(video_id))
# else:
#     print("Invaid video id")