import os
import re
import ffmpeg
from pprint import pprint
from time import sleep

class Converter:
    def __init__(self, folder='C:\\phytonProjects\\phytonEducation\\useful\\', outFolder='C:\\phytonProjects\\phytonEducation\\useful\\', convert=False):
        self.ffmpeg = 'C:/ffmpeg/bin/ffmpeg.exe'
        self.folder = folder
        self.outFolder = outFolder
        self.bitrateVideo = '5000k'
        self.bitrateAudio = '192k'
        self.convert = convert

    def run(self):
        files = self.prepare_video()
        if not files:
            print('Не найдены файлы для конвертации')
            return
        queries = self.prepare_query(files)
        if not queries:
            print('Не удалось создать запросы для ffmpeg')
            return
        self.convert_to_mp4(queries)

    def prepare_video(self):
        videoFiles = {}
        counter = 0
        for root, dirs, files in os.walk(self.folder):
            if not files:
                continue

            for file in files:
                if not file.lower().endswith(('.mp4', 'mkv', 'avi', 'flv', 'mov', 'wmv', 'mpg', 'mpeg', 'm4v', '3gp', '3g2', 'm2ts', 'mts', 'ts', 'webm')):
                    continue

                filepath = os.path.join(root, file)
                info = self.get_video_info(filepath)
                
                if info is None:
                    print(str(counter) + 'Не удалось получить данные из ' + filepath)
                    continue

                videoFiles[counter] = {}
                videoFiles[counter]['path'] = filepath
                videoFiles[counter]['info'] = info
                counter += 1
        return videoFiles

    def get_video_info(self, file):
        videoInfo = {}
        data = ffmpeg.probe(file)
        if not data['streams']:
            return None

        flag = False
        itemNum = 0
        videoInfo['audioTracks'] = {}
        for item in data['streams']:
            if item['codec_type'] == 'video':
                videoInfo['mapVideo'] = itemNum
                videoInfo['width'] = item['coded_width']
                videoInfo['height'] = item['coded_height']
                videoInfo['codecVideo'] = item['codec_name']

                # todo - find other bitrate options 
                if self.has_key(['tags', 'BPS-eng'], item):
                    videoInfo['bitrateVideo'] = item['tags']['BPS-eng']
                flag = True

            if item['codec_type'] == 'audio':
                videoInfo['audioTracks'][itemNum] = {}
                videoInfo['audioTracks'][itemNum]['mapAudio'] = itemNum
                videoInfo['audioTracks'][itemNum]['codecAudio'] = item['codec_name']

                if self.has_key(['tags', 'BPS-eng'], item):
                    videoInfo['audioTracks'][itemNum]['bitrate'] = item['tags']['BPS-eng']
                if self.has_key(['tags', 'BPS'], item):
                    videoInfo['audioTracks'][itemNum]['bitrate'] = item['tags']['BPS']
                if 'bit_rate' in item:
                    videoInfo['audioTracks'][itemNum]['bitrate'] = item['bit_rate']

                if self.has_key(['tags', 'language'], item):
                    videoInfo['audioTracks'][itemNum]['language'] = item['tags']['language']

                if self.has_key(['tags', 'title'], item):
                    videoInfo['audioTracks'][itemNum]['language'] = item['tags']['title']
            itemNum += 1

        if not videoInfo['audioTracks']: # todo - doesn't need for mute video
            return {}
        if flag == False:
            return {}
        
        return videoInfo

    def prepare_query(self, files) -> dict:
        queries = []
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
            query = self.ffmpeg + ' -y -i ' + path

            name, ext = os.path.splitext(path)
            name = self.prepare_name(name)
            newName = name + '.mp4'
            outName = os.path.join(os.path.dirname(self.outFolder), os.path.basename(newName))
            
            if self.has_key(['info', 'bitrateVideo'], file):
                self.bitrateVideo = str(file['info']['bitrateVideo'])

            audio = self.setAudio(file)
            if not audio:
                print('Не удалось получить аудио дорожку' + name)
                continue
                # audio = ' -map 0:' + str(mapAudio) + ' -c:a:' + str(mapAudio) + ' ' + audioTrack['codecAudio'] + ' -b:a ' + bitrate

            query = self.setQueryPass1(file, query)
            queries.append(query)

            query = ''
            query = self.ffmpeg + ' -y -i ' + path + ' -map 0:0'
            query = query + ' -map 0:' + audio['map'] + ' -c:v:0 libx264 -b:v ' + self.bitrateVideo + ' -pass 2 -c:a:' + audio['map'] + ' aac -b:a ' + audio['bitrate'] + ' -movflags +faststart ' + outName
            queries.append(query)
            # ffmpeg -y -i "C:\\phytonProjects\\phytonEducation\\useful\\video\\su.s05e01e02.mkv" -c:v libx264 -b:v 5948k -pass 1 -an -f mp4  NULL
            # ffmpeg -y -i "C:\\phytonProjects\\phytonEducation\\useful\\video\\su.s05e01e02.mkv" -map 0:0 -map 0:1 -c:v:0 libx264 -b:v 5948k -pass 2 -c:a:1 aac -b:a 192k -movflags +faststart output.mp4
        return queries

    def setQueryPass1(self, file, query) -> str:
        if file['info']['codecVideo']:
            codec = file['info']['codecVideo']
        if codec == 'h264':
            codec = 'libx264'  # todo - maybe we can add other codecs
        else:
            codec = 'libx264'
        query = query + ' -c:v ' + codec + ' -b:v ' + self.bitrateVideo + ' -pass 1 -an -f mp4 ' + self.outFolder + 'NULL' # NULL

        return query

    def setAudio(self, file) -> dict:
        audio = {}
        for audioTrack in file['info']['audioTracks'].values():
            language = ''
            if 'language' in audioTrack:
                language = audioTrack['language']

            # if audioTrack['language'] == 'eng':
            #     continue
            # if audioTrack['language'] == 'Original':
            #     continue
            mapAudio = audioTrack['mapAudio']
            if 'bitrate' in audioTrack:
                audio['bitrate'] = str(audioTrack['bitrate'])
            else:
                audio['bitrate'] = self.bitrateAudio
            audio['map'] = str(mapAudio)
            # if audioTrack['language'] == 'Yet Another Studio':
            #     break
            if language == 'rus':
                break
        
        return audio

    def convert_to_mp4(self, queries):
        for query in queries:
            try:
                print(query)
                print('')
                if self.convert == False:
                    continue
                os.system(query)
            except:
                print("Упс! Не удается конвертировать файл: " + query)

    def has_key(self, keys, dict):
        answer = False
        if keys[0] in dict:
            if not keys[1:]:
                return True
            answer = self.has_key(keys[1:], dict[keys[0]])
        return answer

    def prepare_name(self, name):
        name = name.replace(' ', '')
        name = name.replace('\"\'', '')
        name = re.sub(r'su\.s(\d+)e(\d+)e(\d+)',
                      r"S\1E\2E\3.DUB", name, flags=re.IGNORECASE)
        return name

folder = 'G:\\cartoon\\gumball\\1season\\sound\\test\\'
outFolder = 'G:\\cartoon\\gumball\\1season\\sound\\output\\'
Converter = Converter(folder=folder, outFolder=outFolder, convert=True)
Converter.run()

if __name__ == '__main__':
    pass

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
