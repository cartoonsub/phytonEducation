test = {
    'key1': {
        'inner_key1': 1,
        'inner_key2': 2
    },
    
    'key2': {'bitrateEng': {}},
    'videos': {
        'bitrate': {
            'bitrateEng' : True,
        }
    }

}

if 'bitrateEng' in test.keys():
    print('bitrateEng is in test')

# if not 'bitrateEngs' in test['video']['bitrate']:
#     print('fuck')
# for k in test.keys():
#     print(k)
# nested_keys = [k for k in test.keys() if isinstance(test[k], dict)]
# print(nested_keys)