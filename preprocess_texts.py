import argparse
import text
from utils.utils import load_filepaths_and_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_extension", default="cleaned")
    parser.add_argument("--text_index", default=1, type=int)
    parser.add_argument(
        "--filelists",
        nargs="+",
        default=[
            "filelists/ljs_audio_text_val_filelist.txt",
            "filelists/ljs_audio_text_test_filelist.txt",
        ],
    )
    parser.add_argument("--text_cleaners", nargs="+", default=["english_cleaners2"])

    args = parser.parse_args()
    for filelist in args.filelists:
        print("START:", filelist)
        new_filelist = filelist + "." + args.out_extension
        filepaths_and_text = load_filepaths_and_text(filelist)
        size = len(filepaths_and_text)
        with open(new_filelist, "a", encoding="utf-8") as f:
            for i in range(3586, size):
                try:
                    original_text = filepaths_and_text[i][args.text_index]
                    cleaned_text = text._clean_text(original_text, args.text_cleaners)

                    #filepaths_and_text[i][args.text_index] = cleaned_text
                    print(f"Progress: {str(i)}/{str(size)} : {filepaths_and_text[i]}\t\t\t\t.", end="\r")
                    #print(filepaths_and_text[i])
                    f.writelines(filepaths_and_text[i][0] + "|" + cleaned_text + "\n")
                except Exception as e:
                    print(i)
                    break
        print(f"\0\nDone for file {filelist}!")