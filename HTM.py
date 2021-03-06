import Encoder.ascii_converter
from Encoder import encoder
from Algorithms import SpatialPooler
from Algorithms import TemporalMemoryPooler
from Classifier import ClaClassifier
import Utils.FileReader
import numpy as np
# import Algorithms.SpatialPooler as SpatialPooler

if __name__ == "__main__":
    Encoder = encoder.encoder(40)
    SpatialPooler = SpatialPooler.SpatialPooler(40, 2048, 0.07, 0.04, 0.8, 25)
    TemporalMemoryPooler = TemporalMemoryPooler.TemporalMemoryPooler(4, 2048, 0.5, 0.1, 0.02)
    cla_classifier = ClaClassifier.ClaClassifier(2048)
    # Get instruction lines
    instruction_bundle = Utils.FileReader.read_instruction_test_file()
    instruction_lines = instruction_bundle[0]
    i = 0
    for line in instruction_lines:
        i += 1
        data = Encoder.encode({'Instruction': line.rstrip()})
        sp = SpatialPooler.overlap_phase(data)
        t_m = TemporalMemoryPooler.temporal_memory(sp)
        cla_classifier.classify(sp, t_m, line.rstrip(), instruction_bundle[1])


