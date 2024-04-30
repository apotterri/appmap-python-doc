import sys
from datetime import datetime
from pathlib import Path

import appmap

output_directory = Path("tmp/appmap/codeblock")
output_directory.mkdir(parents=True, exist_ok=True)

timestamp = datetime.now().isoformat(timespec="seconds")
output_file = output_directory / f"{timestamp}.appmap.json"

r = appmap.Recording()
with r:
    import sample

    print(sample.C().hello_world(), file=sys.stderr)
    print(sample.C().hello_world(), file=sys.stderr)
    print(sample.C().hello_world(), file=sys.stderr)

with open(output_file, "w") as f:
    f.write(
        appmap.generation.dump(
            r,
            {
                "name": str(timestamp),
                "recorder": {
                    "type": "process",
                    "name": "process",
                },
            },
        )
    )
