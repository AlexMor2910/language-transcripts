from youtube_transcript_api import YouTubeTranscriptApi
import ast, os

def f_get_languages(f1_video_id: str) -> dict|None:
    try:
        f1_api = YouTubeTranscriptApi()
        f1_dict: dict = {}
        f1_count: int = 0
        f1_transcript_list = f1_api.list(f1_video_id)
        for _ in f1_transcript_list:
            f1_dict[_.language_code] = [f1_count+1, _.language]
            f1_count += 1
        return dict(sorted(f1_dict.items(), key=lambda item: item[1][0]))
    except:
        print(f"Could not retrieve a transcript for {f1_video_id} because there aren't any transcripts.")
        return None


def f_create_text_doc(f2_video_id: str, f2_number: int, f2_language_dict: dict)->None:
    try:
        f2_transcript_string = ""
        f2_api = YouTubeTranscriptApi()
        f2_language_list: list[str] = [next(__ for __, _ in f2_language_dict.items() if _[0] == f2_number)]
        f2_transcript = f2_api.fetch(f2_video_id, languages=f2_language_list)
        for _ in f2_transcript.snippets:
            f2_transcript_string += _.text
        f2_filename = f"Transcript_{f2_video_id}_{f2_language_list[0]}.txt"
        if not os.path.exists(f2_filename):
            with open(f2_filename, "a", encoding="UTF-8") as f:
                f.write(f2_transcript_string)
            return None
        base_name = f"Transcript_{f2_video_id}_{f2_language_list[0]}"
        extension = ".txt"
        f2_filename = f"{base_name}{extension}"
        counter = 1
        while os.path.exists(f2_filename):
            f2_filename = f"{base_name}({counter}){extension}"
            counter += 1
        with open(f2_filename, "a", encoding="UTF-8") as f:
            f.write(f2_transcript_string)
            return None
    except StopIteration:
        print(f"Please input a valid language number. {f2_number} is not accepted.")
        return None


def f_input(f3_video_id: str, f3_language_dict: dict):
    f3_input = input("Please input the nummber of the languages you want in a list."
          "\nIf you want all, write 'all'."
          "\nIf you want to exit, write 'x'."
          "\n>")
    if f3_input.startswith("[") and f3_input.endswith("]"):
        f3_list_numbers: list = ast.literal_eval(f3_input)
        for _ in f3_list_numbers:
            f_create_text_doc(f3_video_id, _, f3_language_dict)
            print("Transcript(s) extracted.")
    elif f3_input.lower() == "all":
        for _ in f3_language_dict.values():
            f_create_text_doc(f3_video_id, _[0], f3_language_dict)
            print("Transcript(s) extracted.")
    elif f3_input.lower() == "x":
        print("Have a nice day!")
        return None
    else:
        print("Invalid input. Exiting.")
        return None


if __name__ == "__main__":
    video_id: str = "oaOG1xOk7XY"
    transcript_dict: dict | None = f_get_languages(video_id)

    if not transcript_dict:
        print("Exit condition")
    if transcript_dict:
        print(transcript_dict)

    f_create_text_doc(video_id, 5, transcript_dict)
