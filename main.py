from googletrans import Translator

translator = Translator()
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

file_name = "Oppenheimer2023.srt"
with open(file_name) as f:
    sub_lines = f.readlines()
translated_file_name = "Oppenheimer2023-fa.srt"
with open(translated_file_name, 'w') as f:
    for sub_line in sub_lines:
        if sub_line[0] in nums:
            f.write(sub_line)
        elif sub_line == '\n':
            f.write(sub_line)
        else:
            translated_line = translator.translate(sub_line, dest='fa')
            f.write(translated_line)
