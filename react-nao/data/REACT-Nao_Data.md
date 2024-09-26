# REACT-Nao: Data

## Table of Contents
This file describes the data provided in the `data` folder of the REACT-Nao dataset.
- [react-nao_summary](#react-shutter_summary): Provides additional information about participant and interaction
- [facial_features](#facial_features): Facial analysis of images captured during interaction
- [game_frames](#game_frames): Frame-by-frame information for each game
- [raw_images](#raw_images): Raw images of participant for each game

## react-nao_summary

### Participant / interaction information
`ID`: Unique participant ID

`Condition`: A flag to indicate experimental condition during user study; either `A`, `B`, `C`, or `D`, signifying the combination of Framing and Timing.
| Condition | Framing | Timing |
|-----------|---------|--------|
|A|Team|Before|
|B|Individual|Before|
|C|Team|After|
|D|Individual|After|


`Framing`: Framing independent variable from data collection; either `Individual` or `Team`. 

`Timing`: Timing independent variable from data collection; either `Before` or `After`.

### Basic demographic information
The below table describes the participant-provided demographic information collected during the survey.

| Variable name | Survey Question | Response options|
|---------------| ----------------| ----------------|
|`AGE` | What is your age? | number from 18-99|
|`GENDER`| How do you describe your gender? | Male, Female, Non-binary, Prefer not to say|
|`COUNTRY`| In which country did you spend the majority of your childhood? | Dropdown list of countries
|`ENGLISH`| How would you describe your English level? | Native speaker, Near native / fluent, Highly proficient, Good command, Basic communication skills |
|`OLANG` | What languages, other than Enlgish, do you speak? | Free response |
|`STUD`| Are you a student? | Yes, No|
|`MAJOR`| (If `STUD` == `Yes`) What is your major?  | Free response|
|`OCC`| (If `STUD` == `No`) What is your occupation? | Free response| 
|`OFTEN_1_C`| How often do you use a computer? | Daily, 4-6 times a week, 2-3 times a week, Once a week, Once a month, Less than once a month|
|`OFTEN_2_V`| How often do you interact with robots? | Daily, 4-6 times a week, 2-3 times a week, Once a week, Once a month, Less than once a month |
|`OFTEN_3_R`| How often do you interact with robots? | Daily, 4-6 times a week, 2-3 times a week, Once a week, Once a month, Less than once a month |
|`SI`| Have you ever played the video game Space Invaders before? | Yes, No, Not sure|
|`SI`| Are you a student? | Yes, No|

### Visual self-assessment

Participants responded to questions from the "Self-assessment of visual field" and “Self-assessment of near visual acuity” sections of the ["Quality of Life and Vision Function Questionnaire"](https://pdfs.semanticscholar.org/82bf/adb1ac18801a1d46c78c6e43fa46afb1d164.pdf). 

Response options were `Not at all` (2), `Quite a lot` (3), and `Very much` (4).

|Variable name | Question text|
|----|----|
|`VASSESS_1_ST`|Because of your vision, do you have problems crossing a street?|
|`VASSESS_2_BUMP`|Because of your vision, do you bump against other people when in crowded areas?|
|`VASSESS_3_DIP`|Because of your vision, do you have problems in perceiving a dip on the ground or step?|
|`VASSESS_4_READ`|Because of your vision, do you have problems in reading an article in a newspaper or names/numbers in the telephone directory?|
|`VASSESS_5_MAN`|Because of your vision, do you have problems in doing a manual activity such as cooking, sewing, cutting your nails?|

### Enjoyment of Competition self-assessment
Particpants responded to questions from Enjoyment of Competition subscale from [Houston, J., Harris, P., McIntire, S., & Francis, D. (2002). Revising the competitiveness index using factor analysis. Psychological Reports, 90(1), 31-34](https://journals.sagepub.com/doi/abs/10.2466/pr0.2002.90.1.31).

 Response options were `Strongly disagree` (1), `Disagree` (2), `Neither agree nor disagree` (3), `Agree` (4), and `Strongly agree` (5).

|Variable name | Question text|
|----|----|
|`COMP_1_LIKE`| I like competition.|
|`COMP_2_INDIV`| I am a competitive individual. | 
|`COMP_3_ENJOY`| I enjoy competing against an opponent.|
|`COMP_4_DLIKE`| I don’t like competing against other people| 
|`COMP_5_SAT`| I get satisfaction from competing with others.|
|`COMP_6_UNP`| I find competitive situations unpleasant.|
|`COMP_7_DREAD`| I dread competing against other people.|
|`COMP_8_AVOID`| I try to avoid competing with others.|
|`COMP_9_OUTP`| I often try to outperform others.|

### Ten Item Personality Measure (TIPI) Instrument
Participant responded to questions from [Ten Item Personality Measure (TIPI) Instrument](http://gosling.psy.utexas.edu/scales-weve-developed/ten-item-personality-measure-tipi/).

Participants answered "I see myself as ..." for the below characteristics. Response options were `Strongly disagree` (1), `Disagree` (2), `Slightly disagree` (3), `Neither agree nor disagree` (4), `Slightly agree` (5), `Agree` (6), and `Strongly agree` (7).`

|Variable name | Question text|
|----|----|
|`TIPI2_1_EE`| Extraverted, enthusiastic.|
|`TIPI2_2_CQ`|Critical, quarrelsome.|
|`TIPI2_3_DS`|Dependable, self-disciplined.|
|`TIPI2_4_AE`|Anxious, easily upset.|
|`TIPI2_5_OC`|Open to new experiences, complex.|
|`TIPI2_6_RQ`|Reserved, quiet.|
|`TIPI2_7_SW`|Sympathetic, warm.|
|`TIPI2_8_DC`|Disorganized, careless.|
|`TIPI2_9_CE`|Calm, emotionally stable.|
|`TIPI2_10_CU`|Conventional, uncreative.|


### Berkeley Expressivity Questionnaire
Participants responded to questions from [Berkeley Expressivity Questionnaire]((https://spl.stanford.edu/sites/g/files/sbiybj19321/files/media/file/english.pdf)) from [Gross, J.J., & John, O.P. (1997). Revealing feelings: Facets of emotional expressivity in self-reports, peer ratings, and behavior. Journal of Personality and Social Psychology, 72, 435-448](https://psycnet.apa.org/record/1997-03015-015).

Response options were `Strongly disagree` (1), `Disagree` (2), `Slightly disagree` (3), `Neither agree nor disagree` (4), `Slightly agree` (5), `Agree` (6), and `Strongly agree` (7).`


|Variable name | Question text|
|----|----|
|`BEQ2_1`|Whenever I feel positive emotions, people can easily see exactly what I am feeling.|
|`BEQ2_2`|I sometimes cry during sad movies.|
|`BEQ2_3`|People often do not know what I am feeling.|
|`BEQ2_4`|I laugh out loud when someone tells me a joke that I think is funny.|
|`BEQ2_5`|It is difficult for me to hide my fear.|
|`BEQ2_6`|When I'm happy, my feelings show.|
|`BEQ2_7`|My body reacts very strongly to emotional situations.|
|`BEQ2_8`|I've learned it is better to suppress my anger than to show it.|
|`BEQ2_9`|No matter how nervous or upset I am, I tend to keep a calm exterior.|
|`BEQ2_10`|I am an emotionally expressive person.|
|`BEQ2_11`|I have strong emotions.|
|`BEQ2_12`|I am sometimes unable to hide my feelings, even though I would like to.|
|`BEQ2_13`|Whenever I feel negative emotions, people can easily see exactly what I am feeling.|
|`BEQ2_14`|There have been times when I have not been able to stop crying even though I tried to stop.|
|`BEQ2_15`|I experience my emotions very strongly.|
|`BEQ2_16`|What I'm feeling is written all over my face.|

### Social Value Orientation self-assessment
Participants responded to questions from the instrument from [Lange, P., Otten, W., M. N. De Bruin, E., Joireman, J.: Development of prosocial, individualistic, and competitive orientations: Theory and preliminary evidence. Journal of personality and social psychology 73, 733–46 (11 1997). https://doi.org/10.1037//0022-3514.73.4.733](https://pubmed.ncbi.nlm.nih.gov/9325591/).

These responses are encoded in `Social1`, `Social2`, `Social3`, `Social4`, `Social5`, `Social6`, `Social7`, `Social8`, and `Social9`.




## facial_features

The `facial_features` folder contains 72 folders, one for each participant. Each participant folder `PP###` contains 6 CSV files, one for each game. The files follow the naming convention `facialfeatures_[id]_g[g#].csv`, where:
- `[id]`: Participant ID
- `[g#]`: Game number; either `1`, `2`, `3`, `4`, `5`, or `6`.

These CSVs contain the output for each frame after running the image through [OpenFace 2.0](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Output-Format).

The columns in these CSVs are:
- `id`: Participant ID
- `game file`: `g[g#]` from file name
- `frame`: Game frame number
- columns from OpenFace analysis, as described in the [OpenFace 2.0 wiki](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Output-Format).

## game_frames
Due to its large size, the `game_frames` data is available on a [Dataverse](https://doi.org/10.7910/DVN/RP2SXV).

The `game_frames` folder should be placed in the [react/react-nao/data](/react-nao/data) folder.

The `game_frames` folder contains 72 folders, one for each participant. Each participant folder `PP###` contains 6 json files, one for each game. The files follow the naming convention `gameframes_[id]_g[g#].json`, where:
- `[id]`: Participant ID
- `[g#]`: Game number; either `1`, `2`, `3`, `4`, `5`, or `6`.

The json file loads as a dictionary. The keys of this dictionary are string representations of the `frame_number`. The data is another dictionary with `frame` and `action` information.
- `frame`: The `frame` dictionary has information about the game state at this specific frame of the game.

    |Key|Description |Values |
    |---|---|---|
    |`frame_number`|Frame number as rendered in game |Int|
    |`timestamp`|Clock time of frame|Int|
    |`player_position` & `ai_position`|x-coordinates of player and ai spaceships|Int|
    |`player_lives` & `ai_lives`|Number of lives remaining for player and ai spaceships|Int|
    |`player_score` & `ai_score`|Score at this frame of game (sum was rendered as team score)|Int|
    |`player_bullets_positions` & `ai_bullets_positions` |Lists for [x,y] position of bullets originating from player and ai spaceships |List of [Float,Float] |
    |`enemies_left_positions` & `enemies_right_positions`|Lists for [x,y] position of enemies originating on left and right sides of gamescreen |List of [Float,Float]|
    |`bullets_left_positions` & `bullets_right_positions`|Lists for [x,y] position of bullets originating from left and right enemies |List of [Float,Float]|
    |`can_shoot`|Based on constraints of game, is ai spaceship allowed to shoot in this frame |Boolean|
    |`player_last_shot_time` & `ai_last_shot_time`|Clock time of last time player and ai shot|Int|
    |`player_last_shot_frame` & `ai_last_shot_frame`|Frame number of last frame player and ai shot|Int|
    |`player_avg_frequency`|Average|Float|
    |`frame_sent`|Was frame successfully sent over websocket|Boolean|
    |`player_action`|Action participant ship took in frame (move left, move right, or shoot) |Dictionary: {`left`: Boolean, `right`: Boolean, `shoot`: Boolean, `tried_to_shoot`: Boolean}|
    |`ai_actual_action`|Action that ai ship took in frame, considering all constraints |Dictionary: {`left`: Boolean, `right`: Boolean, `shoot`: Boolean}|
    |`ai_received_action`|Action for ai spaceship received from ai's current policy |Dictionary: {`left`: Boolean, `right`: Boolean, `shoot`: Boolean}|
    |`signal_down` & `signal_up`|Did participant provide negative (down) or positive (up) feedback via keyboard presses |Boolean|
    |`tried_signal_down` & `tried_signal_up`|Did participant try to give negative (down) or positive (up) feedback via keyboard presses, but was within buffer |Boolean|



- `action`: The `action` dictionary has information about the action that the robot spaceship's should take based on its current policy.
    |Key|Description |Values |
    |---|---|---|
    |`left`| Did the robot's spaceship policy decide the spaceship should move left? |True / False|
    | `right`| Did the robot's spaceship policy decide the spaceship should move right?|True / False|
    | `shoot`| Did the robot's spaceship policy decide the spaceship should shoot upwards? |True / False|

## raw_images
Due to their large size, the raw images are available on a [Dataverse](https://doi.org/10.7910/DVN/RP2SXV).
The `raw_images` folder contains 72 folders, one for each participant. Each participant folder `PP###` contains 6 subfolders, one for each game in `[id]/game_data/recorded_frames/`. The subfolders follow the naming convention: `[id]_voff_m[m#]_g[g#]_t[time]`. Then each subfolder contains the images in `webcam\w_[f#]_m[ts]_cm[ts].jpg`. The folder and files use the noted naming conventions, where:
- `[id]`: Participant ID
- `[m#]`: Mode; either `1`, `2`, or `3`.
- `[g#]`: Game number; either `1`, `2`, `3`, `4`, `5`, or `6`.
- `[time]`: Time of game start, in YYYY_MM_DD_HH_MM format.
- `[f#]`: Frame number.
- `[ts]`: Timestamp of camera image from start of interaction.
