# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library





class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
             	  			octoprint.plugin.ShutdownPlugin,
						 octoprint.plugin.EventHandlerPlugin,
						  octoprint.plugin.TemplatePlugin,
						  octoprint.plugin.SettingsPlugin,
						  octoprint.plugin.AssetPlugin,
						  octoprint.plugin.BlueprintPlugin):
	
	def _initgpio(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(26, GPIO.OUT)
		self._gpioup = 1
		GPIO.output(26, True)
		
	
		
		

			
			
while True: # Run forever
GPIO.output(26, True)
    sleep(1)                  # Sleep for 1 second
GPIO.output(26, False)
    sleep(1)    

	

	
	
	

__plugin_name__ = "Hello World"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = HelloWorldPlugin()
