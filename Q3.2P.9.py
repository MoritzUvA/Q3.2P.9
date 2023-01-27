def cheat(exercise):
    if exercise == "Q1.2P.1":
        print("import numpy as np # This line of code needs to be added\nanother_array = np.zeros((2, 4, 6))")
    elif exercise == "Q1.2P.2":
        print("another_array[-1, 0, 2] # -1 returns the last element of a dimension\n# 0.0")
    elif exercise == "Q1.2P.4":
        print("# %paste does not work in a python script, because it is a specific command for the iPython console.",
              "It is not valid\n# python code, so it cannot be written in a script.")
    elif exercise == "Q1.2P.6":
        print("# To install the package, you can write: pip install pip-install-test")
    else:
        print("Go do it yourself yourself!")
