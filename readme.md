# OpenSesame RSVP plugin

## About

This plugin allows you to add a Rapid Servial Visual Presentation element to your experiment.
The plugin can be used, for example, in a concealed information test (CIT). The RSVP plugin
allows for pupil size measurements during a CIT. Previous research has shown that pupil size 
cannot be actively manipulated, while CITs that measure other bodily sensations can be 
manipulated (Chen et al., 2021). 

The project included research into the implementation of pupil size measurements in CIT and
the development of open source tools (preseting stimuli (text/images) on the screen, 
preparation of the stimuli, and analysis of the data) to be used in CIT. The project is 
funded by Police & Science (Politie & Wetenschap). 


## Usage
TODO: insert image of GUI

The GUI shows several elements that can be adjusted to one's wishes. The following elements
can be adjusted:
* mode (text or images)
* targets
* number of targets
* shuffle targets
* distractors
* number of distractors
* shuffle distractors
* stimulus duration
* fixation duration
* positions of the targets
* inter stimulus interval

##### Text stimuli
If the stimuli are **text**, one can type in the target text in the widget, separated by a 
semicolon (';').Another option is to make a textfile ('.txt') with a list of all target words, 
separated by a new line ('/n'). This textfile should be added to the **filepool**, and the 
name of this textfile can be filled in in the widget. For example, the file can be named 
'targets.txt' and this should be filled in in the widget, of course without the quotes. The same 
goes for the distractors.

##### Image stimuli
If the stimuli are **images**, one should **always** add all images of the experiment to the **filepool**. 
In addition, a textfile can be created with a list of all targets. This textfile contains all filenams of 
the images and these files are separated by an enter. The textfile is also added to the filepool and can 
be referred to in the widget, instead of listing all files separated by a semicolon. This is the same for 
the distractors.

## License

No rights reserved. All files in this repository are released into the public domain.