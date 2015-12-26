# Adapted from the msdn documentation
# https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx

Keycode2Description = {
    1: "Left mouse button",
    2: "Right mouse button",
    3: "Control-break processing",
    4: "Middle mouse button",
    5: "X1 mouse button",
    6: "X2 mouse button",
    7: "Undefined",
    8: "BACKSPACE KEY",
    9: "TAB KEY",
    12: "CLEAR KEY",
    13: "ENTER KEY",
    16: "SHIFT KEY",
    17: "CTRL KEY",
    18: "Undefined",
    19: "PAUSE KEY",
    20: "CAPS LOCK KEY",
    21: "IME Hangul mode",
    22: "Undefined",
    23: "IME Junja mode",
    24: "IME final mode",
    25: "IME Kanji mode",
    26: "Undefined",
    27: "ESC KEY",
    28: "IME convert",
    29: "IME nonconvert",
    30: "IME accept",
    31: "IME mode change request",
    32: "SPACEBAR",
    33: "PAGE UP KEY",
    34: "PAGE DOWN KEY",
    35: "END KEY",
    36: "HOME KEY",
    37: "LEFT ARROW KEY",
    38: "UP ARROW KEY",
    39: "RIGHT ARROW KEY",
    40: "DOWN ARROW KEY",
    41: "SELECT KEY",
    42: "PRINT KEY",
    43: "EXECUTE KEY",
    44: "PRINT SCREEN KEY",
    45: "INS KEY",
    46: "DEL KEY",
    47: "HELP KEY",
    48: "0 KEY",
    49: "1 KEY",
    50: "2 KEY",
    51: "3 KEY",
    52: "4 KEY",
    53: "5 KEY",
    54: "6 KEY",
    55: "7 KEY",
    56: "8 KEY",
    57: "9 KEY",
    65: "A KEY",
    66: "B KEY",
    67: "C KEY",
    68: "D KEY",
    69: "E KEY",
    70: "F KEY",
    71: "G KEY",
    72: "H KEY",
    73: "I KEY",
    74: "J KEY",
    75: "K KEY",
    76: "L KEY",
    77: "M KEY",
    78: "N KEY",
    79: "O KEY",
    80: "P KEY",
    81: "Q KEY",
    82: "R KEY",
    83: "S KEY",
    84: "T KEY",
    85: "U KEY",
    86: "V KEY",
    87: "W KEY",
    88: "X KEY",
    89: "Y KEY",
    90: "Z KEY",
    91: "Left Windows KEY (Natural KEYboard)",
    92: "Right Windows KEY (Natural KEYboard)",
    93: "Applications KEY (Natural KEYboard)",
    94: "Reserved",
    95: "Computer Sleep KEY",
    96: "Numeric KEYpad 0 KEY",
    97: "Numeric KEYpad 1 KEY",
    98: "Numeric KEYpad 2 KEY",
    99: "Numeric KEYpad 3 KEY",
    100: "Numeric KEYpad 4 KEY",
    101: "Numeric KEYpad 5 KEY",
    102: "Numeric KEYpad 6 KEY",
    103: "Numeric KEYpad 7 KEY",
    104: "Numeric KEYpad 8 KEY",
    105: "Numeric KEYpad 9 KEY",
    106: "Multiply KEY",
    107: "Add KEY",
    108: "Separator KEY",
    109: "Subtract KEY",
    110: "Decimal KEY",
    111: "Divide KEY",
    112: "F1 KEY",
    113: "F2 KEY",
    114: "F3 KEY",
    115: "F4 KEY",
    116: "F5 KEY",
    117: "F6 KEY",
    118: "F7 KEY",
    119: "F8 KEY",
    120: "F9 KEY",
    121: "F10 KEY",
    122: "F11 KEY",
    123: "F12 KEY",
    124: "F13 KEY",
    125: "F14 KEY",
    126: "F15 KEY",
    127: "F16 KEY",
    128: "F17 KEY",
    129: "F18 KEY",
    130: "F19 KEY",
    131: "F20 KEY",
    132: "F21 KEY",
    133: "F22 KEY",
    134: "F23 KEY",
    135: "F24 KEY",
    144: "NUM LOCK KEY",
    145: "SCROLL LOCK KEY",
    160: "Left SHIFT KEY",
    161: "Right SHIFT KEY",
    162: "Left CONTROL KEY",
    163: "Right CONTROL KEY",
    164: "Left ALT KEY",
    165: "Right ALT KEY",
    166: "Browser Back KEY",
    167: "Browser Forward KEY",
    168: "Browser Refresh KEY",
    169: "Browser Stop KEY",
    170: "Browser Search KEY",
    171: "Browser Favorites KEY",
    172: "Browser Start and Home KEY",
    173: "Volume Mute KEY",
    174: "Volume Down KEY",
    175: "Volume Up KEY",
    176: "Next Track KEY",
    177: "Previous Track KEY",
    178: "Stop Media KEY",
    179: "Play/Pause Media KEY",
    180: "Start Mail KEY",
    181: "Select Media KEY",
    182: "Start Application 1 KEY",
    183: "Start Application 2 KEY",
    186: "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the ';:' KEY",
    187: "For any country/region, the '+' KEY",
    188: "For any country/region, the ',' KEY",
    189: "For any country/region, the '-' KEY",
    190: "For any country/region, the '.' KEY",
    191: "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the '/?' KEY",
    192: "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the '`~' KEY",
    219: "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the '[{' KEY",
    220: "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the '\|' KEY",
    221: "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the ']}' KEY",
    222: "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the 'single-quote/double-quote' KEY",
    223: "Used for miscellaneous characters; it can vary by KEYboard.",
    224: "Reserved",
    225: "OEM specific",
    226: "Either the angle bracket KEY or the backslash KEY on the RT 102-KEY KEYboard",
    229: "IME PROCESS KEY",
    230: "OEM specific",
    231: "Used to pass Unicode characters as if they were KEYstrokes. The VK_PACKET KEY is the low word of a 32-bit Virtual Key value used for non-KEYboard input methods. For more information, see Remark in *KEYBDINPUT*, *SendInput*, *WM_KEYDOWN*, and *WM_KEYUP*",
    232: "Unassigned",
    246: "Attn KEY",
    247: "CrSel KEY",
    248: "ExSel KEY",
    249: "Erase EOF KEY",
    250: "Play KEY",
    251: "Zoom KEY",
    252: "Reserved",
    253: "PA1 KEY",
    254: "Clear KEY"}

