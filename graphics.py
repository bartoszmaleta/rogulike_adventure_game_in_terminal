from time import sleep
from os import system


def introduction_screen():
    return''' Year 2066\n Aliens invaded the Earth! The alien commander - ZorgZorg is hiding somewhere in the 
 mountains and he is preparing for a big attack. 
 You have to find him and defeat him before it's too late! 
 You are the only hope of humankind, otherwise aliens with ZorgZorg as a leader will conquer our planet! HURRY! '''    

 

def logo_of_game():
    logo = ('''    
.oPYo.                                o                          8                     
8                                                                8                     
`Yooo. .oPYo. .oPYo. .oPYo. .oPYo.   o8 odYo. o    o .oPYo. .oPYo8 .oPYo. oPYo. .oPYo. 
    `8 8    8 .oooo8 8    ' 8oooo8    8 8' `8 Y.  .P .oooo8 8    8 8oooo8 8  `' Yb..   
     8 8    8 8    8 8    . 8.        8 8   8 `b..d' 8    8 8    8 8.     8       'Yb. 
`YooP' 8YooP' `YooP8 `YooP' `Yooo'    8 8   8  `YP'  `YooP8 `YooP' `Yooo' 8     `YooP' 
:.....:8 ....::.....::.....::.....::::....::..::...:::.....::.....::.....:..:::::.....:
:::::::8 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::..::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ''')
    return logo

def character_creation_screen():
    system("clear")
    creation_screen = '''
|                                                                                |
|        ┌─┐┬ ┬┌─┐┌─┐┌─┐┌─┐  ┬ ┬┌─┐┬ ┬┬─┐  ┌─┐┬ ┬┌─┐┬─┐┌─┐┌─┐┌┬┐┌─┐┬─┐           |
|        │  ├─┤│ ││ │└─┐├┤   └┬┘│ ││ │├┬┘  │  ├─┤├─┤├┬┘├─┤│   │ ├┤ ├┬┘           |
|        └─┘┴ ┴└─┘└─┘└─┘└─┘   ┴ └─┘└─┘┴└─  └─┘┴ ┴┴ ┴┴└─┴ ┴└─┘ ┴ └─┘┴└─           |
|________________________________________________________________________________|    
|          WIZARD          |         WARRIOR          |         ASSASSIN         |
|   " "                    |                          |                          |
|    "       A             |            ____          |        / V \             |
|    |      /_\            |           | _|_|         |       (|. .|\            |
|    |     | ..|           |           |  | |         |       (\▓▓▓/)            |
|    |   __\ ^^/_          |  __\\   M 888888 M        |      / |\  | \           |
|    @====#######\         |  \_ \\ ||88888888||       |     /_ | \ | _\          |
|         |# * #|\\         |    \_\\|| 888888 ||       |      / |=@=|  \          |
|         /# * #\ \\        |       \||  8888  ||      |     /  |___|  /          |
|        |#  *  #|         |        88|  ||  |88      |    /   || || /           |
|        /#  *  #\         |          | @|| @|        |   //\/\|| ||/            |
|       /#   *   #\        |          | _|| _|        |        /| |\             |
|        [1. CHOOSE]       |        [3. CHOOSE]       |        [5. CHOOSE]       |
|      [2. SHOW INFO]      |      [4. SHOW INFO]      |      [6. SHOW INFO]      |
    '''
    return creation_screen

def get_assassin_asciiart():
    asciiart='''                                               
    █████╗ ███████╗███████╗ █████╗ ███████╗███████╗██╗███╗   ██╗
   ██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██║████╗  ██║
   ███████║███████╗███████╗███████║███████╗███████╗██║██╔██╗ ██║
   ██╔══██║╚════██║╚════██║██╔══██║╚════██║╚════██║██║██║╚██╗██║
   ██║  ██║███████║███████║██║  ██║███████║███████║██║██║ ╚████║
   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝                                                                                                                                                                                                                  
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--`
    '''
    return asciiart

def get_warrior_asciiart():
    asciiart=( """
   ██╗    ██╗ █████╗ ██████╗ ██████╗ ██╗ ██████╗ ██████╗ 
   ██║    ██║██╔══██╗██╔══██╗██╔══██╗██║██╔═══██╗██╔══██╗
   ██║ █╗ ██║███████║██████╔╝██████╔╝██║██║   ██║██████╔╝
   ██║███╗██║██╔══██║██╔══██╗██╔══██╗██║██║   ██║██╔══██╗
   ╚███╔███╔╝██║  ██║██║  ██║██║  ██║██║╚██████╔╝██║  ██║
    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝                                                   
                  .--.
                 /.--.\ 
                 |====|
                 |`::`|  
             .-;`\..../`;_.-^-._
            /  |...::..|`   :   `|
           |   /''';;''|   .:.   |
           ;--'\   ::  |..:::::..|
           <__> >._::_.| ':::::' |
           |  |/   ^^  |   ':'   |
           \::/|       \    :    /
           |||\|        \   :   / 
           ''' |___/\___|`-.:.-`
                \_ || _/    `
                <_ >< _>
                |  ||  |
                |  ||  |
               _\.:||:./_
              /____/\____\  """
                                )
    return asciiart

def get_wizard_asciiart():
    asciiart= """

   ██╗    ██╗██╗███████╗ █████╗ ██████╗ ██████╗ 
   ██║    ██║██║╚══███╔╝██╔══██╗██╔══██╗██╔══██╗
   ██║ █╗ ██║██║  ███╔╝ ███████║██████╔╝██║  ██║
   ██║███╗██║██║ ███╔╝  ██╔══██║██╔══██╗██║  ██║
   ╚███╔███╔╝██║███████╗██║  ██║██║  ██║██████╔╝
    ╚══╝╚══╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                                               
                  .'* *.'
               __/_*_*(_
              / _______ \ 
             _\_)/___\(_/_
            / _((\- -/))_ \ 
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \ 
           / _ \ - | - /_  \ 
          (   ( .;''';. .'  )
          _\"__ /    )\ __"/_
            \/  \   ' /  \/
             .'  '...' ' )
              / /  |  \ \ 
             / .   .   . \ 
            /   .     .   \ 
           /   /   |   \   \ 
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._
 _.-'       |      BBb       '-.  '-.
(________mrf\____.dBBBb.________)____)"""
    
    return asciiart