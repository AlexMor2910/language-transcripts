from auxf_srt import f_pipeline_srt
from auxf_ssa import f_pipeline_ssa
from pathlib import Path


def f_pipeline_ssa_srt():
    f_ssa_srt_handlers = {"srt": f_pipeline_srt, "ssa": f_pipeline_ssa, "ass": f_pipeline_ssa}
    f_ssa_srt_language = input("Please type the language: ")
    for _, __ in f_ssa_srt_handlers.items():
        for ___ in Path().rglob(f"*.{_}"):
            __(str(___), f_ssa_srt_language)
    print("Completed extracting texts from .srt, .ssa and .ass files.")
    return None


if __name__ == "__main__":
    f_pipeline_ssa_srt()