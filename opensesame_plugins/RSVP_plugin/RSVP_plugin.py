#-*- coding:utf-8 -*-

"""
No rights reserved. All files in this repository are released into the public
domain.
"""

from libopensesame.py3compat import *
from libopensesame.item import item
from libqtopensesame.items.qtautoplugin import qtautoplugin
from openexp.canvas import canvas
import numpy as np

class RSVP_plugin(item):

	"""
	This class (the class with the same name as the module) handles the basic
	functionality of the item. It does not deal with GUI stuff.
	"""

	# Provide an informative description for your plug-in.
	description = u'Add an RSVP to your experiment'

	def reset(self):

		"""
		desc:
			Resets plug-in to initial values.
		"""

		self.var._type = u'images'
		self.var._targets = u''
		self.var._distractors = u''
		# self.var._targets_txt = u'4;8'
		# self.var._distractors_txt = u'q;w;e;r;t;y;u;i;o;p;a;s;d;f;g;h'
		self.var._ntargets = 3
		self.var._ndistractors = 3
		self.var._target_positions = u'1;2;4'
		self.var._stimdur = 100
		self.var._fixdur = 1000

	def prepare(self):

		# Call the parent constructor.
		item.prepare(self)

		target_positions = [int(x) - 1 for x in self.var._target_positions.split(';')]
		targets = self.var._targets.split(';')
		distractors = self.var._distractors.split(';')


		if self.var._type == u'text':
			self.var._targets_txt = u'4;8'
			self.var._distractors_txt = u'q;w;e;r;t;y;u;i;o;p;a;s;d;f;g;h'
			self.cnvs_stream = {}
				for i in range(self.var._ndistractors + self.var._ntargets):
					if i in target_positions:
						t = targets.pop(0)
						self.cnvs_stream[str(i)] = canvas(self.experiment)
						self.cnvs_stream[str(i)].text(
						"<span style='color:rgba(0,0,0,.01)'>gb</span>{}<span style='color:rgba(0,0,0,.01)'>gb</span>".format(t),
						font_size=48,
						color=u'rgb(190,190,190)',
						x=0,
						y=0
						)
						self.var.set('stim_%d' % i, t)

					else:
						d = distractors.pop(0)
						self.cnvs_stream[str(i)] = canvas(self.experiment)
						self.cnvs_stream[str(i)].text(
						"<span style='color:rgba(0,0,0,.01)'>gb</span>{}<span style='color:rgba(0,0,0,.01)'>gb</span>".format(d),
						font_size=48,
						color=u'rgb(190,190,190)',
						x=0,
						y=0
						)
						self.var.set('stim_%d' % i, t)
			
		if self.var._type == u'image':
			self.var._targets = u'weird1.jpeg;weird2.jpeg;weird3.jpeg'
			self.var._distractors = u'weird4.jpeg;weird5.jpeg;weird6.jpeg'
			self.cnvs_stream = {}
				for i in range(self.var._ndistractors + self.var._ntargets):
					if i in target_positions:
						t = targets.pop(0)
						self.cnvs_stream[str(i)] = canvas(self.experiment)
						self.cnvs_stream[str(i)].image(self.experiment.pool[t])
						self.var.set('stim_%d' % i, t)

					else:
						d = distractors.pop(0)
						self.cnvs_stream[str(i)] = canvas(self.experiment)
						self.cnvs_stream[str(i)].image(self.experiment.pool[d])
						self.var.set('stim_%d' % i, d)
		


# SEMI-ORIGINAL:
		# self.cnvs_stream = {}
		# for i in range(self.var._ndistractors + self.var._ntargets):
		# 	if i in target_positions:
		# 		t = targets.pop(0)
		# 		self.cnvs_stream[str(i)] = canvas(self.experiment)
		# 		self.cnvs_stream[str(i)].image(self.experiment.pool[t])
		# 		self.var.set('stim_%d' % i, t)

		# 	else:
		# 		d = distractors.pop(0)
		# 		self.cnvs_stream[str(i)] = canvas(self.experiment)
		# 		self.cnvs_stream[str(i)].image(self.experiment.pool[d])
		# 		self.var.set('stim_%d' % i, d)

		# create fixation canvas	
		self.cnvs_fix = canvas(self.experiment)
		self.cnvs_fix.fixdot()

		# # Byte-compile the event handling code (if any)
		# event_handler = self.var.get('_event_handler', _eval=False)
		# if event_handler:
		# 	custom_event_handler = self.python_workspace._compile(
		# 		event_handler
		# 	)
		# else:
		# 	custom_event_handler = None

	def run(self):

		#fixation dot
		self.set_item_onset(self.cnvs_fix.show())
		# self.var.fix_onset = clock.time()
		self.sleep(self.var._fixdur)
		# prev = 0

		for i in range(self.var._ndistractors + self.var._ntargets):
			t = self.cnvs_stream[str(i)].show()
			# print(t - prev)
			# prev = t

			self.sleep(self.var._stimdur)


class qtRSVP_plugin(RSVP_plugin, qtautoplugin):

	"""
	This class handles the GUI aspect of the plug-in. By using qtautoplugin, we
	usually need to do hardly anything, because the GUI is defined in info.json.
	"""

	def __init__(self, name, experiment, script=None):

		"""
		Constructor.

		Arguments:
		name		--	The name of the plug-in.
		experiment	--	The experiment object.

		Keyword arguments:
		script		--	A definition script. (default=None)
		"""

		# We don't need to do anything here, except call the parent
		# constructors.
		RSVP_plugin.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)
