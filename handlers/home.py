from base import Base
import models

class HomeHandler(Base):
    def index(self):
        examples = models.Example.select()
        return self.render('index', examples = examples)