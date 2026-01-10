from main_srt_ssa import f_pipeline_ssa_srt
from main_transcript_api import f_pipeline_tapi

if __name__ == "__main__":
    main_input = input("Plese enter 's' for subtitles, 't' for YouTube transcripts, 'i' for instructions,"
                       " and 'x' for exiting.\n>")
    if main_input.lower() == "s":
        f_pipeline_ssa_srt()
    elif main_input.lower() == "t":
        f_pipeline_tapi()
    elif main_input.lower() == "i":
        print("Instructions")
    elif main_input.lower() == "x":
        print("Have a nice day!")
        pass
    else:
        print("Invalid input. Exiting.")
        pass
