class Signature:
    def __init__(self:object, r:int, s:int, r_id:int):
        self.r = r
        self.s = s
        self.r_id = r_id

    def __str__(self:object) -> str:
        return f"r: {hex(self.r)} \ns: {hex(self.s)}\nr_id: {hex(self.r_id)}"
