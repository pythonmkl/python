# execute the program to use and download with the link on the clipboard
#
clipboard_content=$(xclip -selection clipboard -o)
echo $clipboard_content
python imgsrc.py $clipboard_content
