# encoding: utf-8

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
from vanilla import Window, EditText, Group, Slider
import traceback

class TextViewWidth (PalettePlugin):

	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({
			'en': 'Text View Width',
		})

		M = 10
		width = 150
		height = M * 2.5
		self.paletteView = Window((width, height))
		self.paletteView.group = Group((0, 0, width, height))
		self.paletteView.group.editText = EditText((M, 0, M * 5, M * 2),
						callback=self.editTextCallback,
						sizeStyle = 'small',
						placeholder = 'None',
						continuous = False)
		self.paletteView.group.slider = Slider((M * 7, 0, -M, M * 2),
						callback=self.sliderCallback,
						minValue=1000,
						maxValue=30000,
						sizeStyle = 'small')
		self.dialog = self.paletteView.group.getNSView()

		# self.loadPreferences()
		self.updateWidth(Glyphs.font)

	@objc.python_method
	def start(self):
		# Adding a callback for the 'GSUpdateInterface' event
		Glyphs.addCallback(self.update, UPDATEINTERFACE)

	@objc.python_method
	def __del__(self):
		Glyphs.removeCallback(self.update)

	@objc.python_method
	def loadPreferences(self):
		try:
			# set edit text
			self.paletteView.group.editText.set(str(Glyphs.defaults["com.slobzheninov.textEditWidth"]))

			return Glyphs.defaults["com.slobzheninov.textEditWidth"]
		except:
			return None

	@objc.python_method
	def savePreferences(self, userInput):
		try:
			if userInput:
				Glyphs.defaults["com.slobzheninov.textEditWidth"] = userInput
			else:
				del(Glyphs.defaults["com.slobzheninov.textEditWidth"])
		except:
			print ("Could not save preferences")
			print(traceback.format_exc())

	@objc.python_method
	def editTextCallback(self, sender):
		userInput = sender.get()
		self.savePreferences(userInput)
		font = Glyphs.font
		self.updateWidth(font)

	@objc.python_method
	def sliderCallback(self, sender):
		userInput = int(sender.get())
		self.savePreferences(userInput)
		font = Glyphs.font
		self.updateWidth(font)

	@objc.python_method
	def update(self, sender):
		font = Glyphs.font
		self.updateWidth(font)

	@objc.python_method
	def updateWidth(self, font):
		if not font:
			return

		userInput = self.loadPreferences()
		if not userInput:
			self.paletteView.group.editText.setPlaceholder(str(Glyphs.intDefaults["GSFontViewWidth"]))
			return 
		
		width = None

		userInputSplitted = str(userInput).split(" ")
		# int input or slider
		if len(userInputSplitted) == 1 and userInputSplitted[0].isnumeric():
			width = int(userInput)

		# input in characters (10 n)
		elif len(userInputSplitted) > 1 and userInputSplitted[0].isnumeric() and userInputSplitted[1].isalpha():
			if userInputSplitted[1] in font.glyphs:
				glyph = font.glyphs[userInputSplitted[1]]
				times = float(userInputSplitted[0])
				master = font.selectedFontMaster
				if glyph.layers[master.id].width > 0:
					width = times * glyph.layers[master.id].width
				else:
					print('Text View Width plugin input error:\nGlyph %s (%s) has 0 width' % (glyph.name, master.name))
					Glyphs.showMacroWindow()
			else:
				print('Text View Width plugin input error:\nGlyph %s not found' % userInputSplitted[1])
				Glyphs.showMacroWindow()
		else:
			print('Text View Width plugin input error:\nExpected input example: "12000" (in units) or "10 n" (10 times width of glyph n) or empty')
			Glyphs.showMacroWindow()

		if width:
			Glyphs.intDefaults["GSFontViewWidth"] = int(width)

			# set slider position
			self.paletteView.group.slider.set(int(width))

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
