init_code = """
if not "Car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Car'?")

Car = USER_GLOBAL['Car']

if not '__init__' in vars(Car):
    raise NotImplementedError("Where is '__init__' method?")

from inspect import signature

params = signature(Car.__init__).parameters
if not all((len(params) ==  3, 'self' in params, 'brand' in params, 'model' in params)):
    raise NotImplementedError("Check '__init__' arguments")

if not "ElectricCar" in USER_GLOBAL:
    raise NotImplementedError("Where is 'ElectricCar'?")

ElectricCar = USER_GLOBAL['ElectricCar']

if not issubclass(ElectricCar, Car):
    raise TypeError("'ElectricCar' should be a child of 'Car' class")

if not '__init__' in vars(ElectricCar):
    raise NotImplementedError("Where is '__init__' method?")

params2 = signature(ElectricCar.__init__).parameters
if not all((len(params2) ==  4, 'self' in params2, 'brand' in params2, 'model' in params2, 'battery_capacity' in params2)):
    raise NotImplementedError("Check '__init__' arguments")

if not "my_electric_car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'my_electric_car'?")

my_electric_car = USER_GLOBAL['my_electric_car']

if not isinstance(my_electric_car, ElectricCar):
    raise TypeError("'my_electric_car' should be an instance of 'ElectricCar' class")

if not hasattr(my_electric_car, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'my_electric_car' object?")
    
if not isinstance(my_electric_car.brand, str):
    raise TypeError("'brand' attribute should be of type 'str'")

if not hasattr(my_electric_car, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'my_electric_car' object?")

if not isinstance(my_electric_car.model, str):
    raise TypeError("'model' attribute should be of type 'str'")

if not hasattr(my_electric_car, 'battery_capacity'):
    raise NotImplementedError("Where is 'battery_capacity' attribute of 'my_electric_car' object?")

if not isinstance(my_electric_car.battery_capacity, int):
    raise TypeError("'battery_capacity' attribute should be of type 'int'")
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}

TESTS = {
    "First": [
        prepare_test(middle_code='''''',
                     test="",
                     answer="")]}