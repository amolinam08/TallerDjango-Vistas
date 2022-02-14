from ..models import Measurement, Variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def update_measurement(var_pk, new_var):
    new_variable = Variable.objects.get(pk=new_var["variable"])
    measurement = Measurement.objects.filter(id=var_pk).update(variable = new_variable, value= new_var["value"], unit = new_var["unit"], place = new_var["place"], dateTime= new_var["dateTime"])
    return measurement

def create_measurement(new_var):
    new_variable = Variable.objects.get(pk=new_var["variable"])
    measurement = Measurement(variable = new_variable, value= new_var["value"], unit = new_var["unit"], place = new_var["place"], dateTime= new_var["dateTime"])
    measurement.save()
    return measurement

def delete_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    measurement.delete()
    return measurement
