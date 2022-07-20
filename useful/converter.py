
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

        Копия видео + конвертация аудио в web поддержку: проверить AAC 
        ffmpeg -i "C:\\phytonProjects\\phytonEducation\\useful\\su.s05e01e02.mkv" -vcodec copy -acodec aac -movflags +faststart output.mp4
        '''
        if os.path.isfile(util_path):
            try:
                # os.system(util_path + ' -i ' + '' +' ' + 'output_file')
                pass
            except:
                print("Упс! Не удается конвертировать файл: ")

    def prepare_video(self, folder='C:\\phytonProjects\\phytonEducation\\useful\\'):
        videoFiles = {}
        for root, dirs, files in os.walk(folder):
            if not files:
                continue
            
            for file in files:
                if file.lower().endswith(('.mp4', 'mkv', 'avi', 'flv', 'mov', 'wmv', 'mpg', 'mpeg', 'm4v', '3gp', '3g2', 'm2ts', 'mts', 'ts', 'webm')):
                    # videoFiles.append(os.folder.join(root, file))
                    




dataForConvert = {}
key = 0
for file in videoFiles:
    key += 1
    dataForConvert[key] = {}
    dataForConvert[key]['path'] = file
    
    print('\n\n\n')
    pprint(ffmpeg.probe(file))
    for item in ffmpeg.probe(file)['streams']:
        if item['codec_type'] == 'video':
            dataForConvert[key]['width'] = item['width']
            dataForConvert[key]['height'] = item['height']
            # dataForConvert[key]['bps'] = item['tags']['BPS-eng']
print(dataForConvert)
if __name__ == '__main__':
    pass