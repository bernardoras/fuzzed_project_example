import atheris
import sys
from fuzzed_project_example.parse_people_data import parse_file

def TestOneInput(data):

    try:

        input_data = data.decode("utf-8", errors="ignore")
        parse_file(input_data)

    except ValueError:

        return

if __name__ == "__main__":

    # Atheris instrumentation
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()
