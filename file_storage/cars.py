class Car():

    def read_makes(self):
        with open('car_makes.txt', 'r') as makes:
            car_makes = makes.readlines()
            # print(car_makes)
            return car_makes

    def read_models(self):
        with open('car_models.txt', 'r') as models:
            car_models = models.readlines()
            # print(car_models)
            return car_models

    def makes_and_models(self):
        makes = self.read_makes()
        models = self.read_models()
        new_dict = dict()
        print(new_dict)
        for model in models:
            for make in makes:
                if model[:1] == make[:1]:
                    if make in new_dict:
                        new_dict[make].append(model[2:])
                    else:
                        new_dict[make] = [model[2:]]
        return(print(new_dict))

car = Car()
car.makes_and_models()