import cx_Freeze

executables=[cx_Freeze.Executable("shortesttimefinder.py")]

cx_Freeze.setup(
    name="Shortest Time Finder",
    options={"build_exe": {"packages":["os"],
                            "include_files":["mrt.png"]}},
    executables=executables

)