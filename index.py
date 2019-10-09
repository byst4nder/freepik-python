from flask import Flask, request, render_template
import glob
import os

app = Flask(__name__)

@app.route('/chuli', methods=['POST'])
def chuli():
    from PIL import Image,ImageFont,ImageDraw
    import time
    from tim import clipResizeImg,xq_2,da_sy

    data = request.get_data()
    dir_id = request.form.get('id')
    ys = request.form.get('ys')
    if int(dir_id) <= 1000:
        path = 'G:/1-1000/' + str(dir_id)
    else:
        path = 'G:/1000-2000/' + str(dir_id)

    # 删除桌面upload文件夹所有文件
    print('清空桌面upload文件夹')
    for i in os.listdir('C:/Users/wu/Desktop/upload/'):
        os.remove('C:/Users/wu/Desktop/upload/'+i)
    
    print('制作首图')
    if request.form.get('line_2'):
        img_list = request.form.getlist('img_list[]')
        if ys == 'x1':
            bg = clipResizeImg(
                **{'ori_img': path + '/' + img_list[0], 'dst_w': 800, 'dst_h': 800})

        if ys == 'x4':
            bg = Image.new('RGB', (800, 800), (255, 255, 255))

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[0], 'dst_w': (
                800-20)/2, 'dst_h': (800-20)/2}).convert('RGBA')
            bg.paste(im, (0, 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[1], 'dst_w': (
                800-20)/2, 'dst_h': (800-20)/2}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[2], 'dst_w': (
                800-20)/2, 'dst_h': (800-20)/2}).convert('RGBA')
            bg.paste(im, (0, int(800-(800-20)/2)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[3], 'dst_w': (
                800-20)/2, 'dst_h': (800-20)/2}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), int(800-(800-20)/2)), im)
            im.close()
            
        if ys == 'x9':
            bg = Image.new('RGB', (800, 800), (255, 255, 255))

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[0], 'dst_w': (
                800-40)/3, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (0, 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[1], 'dst_w': (
                800-40)/3, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[2], 'dst_w': (
                800-40)/3, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[3], 'dst_w': (
                800-40)/3, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (0, int((800-40)/3+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[4], 'dst_w': (
                800-40)/3, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), int((800-40)/3+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[5], 'dst_w': (
                800-40)/3, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), int((800-40)/3+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[6], 'dst_w': (
                800-40)/3, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (0, int(800-(800-40)/3+1)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[7], 'dst_w': (
                800-40)/3, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), int(800-(800-40)/3+1)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[8], 'dst_w': (
                800-40)/3, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), int(800-(800-40)/3+1)), im)
            im.close()

        if ys == 'x16':
            bg = Image.new('RGB', (800, 800), (255, 255, 255))

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[0], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (0, 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[1], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (int((800-60)/4+20), 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[2], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (int(((800-60)/4+20)*2), 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[3], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (int(800-(800-60)/4), 0), im)

            # 第二排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[4], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (0, int((800-60)/4+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[5], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (int((800-60)/4+20), int((800-60)/4+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[6], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (int(((800-60)/4+20)*2), int((800-60)/4+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[7], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (int(800-(800-60)/4), int((800-60)/4+20)), im)

            # 第三排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[8], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (0, int(((800-60)/4+20)*2)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[9], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (int((800-60)/4+20), int(((800-60)/4+20)*2)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[10], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (int(((800-60)/4+20)*2), int(((800-60)/4+20)*2)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[11], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (int(800-(800-60)/4), int(((800-60)/4+20)*2)), im)

            # 第四排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[12], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (0, int(800-(800-60)/4)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[13], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (int((800-60)/4+20), int(800-(800-60)/4)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[14], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (int(((800-60)/4+20)*2), int(800-(800-60)/4)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[15], 'dst_w': (
                800-60)/4, 'dst_h': (800-60)/4}).convert('RGBA')
            bg.paste(im, (int(800-(800-60)/4), int(800-(800-60)/4)), im)
            im.close()

        if ys == 'x6':
            bg = Image.new('RGB', (800, 800), (255, 255, 255))

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[0], 'dst_w': (
                800-20)/2, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (0, 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[1], 'dst_w': (
                800-20)/2, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[2], 'dst_w': (
                800-20)/2, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (0, int((800-40)/3+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[3], 'dst_w': (
                800-20)/2, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), int((800-40)/3+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[4], 'dst_w': (
                800-20)/2, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (0, int(800-(800-40)/3+1)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[5], 'dst_w': (
                800-20)/2, 'dst_h': int((800-40)/3)}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), int(800-(800-40)/3+1)), im)

            
            im.close()
            

        if ys == 'x8':
            bg = Image.new('RGB', (800, 800), (255, 255, 255))

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[0], 'dst_w': (800-20)/2, 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (0, 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[1], 'dst_w': (800-20)/2, 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[2], 'dst_w': (800-20)/2, 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (0, int((800-60)/4+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[3], 'dst_w': (800-20)/2, 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), int((800-60)/4+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[4], 'dst_w': (800-20)/2, 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (0, int(((800-60)/4+20)*2)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[5], 'dst_w': (800-20)/2, 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), int(((800-60)/4+20)*2)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[6], 'dst_w': (800-20)/2, 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (0, int(800-(800-60)/4)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[7], 'dst_w': (800-20)/2, 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), int(800-(800-60)/4)), im)

            
            im.close()
            
        
        if ys == 'x10':
            bg = Image.new('RGB', (800, 800), (255, 255, 255))

            # 第1排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[0], 'dst_w': int((800-20)/2), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (0, 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[1], 'dst_w': int((800-20)/2), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), 0), im)

            # 第二排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[2], 'dst_w': int((800-20)/2), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (0, int((800-80)/5+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[3], 'dst_w': int((800-20)/2), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), int((800-80)/5+20)), im)

            # 第3排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[4], 'dst_w': int((800-20)/2), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (0, int(((800-80)/5+20)*2)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[5], 'dst_w': int((800-20)/2), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), int(((800-80)/5+20)*2)), im)

            # 第4排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[6], 'dst_w': int((800-20)/2), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (0, int(((800-80)/5+20)*3)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[7], 'dst_w': int((800-20)/2), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), int(((800-80)/5+20)*3)), im)

            # 第5排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[8], 'dst_w': int((800-20)/2), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (0, int(800-(800-80)/5)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[9], 'dst_w': int((800-20)/2), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int(800-(800-20)/2), int(800-(800-80)/5)), im)

            
            im.close()

        if ys == 'x12':
            bg = Image.new('RGB', (800, 800), (255, 255, 255))

            # 第1排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[0], 'dst_w': int((800-40)/3), 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (0, 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[1], 'dst_w': int((800-40)/3), 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[2], 'dst_w': int((800-40)/3), 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), 0), im)

            # 第2排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[3], 'dst_w': int((800-40)/3), 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (0, int((800-60)/4+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[4], 'dst_w': int((800-40)/3), 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), int((800-60)/4+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[5], 'dst_w': int((800-40)/3), 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), int((800-60)/4+20)), im)

            # 第3排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[6], 'dst_w': int((800-40)/3), 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (0, int(((800-60)/4+20)*2)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[7], 'dst_w': int((800-40)/3), 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), int(((800-60)/4+20)*2)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[8], 'dst_w': int((800-40)/3), 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), int(((800-60)/4+20)*2)), im)

            # 第4排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[9], 'dst_w': int((800-40)/3), 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (0, int(800-((800-60)/4))), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[10], 'dst_w': int((800-40)/3), 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), int(800-((800-60)/4))), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[11], 'dst_w': int((800-40)/3), 'dst_h': int((800-60)/4)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), int(800-((800-60)/4))), im)
            
            
            im.close()
            

        if ys == 'x15':
            bg = Image.new('RGB', (800, 800), (255, 255, 255))

            # 第1排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[0], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (0, 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[1], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[2], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), 0), im)

            # 第2排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[3], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (0, int((800-80)/5+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[4], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), int((800-80)/5+20)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[5], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), int((800-80)/5+20)), im)

            # 第3排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[6], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (0, int(((800-80)/5+20)*2)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[7], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), int((800-80)/5+20)*2), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[8], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), int((800-80)/5+20)*2), im)

            # 第4排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[9], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (0, int(((800-80)/5+20)*3)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[10], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), int((800-80)/5+20)*3), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[11], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), int((800-80)/5+20)*3), im)

            # 第4排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[12], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (0, int(800-(800-80)/5)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[13], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), int(800-(800-80)/5)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[14], 'dst_w': int((800-40)/3), 'dst_h': int((800-80)/5)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), int(800-(800-80)/5)), im)
            
            im.close()
            

        if ys == 's6':
            bg = Image.new('RGB', (800, 800), (255, 255, 255))

            # 第1排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[0], 'dst_w': int((800-40)/3), 'dst_h': int((800-20)/2)}).convert('RGBA')
            bg.paste(im, (0, 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[1], 'dst_w': int((800-40)/3), 'dst_h': int((800-20)/2)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), 0), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[2], 'dst_w': int((800-40)/3), 'dst_h': int((800-20)/2)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), 0), im)

            # 第二排
            im = clipResizeImg(**{'ori_img': path + '/' + img_list[3], 'dst_w': int((800-40)/3), 'dst_h': int((800-20)/2)}).convert('RGBA')
            bg.paste(im, (0, int(800-(800-20)/2)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[4], 'dst_w': int((800-40)/3), 'dst_h': int((800-20)/2)}).convert('RGBA')
            bg.paste(im, (int((800-40)/3+20), int(800-(800-20)/2)), im)

            im = clipResizeImg(**{'ori_img': path + '/' + img_list[5], 'dst_w': int((800-40)/3), 'dst_h': int((800-20)/2)}).convert('RGBA')
            bg.paste(im, (int(800-(800-40)/3+1), int(800-(800-20)/2)), im)
            
            im.close()

        # 旋转图片，添加文字
        bg = bg.convert('RGBA')
        da_bg = Image.new('RGB', (1620,1620),(255,255,255))
        da_bg.paste(bg, (0,0), bg)
        da_bg.paste(bg, (820,0), bg)
        da_bg.paste(bg, (0,820), bg)
        da_bg.paste(bg, (820,820), bg)
        da_bg = da_bg.rotate(20,expand=True)
        da_bg = da_bg.crop((430,430,430+1218,430+1218))
        da_bg.thumbnail((800,800),Image.ANTIALIAS)

        # da_bg = bg

        st_logo = Image.open('D:/freepik-python/st.png')

        da_bg.paste(st_logo,(0,0),st_logo)
            
        heavy_path = 'D:/freepik-python/font/SourceHanSansCN-Heavy.otf'
        medium_path = 'D:/freepik-python/font/SourceHanSansCN-Medium.otf'

        line_1 = request.form.get('line_1')
        line_1 = line_1.upper()
        font_size = 48
        font = ImageFont.truetype(heavy_path,font_size)
        text_width = font.getsize(line_1)
        line_1_img = Image.new('RGB',(text_width[0]+2,text_width[1]),(255,255,255))
        draw = ImageDraw.Draw(line_1_img)
        draw.text((2,0),line_1,(0,0,0),font=font)
        line_1_img = line_1_img.convert('RGBA')
        if text_width[0]+2 <= 230:
            da_bg.paste(line_1_img,(int((290-text_width[0])/2+478),int((94-text_width[1])/2+50)),line_1_img)
        else:
            # line_1_img_width = 230
            line_1_img_height = int(text_width[1]/(text_width[0]/230))
            line_1_img.thumbnail((230,line_1_img_height),Image.ANTIALIAS)
            da_bg.paste(line_1_img,(int((290-230)/2+478),int((94-line_1_img_height)/2+50)),line_1_img)

        line_2_str = request.form.get('line_2')
        line_2_str = line_2_str.upper()
        line_2 = line_2_str.split(' ',1)
        font_size = 115
        font = ImageFont.truetype(heavy_path,font_size)
        text_width = font.getsize(line_2[0])
        line_2_1_img = Image.new('RGB',(text_width[0]+2,text_width[1]),(255,255,255))
        draw = ImageDraw.Draw(line_2_1_img)
        draw.text((2,0),line_2[0],(0,0,0),font=font)
        line_2_1_img = line_2_1_img.convert('RGBA')
        if text_width[0] <= 230:
            da_bg.paste(line_2_1_img,(508,143),line_2_1_img)
            
            text_width = font.getsize(line_2[1])
            line_2_2_img = Image.new('RGB',(text_width[0]+2,text_width[1]),(255,255,255))
            draw = ImageDraw.Draw(line_2_2_img)
            draw.text((2,0),line_2[1],(0,0,0),font=font)
            line_2_2_img = line_2_2_img.convert('RGBA')
            if text_width[0] <= 230:
                da_bg.paste(line_2_2_img,(508,143+126),line_2_2_img)
            else:
                line_2_2_img_h = int(text_width[1]/(text_width[0]/230))
                line_2_2_img.thumbnail((230,line_2_2_img_h),Image.ANTIALIAS)
                da_bg.paste(line_2_2_img,(508,143+126),line_2_2_img)
        else:
            line_2_1_img_h = int(text_width[1]/(text_width[0]/230))
            line_2_1_img.thumbnail((230,line_2_1_img_h),Image.ANTIALIAS)
            da_bg.paste(line_2_1_img,(508,143),line_2_1_img)

            text_width = font.getsize(line_2[1])
            line_2_2_img = Image.new('RGB',(text_width[0]+2,text_width[1]),(255,255,255))
            draw = ImageDraw.Draw(line_2_2_img)
            draw.text((2,0),line_2[1],(0,0,0),font=font)
            line_2_2_img = line_2_2_img.convert('RGBA')
            if text_width[0] <= 230:
                da_bg.paste(line_2_2_img,(508,143+line_2_1_img_h+10),line_2_2_img)
            else:
                line_2_2_img_h = int(text_width[1]/(text_width[0]/230))
                line_2_2_img.thumbnail((230,line_2_2_img_h),Image.ANTIALIAS)
                da_bg.paste(line_2_2_img,(508,143+line_2_1_img_h+10),line_2_2_img)

        line_3 = request.form.get('line_3')
        font_size = 80
        font = ImageFont.truetype(medium_path,font_size)
        text_width = font.getsize(line_3)
        line_3_img = Image.new('RGB',(text_width[0]+2,text_width[1]),(255,255,255))
        draw = ImageDraw.Draw(line_3_img)
        draw.text((2,0),line_3,(0,0,0),font=font)
        line_3_img = line_3_img.convert('RGBA')
        if text_width[0] <= 230:
            line_3_img_h = text_width[1]
            x = int((290-text_width[0])/2+478)
            da_bg.paste(line_3_img,(x,430),line_3_img)
        else:
            line_3_img_h = int(text_width[1]/(text_width[0]/230))
            line_3_img.thumbnail((230,line_3_img_h),Image.ANTIALIAS)
            x = int((290-230)/2+478)
            da_bg.paste(line_3_img,(x,430),line_3_img)

        line_4_str = request.form.get('line_4')
        line_4 = line_4_str.upper()
        line_4 = line_4_str.split(' ',1)
        font = ImageFont.truetype(medium_path,35)
        text_width = font.getsize(line_4[0])
        line_4_1_img = Image.new('RGB',(text_width[0]+2,text_width[1]),(255,255,255))
        draw = ImageDraw.Draw(line_4_1_img)
        draw.text((2,0),line_4[0],(0,0,0),font=font)
        line_4_1_img = line_4_1_img.convert('RGBA')
        if text_width[0] <=230:
            x = int((290-text_width[0])/2+478)
            line_4_1_img_h = int(text_width[1])
            da_bg.paste(line_4_1_img,(x,430+line_3_img_h+15),line_4_1_img)

            text_width = font.getsize(line_4[1])
            line_4_2_img = Image.new('RGB',(text_width[0]+2,text_width[1]),(255,255,255))
            draw = ImageDraw.Draw(line_4_2_img)
            draw.text((2,0),line_4[1],(0,0,0),font=font)
            line_4_2_img = line_4_2_img.convert('RGBA')
            if text_width[0] <= 230:
                x = int((290-text_width[0])/2+478)
                da_bg.paste(line_4_2_img,(x,430+line_3_img_h+15+line_4_1_img_h+10),line_4_2_img)
            else:
                line_4_2_h = text_width[1]/(text_width[0]/230)
                line_4_2_img.thumbnail((230,line_4_2_h),Image.ANTIALIAS)
                x = int((290-230)/2+478)
                da_bg.paste(line_4_2_img,(x,430+line_3_img_h+15+line_4_1_img_h+10),line_4_2_img)
        else:
            line_4_1_img_h = int(text_width[1]/(text_width[0]/230))
            line_4_1_img.thumbnail((230,line_4_1_img_h),Image.ANTIALIAS)
            x = int((290-230)/2+478)
            da_bg.paste(line_4_1_img,(x,430+line_3_img_h+15),line_4_1_img)

            text_width = font.getsize(line_4[1])
            line_4_2_img = Image.new('RGB',(text_width[0]+2,text_width[1]),(255,255,255))
            draw = ImageDraw.Draw(line_4_2_img)
            draw.text((2,0),line_4[1],(0,0,0),font=font)
            line_4_2_img = line_4_2_img.convert('RGBA')
            if text_width[0] <= 230:
                x = int((290-text_width[0])/2+478)
                da_bg.paste(line_4_2_img,(x,430+line_3_img_h+15+line_4_1_img_h+10),line_4_2_img)
            else:
                line_4_2_h = text_width[1]/(text_width[0]/230)
                line_4_2_img.thumbnail((230,line_4_1_img_h),Image.ANTIALIAS)
                x = int((290-230)/2+478)
                da_bg.paste(line_4_2_img,(x,430+line_3_img_h+15+line_4_1_img_h+10),line_4_2_img)

        line_5 = request.form.get('line_5')
        font = ImageFont.truetype(medium_path,25)
        text_width = font.getsize(line_5)
        line_5_img = Image.new('RGB',(text_width[0]+2,text_width[1]),(255,255,255))
        draw = ImageDraw.Draw(line_5_img)
        draw.text((2,0),line_5,(0,0,0),font=font)
        line_5_img = line_5_img.convert('RGBA')
        if text_width[0] <= 230:
            x = int((290-text_width[0])/2+478)
            da_bg.paste(line_5_img,(x,700),line_5_img)
        else:
            x = int((290-230)/2+478)
            line_5_img_h = int(text_width[1]/(text_width[0]/230))
            line_5_img.thumbnail((230,line_5_img_h),Image.ANTIALIAS)
            da_bg.paste(line_5_img,(x,700),line_5_img)

        da_bg.save('C:/Users/wu/Desktop/upload/0.jpg', quality=90)
    
    print('首图添加文案')
    cl = request.form.get('cl')
    if cl == 'st_xq_2':
        xq_2(path)
    return data

