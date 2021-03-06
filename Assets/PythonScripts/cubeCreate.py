import math

red = unity.Color.red
blue = unity.Color.blue
green = unity.Color.green
yellow = unity.Color.yellow
white = unity.Color.white

class Sphere():
	def __init__(self, x, y, z, color):
		self._x = x
		self._y = y
		self._z = z
		self._color = color
		self._object = unity.GameObject.CreatePrimitive(unity.PrimitiveType.Sphere)
		self._object.transform.position = unity.Vector3(x, y, z)
		self._object.renderer.material.color = self._color


	def changeColor(self, newColor):
		self._object.renderer.material.color = newColor

	def getTransform(self):
		return self._object.transform

	def update(self):
		pass

	def getObject(self):
		return self._object

class Snowman():
	def __init__(self, x, y, z):
		self._head = Sphere(x, y + 1, z, white)
		self._body = Sphere(x, y, z, white)
		self._bottom = Sphere(x, y - 1, z, white)
		self._object = unity.GameObject()
		self._object.name = "Snowman"
		self._head.getTransform().parent = self._object.transform
		self._body.getTransform().parent = self._object.transform
		self._bottom.getTransform().parent = self._object.transform

	def update(self):
		pass
		#self._obj.AddComponent(unity.Text)

	def getObject(self):
		return self._object


class Tree():
	def __init__(self, x, y, z, depth, scale):
		self._object = unity.GameObject("Tree")
		if depth > 6:
			depth = 6
		self.draw(x, y, z, 90.0, depth, scale)

	def draw(self, x1, y1, z1, angle, depth, scale):
		if depth != 0:
			x2 = x1 + int(math.cos(math.radians(angle)) * depth * scale)
			y2 = y1 + int(math.sin(math.radians(angle)) * depth * scale)
			z2 = z1 + int(math.cos(math.radians(angle)) * depth * scale)
			self.drawBranch(x1, y1, z1, x2, y2, z2, red)
			self.draw(x2, y2, z2, angle - 20, depth - 1, scale)
			self.draw(x2, y2, z2, angle + 20, depth - 1, scale)

	def drawBranch(self, x1, y1, z1, x2, y2, z2, color):
		branch = unity.GameObject("Branch")
		branch.transform.parent = self._object.transform
		line = branch.AddComponent("LineRenderer")
		line.SetPosition(0, unity.Vector3(x1, y1, z1))
		line.SetPosition(1, unity.Vector3(x2, y2, z2))
		line.SetWidth(.25, .25)
		
	def update(self):
		pass