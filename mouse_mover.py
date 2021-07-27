from ctypes import Structure, windll, c_uint, sizeof, byref
import time

TIMEOUT_S = 50
move_dxdy = 1

mouse_event = windll.user32.mouse_event


class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

def move_mouse_pointer():
	global move_dxdy
	move_dxdy = move_dxdy * -1
	mouse_event(1, move_dxdy, move_dxdy, 0, 0)
	pass

windll.kernel32.SetConsoleTitleW("Idle mouse mover.")

while True:
	duration = TIMEOUT_S - get_idle_duration();
	print(f"[{time.strftime('%H:%M:%S')}] duration: {duration}, idle:{TIMEOUT_S - duration}");
	if duration > 0:
		time.sleep(duration)
	else:
		move_mouse_pointer()