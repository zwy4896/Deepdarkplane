from Entities.sounds import Sounds

sounds = Sounds()
def get_sound(fileName: str, volume: float):
    asset_sound = sounds.sound(fileName, volume)

    return asset_sound

def get_bgm(fileName: str, volume: float):
    sounds.sound_loop(fileName, volume)