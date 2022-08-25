import os
import sys
import eyed3

def main():
    if len(sys.argv) < 2:
        print("[?] Usage: python3 lyric-extract.py <album-directory>")
        sys.exit()

    path = sys.argv[1]

    print("[+] Extracting lyrics from this directory: " + str(path))

    if not os.path.isdir(path):
        print("[!] Directory invalid!")
        sys.exit()

    directory = os.fsencode(path)

    for root, subdirs, files in os.walk(directory):
         path = os.path.relpath(root, directory).split(os.sep.encode())
         for file in files:
             filename = os.fsdecode(file)
             if filename.endswith(".mp3"):
                 mp3_file_ptr = os.path.join(root.decode(), filename)

                 print("[+] Extracting: " + mp3_file_ptr)

                 track = eyed3.load(mp3_file_ptr)
                 tag = track.tag

                 base_song_name = os.path.splitext(filename)[0]
                 lrc_file_ptr = os.path.join(root.decode('utf-8'), base_song_name + ".lrc")
                 lyric_file = open(lrc_file_ptr, "wb")
                 if len(tag.lyrics) > 0:
                     lyrics = tag.lyrics[0].text
                     lyric_file.write(lyrics.encode("utf-8"))
                 else:
                     print("[!] Track has no lyric data! Writing a blank LRC...")
                 lyric_file.close()

if __name__ == "__main__":
     main()
