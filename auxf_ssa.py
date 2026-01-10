from auxf_srt import f_write_txt_file
import pysubs2


def f_clean_name_ssa(f7_filename: str) -> str:
    f7_removals = str.maketrans("", "", "[].-")
    f7_cleaned_filename: str = f7_filename.removesuffix(".ssa").removesuffix(".ass")
    return f7_cleaned_filename.translate(f7_removals)


def f_handle_ssa(f6_filename: str)-> list[str]:
    f6_subs = pysubs2.load(f6_filename)
    f6_ignore_styles: list[str] = ['staff', 'op', 'ed', 'title', 'screen', 'fx']
    f6_complete_text: list[str] = []
    for _ in f6_subs:
        if _.is_comment:
            continue
        if _.text.startswith('m '):
            continue
        style_lower = _.style.lower()
        if any(__ in style_lower for __ in f6_ignore_styles):
            continue
        f6_complete_text.append(_.plaintext.strip())
    return f6_complete_text


def f_pipeline_ssa(main_ssa_filepath: str, main_ssa_language: str):
    try:
        main_ssa_clean_name: str = f_clean_name_ssa(main_ssa_filepath)
        main_ssa_complete_text: list = f_handle_ssa(main_ssa_filepath)
        f_write_txt_file(main_ssa_complete_text, main_ssa_clean_name, main_ssa_language)
        return None
    except Exception as e:
        print(f"{e}")
        return None
