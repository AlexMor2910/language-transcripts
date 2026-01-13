from auxf_transcript_api import f_get_languages, f_input


def f_pipeline_tapi():
    main_tapi_identifier: str = input("Please write the YouTube video link identifier:\n>")
    main_tapi_transcript_dict: dict|None = f_get_languages(main_tapi_identifier)
    if not main_tapi_transcript_dict:
        return None
    if main_tapi_transcript_dict:
        print("Available languages:")
        for _ in main_tapi_transcript_dict.values():
            print(_[0], _[1])
    try:
        f_input(main_tapi_identifier, main_tapi_transcript_dict)
    except Exception as e:
        print(f"{e}")
        return None


if __name__ == "__main__":
    f_pipeline_tapi()

