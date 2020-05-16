import os

class Structure(object):
    """docstring for Structure."""

    def __init__(self):
        super(Structure, self).__init__()
        self.self = self

        # Home of project
        self.base = "/Users/jamesonlee/Documents/projects/chinese"

        # This is where I store my notes
        self.lessons = os.path.join(self.base, "lessons")

        # This is where pipeline details are stored
        self.pipeline = os.path.join(self.base, "pipeline")
        self.classes = os.path.join(self.pipeline, "classes")
        self.functions = os.path.join(self.pipeline, "functions")

        # This is where new card packages are stored
        self.packages = os.path.join(self.base, "packages")
