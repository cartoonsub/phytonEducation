
import os
import re
import ffmpeg
from pprint import pprint

class Converter:
    def __init__(self):
        self.ffmpeg = 'C:/ffmpeg/bin/ffmpeg.exe'

    def convert_to_mp4(queries):
        
        # if os.path.isfile(util_path):
        for query in queries:
            try:
                os.system(query)
            except:
                print("Упс! Не удается конвертировать файл: " + query)


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

    def has_key(self, keys, dict):
        answer = False
        if keys[0] in dict:
            if not keys[1:]:
                return True
            answer = self.has_key(keys[1:], dict[keys[0]])
        return answer

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
                
                if self.has_key(['tags', 'BPS-eng'], item):
                    videoInfo['bitrateVideo'] = item['tags']['BPS-eng']
            
            if item['codec_type'] == 'audio':
                videoInfo['audioTracks'][itemNum] = {}
                videoInfo['audioTracks'][itemNum]['mapAudio'] = itemNum
                videoInfo['audioTracks'][itemNum]['codecAudio'] = item['codec_name']

                if self.has_key(['tags', 'BPS-eng'], item):
                    videoInfo['audioTracks'][itemNum]['bitrate'] = item['tags']['BPS-eng']

                if self.has_key(['tags', 'language'], item):
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

    def prepare_name(self, name):
        name = name.replace(' ', '')
        name = name.replace('\"\'', '')
        name = re.sub(r'su\.s(\d+)e(\d+)e(\d+)', r"S\1E\2E\3.DUB", name, flags=re.IGNORECASE)
        return name

    def prepare_query(self, files) -> dict:
        queries = []
        util_path = 'C:/ffmpeg/bin/ffmpeg.exe'
        mainFields = ['path', 'info']
        if not files:
            return {}
        for file in files.values():
            flag = True
            for field in mainFields:
                if field not in file:
                    flag = False
            if not flag:
                continue
            
            path = '"' + file['path'] + '"'
            query = util_path + ' -y -i ' + path


            name, ext = os.path.splitext(path)
            name = self.prepare_name(name)
            outName = name + '.mp4"'

            if self.has_key(['info', 'bitrateVideo'], file):
                bitrate = str(file['info']['bitrateVideo'])
            else:
                bitrate = '4000k'

            if file['info']['codecVideo']:
                codec = file['info']['codecVideo']
                if codec == 'h264':
                    codec = 'libx264' #todo
            else:
                codec = 'libx264'

            query = query + ' -c:v ' + codec + ' -b:v ' + bitrate + ' -pass 1 -an -f mp4  NULL'
            queries.append(query)

            audio = {}
            
            for audioTrack in file['info']['audioTracks'].values():
                if audioTrack['language'] == 'eng':
                    continue
                mapAudio = audioTrack['mapAudio']
                if 'bitrate' in audioTrack:
                    audio['bitrate'] = str(audioTrack['bitrate'])
                else:
                    audio['bitrate'] = '192k'
                audio['map'] = str(mapAudio)
                
                # audio = ' -map 0:' + str(mapAudio) + ' -c:a:' + str(mapAudio) + ' ' + audioTrack['codecAudio'] + ' -b:a ' + bitrate
                
            query = ''
            query = util_path + ' -y -i ' + path + ' -map 0:0'
            query = query + ' -map 0:' + audio['map'] + ' -c:v:0 libx264 -b:v ' + bitrate + ' -pass 2 -c:a:' + audio['map'] + ' aac -b:a ' + audio['bitrate'] + ' -movflags +faststart ' + outName
            queries.append(query)
            # ffmpeg -y -i "C:\\phytonProjects\\phytonEducation\\useful\\video\\su.s05e01e02.mkv" -c:v libx264 -b:v 5948k -pass 1 -an -f mp4  NULL 
            # ffmpeg -y -i "C:\\phytonProjects\\phytonEducation\\useful\\video\\su.s05e01e02.mkv" -map 0:0 -map 0:1 -c:v:0 libx264 -b:v 5948k -pass 2 -c:a:1 aac -b:a 192k -movflags +faststart output.mp4 
        return queries
        
files = Converter().prepare_video()
# pprint(files)
queries = Converter().prepare_query(files)
Converter.convert_to_mp4(queries)
# print(queries)
if __name__ == '__main__':
    pass