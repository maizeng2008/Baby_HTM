import numpy as np
from Algorithms import SpatialPooler
import math


class ClaClassifier:
    # predicted field shall be consistent
    def __init__(self, spatial_size):
        # buckets will have all the previous representation include the spatial pooler and the value of the predict
        # field
        self.buckets = {}
        # self.sequence = []
        # self.col = []
        self.spatial_size = spatial_size
        # self.next_pattern = SpatialPooler.SpatialPooler(num_bits
        #                                                 , spatial_size
        #                                                 , permanence_inc
        #                                                 , permanence_dec
        #                                                 , permanence_threshold
        #                                                 , overlap_threshold)
        # self.next_spatial_pattern = np.zeros(self.spatial_size)

    def classify(self, spatial_pooler, temporal_pooler, predict_field_value, result_file_name):
        result_file = open(result_file_name, 'a')
        # if predict field is in the buckets
        # Already know which bucket it is
        # only need to know the probability distribution of each bucket in the buckets
        if predict_field_value in self.buckets.keys():
            # Create a prediction table a dict and will eventually print it
            prediction_table = {}
            # know each column probability distribution
            spatial_pooler_pattern = np.zeros(self.spatial_size)
            # let the winner cell column number to be 1
            spatial_pooler_pattern[spatial_pooler.winner_columns] = 1
            self.buckets[predict_field_value] += spatial_pooler_pattern
            sum_array = np.sum(self.buckets[predict_field_value])
            uniform_array = np.divide(self.buckets[predict_field_value], float(sum_array))

            # New added dont know whether it is correct
            # order = uniform_array.argsort()[::-1]
            # not_select_columns = order[math.ceil(self.spatial_size*0.02):]
            # for i in range(len(not_select_columns)):
            #     uniform_array[not_select_columns[i]] = 0

            winner_cols = np.where(self.buckets[predict_field_value] > 0)
            for s_p_key in self.buckets.keys():
                summation = 0
                sp_compare_cols = np.where(self.buckets[s_p_key])[0]
                for c_index in winner_cols[0]:
                    for i in range(3):
                        pre_matrix = temporal_pooler.temporal_memory_pooler[c_index][i]
                        pre_sum = np.sum(pre_matrix, axis=1)
                        for same_col in sp_compare_cols:
                            summation += pre_sum[same_col]
                        # print(summation)
                summation = summation * uniform_array[c_index]
                prediction_table[s_p_key] = summation
            # do the uniform
            summation_prediction = 0
            for key in prediction_table.keys():
                summation_prediction += prediction_table[key]
            print("The predict value coming after value: {}".format(predict_field_value))
            result_file.write("The predict value coming after value: {}\n".format(predict_field_value))
            for key in prediction_table.keys():
                print("The probability that {} will come next is: {}".format(key, prediction_table[
                    key] / summation_prediction))
                result_file.write("The probability that {} will come next is: {}\n".format(key, prediction_table[
                    key] / summation_prediction))
        # if predict field is not in the buckets
        else:
            self.buckets[predict_field_value] = np.zeros(self.spatial_size)
            self.buckets[predict_field_value][spatial_pooler.winner_columns] = 1
            print("First time meet this value: {}".format(predict_field_value))
            result_file.write("First time meet this value: {}\n".format(predict_field_value))