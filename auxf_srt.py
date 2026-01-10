import chardet, os, srt, re


def f_detect_encoding(f4_filepath: str)->str:
    with open(f4_filepath, 'rb') as f:
        return chardet.detect(f.read())['encoding']


def clean_subtitle_text(f1_subtitle: str) -> str:
    return re.sub(r'<[^>]*>', '', f1_subtitle).replace('\n', ' ')


def f_extract_subtitles(f5_filepath: str)->list:
    with open(f5_filepath, 'r', encoding=f_detect_encoding(f5_filepath)) as f:
        subs: list = list(srt.parse(f.read()))
        return [clean_subtitle_text(_.content) for _ in subs]


def f_name_file(f2_filename: str, f2_language: str)->str:
    f2_written_filename: str = f"Subtitles_{f2_filename}_{f2_language}.txt"
    if not os.path.exists(f2_written_filename):
        return f2_written_filename
    f2_base_name: str = f"Subtitles_{f2_filename}_{f2_language}"
    f2_extension: str = ".txt"
    f2_written_filename_new: str = f"{f2_base_name}{f2_extension}"
    f2_counter: int = 1
    while os.path.exists(f2_written_filename_new):
        f2_written_filename_new = f"{f2_base_name}({f2_counter}){f2_extension}"
        f2_counter += 1
    return f2_written_filename_new


def f_write_txt_file(f3_clean_text: list, f3_filename: str, f3_language: str):
    f3_transcript_string = "\n".join(f3_clean_text)
    f3_written_filename: str = f_name_file(f3_filename, f3_language)
    with open(f3_written_filename, "a", encoding="utf-8") as f:
        f.write(f3_transcript_string)
    return None


def f_pipeline_srt(main_srt_filepath: str, main_srt_language: str)->None:
    try:
        main_srt_filename: str = main_srt_filepath.removesuffix(".srt").replace(".", " ")
        main_srt_clean_text: list = f_extract_subtitles(main_srt_filepath)
        f_write_txt_file(main_srt_clean_text, main_srt_filename, main_srt_language)
        return None
    except Exception as e:
        print(f"{e}")
        return None
