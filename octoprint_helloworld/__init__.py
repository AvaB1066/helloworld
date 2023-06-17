# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import RPi.GPIO as GPIO
from flask import jsonify, request


class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
						  octoprint.plugin.ShutdownPlugin,
						  octoprint.plugin.EventHandlerPlugin,
						  octoprint.plugin.TemplatePlugin,
						  octoprint.plugin.SettingsPlugin,
						  octoprint.plugin.AssetPlugin,
						  octoprint.plugin.BlueprintPlugin):
	
	
	
	
	
		def __init__(self):
		self.i = 0
		self._gpioup = 0
		self._powerup = 0
		self._onevents = ["OPERATIONAL"]
		self._offevents = ["ERROR", "CLOSED_WITH_ERROR", ]


		
		
		def _initgpio(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(26, GPIO.OUT)
		self._gpioup = 1
		
		
def readtemperature(self, comm_instance, parsed_temperatures, *args, **kwargs):
current_temp = parsed_temperatures['B'][0]

while True:
	if current_temp >=50:
		GPIO.output(26,True)
	else:
		GPIO.output(26,False)



	def on_after_startup(self):
		self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

	def get_settings_defaults(self):
		return dict(url="https://en.wikipedia.org/wiki/Hello_world")

	def get_template_configs(self):
		return [
			dict(type="navbar", custom_bindings=False),
			dict(type="settings", custom_bindings=False)
		]

	def get_assets(self):
		return dict(
			js=["js/helloworld.js"],
			css=["css/helloworld.css"],
			less=["less/helloworld.less"]
		)

__plugin_name__ = "Hello World"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = HelloWorldPlugin()
