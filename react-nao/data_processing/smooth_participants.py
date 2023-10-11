
#SMOOTHING CODE
import pandas as pd
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from natsort import natsorted

INPUT_FOLDER = '../data/facial_features/'
OUTPUT_FOLDER = '../processed_data/smoothed_facial_features/'

AU_cols = ['AU01_r','AU02_r','AU04_r','AU05_r','AU06_r','AU07_r','AU09_r',
           'AU10_r','AU12_r','AU14_r','AU15_r','AU17_r','AU20_r','AU23_r',
           'AU25_r','AU26_r','AU45_r']

#other_face_cols = ['gaze_angle_x', 'gaze_angle_y', 'pose_Tx', 'pose_Ty', 'pose_Tz', 'pose_Rx', 'pose_Ry', 'pose_Rz']

of_stats = ['mean','max','50%','std','count']

def load_participant_csv(i):
    file_list = glob.glob(folder_path + "/*.csv")
    new_features_df = pd.DataFrame(pd.read_csv(file_list[i]))
    return new_features_df

def smooth_df(new_features_df):
    for col in AU_cols:
        new_features_df[col] = new_features_df[col].rolling(window=30,win_type="gaussian",center=True).mean(std=10)
    return new_features_df

def load_all_participants():
    path_name = INPUT_FOLDER
    if not os.path.exists(OUTPUT_FOLDER):
    # If it doesn't exist, create it
        os.makedirs(OUTPUT_FOLDER)

    folder = natsorted(os.listdir(path_name))
    file_list = []
    for p_id in folder:
        if not os.path.exists(OUTPUT_FOLDER+p_id):
        # If it doesn't exist, create it
            os.makedirs(OUTPUT_FOLDER+p_id)

        pid_folder = os.listdir(INPUT_FOLDER+p_id)
        for game in pid_folder:
            game_AU_csv_path = path_name+p_id+'/'+game
            file_list.append(game_AU_csv_path)

    for i in range(0, len(file_list)):
        print(f"Working on {i} of {len(file_list)}")
        participant_df = new_features_df = pd.DataFrame(pd.read_csv(file_list[i]))
        smoothed_df = smooth_df(participant_df)
        smoothed_df = smoothed_df.fillna(0)
        new_file = f'{OUTPUT_FOLDER}'
        p_id =file_list[i].split("/")[-2] + '/'
        file = 'smoothed_' + file_list[i].split("/")[-1]
        new_file+=p_id+file
        #AU_cols = AU_cols.insert(0,"frame")
        df_cols = ['frame','AU01_r','AU02_r','AU04_r','AU05_r','AU06_r','AU07_r','AU09_r',
           'AU10_r','AU12_r','AU14_r','AU15_r','AU17_r','AU20_r','AU23_r',
           'AU25_r','AU26_r','AU45_r']
        smoothed_df = smoothed_df[df_cols]
        smoothed_df.to_csv(new_file,index=False)


print("starting")
load_all_participants()
print("finished")
