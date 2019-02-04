# meetingbot

The meetingbot is a simple agenda-setter for regular (weekly) group meetings. It collects content from personal folders on a shared repository. Its main purpose is to nudge all group members to come prepared to the group meeting and share their achievements and challenges. The structure of the meeting was designed collectively by the early career researchers at the nanoLINX group at Utrecht University, who inspired Sanli to write the first version of the bot. 

## Folder structure
Each lab member has a personal (to avoid merge conflicts) folder with this structure

..
Admin  
Membername  
|  
|--HiLoPlan  
   |--Membername_hilo_2019_01.md  
|  
|--Publications  
|--Reports  

It is important that the files in the HiLoPlan folder follow to the standard filenames. Inside this folder each file contains: 

* Highlight: _{which achievement of the last week was most satisfying to you, in a couple of sentences}_. 
* Lowlight: _{which issue bothered you most or blocked you from exercising your plan}_. 
* Plan:  _{things in your to do list for the next week?}_. 

Subject to not breaking the bot, members can insert whatever they like in the meeting agenda by editing their hilo files.


## Execution

Set the correct week in the code and run `.\Admin\MeetingBot.py` to create the first draft. The notes will be amended and edited during the meeting. To avoid overwriting the report by accidentally running the bot again, it is recommended to change the filename right before or after the meeting or to move it to another folder for future reference.

