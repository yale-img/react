import pandas as pd
import glob
import os

INPUT_FOLDER = '../processed_data/smoothed_facial_features'
ACTION_FOLDER = '../data/robot_actions'
OUTPUT_FOLDER = '../processed_data'

AU_cols = ['AU01_r','AU02_r','AU04_r','AU05_r','AU06_r','AU07_r','AU09_r',
           'AU10_r','AU12_r','AU14_r','AU15_r','AU17_r','AU20_r','AU23_r',
           'AU25_r','AU26_r','AU45_r']

other_face_cols = ['gaze_angle_x', 'gaze_angle_y', 'pose_Tx', 'pose_Ty', 'pose_Tz', 'pose_Rx', 'pose_Ry', 'pose_Rz']

of_stats = ['mean','max','50%','75%','25%','std','count']

def load_participant_csv(i):
    folder_path = INPUT_FOLDER
    file_list = glob.glob(folder_path + "/*.csv")
    new_features_df = pd.DataFrame(pd.read_csv(file_list[i]))
    return new_features_df

def add_action_nums(df):
    pid = df.loc[0,'id']
    photo_file = df.loc[0,'photo file']
    robot_actions = pd.read_csv(f'{ACTION_FOLDER}/robotactions_{pid}_{photo_file}.csv')
    
    action_numbers = []
    actions = []
    
    for _, timestamp_row in df.iterrows():
        timestamp = timestamp_row['timestamp']
        
        matching_row = robot_actions[((robot_actions['start_time'] < timestamp) & (timestamp <= robot_actions['start_time'].shift(-1, fill_value=float('inf'))))]
        
        if not matching_row.empty:
            action_numbers.append(matching_row.index[0]+1)
            actions.append(matching_row['high_level_action'].values[0])
        else:
            action_numbers.append(-1)
            actions.append("outside")
    
    df['action_num'] = action_numbers
    df['high-level action num'] = actions

    return df

def summarize_df(new_features_df,of_col):
    # sum AUs
    new_features_df["AU_sum"] = new_features_df[AU_cols].sum(axis=1)
    
    #new_features_df['action_num'] = new_features_df['high-level action num'].apply(lambda x: math.ceil(x / 2))
    df = new_features_df.groupby("action_num")[of_col].describe()[of_stats]
    df.reset_index(inplace=True)
    df['id'] = new_features_df['id']
    df['photo_file'] = new_features_df['photo file']
    df['of_col'] = of_col

    return df

def load_all_participants():
    folder_path = INPUT_FOLDER
    file_list = glob.glob(folder_path + "/*.csv")
    empty = True
    for i in range(0, len(file_list)):
        print(f"Working on {i} of {len(file_list)}")
        participant_df = load_participant_csv(i)
        participant_df = add_action_nums(participant_df)
        for of_col in AU_cols + other_face_cols + ['AU_sum']:
            new_sum_df = summarize_df(participant_df,of_col)
            if empty:
                sum_df = new_sum_df
                empty = False
            else:
                sum_df =  pd.concat([sum_df,new_sum_df])
    sum_df.to_csv(f"{OUTPUT_FOLDER}/participant_summaries_facialfeatures.csv",index=False)
    

def main():
    print("starting")
    load_all_participants()
    print("finished")
    
if __name__ == "__main__":
    main()