from PIL import Image, ImageFont, ImageDraw
import pandas as pd

def main():
    print("Sedang Diproses!")
    names = pd.read_csv('peserta.csv')
    for i,row in names.iterrows():
        name = str(row['Name'])
        name = name.title()
        word_length = len(name.split(" "))

        empty_img = Image.open("sertif.png").convert("RGB")


        if(word_length > 4):
            font_size = 70
            bottom = -50
        else:
            font_size = 80
            bottom = -50


        W,H = empty_img.size 
        font = ImageFont.truetype(r"Poppins-Bold.ttf", font_size)
        (_, _, w, h) = font.getbbox(name)
        width = ((W-w)/2)
        height = ((H-h)/2.43) + bottom


        image_editable = ImageDraw.Draw(empty_img)
        image_editable.multiline_text((width,height), name, (35, 57, 75), font=font)
        empty_img.save("hasil/{}.pdf".format(name.replace(" ", "_")))
        print('Processed {} Rows'.format(i))
    print("Process Complete, Silahkan Cek Folder Hasil!")

if __name__ == "__main__":
    main()