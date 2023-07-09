# Differential Drive type robot
import math
class DD_:
	def __init__(self, width, height, wheelR, min_v, max_v, min_w, max_w, max_mss, max_radss):
		# constant information
		self.width = width
		self.height = height
		self.wheelR = wheelR	# wheel radiua (m)
		self.min_v = min_v 		# ms^(-1) min linear velocity
		self.max_v = max_v 		# ms^(-1) max linear velocity
		self.min_w = min_w  	# rads^(-1) min angular velocity
		self.max_w = max_w		# rads^(-1) max angular velocity
		self.max_lin_mss = max_mss 		# ms^(-2) max acc/deceleration of robot
		self.max_rot_radss = max_radss 	# rads^(-2) max acc/deceleration of robot

		# robot navigation information
		self.x = 0
		self.y = 0
		self.theta = 0
		self.lin_vel = 0
		self.rot_vel = 0
  
	def InitPos(self, x, y, theta, v, w):
		self.x = x
		self.y = y
		self.theta = theta
		self.lin_vel = v
		self.rot_vel = w

	def StepDT(self, v, w, dt):
		self.x += v * math.cos(self.theta) * dt
		self.y += v * math.sin(self.theta) * dt
		self.theta += w*dt
	
	def GetCurPos(self):
		return (self.x, self.y, self.theta)