@app.route('/', methods=['GET'])
def index():
    import requests
    from tim import jieya
    # 如果传入了文件夹ID
    if(request.args.get('id')):
        dir_id = request.args.get('id')
        if int(dir_id) <= 1000:
            path = 'G:/1-1000/' + str(dir_id)
        else:
            path = 'G:/1000-2000/' + str(dir_id)

        # 如果文件夹存在
        if os.path.exists(path):
            jieya(path)
            jpg_list = []
            for jpg in os.listdir(path):
                jpg_path = path+'/'+jpg
                if jpg.endswith('.jpg') or jpg.endswith('.png'):
                    jpg_dic = {}
                    html = requests.get(
                        'http://127.0.0.1:5000/tim?src='+jpg_path).text
                    jpg_dic['name'] = jpg
                    jpg_dic['path'] = html
                    jpg_list.append(jpg_dic)
            info = ''
            jpg_num = len(jpg_list)
        else:
            jpg_list = []
            info = '文件夹不存在'
            jpg_num = ''

        return render_template(
            'index.html',
            jpg_list=jpg_list,
            id=request.args.get('id'),
            next_id='http://127.0.0.1:5000/?id=' +
            str(int(request.args.get('id'))+1),
            pev_id='http://127.0.0.1:5000/?id=' +
            str(int(request.args.get('id'))-1),
            info=info,
            jpg_num=jpg_num
        )
    else:
        return render_template(
            'index.html',
            id='请输入文件夹ID'
        )

