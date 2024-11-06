"""
Ryan Siu
Runs imgd with student output against expected output
and produces images showing the pixel differences.
"""
import subprocess
import os

import hw3

PLOTS = [
    "line_plot_bachelors.png",
    "bar_chart_high_school.png",
]
IMGD_ARGS = [
    "--pixel-correct-threshold", "0.99",
    "--diff-mode", "always",
    "--correct-colour", "ffffff",
]


def run_imgd(expected, actual, args=IMGD_ARGS):
    """
    Runs imgd of student output against expected.
    Produces diff image only if both student and expected output exist.
    """
    if not os.path.exists(actual):
        print(f"Could not find the file: {actual} after running hw3.py\n"
              "Make sure to call the plotting functions in your main method!")
    elif not os.path.exists(expected):
        print(f"Could not find the file: {expected}\n")
    else:
        print(f"Running image comparison tool on {actual}...")
        output = subprocess.run(["/opt/ed/bin/imgd", expected, actual]
                                + args, capture_output=True)
        output = output.stdout.decode("utf-8")
        if "Your image's" in output:
            output += ("Be sure that you call sns.set() and are passing"
                       " in bbox_inches='tight' to your savefig call\n")
        print(output)
        os.rename("diff.png", f"{os.path.splitext(actual)[0]}_diff.png")


def main():
    hw3.main()
    print()
    for plot_name in PLOTS:
        run_imgd(f"expected/{plot_name}", plot_name)


if __name__ == "__main__":
    main()
