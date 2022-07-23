
from itertools import count
import os
import ffmpeg
from pprint import pprint

class Converter:
    def __init__(self):
        self.ffmpeg = 'C:/ffmpeg/bin/ffmpeg.exe'

    def convert_to_mp4(file):
        name, ext = os.path.splitext(file)
        out_name = name + ".mp4"
        print("Finished converting {}".format(file))

        util_path = 'C:/ffmpeg/bin/ffmpeg.exe'

        '''
        двухполосный видео в mp4 : убрал ( -vtag xvid ) - возможно не будет работать на тв 
        Вроде лучший вариант для использования:
        ffmpeg -y -i "C:\\phytonProjects\\phytonEducation\\useful\\su.s05e01e02.mkv" -c:v libx264 -b:v 5948k -pass 1 -an -f mp4  NULL 

        ffmpeg -y -i "C:\\phytonProjects\\phytonEducation\\useful\\su.s05e01e02.mkv" -c:v libx264 -b:v 5948k -pass 2 -c:a aac -b:a 192k -movflags +faststart output.mp4


        без потери качества todo: проверить AAC для аудио и x264 для видео 
        подойдет для скорости
        ffmpeg -i "C:\\phytonProjects\\phytonEducation\\useful\\su.s05e01e02.mkv" -vcodec copy -acodec copy -movflags +faststart output.mp4

        Копия видео + конвертация аудио в web поддержку: проверить AAC and h264
        ffmpeg -i "C:\\phytonProjects\\phytonEducation\\useful\\video\\su.s05e01e02.mkv" -vcodec copy -acodec aac -movflags +faststart output.mp4

        Использование разных дорожек:
        ffmpeg -i "C:\\phytonProjects\\phytonEducation\\useful\\video\\su.s05e01e02.mkv" -map 0:0 -map 0:1 -c:v:0 copy -c:a:1 aac -b:a 320k -movflags +faststart output.mp4
        ffmpeg -i "C:\\phytonProjects\\phytonEducation\\useful\\video\\su.s05e01e02.mkv" -map 0:0 -map 0:1 -map 0:2 -c:v:0 copy -c:a:1 aac -b:a 320k -c:a:2 aac -b:a 92k -movflags +faststart output.mp4

        ffmpeg -y -i "C:\\phytonProjects\\phytonEducation\\useful\\video\\su.s05e01e02.mkv" -c:v libx264 -b:v 5948k -pass 1 -an -f mp4  NULL 
        ffmpeg -y -i "C:\\phytonProjects\\phytonEducation\\useful\\video\\su.s05e01e02.mkv" -map 0:0 -map 0:1 -c:v:0 libx264 -b:v 5948k -pass 2 -c:a:1 aac -b:a 192k -movflags +faststart output.mp4




        '''
        if os.path.isfile(util_path):
            try:
                # os.system(util_path + ' -i ' + '' +' ' + 'output_file')
                pass
            except:
                print("Упс! Не удается конвертировать файл: ")

    def get_video_info(self, file):
        videoInfo = {}
        data = ffmpeg.probe(file)
        if not data['streams']:
            return None
        # pprint(data['streams'])
        itemNum = 0
        videoInfo['audioTracks'] = {}
        for item in data['streams']:
            if item['codec_type'] == 'video':
                videoInfo['mapVideo'] = itemNum
                videoInfo['width'] = item['coded_width']
                videoInfo['height'] = item['coded_height']
                videoInfo['codecVideo'] = item['codec_name']
                if item['tags']['BPS-eng']:
                    videoInfo['bitrate'] = item['tags']['BPS-eng']
            
            if item['codec_type'] == 'audio':
                videoInfo['audioTracks'][itemNum] = {}
                videoInfo['audioTracks'][itemNum]['mapAudio'] = itemNum
                videoInfo['audioTracks'][itemNum]['codecAudio'] = item['codec_name']
                if item['tags']['BPS-eng']:
                    videoInfo['audioTracks'][itemNum]['bitrate'] = item['tags']['BPS-eng']
                if item['tags']['language']:
                    videoInfo['audioTracks'][itemNum]['language'] = item['tags']['language']
                
            itemNum += 1

        return videoInfo

        
    def prepare_video(self, folder='C:\\phytonProjects\\phytonEducation\\useful\\'):
        videoFiles = {}
        counter = 0
        for root, dirs, files in os.walk(folder):
            if not files:
                continue
            
            for file in files:
                if not file.lower().endswith(('.mp4', 'mkv', 'avi', 'flv', 'mov', 'wmv', 'mpg', 'mpeg', 'm4v', '3gp', '3g2', 'm2ts', 'mts', 'ts', 'webm')):
                    continue
                filepath = os.path.join(root, file)
                videoFiles[counter] = {}
                videoFiles[counter]['path'] = filepath
                videoFiles[counter]['info'] = self.get_video_info(filepath)
                counter += 1
        return videoFiles

files = Converter().prepare_video()
pprint(files)
if __name__ == '__main__':
    pass