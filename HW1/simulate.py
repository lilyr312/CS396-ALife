import dm_control
from dm_control import mujoco
import time

m = mujoco.MjModel.from_xml_path("cs396-A1.xml")
d = mujoco.MjData(m)
r = mujoco.Renderer(m)
v = mujoco.viewer.launch_passive(m, d)

for _ in range(1000):
	mn = ["lb_motor", "rb_motor", "lf_motor", "rf_motor"]
	mi = [mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_ACTUATOR, n) for n in mn]
	for i in mi:
		d.ctrl[i] = 1.0

	mujoco.mj_step(m, d)
	v.sync()
	time.sleep(1/100)
v.close()
