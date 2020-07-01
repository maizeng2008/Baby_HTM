import Encoder.ascii_converter
from Encoder import encoder
from Algorithms import SpatialPooler
from Algorithms import TemporalMemoryPooler
from Classifier import ClaClassifier
import Utils.FileReader
# import Algorithms.SpatialPooler as SpatialPooler

if __name__ == "__main__":
    Encoder = encoder.encoder(80)
    SpatialPooler = SpatialPooler.SpatialPooler(80, 2048, 0.07, 0.02, 0.5, 25)
    TemporalMemoryPooler = TemporalMemoryPooler.TemporalMemoryPooler(4, 2048, 0.5, 0.07, 0.02)
    cla_classifier = ClaClassifier.ClaClassifier(2048)

    instruction_lines = Utils.FileReader.read_instruction_test_file()
    for line in instruction_lines:
        sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction': line.rstrip()}))
        t_m = TemporalMemoryPooler.temporal_memory(sp)
        cla_classifier.classify(sp, t_m, line.rstrip())

    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Print'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Print')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Print'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Print')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')
    # sp = SpatialPooler.overlap_phase(Encoder.encode({'Instruction1': 'Set'}))
    # t_m = TemporalMemoryPooler.temporal_memory(sp)
    # cla_classifier.classify(sp, t_m, 'Set')

