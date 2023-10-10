import pandas as pd
import glob
import os

INPUT_FOLDER = '../data/facial_features'
ACTION_FOLDER = '../data/robot_actions'
OUTPUT_FOLDER = '../processed_data/smoothed_facial_features/'

AU_cols = ['AU01_r','AU02_r','AU04_r','AU05_r','AU06_r','AU07_r','AU09_r',
           'AU10_r','AU12_r','AU14_r','AU15_r','AU17_r','AU20_r','AU23_r',
           'AU25_r','AU26_r','AU45_r']

other_face_cols = ['gaze_angle_x', 'gaze_angle_y', 'pose_Tx', 'pose_Ty', 'pose_Tz', 'pose_Rx', 'pose_Ry', 'pose_Rz']

of_stats = ['mean','max','50%','std','count']

def smooth_df(new_features_df):
    for col in AU_cols + other_face_cols:
        new_features_df[col] = new_features_df[col].rolling(window=30,win_type="gaussian",center=True).mean(std=10)
    return new_features_df

def load_all_participants():
    folder_path = INPUT_FOLDER
    file_list = glob.glob(folder_path + "/*.csv")
    
    if not os.path.exists(OUTPUT_FOLDER):
    # If it doesn't exist, create it
        os.makedirs(OUTPUT_FOLDER)
    
    for i in range(0, len(file_list)):
        print(f"Working on {i} of {len(file_list)}")
        participant_df = pd.DataFrame(pd.read_csv(file_list[i]))
        smoothed_df = smooth_df(participant_df)
        new_file = f'{OUTPUT_FOLDER}/{file_list[i].split("/")[-1]}'
        smoothed_df.to_csv(new_file,index=False)
    

def main():
    print("starting")
    load_all_participants()
    print("finished")
    
if __name__ == "__main__":
    main()