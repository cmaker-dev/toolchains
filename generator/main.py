from pathlib import Path
from json import dumps


def write_toolchains():
    with open("./targets.txt") as f:
        for line in f:
            [arch, vendor, *os] = line.split("-")
            os = "-".join(os).strip().capitalize()
            path = Path(f"../toolchains/{arch}")
            path.mkdir(parents=True, exist_ok=True)
            with open(f"../toolchains/{arch}/{line.rstrip()}.cmake", "w") as toolchain:
                toolchain.write(f"""
set(CMAKE_SYSTEM_NAME {os})
set(CMAKE_SYSTEM_PROCESSOR {arch})
set(CMAKE_C_COMPILER clang)
set(CMAKE_C_COMPILER_TARGET {line.strip()})
set(CMAKE_CXX_COMPILER clang++)
set(CMAKE_CXX_COMPILER_TARGET {line.strip()})
                """.strip().lstrip())


def write_toolchains_json():
    json = []
    for path in Path("../toolchains").iterdir():
        if path.is_dir():
            for file in path.iterdir():
                if file.is_file() and file.suffix == ".cmake":
                    json.append({
                        "name": file.stem,
                        "path":  "./" + str(file).lstrip("../")
                    })

    with open("../toolchains.json", "w") as f:
        f.write(dumps(json, indent=4))


if __name__ == "__main__":
    write_toolchains()
    write_toolchains_json()
