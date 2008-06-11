#!/usr/bin/env python
import tc3625
import time

ctlr=tc3625.TC3625()

ctlr.print_all()
print 

units = ctlr.get_working_units()
print units
if units=='C':
    ctlr.set_working_units('F')
else:
    ctlr.set_working_units('C')
units = ctlr.get_working_units()
print units

setpt = ctlr.get_setpt()
print setpt
ctlr.set_setpt(setpt-5)
for i in range(0,100):
    print ctlr.get_setpt()


#ctlr.print_all()

if 0:
    
    ctlr.power_off()
    ctlr.set_shutdown_if_alarm(tc3625.SHUTDOWN_IF_ALARM_ON)
    ctlr.set_proportional_bandwidth(30)
    ctlr.set_integral_gain(0)
    ctlr.set_derivative_gain(0)
    ctlr.set_working_units(tc3625.TEMP_C)
    ctlr.set_high_alarm(40)
    ctlr.set_output_polarity(tc3625.POLARITY_HEAT_WP2POS_WP1NEG)
    ctlr.set_over_current_restart_type(tc3625.OVER_CURRENT_RESTART_MAX_ATTEMPT)
    ctlr.set_over_current_restart_num(5)
    ctlr.set_control_type(tc3625.CONTROL_TYPE_COMPUTER)
    ctlr.set_setpt(0)
    ctlr.print_all_prop()
    # print 
#     prop = {
#         'JP3 display': tc3625.JP3_DISPLAY_ON,
#         'alarm deadband':2.0,
#         'alarm latch': tc3625.ALARM_LATCH_ON,
#         }
#     ctlr.set_by_dict(prop)
#     ctlr.print_all_prop()
#     print

#     prop = {
#         'JP3 display': tc3625.JP3_DISPLAY_OFF,
#         'alarm deadband':1.0,
#         'alarm latch': tc3625.ALARM_LATCH_OFF,
#         }

#     ctlr.set_by_dict(prop)
#     ctlr.print_all_prop()
#     print

if 0:
    ctlr.set_shutdown_if_alarm(tc3625.SHUTDOWN_IF_ALARM_ON)
    ctlr.set_proportional_bandwidth(50)
    #ctlr.set_integral_gain(0)
    ctlr.set_integral_gain(0.1)
    ctlr.set_derivative_gain(0)
    ctlr.set_working_units(tc3625.TEMP_C)
    ctlr.set_high_alarm(40)
    ctlr.set_output_polarity(tc3625.POLARITY_HEAT_WP2POS_WP1NEG)
    ctlr.set_over_current_restart_type(tc3625.OVER_CURRENT_RESTART_MAX_ATTEMPT)
    ctlr.set_over_current_restart_num(5)
    #ctlr.set_control_type(tc3625.CONTROL_TYPE_COMPUTER)
    ctlr.set_heat_multiplier(0.05)
    ctlr.set_cool_multiplier(0.05)
    ctlr.set_control_type(tc3625.CONTROL_TYPE_PID)
    ctlr.set_setpt(10)
    ctlr.print_all_prop()
    print 

    ctlr.power_on()
    
    ctlr.print_all_prop()
    print 
    t0 = time.time()
    t1 = time.time()
    while t1- t0 < 60.0:
        print_tpl = (t1-t0,ctlr.get_input1(), ctlr.get_power_output(), ctlr.get_output_current())
        print 't: %1.2f, temp: %1.2f, power: %1.2f, curr: %f'%print_tpl
        time.sleep(0.25)
        t1 = time.time()


    ctlr.power_off()

    ctlr.print_all_prop()
    print 

ctlr.close()
