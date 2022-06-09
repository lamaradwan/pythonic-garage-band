#Base class
class Musician():
    def __init__(self,name):
        self.name = name

class Guitarist(Musician):
    def __init__(self,name):
        Musician.__init__(self,name)


    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def __init__(self, name):
        Musician.__init__(self,name)

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name):
        Musician.__init__(self,name)

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"



class Band():
    instances = []
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.instances.append(self)


    def play_solos(self):
        sounds = []
        for member in self.members:
            sounds.append(member.play_solo())
        return(sounds)


    @classmethod
    def to_list(cls):
        return Band.instances



if __name__ == "__main__":
    # lama = Guitarist("Lama Radwan")
    # print(repr(lama))
    # print(lama.get_instrument())
    # print(lama.play_solo())


    #
    # the_nobodies = Band("The Nobodies", [])
    # all = Band.bandsList
    # print(all)
    #
    # print(all[0])
    # print(len(all))





    #
    wama = Band("WAMA",["lina","sameer","tawfiq"])
    # print(wama.members)

    tror = Band("tror",["lina","sameer","tawfiq"])
    # print(len(tror.members))

    allBands = Band.to_list()
    print(allBands)
    print(allBands[0])
    print(len(allBands))

    # members = [
    #     Guitarist("Kurt Cobain"),
    #     Bassist("Krist Novoselic"),
    #     Drummer("Dave Grohl"),
    # ]
    #
    # solos = Band("Nirvana", members)
    #
    # sounds = []
    # for member in solos.members:
    #     sounds.append(member.play_solo())
    # print(sounds)

    # print(solos.play_solos())
