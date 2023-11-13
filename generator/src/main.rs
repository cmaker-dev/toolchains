


fn main() {
    let targets_file = std::fs::read_to_string("./targets.txt").unwrap();

    for line in targets_file.lines() {
        let stuff = line.split('-').collect::<Vec<&str>>();
        let [arch, vendor, os @ ..] = stuff.as_slice() else {
            panic!("Invalid target format");
        };
        let mut os = os.join("-");
        println!("{arch} {vendor} {os}");
        os.get_mut(0..1).unwrap().make_ascii_uppercase();
        let temp = format!(r"
set(CMAKE_SYSTEM_NAME {os})
set(CMAKE_SYSTEM_PROCESSOR {arch})
set(CMAKE_C_COMPILER clang)
set(CMAKE_C_COMPILER_TARGET {line})
set(CMAKE_CXX_COMPILER clang++)
set(CMAKE_CXX_COMPILER_TARGET {line})
");
        if !std::path::Path::new(format!("../toolchains/{arch}").as_str()).exists() {
            std::fs::create_dir(format!("../toolchains/{arch}")).unwrap();
        }

        std::fs::write(format!("../toolchains/{arch}/{line}.cmake"), temp).unwrap();



    }

}
