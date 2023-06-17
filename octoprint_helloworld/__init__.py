# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import RPi.GPIO as GPIO
from flask import jsonify, request


GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
						  octoprint.plugin.ShutdownPlugin,
						  octoprint.plugin.EventHandlerPlugin,
						  octoprint.plugin.TemplatePlugin,
						  octoprint.plugin.SettingsPlugin,
						  octoprint.plugin.AssetPlugin,
						  octoprint.plugin.BlueprintPlugin):
while True: # Run forever
    GPIO.output(26, GPIO.HIGH) # Turn on
    sleep(3)                  # Sleep for 1 second
    GPIO.output(26, GPIO.LOW)  # Turn off
    sleep(3)    
	





	def get_assets(self):
		return dict(
			js=["js/helloworld.js"],
			css=["css/helloworld.css"],
			less=["less/helloworld.less"]
		)

__plugin_name__ = "Hello World"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = HelloWorldPlugin()
