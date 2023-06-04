# Introduction
This is my personal website, hosted on pauluv.com. It is written using Flask and Bootstrap.

# Paths
Posts are stored in a <code>category/title</code> folder structure within the <code>nirepage/content</code> directory. Inside, there should be a single <code>.md</code> file for each language, along with images used in the post. The name of the <code>.md</code> file does not matter, as long as it follows the format <code>*_{lang_code}.md</code>, where <code>{lang_code}</code> is replaced with the corresponding language. Currently supported languages are English (en), Basque (eus), and Spanish (es).
Images for the gallery are stored in a <code>gallery</code> folder, not included in the repo for space reasons. The script <code>add_captions.py</code> can be used to create captions for the images in the correct format, as long as the images filenames start with the date: <code>YYYYMMDD_*.jpg</code>.
