# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BMC)   # Use physical pin numbering
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)   # Set pin 8 to be an output pin and set initial value to low (off)





class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
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
			
			
			
while True:
	GPIO.output(26, GPIO.HIGH) # Turn on
	sleep(1)                  # Sleep for 1 second
	GPIO.output(26, GPIO.LOW)  # Turn off
	sleep(1)                  # Sleep for 1 second
		)
	
	
	
	

__plugin_name__ = "Hello World"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = HelloWorldPlugin()
