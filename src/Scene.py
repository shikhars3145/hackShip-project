# Class responsible for event handling and rendering
class Scene:
    def handleEvent(self, event):
        """Handle pygame event."""
        pass

    def render(self, screen):
        """Render contents on screen."""
        pass

    def checkCollision(self):
        """Check if Collision happens between garbage and the player"""
        pass

    def nextScene(self):
        """Return scene object for next frame"""
        # By default, do not transition to another scene.
        return self
