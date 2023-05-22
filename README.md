# Introduction
This is my personal website, hosted on pauluv.com. It is written using Flask and Bootstrap.

# Paths
The file <code>nirepage/paths.json</code> contains the paths to the 'content' and 'img' directories, where blog posts and website images are stored, respectively. Tose directories must be mapped to wherever those files are stored when running the docker container.

Posts are stored in a <code>category/title</code> folder structure within the <code>/content</code> directory. Inside, there should be a single <code>.md</file> for each language, along with images used in the post. The name of the <code>.md</code> file does not matter, as it follows the format <code>*_{lang_code}.md</code>, where <code>{lang_code}</code> is replaced with the corresponding language. Currently supported languages are English (en), Basque (eus), and Spanish (es).
