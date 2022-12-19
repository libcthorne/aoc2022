import functools
from collections import Counter
from pprint import pprint


f = open("day7input.txt")
contents = f.read().rstrip().split("\n")
state = functools.reduce(
    lambda state, cmd: {
        "current_directory": (
            "/"
            if cmd == "$ cd /"
            else (
                    "/".join(state["current_directory"].split("/")[:-2]) + "/"
                    if cmd == "$ cd .."
                    else (
                            state["current_directory"] + cmd.split("$ cd ")[1] + "/"
                            if cmd.startswith("$ cd ")
                            else state["current_directory"]
                    )
            )
        ),
        "directories": state["directories"] | {state["current_directory"]},
        "file_sizes": state["file_sizes"] | {
            state["current_directory"]: (
                state["file_sizes"].get(state["current_directory"], []) + [int(cmd.split(" ")[0])]
                if not cmd.startswith("dir ") and not cmd.startswith("$ cd ") and not cmd.startswith("$ ls")
                else state["file_sizes"].get(state["current_directory"], [])
            )
        },
    },
    contents,
    {
        "current_directory": "/",
        "directories": set(),
        "file_sizes": {},
    },
)


def chunk_path(path):
    """
    "/a/b/c/"

    =>

    [
        "/",
        "/a/",
        "/a/b/",
        "/a/b/c/",
    ]
    """
    return [
        path.rstrip("/").rsplit("/", split_count)[0] + "/"
        for split_count in reversed(range(path.count("/")))
    ]


def deep_get(obj, path):
    return functools.reduce(
        lambda branch, key: branch.get(key, {}),
        chunk_path(path),
        obj,
    )


def sum_file_sizes(directory):
    return sum(
        deep_get(tree, directory).get("__file_sizes__", [])
    ) + sum(
        sum_file_sizes(sub_directory)
        for sub_directory in deep_get(tree, directory)
        if sub_directory != "__file_sizes__"
    )


tree = functools.reduce(
    lambda tree, item: tree | functools.reduce(
        lambda children, directory: {
            directory: deep_get(tree, directory) | children
        },
        # Work from inside outwards
        reversed(chunk_path(item[0])),
        {"__file_sizes__": item[1]},
    ),
    state["file_sizes"].items(),
    {},
)

counter = Counter({
    directory: size
    for directory in state["directories"]
    if (size := sum_file_sizes(directory)) <= 100000 or True
})

pprint(counter)
# print(sum(counter.values()))

# Max:     70000000
# Current: 43313415

# >>> 70000000
#   - 43313415
#   = 26686585

#   30000000
# - 26686585
# = 3313415
