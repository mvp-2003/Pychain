import hashlib

class TendLock:
    def __init__(self, prHash, TrList):
        self.prHash = prHash
        self.TrList = TrList

        self.mkblk = "-".join(TrList)+"-"+prHash
        self.hashnow = hashlib.sha256(self.mkblk.encode()).hexdigest()

t1 = "A sends 1 PC to B"
t2 = "B sends 2 PC to C"
t3 = "C sends 1.3 PC to D"
t4 = "D sends 0.9 PC to A"
t5 = "A sends 0.1 PC to E"
t6 = "E sends 0.2 PC to C"

start_chain_1 = TendLock("", [t1, t2])

print(start_chain_1.mkblk)
print(start_chain_1.hashnow)

start_chain_2 = TendLock(start_chain_1.hashnow, [t3, t4])

print(start_chain_2.mkblk)
print(start_chain_2.hashnow)

start_chain_3 = TendLock(start_chain_2.hashnow, [t5, t6])

print(start_chain_3.mkblk)
print(start_chain_3.hashnow)