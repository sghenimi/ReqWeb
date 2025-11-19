from threading import Thread


# 1) la function à exécuter
def actor(text, count):
    for i in range(count):
        print(text * 2)


class Actor(Thread):
    def __init__(self, text, count):
        Thread.__init__(self)
        self.text = text
        self.count = count
        self.size = 0

    def run(self):
        for i in range(self.count):
            print(self.text, end="")
        self.size = len(self.text) * self.count


def main_1():
    # 2) initialisation
    actors = [Thread(target=actor, args=(text, 10)) for text in "#@&$"]

    # 3) lancement des threads
    for thread in actors:
        thread.start()

    # 4) attente que tous les threads soient finis
    for thread in actors:
        thread.join()

    # finalize
    print("\nLes threads sont terminés")


def main():
    # initialisation
    actors = [Actor(text, 10) for text in "#@&$"]
    # lancement des threads
    for thread in actors:
        thread.start()
    # attente que tous les threads aient terminés
    for thread in actors:
        thread.join()
    # affichage des résultats
    print()
    for thread in actors:
        print(f"ID({thread.name}) Text('{thread.text}') Size({thread.size})")
    # finalize
    print("nLes threads sont terminésn")


if __name__ == "__main__":
    main()
