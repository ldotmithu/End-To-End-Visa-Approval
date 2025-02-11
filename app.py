from pathlib import Path
with open(Path('atrifacts\data_validation\status.txt'),'r') as f:
    file = f.read().split(':')[-1].strip()
    if file == "True":
        print('1')
    else:
        print('0')        
    