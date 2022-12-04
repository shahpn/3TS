# Import the required module for text 
# to speech 

import PySimpleGUI as sg
import gtts
from gtts import gTTS
from googletrans import Translator, constants
from time import sleep
import pyglet
from io import BytesIO
import PySimpleGUI as sg
import os

languages = ['Afrikaans',
            'Arabic',
            'Bulgarian',
            'Bengali',
            'Bosnian',
            'Catalan',
            'Czech',
            'Danish',
            'German',
            'Greek',
            'English',
            'Spanish',
            'Estonian',
            'Finnish',
            'French',
            'Gujarati',
            'Hindi',
            'Croatian',
            'Hungarian',
            'Indonesian',
            'Icelandic',
            'Italian',
            'Hebrew',
            'Japanese',
            'Javanese',
            'Khmer',
            'Kannada',
            'Korean',
            'Latin',
            'Latvian',
            'Malayalam',
            'Marathi',
            'Malay',
            'Myanmar (Burmese)',
            'Nepali',
            'Dutch',
            'Norwegian',
            'Polish',
            'Portuguese',
            'Romanian',
            'Russian',
            'Sinhala',
            'Slovak',
            'Albanian',
            'Serbian',
            'Sundanese',
            'Swedish',
            'Swahili',
            'Tamil',
            'Telugu',
            'Thai',
            'Filipino',
            'Turkish',
            'Ukrainian',
            'Urdu',
            'Vietnamese',
            'Chinese (Simplified)',
            'Chinese (Mandarin/Taiwan)',
            'Chinese (Mandarin)']



def second_window():

    layout = [[sg.Text('Desired File Name')],
              [sg.Input(size = (20, 1), key = 'fileName')],
              [sg.Button('Save', key = 'exportFile')]]

    window = sg.Window('Second Form', layout, size = (200, 100))

    while True:
        event, values = window.read()
        if event in (None, 'EXIT'):
            break

        if event == 'exportFile':
            saveAudio(str(values['fileName']) + '.mp3')
            window.close()




def mainWindow():

    sg.theme('DarkGreen3')
    sg.set_options(element_padding=(0, 0))    

    left = [
                [sg.Text('Insert text for translation', size = (30, 1))],
                [sg.MLine(size = (45, 5), key = '-QUERY-', do_not_clear = True)]
            ]

    right = [
                [sg.Text('Translated text', size = (30, 1))],
                [sg.Output(size = (45, 5), key = '_output_')]
            ]

    # ------ GUI Defintion ------ #
    layout = [
              [
                sg.Column(left, vertical_alignment = 'top', expand_x = 'True'),
                sg.Column(right, vertical_alignment = 'top')
              ],

              [sg.Text('Language'),
                sg.Combo(languages, enable_events = True, key = 'language', pad = 15)],
              
              [sg.Button('Translate')],
              
              [
                sg.Button('Hear Translation', key = 'audio', pad = 15, visible = False, disabled = True),
                sg.Button('Export Translation', key = 'export', visible = False, disabled = True)
              ]
              
    ]

    window = sg.Window("Threet",
                       layout,
                       default_element_size=(12, 1),
                       grab_anywhere=True,
                       default_button_element_size=(12, 1),
                       size = (725, 250),
                       element_justification = 'center')

    # ------ Loop & Process button menu choices ------ #
    while True:
        event, values = window.read()
        if event in (None, 'EXIT'):
            try:
                os.remove('temp.mp3')

            except:
                pass

            break

        if event == 'Translate':
            
            
            window.FindElement('_output_').Update('')
            query = values['-QUERY-'].rstrip()
            target = values['language']
            translate(query, target)
            if (window['_output_'] != '' and target != '' and query != ''):
                window['audio'].Update(visible = True, disabled = False)
                window['export'].Update(visible = True, disabled = False)

            else:
                window['_output_'].Update('')
                window['audio'].Update(visible = False, disabled = True)
                window['export'].Update(visible = False, disabled = True)

        if event == 'audio':
            playAudio()

        if event == 'export':
            second_window()


            
def translate(translateString, landingLang):

    if str(translateString) == "" or str(landingLang) == "":
        return
    
    keys = {'Afrikaans': 'af',
            'Arabic': 'ar',
            'Bulgarian': 'bg',
            'Bengali': 'bn',
            'Bosnian': 'bs',
            'Catalan': 'ca',
            'Czech': 'cs',
            'Danish': 'da',
            'German': 'de',
            'Greek': 'el',
            'English': 'en',
            'Spanish': 'es',
            'Estonian': 'et',
            'Finnish': 'fi',
            'French': 'fr',
            'Gujarati': 'gu',
            'Hindi': 'hi',
            'Croatian': 'hr',
            'Hungarian': 'hu',
            'Indonesian': 'id',
            'Icelandic': 'is',
            'Italian': 'it',
            'Hebrew': 'iw',
            'Japanese': 'ja',
            'Javanese': 'jw',
            'Khmer': 'km',
            'Kannada': 'kn',
            'Korean': 'ko',
            'Latin': 'la',
            'Latvian': 'lv',
            'Malayalam': 'ml',
            'Marathi': 'mr',
            'Malay': 'ms',
            'Myanmar (Burmese)': 'my',
            'Nepali': 'ne',
            'Dutch': 'nl',
            'Norwegian': 'no',
            'Polish': 'pl',
            'Portuguese': 'pt',
            'Romanian': 'ro',
            'Russian': 'ru',
            'Sinhala': 'si',
            'Slovak': 'sk',
            'Albanian': 'sq',
            'Serbian': 'sr',
            'Sundanese': 'su',
            'Swedish': 'sv',
            'Swahili': 'sw',
            'Tamil': 'ta',
            'Telugu': 'te',
            'Thai': 'th',
            'Filipino': 'tl',
            'Turkish': 'tr',
            'Ukrainian': 'uk',
            'Urdu': 'ur',
            'Vietnamese': 'vi',
            'Chinese (Simplified)': 'zh-CN',
            'Chinese (Mandarin/Taiwan)': 'zh-TW',
            'Chinese (Mandarin)': 'zh'}
    
    original = translateString
    translator = Translator()
    if landingLang in keys:
        try:
            os.remove('temp.mp3')
        except:
            pass

        translation = translator.translate(original, keys[landingLang])
        mytext = translation.text
        print(translation.text)

        sound = gTTS(text = mytext, lang = keys[landingLang], slow = False)
        sound.save('temp.mp3')
        

    else: return

def playAudio():

    player = pyglet.media.Player()
    source = pyglet.media.load('temp.mp3')
    player.queue(source)
    
    player.play()

    sleep(source.duration)

def saveAudio(newName):
    os.rename('temp.mp3', newName)

mainWindow()