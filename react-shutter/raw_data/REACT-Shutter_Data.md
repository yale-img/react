# REACT-Shutter: Data

## Table of Contents
This files describes the data provided in the `raw_data` folder of the REACT-Shutter dataset.
- [react-shutter_summary](#react-shutter_summary): Provides additional information about task and interaction
- [robot_actions](#robot_actions): Timestamps and details of robot actions during interaction
- [facial_features](#facial_features): Facial analysis of images captured during interaction

## react-shutter_summary

### Participant / interaction information
`ID`: Unique participant ID

`session1`: Either `whole` or `photo`, signifying which photography interaction occurred first

`session2`: Either `whole` or `photo`, signifying which photography interaction occurred second

`session_order`: A flag to indicate the order of the two sessions; either `A` (`photo` then `whole`) or `B` (`whole` then `photo`)

`annotation_order`: Either `row` or `col`, signifying the experimental condition for annotation order

### Annotation Data
`[whole/photo]_t[t#]_a[a#]_[p/s/e]`: Participant provided annotations scoring the robot actions on a 1-7 scale
- `[whole/photo]`: Whether the photograph was part of the `whole` or `photo` session; one session consists of 3 photographs
- `[t#]`: Photography task number within session; either `1`, `2`, or `3`; one photography task has 1 photograph, preceeded by 4 actions
- `[a#]`: Action number in session; either `1`, `2`, `3`, `4`, or `5`; the 5th action is the photo-taking action
- `[p/s/e]`: Dimension for annotation; either`p` = proficiency, `s` = social appropriateness, `e` = entertainment 

### Demographic information
The below table describes the participant-provided demographic information collected during the survey.

| Variable name | Survey Question | Response options|
|---------------| ----------------| ----------------|
|`age` | What is your age? | number from 18-99|
|`gender`| How do you describe your gender? | Male, Female, Non-binary, Prefer not to say, Not listed (fill in text box) |
|`country`| In which country did you spend the majority of your childhood? | Dropdown list of countries
|`english`| How would you describe your English level? | Native speaker, Near native / fluent, Highly proficient, Good command, Basic communication skills |
|`other language` | What languages, other than Enlgish, do you speak? | Free response |
|`student`| Are you a student? | Yes, No|
|`major`| If you are a student, what is your major? | Free response|
|`occupation`| If you are NOT a student, what is your occupation? | Free response| 
|`use computer`| How often do you use a computer? | Daily, 4-6 times a week, 2-3 times a week, Once a week, Once a month, Less than once a month
|`interact with robots`| How often do you interact with robots? | Daily, 4-6 times a week, 2-3 times a week, Once a week, Once a month, Less than once a month
|`robot/ai background`| Robotics / AI Background| I have studied AI or robotics technically; I have not studient AI/robotics technically, but I have followed the topics in the news or elsewhere; I am not familiar with AI/robotics technologies at all; Other|

## robot_actions
The `robot_actions` folder contains 240 CSV files, one for each photography task for each participant (40 participants * 6 photography tasks). The files follow the naming convention `robotactions_[id]_[whole/photo]_photo[p#].csv`, where:
- `[id]`: Participant ID
- `[whole/photo]`: Whether the photograph was part of the `whole` or `photo` session; one session consists of 3 photographs
- `[p#]`: Photography task number within session; either `1`, `2`, or `3`; one photography task has 1 photograph, preceeded by 4 actions

Each csv contains 9 rows of data, highlighting different robot actions within the interaction:
- The first 4 rows are the 4 actions preceeding the photo-taking action
- The 5th row is when Shutter announces it will take a photo.
- The 6th row is when Shutter takes the photo.
- The 7th row is when Shutter turns to look at the photo.
- The 8th row is when Shutter tells the participant to complete the survey questions.
- The 9th row is when Shutter tells the participant that Shutter will now rest.

The columns in these CSVs are:
- `id`: Participant ID
- `photo file`: `[whole/photo]_photo[p#]` from file name
- `start_time`: time action started
- `stop_time`: time action ended
- `high_level_action`: description of action
- `action_info`: additional information about action (e.g., dialogue for verbal tasks)

## facial_features

The `facial_features` folder contains 240 CSV files, one for each photography task for each participant (40 participants * 6 photography tasks). The files follow the naming convention `facialfeatures_[id]_[whole/photo]_photo[p#].csv`, where:
- `[id]`: Participant ID
- `[whole/photo]`: Whether the photograph was part of the `whole` or `photo` session; one session consists of 3 photographs
- `[p#]`: Photography task number within session; either `1`, `2`, or `3`; one photography task has 1 photograph, preceeded by 4 actions

These CSVs contain the output for each frame after running the image through [OpenFace 2.0](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Output-Format).

The columns in these CSVs are:
- `id`: Participant ID
- `photo file`: `[whole/photo]_photo[p#]` from file name
- columns from OpenFace analysis, as described in the [OpenFace 2.0 wiki](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Output-Format).