from pybpodapi.protocol import Bpod, StateMachine
my_bpod = Bpod(emulator_mode=True)
sma = StateMachine(my_bpod)
n_pwm_outputs = len([attr for attr in dir(
    Bpod.OutputChannels) if attr.startswith('PWM')])
for i in range(10):
    sma.add_state(
        state_name='State{}'.format(i),
        state_timer=1,
        state_change_conditions={Bpod.Events.Tup: 'State{}'.format(i + 1)},
        output_actions=[(getattr(Bpod.OutputChannels,
                                 f'PWM{(i % n_pwm_outputs) + 1}'), 255)])
sma.add_state(
    state_name='State10',
    state_timer=1,
    state_change_conditions={Bpod.Events.Tup: 'exit'},
    output_actions=[])
my_bpod.send_state_machine(sma)
my_bpod.run_state_machine(sma)
