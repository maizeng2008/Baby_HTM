

class Cell:
    def __init__(self
                 , num_bits
                 , temporal_memory_size
                 , permanence_inc
                 , permanence_dec
                 , permanence_threshold
                 , overlap_threshold):
        self.is_active = False