Description2Keycode = {
    "Left mouse button": 1,
    "Right mouse button": 2,
    "Control-break processing": 3,
    "Middle mouse button (three-button mouse)": 4,
    "X1 mouse button": 5,
    "X2 mouse button": 6,
    "Undefined": 18,
    "BACKSPACE KEY": 8,
    "TAB KEY": 9,
    "CLEAR KEY": 12,
    "ENTER KEY": 13,
    "SHIFT KEY": 16,
    "CTRL KEY": 17,
    "ALT KEY": 18,
    "PAUSE KEY": 19,
    "CAPS LOCK KEY": 20,
    "IME Kana mode": 21,
    "IME Hanguel mode (maintained for compatibility; use *VK_HANGUL*)": 21,
    "IME Hangul mode": 21,
    "IME Junja mode": 23,
    "IME final mode": 24,
    "IME Hanja mode": 25,
    "IME Kanji mode": 25,
    "ESC KEY": 27,
    "IME convert": 28,
    "IME nonconvert": 29,
    "IME accept": 30,
    "IME mode change request": 31,
    "SPACEBAR": 32,
    "PAGE UP KEY": 33,
    "PAGE DOWN KEY": 34,
    "END KEY": 35,
    "HOME KEY": 36,
    "LEFT ARROW KEY": 37,
    "UP ARROW KEY": 38,
    "RIGHT ARROW KEY": 39,
    "DOWN ARROW KEY": 40,
    "SELECT KEY": 41,
    "PRINT KEY": 42,
    "EXECUTE KEY": 43,
    "PRINT SCREEN KEY": 44,
    "INS KEY": 45,
    "DEL KEY": 46,
    "HELP KEY": 47,
    "0 KEY": 48,
    "1 KEY": 49,
    "2 KEY": 50,
    "3 KEY": 51,
    "4 KEY": 52,
    "5 KEY": 53,
    "6 KEY": 54,
    "7 KEY": 55,
    "8 KEY": 56,
    "9 KEY": 57,
    "A KEY": 65,
    "B KEY": 66,
    "C KEY": 67,
    "D KEY": 68,
    "E KEY": 69,
    "F KEY": 70,
    "G KEY": 71,
    "H KEY": 72,
    "I KEY": 73,
    "J KEY": 74,
    "K KEY": 75,
    "L KEY": 76,
    "M KEY": 77,
    "N KEY": 78,
    "O KEY": 79,
    "P KEY": 80,
    "Q KEY": 81,
    "R KEY": 82,
    "S KEY": 83,
    "T KEY": 84,
    "U KEY": 85,
    "V KEY": 86,
    "W KEY": 87,
    "X KEY": 88,
    "Y KEY": 89,
    "Z KEY": 90,
    "Left Windows KEY (Natural KEYboard)": 91,
    "Right Windows KEY (Natural KEYboard)": 92,
    "Applications KEY (Natural KEYboard)": 93,
    "Reserved": 252,
    "Computer Sleep KEY": 95,
    "Numeric KEYpad 0 KEY": 96,
    "Numeric KEYpad 1 KEY": 97,
    "Numeric KEYpad 2 KEY": 98,
    "Numeric KEYpad 3 KEY": 99,
    "Numeric KEYpad 4 KEY": 100,
    "Numeric KEYpad 5 KEY": 101,
    "Numeric KEYpad 6 KEY": 102,
    "Numeric KEYpad 7 KEY": 103,
    "Numeric KEYpad 8 KEY": 104,
    "Numeric KEYpad 9 KEY": 105,
    "Multiply KEY": 106,
    "Add KEY": 107,
    "Separator KEY": 108,
    "Subtract KEY": 109,
    "Decimal KEY": 110,
    "Divide KEY": 111,
    "F1 KEY": 112,
    "F2 KEY": 113,
    "F3 KEY": 114,
    "F4 KEY": 115,
    "F5 KEY": 116,
    "F6 KEY": 117,
    "F7 KEY": 118,
    "F8 KEY": 119,
    "F9 KEY": 120,
    "F10 KEY": 121,
    "F11 KEY": 122,
    "F12 KEY": 123,
    "F13 KEY": 124,
    "F14 KEY": 125,
    "F15 KEY": 126,
    "F16 KEY": 127,
    "F17 KEY": 128,
    "F18 KEY": 129,
    "F19 KEY": 130,
    "F20 KEY": 131,
    "F21 KEY": 132,
    "F22 KEY": 133,
    "F23 KEY": 134,
    "F24 KEY": 135,
    "NUM LOCK KEY": 144,
    "SCROLL LOCK KEY": 145,
    "Left SHIFT KEY": 160,
    "Right SHIFT KEY": 161,
    "Left CONTROL KEY": 162,
    "Right CONTROL KEY": 163,
    "Left ALT KEY": 164,
    "Right ALT KEY": 165,
    "Browser Back KEY": 166,
    "Browser Forward KEY": 167,
    "Browser Refresh KEY": 168,
    "Browser Stop KEY": 169,
    "Browser Search KEY": 170,
    "Browser Favorites KEY": 171,
    "Browser Start and Home KEY": 172,
    "Volume Mute KEY": 173,
    "Volume Down KEY": 174,
    "Volume Up KEY": 175,
    "Next Track KEY": 176,
    "Previous Track KEY": 177,
    "Stop Media KEY": 178,
    "Play/Pause Media KEY": 179,
    "Start Mail KEY": 180,
    "Select Media KEY": 181,
    "Start Application 1 KEY": 182,
    "Start Application 2 KEY": 183,
    "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the ';:' KEY": 186,
    "For any country/region, the '+' KEY": 187,
    "For any country/region, the ',' KEY": 188,
    "For any country/region, the '-' KEY": 189,
    "For any country/region, the '.' KEY": 190,
    "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the '/?' KEY": 191,
    "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the '`~' KEY": 192,
    "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the '[{' KEY": 219,
    "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the '\|' KEY": 220,
    "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the ']}' KEY": 221,
    "Used for miscellaneous characters; it can vary by KEYboard.For the US standard KEYboard, the 'single-quote/double-quote' KEY": 222,
    "Used for miscellaneous characters; it can vary by KEYboard.": 223,
    "OEM specific": 230,
    "Either the angle bracket KEY or the backslash KEY on the RT 102-KEY KEYboard": 226,
    "IME PROCESS KEY": 229,
    "Used to pass Unicode characters as if they were KEYstrokes. The VK_PACKET KEY is the low word of a 32-bit Virtual Key value used for non-KEYboard input methods. For more information, see Remark in *KEYBDINPUT*, *SendInput*, *WM_KEYDOWN*, and *WM_KEYUP*": 231,
    "Unassigned": 232,
    "Attn KEY": 246,
    "CrSel KEY": 247,
    "ExSel KEY": 248,
    "Erase EOF KEY": 249,
    "Play KEY": 250,
    "Zoom KEY": 251,
    "PA1 KEY": 253,
    "Clear KEY": 254}
