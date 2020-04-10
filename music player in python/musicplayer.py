from pygame import mixer

mixer.init()
mixer.music.load("Singappenney.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()

while True:
    print("press 'p' to pause")
    print("press 'r' to resume")
    print("press 'v' set volume")
    print("press 'e' to exit")
    
    ch = input("['p','r','v','e']>>>")
    
    if ch == "p":
        mixer.music.pause()
    elif ch == "r":
        mixer.music.unpause()
    elif ch == "v":
        v = float(input("enter volume: "))
        mixer.music.set_volume(v)
    elif ch == "e":
        mixer.music.stop()
        break
    