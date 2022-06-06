# OpenSesame RSVP plugin
![RSVP_plugin](/opensesame_plugins/RSVP_plugin/RSVP_plugin_large.png)

## About

This plugin allows you to add a Rapid Serial Visual Presentation element to your experiment.
The plugin can be used, for example, in a concealed information test (CIT). The RSVP plugin
allows for pupil size measurements during a CIT. Previous research has shown that pupil size 
cannot be actively manipulated, while CITs that measure other bodily sensations can be 
manipulated (Chen et al., 2021). 

The project included research into the implementation of pupil size measurements in CIT and
the development of open source tools (preseting stimuli (text/images) on the screen, 
preparation of the stimuli, and analysis of the data) to be used in CIT. The project is 
funded by Police & Science (Politie & Wetenschap). 

## Features
The RSVP plugin provides an easy tool that can be implemented in an experiment. It contains
the following features:
* An automated rapid serial visual Presentation
* Compatible with both text and image stimuli
* Contains an inter stimulus interval
* Targets and distractors can shuffle
* Number of targets and distractors can be adjusted
* Position of the targets and distractors can be adjusted

## Getting started
The plugin works for OpenSesame, so make sure to have installed [OpenSesame](https://osdoc.cogsci.nl/3.2/download) on your computer.

Next, install the RSVP plugin in OpenSesame as follows:
'''
import pip
pip.main(['instal', 'opensesame-plugin-rsvp'])
'''



## Usage
The plugin looks as follows:

![GUI](/GUI.png)

The plugin shows several elements that can be adjusted to one's wishes. The following elements
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

#### Text stimuli
If the stimuli are **text**, one can type in the target text in the widget, separated by a 
semicolon (';').Another option is to make a textfile ('.txt') with a list of all target words, 
separated by a new line ('/n'). This textfile should be added to the **filepool**, and the 
name of this textfile can be filled in in the widget. For example, the file can be named 
'targets.txt' and this should be filled in in the widget, of course without the quotes. The same 
goes for the distractors.

#### Image stimuli
If the stimuli are **images**, one should **always** add all images of the experiment to the **filepool**. 
In addition, a textfile can be created with a list of all targets. This textfile contains all filenams of 
the images and these files are separated by an enter. The textfile is also added to the filepool and can 
be referred to in the widget, instead of listing all files separated by a semicolon. This is the same for 
the distractors.

## License

No rights reserved. All files in this repository are released into the public domain.