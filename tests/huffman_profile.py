import base64
import cProfile
import pstats

import huffman.huffman


def read_text(file_name):
    with open(file_name, "rb") as f:
        text = f.read()

    return text


def read_image(file_name):
    with open(file_name, "rb") as f:
        text = str(base64.b64encode(f.read()))
    return text


test_cases = {
    "text": (
        ["data/pg1497.txt", "data/pg1727.txt", "data/pg6130.txt"],
        read_text,
        1000,
    ),
    "image": (["data/dj_official.jpg"], read_image, 200),
}

branching_factors = range(2, 24)
output_file = "data/stats_huffman.csv"


def write_header(f):
    f.write(
        "test_case,branching_factor,method_name,total_time,cumulative_time,per_call_time\n"
    )


def write_row(
        f,
        test_case: str,
        branching_factor: int,
        method_name: str,
        total_time: float,
        cumulative_time: float,
        per_call_time: float,
) -> None:
    f.write(
        f"{test_case},{branching_factor},{method_name},{total_time},{cumulative_time},{per_call_time}\n"
    )


def get_running_times(st):
    ps = st.strip_dirs().stats

    def is_heap_method(k):
        return (
                "heap" in k[2]
                or "create_encoding" in k[2]
                or (
                        "heap.py" in k
                        and (
                                "top" in k[2]
                                or "insert" in k[2]
                                or "_push_down" in k[2]
                                or "_bubble_up" in k[2]
                                or "_highest_priority_child_index" in k[2]
                        )
                )
        )

    keys = list(filter(is_heap_method, ps.keys()))

    return [(key[2], ps[key][2], ps[key][3], ps[key][3] / ps[key][1]) for key in keys]


def test_profile_huffman():
    with open(output_file, 'w') as f:
        write_header(f)

        for test_case, (file_names, read_func, runs) in test_cases.items():
            file_contents = [read_func(file_name) for file_name in file_names]
            for _ in range(runs):
                for b in branching_factors:
                    pro = cProfile.Profile()
                    for file_content in file_contents:
                        pro.runcall(huffman.huffman.huffman, file_content, b)

                    st = pstats.Stats(pro)

                    for method_name, total_time, cumulative_time, per_call_time in get_running_times(st):
                        write_row(f, test_case, b, method_name, total_time, cumulative_time, per_call_time)