@app.route('/tim', methods=['GET'])
def tim():
    import base64
    from io import BytesIO
    from PIL import Image
    img_path = request.args.get('src')
    im = Image.open(img_path)
    im.thumbnail((150, 150))
    io_obj = BytesIO()
    im.save(io_obj, 'png')
    return 'data:image/png;base64,' + base64.b64encode(io_obj.getvalue()).decode('ascii')

@app.route('/freepik', methods=['GET','POST'])
def freepik():
    import pymysql
    db = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '',
        db = 'freepik',
        charset = 'utf8'
    )
    cursor = db.cursor()
    
    page_number = request.args.get('page')
    if request.args.get('page'):
        page_number = request.args.get('page')
    else:
        page_number = 1

    mysql_number = int(page_number)*120-120

    sql = "select * from freepik where `zt`= '0' limit " + str(mysql_number) + ",120"
    cursor.execute(sql)
    res = cursor.fetchmany(120)
    
    if int(page_number)-1 <= 0:
        pre_page = 1
    else:
        pre_page = str(int(page_number)-1)

    next_page = str(int(page_number)+1)

    if request.form.getlist('id_list[]'):
        for i in request.form.getlist('id_list[]'):
            sql = "UPDATE `freepik` SET `zt` = '1' WHERE `freepik`.`id` = '"+i+"'"
            cursor.execute(sql)
    
    db.commit()
    db.close()
    
    return render_template(
        'freepik_list.html',
        page_number = page_number,
        res = res,
        pre_page = pre_page,
        next_page = next_page
    )


if __name__ == '__main__':
    app.debug = True
    app.run()