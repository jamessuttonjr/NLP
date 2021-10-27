from pathlib import Path
import imageio
from wordcloud import WordCloud

text = Path('RomeoAndJuliet.txt').read_text()

mask_image = imageio.imread("mask_heart.png")

wordcloud = WordCloud(colormap='prism',mask=mask_image,background_color='White')

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("RomeoAndJuiletHeart.png")

print("done")