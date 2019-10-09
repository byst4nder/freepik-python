from PIL import Image
import os


def clipResizeImg(**args):   
    args_key = {'ori_img':'','dst_w':'','dst_h':''}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]
        
    im = Image.open(arg['ori_img'])
    ori_w,ori_h = im.size

    dst_scale = float(arg['dst_w'] / arg['dst_h']) #目标高宽比
    ori_scale = float(ori_w / ori_h) #原高宽比
    
    if dst_scale < ori_scale:
        h_sca = float(ori_h/arg['dst_h'])
        new_w = int(ori_w/h_sca)
        im = im.resize((new_w,int(arg['dst_h'])),Image.ANTIALIAS)
        x = int((new_w-arg['dst_w'])/2)
        im = im.crop((x,0,x+arg['dst_w'],arg['dst_h']))
    elif dst_scale > ori_scale:
        w_sca = float(ori_w/arg['dst_w'])
        new_h = int(ori_h/w_sca)
        im = im.resize((int(arg['dst_w']),new_h),Image.ANTIALIAS)
        x = int((new_h-arg['dst_h'])/2)
        im = im.crop((0,x,arg['dst_w'],x+arg['dst_h']))
    elif dst_scale == ori_scale:
        w_sca = float(ori_w/arg['dst_w'])
        new_h = int(ori_h/w_sca)
        im = im.resize((int(arg['dst_w']),new_h),Image.ANTIALIAS)
    return im

def da_sy(im):
    '''
    详情图自动打水印
    '''
    im = im.convert('RGBA')
    da_logo = Image.open('D:/freepik-python/da_logo.png')
    im_size = im.size
    da_logo_size = da_logo.size
    x_num = int(im_size[0]/da_logo_size[0]+1)
    y_num = int(im_size[1]/da_logo_size[1]+1)
    all_num = int(x_num*y_num)
    x = 0
    y = 0
    paste_num = 0
    while paste_num <= all_num:
        im.paste(da_logo,(int(x*da_logo_size[0]),int(y*da_logo_size[1]+20)),da_logo)
        paste_num += 1
        x += 1
        if x == x_num:
            y += 1
            x = 0
    im = im.convert('RGB')
    return im

def jieya(path):
    '''
    自动解压zip文件，如果文件存在则自动重命名
    但是如果重复2次以上，还是会出现问题。
    '''
    import os
    import zipfile
    for one_file in os.listdir(path):
        one_file_path = path + '/' + one_file
        if(one_file_path).endswith('.zip'):
            zf = zipfile.ZipFile(one_file_path)
            zf_rename_num = 0
            for one_zf in zf.namelist():
                
                one_zf_path = path+'/'+one_zf
                if(one_zf_path).endswith('.txt'):
                    pass
                else:
                    if os.path.exists(one_zf_path):
                        os.rename( one_zf_path,str(os.path.splitext(one_zf_path)[0]) + '(' + str(zf_rename_num) + ')' + str(os.path.splitext(one_zf_path)[1]) )
                    zf_rename_num = zf_rename_num + 1
                    zf.extract(one_zf,path)
            zf.close()


def rename(path):
    '''
    自动文件重命名
    最后加入了zip文件判断然后删除
    因为这个重命名是在需要处理详情页的时候再删除zip文件
    防止在get文件夹path的时候出错，但是zip文件已经没了的尴尬
    判断是否已经重命名过，如果已经重命名则跳过
    '''
    import os
    import time
    jpg_num     = 1
    ai_num      = 1
    psd_num     = 1
    eps_num     = 1
    now = int(time.time())
    timeStruct = time.localtime(now)
    strTime = time.strftime("%Y%m%d%H%M", timeStruct)

    for one_file in os.listdir(path):
        one_file_path = path + '/' + one_file
       
        if(one_file_path).endswith('.zip'):
            os.remove(one_file_path)
        
        if 'xiaoxisc' in os.path.splitext(one_file_path)[0]:
            print('文件已经重命名过了。')
            return
        else:
            if(one_file_path).endswith('.jpg'):
                os.rename(one_file_path, path + '/小夕素材_xiaoxisc.com_' + strTime + '_' + str(jpg_num) + str(os.path.splitext(one_file_path)[1]))
                jpg_num += 1
            if(one_file_path).endswith('.psd'):
                os.rename(one_file_path, path + '/小夕素材_xiaoxisc.com_' + strTime + '_' + str(psd_num) + str(os.path.splitext(one_file_path)[1]))
                psd_num += 1
            if(one_file_path).endswith('.ai'):
                os.rename(one_file_path, path + '/小夕素材_xiaoxisc.com_' + strTime + '_' + str(ai_num) + str(os.path.splitext(one_file_path)[1]))
                ai_num += 1
            if(one_file_path).endswith('.eps'):
                os.rename(one_file_path, path + '/小夕素材_xiaoxisc.com_' + strTime + '_' + str(eps_num) + str(os.path.splitext(one_file_path)[1]))
                eps_num += 1
        


