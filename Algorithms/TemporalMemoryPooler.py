import numpy as np
import bitarray as bitarray
import random


class TemporalMemoryPooler:

    def __init__(self
                 , num_cells
                 , temporal_memory_size
                 , base_value
                 , permanence_inc
                 , permanence_dec):
        self.num_cells = num_cells
        self.temporal_memory_size = temporal_memory_size
        self.temporal_memory_pooler = np.zeros(
            (temporal_memory_size, self.num_cells, temporal_memory_size, self.num_cells))
        self.base_value = base_value
        self.permanence_inc = permanence_inc
        self.permanence_dec = permanence_dec
        # self.predicted_state_matrix = np.zeros((self.temporal_memory_size, self.num_cells))
        self.predicted_state_columns = np.zeros((self.temporal_memory_size, self.num_cells))
        self.predicted_state_columns_nums = []
        self.previous_active_columns = np.zeros((self.temporal_memory_size, self.num_cells))
        self.previous_active_col_nums = []
        self.active_state_matrix = np.zeros((temporal_memory_size, self.num_cells))

    def temporal_memory(self, spatial_pool):
        # if previously do not have active columns just record the previously active columns
        # and selecting randomly one cell as the lateral cell
        recording_previous = np.zeros((self.temporal_memory_size, self.num_cells))
        recording_predicted = np.zeros((self.temporal_memory_size, self.num_cells))
        if len(self.previous_active_col_nums) == 0:
            # print("here")
            for winner_column_num in spatial_pool.winner_columns:
                self.previous_active_col_nums.append(winner_column_num)
                self.previous_active_columns[winner_column_num][random.randint(0, self.num_cells - 1)] = 1
                recording_previous = self.previous_active_columns
                # print(np.where(recording_previous))
                # self.previous_active_col_nums = np.where(np.sum(recording_previous, axis=1))
        # if previously have active columns find previously active column
        else:
            for pre_col_num in self.previous_active_col_nums:
                copy = np.zeros(self.num_cells)
                copy = self.previous_active_columns[pre_col_num]
                pre_col_cells = np.where(copy > 0)
                # print("Here")
                # print(pre_col_cells)
                # print("Here")
                for pre_col_cell in pre_col_cells[0]:
                    for winner_column_num in spatial_pool.winner_columns:
                        # if system has predicted the column should be active
                        if winner_column_num in self.predicted_state_columns_nums[0]:
                            now_col_cells = np.where(self.previous_active_columns[winner_column_num] > 0)
                            for now_col_cell in now_col_cells[0]:
                                self.temporal_memory_pooler[winner_column_num][now_col_cell][pre_col_num][pre_col_cell] \
                                    += self.permanence_inc
                                recording_previous[winner_column_num][now_col_cell] = 1
                                recording_predicted += self.temporal_memory_pooler[winner_column_num][now_col_cell]
                        else:
                            now_col_cells = np.where(self.predicted_state_columns[winner_column_num] == 0)
                            if len(now_col_cells) == 0:
                                now_col_cell = random.randint(0, self.num_cells - 1)
                                if self.temporal_memory_pooler[winner_column_num][now_col_cell][pre_col_num][
                                    pre_col_cell] \
                                        == 0:
                                    self.temporal_memory_pooler[winner_column_num][now_col_cell][pre_col_num][
                                        pre_col_cell] \
                                        = self.base_value
                                    recording_previous[winner_column_num][now_col_cell] = 1
                                    recording_predicted += self.temporal_memory_pooler[winner_column_num][now_col_cell]
                                else:
                                    self.temporal_memory_pooler[winner_column_num][now_col_cell][pre_col_num][
                                        pre_col_cell] \
                                        += self.permanence_inc
                                    recording_previous[winner_column_num][now_col_cell] = 1
                                    recording_predicted += self.temporal_memory_pooler[winner_column_num][now_col_cell]
                            else:
                                for now_col_cell in now_col_cells[0]:
                                    if self.temporal_memory_pooler[winner_column_num][now_col_cell][pre_col_num][
                                        pre_col_cell] \
                                            == 0:
                                        self.temporal_memory_pooler[winner_column_num][now_col_cell][pre_col_num][
                                            pre_col_cell] \
                                            = self.base_value
                                        recording_previous[winner_column_num][now_col_cell] = 1
                                        recording_predicted += self.temporal_memory_pooler[winner_column_num][
                                            now_col_cell]
                                    else:
                                        self.temporal_memory_pooler[winner_column_num][now_col_cell][pre_col_num][pre_col_cell] \
                                            += self.permanence_inc
                                        recording_previous[winner_column_num][now_col_cell] = 1
                                        copy = self.temporal_memory_pooler[winner_column_num][now_col_cell]
                                        # print("now_col_cell{}".format(now_col_cell))
                                        recording_predicted += copy
            # update previous col matrix
        # np.copyto(self.previous_active_columns, recording_previous)
        self.previous_active_columns = 0 + recording_previous
        np.copyto(self.predicted_state_columns, recording_predicted)
        self.predicted_state_columns_nums = np.where(np.sum(recording_predicted, axis=0) > 0)
        recording_previous_sum = np.sum(recording_previous, axis=1)
        previous_active_col_nums_index = np.where(recording_previous_sum > 0)[0]
        indices = []
        for index in previous_active_col_nums_index:
            indices.append(index)
        self.previous_active_col_nums = indices
        # print(np.where(self.temporal_memory_pooler))
        # print(self.predicted_state_columns_nums)
        # print(self.previous_active_col_nums)
        # print("1")
        return self
