# REACT-Shutter: Data Processing

## Table of Contents
This files describes the data provided in the `data` folder of the REACT-Shutter dataset.
- [smooth_participants.py](#smooth_participants.py): Smooth individual OpenFace features with a Gaussian window function.

- [add_actions_and_summarize_participants.py](#add_actions_and_summarize_participants.py): Segment frames into action segments and calculate statistics for actions.

## smooth_participants.py
The `smooth_participants.py` file creates new CSV files with smoothed OpenFace features in `processed_data/smoothed_facial_features`.

Run file from `data_processing` folder:
``` 
cd react/react-shutter/data_processing
python3 smooth_participants.py
```

## add_actions_and_summarize_participants.py
The `add_actions_and_summarize_participants.py` uses the smoothed OpenFace features in `processed_data/smoothed_facial_features` and creates `processed_data/participant_summaries_facialfeatures.csv` for analysis.

Run file from `data_processing` folder:
```
cd react/react-shutter/data_processing
python3 add_actions_and_summarize_participants.py
```