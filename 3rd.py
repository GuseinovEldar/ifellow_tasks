class BaseConverter():
    def __init__(self, degree):
        self.degree = degree

    def converttokelvin(self):
        print (self.degree, "градус по Цельсию это", self.degree + 273.15, "по Кельвину")

    def converttofahrenheit (self):
        print (self.degree, "градус по Цельсию это",  self.degree * 1.8 + 32, "градус по Фарингейту")

test_degree = BaseConverter(99)

test_degree.converttokelvin()
test_degree.converttofahrenheit()