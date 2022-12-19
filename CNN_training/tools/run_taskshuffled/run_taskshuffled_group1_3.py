#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'junxi'

import main_taskshuffled_group1_3
import yaml

# task_dict = {'EMOTION': 176, 'GAMBLING': 253, 'LANGUAGE': 316, 'MOTOR': 284, 'RELATIONAL': 232, 'SOCIAL': 274, 'WM': 405}
task_dict = {'EMOTION': 176, 'GAMBLING': 253, 'LANGUAGE': 316, 'MOTOR': 284, 'RELATIONAL': 232, 'SOCIAL': 274, 'WM': 405}
iStart = 1 # define here.
iEnd = 10 # define here.

if __name__ == '__main__':
    rsn_i = 3
    experiment_cls_path = '/data/hzb1/Projects/S900_RSN/New_Adjusted_GSextract_order/CNN_training/experiments/task_shuffled/cls_shuffled_group1_%d.yaml'%(rsn_i)
    with open(experiment_cls_path) as f:
        content = yaml.load(f)

        # output: <type 'dict'>
        # print(type(content))
        # print(content)

        content['DATASET']['TRAIN_SPLIT'] = 'Contact_Data_taskshuffled_Group_1/%02d'%(rsn_i)
        content['DATASET']['VAL_SPLIT'] = 'Contact_Data_taskshuffled_Group_1_for_test/%02d' % (rsn_i)
        content['DATASET']['NUM_POINTS'] = 1940
        content['TRAIN']['OUTPUT_DIR'] = 'output/Contact_Data_taskshuffled_Group_1_test_consistent/%02d' % (rsn_i)
        content['TEST']['RESULT_DIR'] = 'output/Contact_Data_taskshuffled_Group_1_test_consistent/%02d' % (rsn_i)
        content['BASIC']['LOG_DIR'] = 'logs/Contact_Data_taskshuffled_Group_1_test_consistent/%02d'% (rsn_i)
        content['TRAIN']['EPOCH_NUM'] = 500

        # print(content)

    with open(experiment_cls_path, 'w') as nf:
        yaml.dump(content, nf)
    main_taskshuffled_group1_3.main()