def thumb_by_width(im,width):
    '''
    因为涉及到图片如果是横着的，要转换为竖着的。
    size[0] <= size[1]  :   如果宽度小于高度是竖着的 或 等于正方形直接缩小
    否则逆时针旋转90度
    Image.ANTIALIAS平滑resize
    '''
    im = Image.open(im)
    size = im.size
    if size[0] <= size[1]:
        height = int(size[1]/(size[0]/width))
    else:
        im = im.rotate(-90,expand=True)
        size = im.size
        height = int(size[1]/(size[0]/width))
    im = im.resize((width,height),Image.ANTIALIAS)
    return im

def xq_2(path):
    '''
    把图片分为两栏，遍历图片高度，左右两栏哪个高度更低，就添加进去新的图片。
    可以保证最后出来的大图两边差不多一致。
    遍历的同时建立两个数组，加入已经遍历好了的图片lan_num_list
    然后根据两栏的数据图片遍历，来粘贴到da_bg大图背景里面
    '''
    print('拼接图片')
    lan_1_height = 0
    lan_2_height = 0
    lan_1_list = []
    lan_2_list = []
    jiange = 5
    for one_file in os.listdir(path):
        one_file_path = path + '/' + one_file
        if(one_file_path).endswith('.jpg') or one_file_path.endswith('.png'):
            width = int((750-jiange)/2)
            im = thumb_by_width(one_file_path,width)
            img_height = im.size[1]
            if lan_1_height == min(lan_1_height,lan_2_height):
                lan_1_height = lan_1_height + img_height
                lan_1_list.append(one_file_path)
            else:
                lan_2_height = lan_2_height + img_height
                lan_2_list.append(one_file_path)
    da_bg_h = int(max(lan_1_height,lan_2_height)+(max(len(lan_1_list),len(lan_2_list))-1)*jiange+20)
    da_bg = Image.new('RGB',(750,da_bg_h),(255,255,255))
    lan_1_height = 20
    lan_2_height = 20
    for i in lan_1_list:
        im = thumb_by_width(i,width)
        im = im.convert('RGBA')
        img_size = im.size
        da_bg.paste(im,(0,lan_1_height),im)
        lan_1_height = lan_1_height + jiange + img_size[1]
    for i in lan_2_list:
        im = thumb_by_width(i,width)
        im = im.convert("RGBA")
        img_size = im.size
        da_bg.paste(im,(int(750-(width)),lan_2_height),im)
        lan_2_height = lan_2_height + jiange + img_size[1]

    print('添加水印')
    da_bg = da_sy(da_bg)
    
    '''
    clipnum ：裁剪次数
    imgnum  ：图片保存到upload文件夹的文件名。
    每张图片的裁剪高度为1000，利用while建立循环。
    因为clipnum初始值为0，所以直接可以用大图高度除以1000以后的次数值。
    crop的左、右值是固定的0和750。有上、下值不同。
    上值0为起点，下值为上值+1000
    如果是最后一次裁剪，直接使用da_bg的高度。

    '''
    print('裁剪图片')
    clipnum = 0
    imgnum = 1
    while clipnum <= int(da_bg_h/1000):
        shang = clipnum * 1000
        if clipnum == int(da_bg_h/1000):
            xia = da_bg_h
        else:
            xia = shang + 1000
        im = da_bg.crop((0,shang,750,xia))
        xia = xia + 1000
        im.save('C:/Users/wu/Desktop/upload/'+str(imgnum)+'.jpg',quality = 90)
        imgnum += 1
        clipnum += 1
    
    print('重命名文件')
    rename(path)
    da_bg.close()