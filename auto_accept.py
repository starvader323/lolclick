import pyautogui as PAG
import psutil
import win32gui as w32g
import time
import os
# imagen_de_play = 
def locate_lol_accept(window_loc):
	for a in imagen_de_accept:
		try:
			img_locate = PAG.locateCenterOnScreen(a, region=window_loc)
			if img_locate == None: pass
			else: PAG.click(img_locate)
		except: pass
# def locate_lol_play(window_loc):
def find_window(window_name):
	win_hwnd = w32g.FindWindowEx(0,0,None,window_name)
	if win_hwnd == 0:
		time.sleep(10)
		return win_hwnd
	else:
		window_loc = w32g.GetWindowRect(win_hwnd)
		while window_loc == None: window_loc = w32g.GetWindowRect(win_hwnd)
		return window_loc

def find_process(procname,stillhere):
	if stillhere == True:
		return stillhere
	else:
		for proc in psutil.process_iter():
			if proc.name() == procname:
				pid = proc.pid
				return True, pid
			else: return None, None
main = 'D:\\lol_images'
for roots,dirs,files in os.walk(main):
	imagen_de_accept = files
#find process continuously
isthere, stillhere = find_process("League of Legends", None)
while isthere == None:
	isthere, stillhere = find_process("League of Legends", None)

while isthere:
	if find_window("League Of Legends (TM) Client") != 0:
		locate_lol_accept(find_window("League of Legends"))
	isthere = find_process("League of Legends", None)
	if isthere == None: 
		isthere = False
exit()

# not finished left off where I was wondering how to loop this in terms of not using any resuoursces until the game has ended