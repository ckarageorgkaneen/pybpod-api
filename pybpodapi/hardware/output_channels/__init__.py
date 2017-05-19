from pybpodapi.settings import BPOD_VERSION
from pybpodapi.settings import BPOD_FIRMWARE_VERSION

if BPOD_VERSION == '0.7.5' and BPOD_FIRMWARE_VERSION == '9':
	from pybpodapi.hardware.output_channels.bpod0_7_5_fw9 import OutputChannel
else:
	from pybpodapi.hardware.output_channels.bpod0_7_5_fw9 import OutputChannel
