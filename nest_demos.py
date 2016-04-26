import nest

def init_nest():
    username = 'will+nestdev@unikey.com'
    password = 'c*8qyHcnB!62'

    napi = nest.Nest(username, password)
    return napi

def nest_set_away(napi, is_away):
    if len(napi.structures):
        napi.structures[0].away = is_away


def get_nest_temp(napi):
    if len(napi.devices):
        return nest.utils.c_to_f(napi.devices[0].temperature)
    else:
        return 0;


def set_nest_temp(napi, temp):
    if len(napi.devices):
        napi.devices[0].temperature = nest.utils.f_to_c(temp)
if __name__ == '__main__':
	napi = init_nest()

	for structure in napi.structures:
	    print('Name: %s' % structure.name)
	    print('Away: %s' % structure.away)
	
	    for device in structure.devices:
	        print( ' Device: %s' % device.name)
	        print( ' Temp: %0.1f' % device.temperature)


	set_nest_temp(napi, 88)
	print(get_nest_temp(napi))
	print(get_nest_target(napi))
