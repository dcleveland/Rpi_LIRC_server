"""Config file to store remote definitions."""

REMOTES = {
  "TV": {
      "ON": {"show": 1, "code": "0x9966", "repeat": 0},
      "OFF": {"show": 1, "code": "0x19E6", "repeat": 0},
      "HDMI": {"show": 1, "code": "0xD12E", "repeat": 0},
      "HDMI1": {"show": 1, "code": "0x9768", "repeat": 0},
      "HDMI2": {"show": 1, "code": "0x7D82", "repeat": 0},
      "HDMI3": {"show": 1, "code": "0x43BC", "repeat": 0},
      "HDMI4": {"show": 1, "code": "0xA35C", "repeat": 0},
      "Power": {"show": 1, "code": "0x40BF", "repeat": 0},
      "Source": {"show": 1, "code": "0x807F", "repeat": 0},
      "TV": {"show": 0, "code": "0xBE41", "repeat": 0},
      "DVD": {"show": 0, "code": "0x7E81", "repeat": 0},
      "STB": {"show": 0, "code": "0xFE01", "repeat": 0},
      "Cable": {"show": 0, "code": "0xDE21", "repeat": 0},
      "1": {"show": 1, "code": "0x20DF", "repeat": 0},
      "2": {"show": 1, "code": "0xA05F", "repeat": 0},
      "3": {"show": 1, "code": "0x609F", "repeat": 0},
      "4": {"show": 1, "code": "0x10EF", "repeat": 0},
      "5": {"show": 1, "code": "0x906F", "repeat": 0},
      "6": {"show": 1, "code": "0x50AF", "repeat": 0},
      "7": {"show": 1, "code": "0x30CF", "repeat": 0},
      "8": {"show": 1, "code": "0xB04F", "repeat": 0},
      "9": {"show": 1, "code": "0x708F", "repeat": 0},
      "Dashes": {"show": 0, "code": "0xC43B", "repeat": 0},
      "0": {"show": 1, "code": "0x8877", "repeat": 0},
      "Pre-": {"show": 0, "code": "0xC837", "repeat": 0},
      "TV/V": {"show": 0, "code": "0xC23D", "repeat": 0},
      "ChList": {"show": 0, "code": "0xD629", "repeat": 0},
      "D.nu": {"show": 0, "code": "0x718E", "repeat": 0},
      "Record": {"show": 0, "code": "0x926D", "repeat": 0},
      "Rewind": {"show": 0, "code": "0xA25D", "repeat": 0},
      "Stop": {"show": 0, "code": "0x629D", "repeat": 0},
      "Play/use": {"show": 0, "code": "0xE21D", "repeat": 0},
      "Forward": {"show": 0, "code": "0x12ED", "repeat": 0},
      "VolUp": {"show": 1, "code": "0xE01F", "repeat": 1},
      "VolDown": {"show": 1, "code": "0xD02F", "repeat": 1},
      "ChUp": {"show": 0, "code": "0x48B7", "repeat": 1},
      "ChDown": {"show": 0, "code": "0x08F7", "repeat": 1},
      "Mute": {"show": 1, "code": "0xF00F", "repeat": 0},
      "Menu": {"show": 0, "code": "0x58A7", "repeat": 0},
      "Exit": {"show": 0, "code": "0xB44B", "repeat": 0},
      "Up": {"show": 1, "code": "0x06F9", "repeat": 1},
      "Down": {"show": 1, "code": "0x8679", "repeat": 1},
      "Left": {"show": 1, "code": "0xA659", "repeat": 1},
      "Right": {"show": 1, "code": "0x46B9", "repeat": 1},
      "Enter:": {"show": 1, "code": "0x16E9", "repeat": 0},
      "Return": {"show": 1, "code": "0x1AE5", "repeat": 0},
      "Info": {"show": 0, "code": "0xF807", "repeat": 0},
      "AnyNet": {"show": 0, "code": "0xE916", "repeat": 0},
      "Red": {"show": 0, "code": "0x36C9", "repeat": 0},
      "Green": {"show": 0, "code": "0x28D7", "repeat": 0},
      "Yellow": {"show": 0, "code": "0xA857", "repeat": 0},
      "Blue": {"show": 0, "code": "0x6897", "repeat": 0},
      "Text/x": {"show": 0, "code": "0x34CB", "repeat": 0},
      "P.ze": {"show": 0, "code": "0x7C83", "repeat": 0},
      "P.de": {"show": 0, "code": "0x14EB", "repeat": 0},
      "PIP": {"show": 0, "code": "0x04FB", "repeat": 0},
      "Guide": {"show": 0, "code": "0xF20D", "repeat": 0},
      "Dual": {"show": 0, "code": "0x00FF", "repeat": 0},
      "Still": {"show": 0, "code": "0x42BD", "repeat": 0},
      "SubTitle": {"show": 0, "code": "0xA45B", "repeat": 0}
  },
  "Cable": {
        "POWER": {"show": 1, "code": "0x0000000000005006", "repeat": 0},
        "1": {"show": 1, "code": "0x000000000000800F", "repeat": 0},
        "2": {"show": 1, "code": "0x0000000000004007", "repeat": 0},
        "3": {"show": 1, "code": "0x000000000000C00B", "repeat": 0},
        "4": {"show": 1, "code": "0x0000000000002003", "repeat": 0},
        "5": {"show": 1, "code": "0x000000000000A00D", "repeat": 0},
        "6": {"show": 1, "code": "0x0000000000006005", "repeat": 0},
        "7": {"show": 1, "code": "0x000000000000E009", "repeat": 0},
        "8": {"show": 1, "code": "0x0000000000001001", "repeat": 0},
        "9": {"show": 1, "code": "0x000000000000900E", "repeat": 0},
        "MUTE": {"show": 0, "code": "0x000000000000F008", "repeat": 0},
        "0": {"show": 1, "code": "0x0000000000000000", "repeat": 0},
        "MUSIC": {"show": 0, "code": "0x000000000000080F", "repeat": 0},
        "VOLUP": {"show": 0, "code": "0x000000000000B00C", "repeat": 1},
        "LAST": {"show": 1, "code": "0x000000000000C803", "repeat": 0},
        "CHNUP": {"show": 1, "code": "0x000000000000D00A", "repeat": 1},
        "VOLDN": {"show": 0, "code": "0x0000000000007004", "repeat": 1},
        "FAV": {"show": 0, "code": "0x000000000000A805", "repeat": 0},
        "CHNDN": {"show": 1, "code": "0x0000000000003002", "repeat": 1},
        "PPV": {"show": 0, "code": "0x0000000000006809", "repeat": 0},
        "GUIDE": {"show": 0, "code": "0x0000000000000C0B", "repeat": 0},
        "EXIT": {"show": 1, "code": "0x000000000000480B", "repeat": 0},
        "INFO": {"show": 1, "code": "0x000000000000CC05", "repeat": 0},
        "MENU": {"show": 0, "code": "0x0000000000009806", "repeat": 0},
        "UP": {"show": 1, "code": "0x0000000000002C09", "repeat": 1},
        "DOWN": {"show": 1, "code": "0x000000000000AC01", "repeat": 1},
        "LEFT": {"show": 1, "code": "0x0000000000006C0E", "repeat": 1},
        "RIGHT": {"show": 1, "code": "0x000000000000EC06", "repeat":10},
        "PGUP": {"show": 1, "code": "0x0000000000005C0C", "repeat": 1},
        "PGDN": {"show": 1, "code": "0x000000000000DC04", "repeat": 1},
        "THEME": {"show": 0, "code": "0x000000000000E801", "repeat": 0},
        "CANCEL": {"show": 1, "code": "0x0000000000001406", "repeat": 0},
        "DAY": {"show": 0, "code": "0x0000000000009C02", "repeat": 0},
        "DAY": {"show": 0, "code": "0x0000000000001C0A", "repeat": 0},
        "BYPASS": {"show": 0, "code": "0x000000000000280D", "repeat": 0},
        "LIST": {"show": 0, "code": "0x000000000000E40E", "repeat": 0},
        "ENTER": {"show": 1, "code": "0x000000000000080F", "repeat": 0},
  },
  "BlueRay": {
      "KEY_POWER": {"show": 1, "code": "0xA8B", "repeat": 0},
      "KEY_POWEROFF": {"show": 1, "code": "0xF4B", "repeat": 0},
      "KEY_POWERON": {"show": 1, "code": "0x74B", "repeat": 0},
      "KEY_1": {"show": 0, "code": "0x00B", "repeat": 0},
      "KEY_2": {"show": 0, "code": "0x80B", "repeat": 0},
      "KEY_3": {"show": 0, "code": "0x40B", "repeat": 0},
      "KEY_4": {"show": 0, "code": "0xC0B", "repeat": 0},
      "KEY_5": {"show": 0, "code": "0x20B", "repeat": 0},
      "KEY_6": {"show": 0, "code": "0xA0B", "repeat": 0},
      "KEY_7": {"show": 0, "code": "0x60B", "repeat": 0},
      "KEY_8": {"show": 0, "code": "0xE0B", "repeat": 0},
      "KEY_9": {"show": 0, "code": "0x10B", "repeat": 0},
      "KEY_0": {"show": 0, "code": "0x90B", "repeat": 0},
      "KEY_AUDIO": {"show": 1, "code": "0x26B", "repeat": 0},
      "KEY_SUBTITLE": {"show": 1, "code": "0xC6B", "repeat": 0},
      "KEY_FAVORITES": {"show": 0, "code": "0x7AB", "repeat": 0},
      "KEY_YELLOW": {"show": 0, "code": "0x96B", "repeat": 0},
      "KEY_BLUE": {"show": 0, "code": "0x66B", "repeat": 0},
      "KEY_RED": {"show": 0, "code": "0xE6B", "repeat": 0},
      "KEY_GREEN": {"show": 0, "code": "0x16B", "repeat": 0},
      "KEY_TOPMENU": {"show": 0, "code": "0x34B", "repeat": 0},
      "KEY_MENU": {"show": 1, "code": "0x94B", "repeat": 0},
      "KEY_RETURN": {"show": 1, "code": "0xC2B", "repeat": 0},
      "KEY_OPTIONS": {"show": 0, "code": "0xFCB", "repeat": 0},
      "KEY_UP": {"show": 1, "code": "0x9CB", "repeat": 1},
      "KEY_DOWN": {"show": 1, "code": "0x5CB", "repeat": 1},
      "KEY_LEFT": {"show": 1, "code": "0xDCB", "repeat": 1},
      "KEY_RIGHT": {"show": 1, "code": "0x3CB", "repeat": 1},
      "KEY_ENTER": {"show": 1, "code": "0xBCB", "repeat": 0},
      "KEY_HOME": {"show": 1, "code": "0x42B", "repeat": 0},
      "KEY_PREVIOUS": {"show": 1, "code": "0xEAB", "repeat": 0},
      "KEY_NEXT": {"show": 1, "code": "0x6AB", "repeat": 0},
      "KEY_REPLAY": {"show": 0, "code": "0x6EB", "repeat": 0},
      "KEY_ADVANCE": {"show": 0, "code": "0xAEB", "repeat": 0},
      "KEY_REWIND": {"show": 1, "code": "0xD8B", "repeat": 0},
      "KEY_PLAY": {"show": 1, "code": "0x58B", "repeat": 0},
      "KEY_FASTFORWARD": {"show": 1, "code": "0x38B", "repeat": 0},
      "KEY_DISPLAY": {"show": 0, "code": "0x82B", "repeat": 0},
      "KEY_PAUSE": {"show": 1, "code": "0x98B", "repeat": 0},
      "KEY_STOP": {"show": 1, "code": "0x18B", "repeat": 0},
      "KEY_EJECT": {"show": 1, "code": "0x68B", "repeat": 0},
      "KEY_TV_INPUT": {"show": 0, "code": "0xA50", "repeat": 0},
      "KEY_TV_POWER": {"show": 0, "code": "0xA90", "repeat": 0},
      "KEY_TV_VOLUMEUP": {"show": 0, "code": "0x490", "repeat": 1},
      "KEY_TV_VOLUMEDOWN": {"show": 0, "code": "0xC90", "repeat": 1},
  },
  "Receiver": {
      "PROGRAM_ENHANCER_AUTO": {"show": 0, "code": "0x7E811BE4", "repeat": 0},
      "PROGRAM_2CH_STEREO": {"show": 1, "code": "0x7E8103FC", "repeat": 0},
      "PROGRAM_ADVENTURE": {"show": 0, "code": "0x7E81DF20", "repeat": 0},
      "PROGRAM_CELLAR_CLUB": {"show": 0, "code": "0x7E81B34C", "repeat": 0},
      "PROGRAM_CHAMBER": {"show": 0, "code": "0x7E81F50A", "repeat": 0},
      "PROGRAM_EFFECT_ON": {"show": 0, "code": "0x7E81E41B", "repeat": 0},
      "PROGRAM_MOVIE_STANDARD": {"show": 0, "code": "0x7E817F80", "repeat": 0},
      "PROGRAM_ENHANCER_OFF": {"show": 0, "code": "0x7E819B64", "repeat": 0},
      "PROGRAM_ACTION_GAME": {"show": 0, "code": "0x7E814FB0", "repeat": 0},
      "PROGRAM_DRAMA": {"show": 0, "code": "0x7E813FC0", "repeat": 0},
      "PROGRAM_HALL_IN_MUNICH": {"show": 0, "code": "0x7E818778", "repeat": 0},
      "PROGRAM_HALL_IN_VIENNA": {"show": 0, "code": "0x7E81A758", "repeat": 0},
      "PROGRAM_THE_BOTTOM_LINE": {"show": 0, "code": "0x7E8137C8", "repeat": 0},
      "PROGRAM_MONO_MOVIE": {"show": 0, "code": "0x7E81EF10", "repeat": 0},
      "PROGRAM_MUSIC_VIDEO": {"show": 0, "code": "0x7E81CF30", "repeat": 0},
      "PROGRAM_PURE_DIRECT_OFF": {"show": 0, "code": "0x7E8141BE", "repeat": 0},
      "PROGRAM_PURE_DIRECT_ON": {"show": 0, "code": "0x7E8101FE", "repeat": 0},
      "PROGRAM_THE_ROXY_THEATRE": {"show": 0, "code": "0x7E81B748", "repeat": 0},
      "PROGRAM_ROLEPLAYING_GAME": {"show": 0, "code": "0x7E81738C", "repeat": 0},
      "PROGRAM_SCI_FI": {"show": 0, "code": "0x7E815FA0", "repeat": 0},
      "PROGRAM_SPECTACLE": {"show": 0, "code": "0x7E819F60", "repeat": 0},
      "PROGRAM_SPORTS": {"show": 0, "code": "0x7E811FE0", "repeat": 0},
      "PROGRAM_SURROUND_DECODE_ON": {"show": 0, "code": "0x7E81BF40", "repeat": 0},
      "PROGRAM_STRAIGHT": {"show": 0, "code": "0x7E8107F8", "repeat": 0},
      "PROGRAM_7CH_STEREO": {"show": 0, "code": "0x7E81FF00", "repeat": 0},
      "OUTPUT_HDMI_OUT1": {"show": 0, "code": "0x7E8104FA", "repeat": 0},
      "OUTPUT_HDMI_OUT1AND2": {"show": 0, "code": "0x7E8155AB", "repeat": 0},
      "OUTPUT_HDMI_OUT2": {"show": 0, "code": "0x7E81847A", "repeat": 0},
      "OUTPUT_HDMI_OUT_OFF": {"show": 0, "code": "0x7E8141BF", "repeat": 0},
      "MENU_ADAPTIVE_DRC_OFF": {"show": 0, "code": "0x7E81AE50", "repeat": 0},
      "MENU_ADAPTIVE_DRC_ON": {"show": 0, "code": "0x7E812ED0", "repeat": 0},
      "MENU_ADAPTIVE_DSP_OFF": {"show": 0, "code": "0x7E81EE10", "repeat": 0},
      "MENU_ADAPTIVE_DSP_ON": {"show": 0, "code": "0x7E816E90", "repeat": 0},
      "MENU_DUAL_MONO_ALL": {"show": 0, "code": "0x7E81A956", "repeat": 0},
      "MENU_DUAL_MONO_MAIN": {"show": 0, "code": "0x7E81C936", "repeat": 0},
      "MENU_DUAL_MONO_SUB": {"show": 0, "code": "0x7E8129D6", "repeat": 0},
      "MENU_EXTED_SUR_AUTO": {"show": 0, "code": "0x7E813EC1", "repeat": 0},
      "MENU_EXTED_SUR_ON": {"show": 0, "code": "0x7E811DE2", "repeat": 0},
      "MENU_EXTED_SUR_OFF": {"show": 0, "code": "0x7E819D62", "repeat": 0},
      "MENU_EXTED_SUR_PLIIX_MOVIE": {"show": 0, "code": "0x7E81BB44", "repeat": 0},
      "MENU_EXTED_SUR_PLIIX_MUSIC": {"show": 0, "code": "0x7E817B84", "repeat": 0},
      "MENU_HDMI_AUTO_LIPSYNC_OFF": {"show": 0, "code": "0x7E8121DF", "repeat": 0},
      "MENU_HDMI_AUTO_LIPSYNC_ON": {"show": 0, "code": "0x7E81C13F", "repeat": 0},
      "MENU_NEO6_MOVIE": {"show": 0, "code": "0x7E819669", "repeat": 0},
      "MENU_NEO6_MUSIC": {"show": 0, "code": "0x7E8156A9", "repeat": 0},
      "MENU_PLIIX_GAME": {"show": 0, "code": "0x7E81E31C", "repeat": 0},
      "MENU_PLIIX_MOVIE": {"show": 0, "code": "0x7E81E619", "repeat": 0},
      "MENU_PLIIX_MUSIC": {"show": 0, "code": "0x7E8116E9", "repeat": 0},
      "MENU_PRO_LOGIC": {"show": 0, "code": "0x7E81936C", "repeat": 0},
      "MENU_TRIGGER1_MANUAL_OFF": {"show": 0, "code": "0x7E8102FC", "repeat": 0},
      "MENU_TRIGGER1_MANUAL_ON": {"show": 0, "code": "0x7E81FC02", "repeat": 0},
      "MEMORY_VOLUME_MEMORY1": {"show": 0, "code": "0x7E81D629", "repeat": 0},
      "MEMORY_VOLUME_MEMORY2": {"show": 0, "code": "0x7E8136C9", "repeat": 0},
      "MEMORY_VOLUME_MEMORY3": {"show": 0, "code": "0x7E81B649", "repeat": 0},
      "MEMORY_VOLUME_MEMORY4": {"show": 0, "code": "0x7E817689", "repeat": 0},
      "MEMORY_VOLUME_MEMORY5": {"show": 0, "code": "0x7E81F609", "repeat": 0},
      "MEMORY_VOLUME_MEMORY6": {"show": 0, "code": "0x7E810EF1", "repeat": 0},
      "MEMORY_VOLUME_RECALL1": {"show": 0, "code": "0x7E81AE51", "repeat": 0},
      "MEMORY_VOLUME_RECALL2": {"show": 0, "code": "0x7E816E91", "repeat": 0},
      "MEMORY_VOLUME_RECALL3": {"show": 0, "code": "0x7E81EE11", "repeat": 0},
      "MEMORY_VOLUME_RECALL4": {"show": 0, "code": "0x7E811EE1", "repeat": 0},
      "MEMORY_VOLUME_RECALL5": {"show": 0, "code": "0x7E819E61", "repeat": 0},
      "MEMORY_VOLUME_RECALL6": {"show": 0, "code": "0x7E815EA1", "repeat": 0},
      "VOLUME_MUTE_OFF": {"show": 0, "code": "0x7E81C53A", "repeat": 0},
      "VOLUME_MUTE_ON_-DB": {"show": 0, "code": "0x7E81FB04", "repeat": 0},
      "VOLUME_MUTE_ON_-DB": {"show": 0, "code": "0x7E81C638", "repeat": 0},
      "VOLUME_MUTE_ON": {"show": 0, "code": "0x7E8145BA", "repeat": 0},
      "POWER_POWER_ON": {"show": 1, "code": "0x7E817E81", "repeat": 0},
      "POWER_SLEEP_OFF": {"show": 0, "code": "0x7E81D826", "repeat": 0},
      "POWER_SLEEP_ON": {"show": 0, "code": "0x7E816896", "repeat": 0},
      "POWER_STANDBY": {"show": 0, "code": "0x7E81FE01", "repeat": 0},
      "MEMORY_SCENE1": {"show": 0, "code": "0x5EA100FE", "repeat": 0},
      "MEMORY_SCENE2": {"show": 0, "code": "0x5EA1C03E", "repeat": 0},
      "MEMORY_SCENE3": {"show": 0, "code": "0x5EA1609E", "repeat": 0},
      "MEMORY_SCENE4": {"show": 0, "code": "0x5EA1906E", "repeat": 0},
      "MEMORY_MEMORY": {"show": 0, "code": "0xFE80E618", "repeat": 0},
      "VOLUME_MUTE": {"show": 1, "code": "0x5EA138C7", "repeat": 0},
      "VOLUME_VOLUME-": {"show": 1, "code": "0x5EA1D827", "repeat": 1},
      "VOLUME_VOLUME+": {"show": 1, "code": "0x5EA158A7", "repeat": 1},
      "MENU_DOWN": {"show": 0, "code": "0x5EA139C6", "repeat": 0},
      "MENU_ENTER": {"show": 0, "code": "0x5EA17B84", "repeat": 0},
      "MENU_LEFT": {"show": 0, "code": "0x5EA1F906", "repeat": 0},
      "MENU_ON_SCREEN": {"show": 0, "code": "0x5EA121DE", "repeat": 0},
      "MENU_RETURN": {"show": 0, "code": "0x5EA155AA", "repeat": 0},
      "MENU_RIGHT": {"show": 0, "code": "0x5EA17986", "repeat": 0},
      "MENU_OPTION": {"show": 0, "code": "0x5EA1D628", "repeat": 0},
      "MENU_UP": {"show": 0, "code": "0x5EA1B946", "repeat": 0},
      "POWER_POWER_ON_STANDBY": {"show": 0, "code": "0x7E8154AB", "repeat": 0},
      "POWER_SLEEP": {"show": 0, "code": "0x5EA10CF3", "repeat": 0},
      "INPUT_AUDIO1": {"show": 1, "code": "0x5EA1A658", "repeat": 0},
      "INPUT_AUDIO2": {"show": 1, "code": "0x5EA116E8", "repeat": 0},
      "INPUT_AV1": {"show": 1, "code": "0x5EA1CA34", "repeat": 0},
      "INPUT_AV2": {"show": 1, "code": "0x5EA16A94", "repeat": 0},
      "INPUT_AV3": {"show": 1, "code": "0x5EA19A64", "repeat": 0},
      "INPUT_AV4": {"show": 1, "code": "0x5EA13AC4", "repeat": 0},
      "INPUT_AV5": {"show": 1, "code": "0x5EA1FA04", "repeat": 0},
      "INPUT_AV6": {"show": 1, "code": "0x5EA146B8", "repeat": 0},
      "INPUT_DOCK": {"show": 0, "code": "0xFE8052AD", "repeat": 0},
      "INPUT_HDMI1": {"show": 1, "code": "0x5EA1E21C", "repeat": 0},
      "INPUT_HDMI2": {"show": 1, "code": "0x5EA152AC", "repeat": 0},
      "INPUT_HDMI3": {"show": 1, "code": "0x5EA1B24C", "repeat": 0},
      "INPUT_HDMI4": {"show": 1, "code": "0x5EA10AF4", "repeat": 0},
      "INPUT_HDMI5": {"show": 1, "code": "0x5EA10EF0", "repeat": 0},
      "INPUT_VAUX": {"show": 0, "code": "0x5EA1CE30", "repeat": 0},
      "INPUT_INPUT": {"show": 0, "code": "0x5EA1C43A", "repeat": 0},
      "INPUT_INPUT": {"show": 0, "code": "0x5EA1F806", "repeat": 0},
      "INPUT_MULTI_CH_IN": {"show": 0, "code": "0x5EA1E11E", "repeat": 0},
      "INPUT_PHONO": {"show": 0, "code": "0x5EA128D7", "repeat": 0},
      "INPUT_TUNER": {"show": 0, "code": "0x5EA16897", "repeat": 0},
      "DISPLAY_INFO": {"show": 0, "code": "0x5EA1E41A", "repeat": 0},
      "DISPLAY_DISPLAY": {"show": 0, "code": "0xFE8006F9", "repeat": 0},
      "NUMBER_0": {"show": 0, "code": "0xFE805AA5", "repeat": 0},
      "NUMBER_1": {"show": 0, "code": "0xFE808A75", "repeat": 0},
      "NUMBER_2": {"show": 0, "code": "0xFE804AB5", "repeat": 0},
      "NUMBER_3": {"show": 0, "code": "0xFE80CA35", "repeat": 0},
      "NUMBER_4": {"show": 0, "code": "0xFE802AD5", "repeat": 0},
      "NUMBER_5": {"show": 0, "code": "0xFE80AA55", "repeat": 0},
      "NUMBER_6": {"show": 0, "code": "0xFE806A95", "repeat": 0},
      "NUMBER_7": {"show": 0, "code": "0xFE80EA15", "repeat": 0},
      "NUMBER_8": {"show": 0, "code": "0xFE801AE5", "repeat": 0},
      "NUMBER_9": {"show": 0, "code": "0xFE809A65", "repeat": 0},
      "NUMBER_ENT": {"show": 0, "code": "0xFE803AC5", "repeat": 0},
      "OPERATION_FM": {"show": 0, "code": "0xFE801AE4", "repeat": 0},
      "OPERATION_AM": {"show": 0, "code": "0xFE80AA54", "repeat": 0},
      "OPERATION_PAUSE": {"show": 0, "code": "0xFE80E619", "repeat": 0},
      "OPERATION_PLAY": {"show": 0, "code": "0xFE8016E9", "repeat": 0},
      "OPERATION_REC": {"show": 0, "code": "0xFE806699", "repeat": 0},
      "OPERATION_STOP": {"show": 0, "code": "0xFE809669", "repeat": 0},
      "OPERATION_REW": {"show": 0, "code": "0xFE8056A9", "repeat": 0},
      "OPERATION_FF": {"show": 0, "code": "0xFE80D629", "repeat": 0},
      "OPERATION_SKIP": {"show": 0, "code": "0xFE8036C9", "repeat": 0},
      "OPERATION_SKIP": {"show": 0, "code": "0xFE80B649", "repeat": 0},
      "OPERATION_PRESET": {"show": 0, "code": "0xFE807A84", "repeat": 0},
      "OPERATION_PRESET": {"show": 0, "code": "0xFE80DA24", "repeat": 0},
      "OPERATION_TUNING": {"show": 0, "code": "0xFE8026D8", "repeat": 0},
      "OPERATION_TUNING": {"show": 0, "code": "0xFE808678", "repeat": 0},
      "NUMBER_0": {"show": 0, "code": "0xFE80DA25", "repeat": 0},
  }
}

MACROS = {
  "HBO": {
      "commands": [("Cable", "6"), ("Cable", "5"), ("Cable", "1")],
      "sleep": 0.2
      },
  "HBO2": {
      "commands": [("Cable", "6"), ("Cable", "5"), ("Cable", "2")],
      "sleep": 0.2
      },
  "ABC": {
      "commands": [("Cable", "7"), ("Cable", "0"), ("Cable", "7")],
      "sleep": 0.2
      },
  "CBS": {
      "commands": [("Cable", "7"), ("Cable", "0"), ("Cable", "2")],
      "sleep": 0.2
      },
  "FOX": {
      "commands": [("Cable", "7"), ("Cable", "0"), ("Cable", "5")],
      "sleep": 0.2
      },
  "NBC": {
      "commands": [("Cable", "7"), ("Cable", "0"), ("Cable", "4")],
      "sleep": 0.2
      }
}