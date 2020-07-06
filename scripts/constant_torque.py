import time

import gym
import numpy as np

print("Creating gym object...")
# Creates and returns Pendulum env object
env_pend = gym.make("pendulum-v0")

print("Setting to constant torque")
action = np.array([2.0])

s_next, r, done, _ = env_pend.step(action)
time.sleep(1)
s_next, r, done, _ = env_pend.step(action)

print("obs: {}".format(s_next))
print("state: {}".format(env_pend.state))

print("Sleeping...")
time.sleep(3)

print("\nDone!")


#
