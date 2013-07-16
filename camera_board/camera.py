import datetime
import os
import re

class Camera:
  model = ""
  usb_location = ""
  def detect_gphoto(self):
    location = os.popen('which gphoto2').read().rstrip()
    if location == "":
      raise Exception("gphoto2 not found!")

  def setup(self):
    autodetected = os.popen('gphoto2 --auto-detect').read().split('\n')
    camera_string = filter(None, autodetected)[-1].rstrip()

    if re.match("{-}+", camera_string):
      raise Exception("Camera cannot be found!")
    else:
      self.model, self.usb_location = self.parse_camera_string(camera_string)

  def parse_camera_string(self, camera_string):
    camera_parts = camera_string.split()
    usb_location = camera_parts[-1]
    model_parts = camera_parts[0:(len(camera_parts)-1)]
    model = " ".join(model_parts)

    return (model, usb_location)

  def print_camera_info(self):
    print "Camera: " + self.model
    print "USB Location: " + self.usb_location

  def capture_photo(self):
    date = str(datetime.datetime.now())
    filename = "image_" + date + ".cr2"

    cmd = "gphoto2 --capture-image-and-download --filename=" + filename
    os.popen(cmd)

    return filename
