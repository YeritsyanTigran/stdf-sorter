from reader.stdf.stdf_reader import Reader

files = ['./data/demofile.stdf']
std = Reader()
for input_file in files:
    std.load_stdf_file(input_file)
    for rec_name, header, body in std:
        print(rec_name, header, body)
