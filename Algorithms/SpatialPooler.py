import numpy as np
import math


def overlap(x):
    return x == 1


class SpatialPooler:

    def __init__(self, num_bits, spatial_size, permanence_inc, permanence_dec, permanence_threshold, overlap_threshold):
        self.nbits = num_bits
        self.spatial_pooler = np.random.uniform(low=0.0, high=1.0, size=(spatial_size, num_bits))
        self.overlap_score_table = np.ones((spatial_size, num_bits))
        self.permanence_inc = permanence_inc
        self.permanence_dec = permanence_dec
        self.permanence_threshold = permanence_threshold
        self.overlap_threshold = overlap_threshold
        self.overlap_ranked_table = np.zeros(spatial_size)
        self.num_winner_columns = math.ceil(spatial_size * 0.02)
        self.winner_columns = np.zeros(self.num_winner_columns)
        self.s_p_visual = np.zeros(spatial_size)
        self.spatial_size = spatial_size

    def overlap_phase(self, data):
        for (row_number, overlap_row_number) in zip(range(self.spatial_pooler.shape[0])
                , range(self.overlap_score_table.shape[0])):
            for cell_permanence_number, ref, is_overlap_number in zip(range(self.spatial_pooler.shape[1])
                    , data, range(self.overlap_score_table.shape[1])):
                if ref == 1:
                    if self.spatial_pooler[row_number][cell_permanence_number] > self.permanence_threshold:
                        # overlap happens
                        self.spatial_pooler[row_number][cell_permanence_number] += self.permanence_inc
                        self.overlap_score_table[row_number][cell_permanence_number] = 1
                    elif self.spatial_pooler[row_number][cell_permanence_number] <= 0:
                        self.spatial_pooler[row_number][cell_permanence_number] = 0
                        self.overlap_score_table[row_number][cell_permanence_number] = 0
                        continue
                    elif self.spatial_pooler[row_number][cell_permanence_number] < self.permanence_threshold:
                        # overlap doesnt happen
                        self.spatial_pooler[row_number][cell_permanence_number] -= self.permanence_dec
                        self.overlap_score_table[row_number][cell_permanence_number] = 0
                else:
                    if self.spatial_pooler[row_number][cell_permanence_number] > 0:
                        self.spatial_pooler[row_number][cell_permanence_number] = 0  # overlap doesnt happen
                        self.overlap_score_table[row_number][cell_permanence_number] = 0
                    else:
                        self.spatial_pooler[row_number][
                            cell_permanence_number] -= self.permanence_dec  # overlap doesnt happen
                        self.overlap_score_table[row_number][cell_permanence_number] = 0

        for row_number in range(self.overlap_score_table.shape[0]):
            self.overlap_ranked_table[row_number] = \
                sum(1 for x in self.overlap_score_table[row_number] if overlap(x))
        order = self.overlap_ranked_table.argsort()[::-1]
        self.winner_columns = order[:self.num_winner_columns]
        self.s_p_visual = np.zeros(self.spatial_size)
        for c_ind in self.winner_columns:
            self.s_p_visual[c_ind] = 1
        f = open("./s_p_visual.txt", "a")
        for i in range(self.spatial_size):
            if self.s_p_visual[i] == 1:
                f.write('1 ')
            else:
                f.write('0 ')
            if i % 64 == 0 and i != 0:
                f.write("\r\n")
        f.write("\r\n")
        f.write("\r\n")
        f.write("\r\n")
        f.close()
        return self

    # def rank_overlap_scores(self):
    #     print(self.overlap_ranked_table)
    #     for row_number in range(self.overlap_score_table.shape[0]):
    #         print(self.overlap_score_table[row_number])
    #         self.overlap_ranked_table[row_number] = \
    #             sum(1 for x in self.overlap_score_table[row_number] if self.overlap(x))
    #     order = self.overlap_ranked_table.argsort()[::-1]
    #     # ranks = order.argsort()
    #     # f = open("overlap_ranked_table.txt", "w")
    #     # print(self.overlap_ranked_table)
    #     # np.savetxt(f, self.overlap_ranked_table, fmt='%.1f')
    #     # f.close()
    #     # print(order)
    #     # f = open("order.txt", "w")
    #     # np.savetxt(f, order, fmt='%.1f')
    #     # f.close()
    #     # print("Output sorted array : ", self.overlap_ranked_table[order])
    #     # f = open("overlap_ranked_table_ordered.txt", "w")
    #     # np.savetxt(f, self.overlap_ranked_table[order], fmt='%.1f')
    #     # f.close()
    #     # ranks = order.argsort()
    #     # f = open("ranked.txt", "w")
    #     # np.savetxt(f, ranks, fmt='%.1f')
    #     # f.close()
    #     self.winner_columns = order[:self.num_winner_columns]
    #     # print(self.winner_columns)
    #     # print(np.where(self.overlap_ranked_table >= self.overlap_threshold))
    #     # print(ranks)
