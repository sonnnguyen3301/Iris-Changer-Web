
from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage


def button(request):
    return render(request,'blog/home.html')
def output(request):
    data=requests.get('https://www.google.com/')
    print(data.text)
    data=data.text
    return render(request,'blog/home.html',{'data':data})
def external(request):
    left_eye_thres= request.POST.get('left_eye_thres')
    right_eye_thres= request.POST.get('right_eye_thres')
    
    print("left_eye_thres",left_eye_thres)
    print("right_eye_thres",right_eye_thres)

    image = request.FILES['image']
    # Open CV
    if "autumn_c" in request.POST:
        color_tag = "0"
        Tag_type = "opencv"
    elif 'bone_c' in request.POST:   
        color_tag = "1"
        Tag_type = "opencv"
    elif "jet_c" in request.POST:
        color_tag = "2"
        Tag_type = "opencv"
    elif 'winter_c' in request.POST:   
        color_tag = "3"
        Tag_type = "opencv"
    elif 'rainbow_c' in request.POST: 
        color_tag = "4"
        Tag_type = "opencv"
    elif 'ocean_c' in request.POST: 
        color_tag = "5"
        Tag_type = "opencv"
    elif 'summer_c' in request.POST: 
        color_tag = "6"
        Tag_type = "opencv"
    elif 'spring_c' in request.POST: 
        color_tag = "7"
        Tag_type = "opencv"
    elif 'cool_c' in request.POST: 
        color_tag = "8"
        Tag_type = "opencv"
    elif 'hsv_c' in request.POST: 
        color_tag = "9"
        Tag_type = "opencv"
    elif 'pink_c' in request.POST: 
        color_tag = "10"
        Tag_type = "opencv"
    elif 'hot_c' in request.POST: 
        color_tag = "11"
        Tag_type = "opencv"
    elif 'parula_c' in request.POST:
        color_tag = "12"
        Tag_type = "opencv" 
    elif 'magma_c' in request.POST: 
        color_tag = "13"
        Tag_type = "opencv"
    elif 'inferno_c' in request.POST: 
        color_tag = "14"
        Tag_type = "opencv"
    elif 'plasma_c' in request.POST: 
        color_tag = "15"
        Tag_type = "opencv"
    elif 'viridis_c' in request.POST: 
        color_tag = "16"
        Tag_type = "opencv"
    elif 'cividis_c' in request.POST: 
        color_tag = "17"
        Tag_type = "opencv"
    elif 'twilight_c' in request.POST: 
        color_tag = "18"
        Tag_type = "opencv"
    elif 'twilight_shifted_c' in request.POST: 
        color_tag = "19"
        Tag_type = "opencv"
    elif 'turbo_c' in request.POST: 
        color_tag = "20"
        Tag_type = "opencv"
    elif 'deepgreen_c' in request.POST: 
        color_tag = "21"
        Tag_type = "opencv"

    #Perceptiually
    elif 'viridis' in request.POST: 
        color_tag = "viridis"
        Tag_type = "matplot"
    elif 'plasma' in request.POST: 
        color_tag = "plasma"
        Tag_type = "matplot"
    elif 'inferno' in request.POST: 
        color_tag = "inferno"
        Tag_type = "matplot"
    elif 'magma' in request.POST: 
        color_tag = "magma"
        Tag_type = "matplot"
    elif 'cividis' in request.POST: 
        color_tag = "cividis"
        Tag_type = "matplot"
    elif 'viridis_r' in request.POST:
        color_tag = "viridis_r"
        Tag_type = "matplot" 
    elif 'plasma_r' in request.POST: 
        color_tag = "plasma_r"
        Tag_type = "matplot"
    elif 'inferno_r' in request.POST: 
        color_tag = "inferno_r"
        Tag_type = "matplot"
    elif 'magma_r' in request.POST: 
        color_tag = "magma_r"
        Tag_type = "matplot"
    elif 'cividis_r' in request.POST: 
        color_tag = "cividis_r"
        Tag_type = "matplot"

    #Sequential(1)
    elif 'Greys' in request.POST: 
        color_tag = "Greys"
        Tag_type = "matplot"
    elif 'Purples' in request.POST: 
        color_tag = "Purples"
        Tag_type = "matplot"
    elif 'Blues' in request.POST: 
        color_tag = "Blues"
        Tag_type = "matplot"
    elif 'Greens' in request.POST: 
        color_tag = "Greens"
        Tag_type = "matplot"
    elif 'Oranges' in request.POST: 
        color_tag = "Oranges"
        Tag_type = "matplot"
    elif 'Reds' in request.POST: 
        color_tag = "Reds"
        Tag_type = "matplot"
    elif 'YlOrBr' in request.POST: 
        color_tag = "YlOrBr"
        Tag_type = "matplot"
    elif 'YlOrRd' in request.POST: 
        color_tag = "YlOrRd"
        Tag_type = "matplot"
    elif 'OrRd' in request.POST: 
        color_tag = "OrRd"
        Tag_type = "matplot"
    elif 'PuRd' in request.POST: 
        color_tag = "PuRd"
        Tag_type = "matplot"
    elif 'RdPu' in request.POST: 
        color_tag = "RdPu"
        Tag_type = "matplot"
    elif 'BuPu' in request.POST: 
        color_tag = "BuPu"
        Tag_type = "matplot"
    elif 'GnBu' in request.POST: 
        color_tag = "GnBu"
        Tag_type = "matplot"
    elif 'PuBu' in request.POST: 
        color_tag = "PuBu"
        Tag_type = "matplot"
    elif 'YlGnBu' in request.POST: 
        color_tag = "YlGnBu"
        Tag_type = "matplot"
    elif 'PuBuGn' in request.POST: 
        color_tag = "PuBuGn"
        Tag_type = "matplot"
    elif 'BuGn' in request.POST: 
        color_tag = "BuGn"
        Tag_type = "matplot"
    elif 'YlGn' in request.POST: 
        color_tag = "YlGn"
        Tag_type = "matplot"
    elif 'Greys_r' in request.POST: 
        color_tag = "Greys_r"
        Tag_type = "matplot"
    elif 'Purples_r' in request.POST: 
        color_tag = "Purples_r"
        Tag_type = "matplot"
    elif 'Blues_r' in request.POST: 
        color_tag = "Blues_r"
        Tag_type = "matplot"
    elif 'Greens_r' in request.POST: 
        color_tag = "Greens_r"
        Tag_type = "matplot"
    elif 'Oranges_r' in request.POST: 
        color_tag = "Oranges_r"
        Tag_type = "matplot"
    elif 'Reds_r' in request.POST: 
        color_tag = "Reds_r"
        Tag_type = "matplot"
    elif 'YlOrBr_r' in request.POST: 
        color_tag = "YlOrBr_r"
        Tag_type = "matplot"
    elif 'YlOrRd_r' in request.POST: 
        color_tag = "YlOrRd_r"
        Tag_type = "matplot"
    elif 'OrRd_r' in request.POST: 
        color_tag = "OrRd_r"
        Tag_type = "matplot"
    elif 'PuRd_r' in request.POST: 
        color_tag = "PuRd_r"
        Tag_type = "matplot"
    elif 'RdPu_r' in request.POST: 
        color_tag = "RdPu_r"
        Tag_type = "matplot"
    elif 'BuPu_r' in request.POST: 
        color_tag = "BuPu_r"
        Tag_type = "matplot"
    elif 'GnBu_r' in request.POST: 
        color_tag = "GnBu_r"
        Tag_type = "matplot"
    elif 'PuBu_r' in request.POST: 
        color_tag = "PuBu_r"
        Tag_type = "matplot"
    elif 'YlGnBu_r' in request.POST: 
        color_tag = "YlGnBu_r"
        Tag_type = "matplot"
    elif 'PuBuGn_r' in request.POST: 
        color_tag = "PuBuGn_r"
        Tag_type = "matplot"
    elif 'BuGn_r' in request.POST: 
        color_tag = "BuGn_r"
        Tag_type = "matplot"
    elif 'YlGn_r' in request.POST: 
        color_tag = "YlGn_r"
        Tag_type = "matplot"
    
    #Sequential(2)
    elif 'binary' in request.POST: 
        color_tag = "binary"
        Tag_type = "matplot"
    elif 'gist_yarg' in request.POST: 
        color_tag = "gist_yarg"
        Tag_type = "matplot"
    elif 'gist_gray' in request.POST: 
        color_tag = "gist_gray"
        Tag_type = "matplot"
    elif 'gray' in request.POST: 
        color_tag = "gray"
        Tag_type = "matplot"
    elif 'bone' in request.POST: 
        color_tag = "bone"
        Tag_type = "matplot"
    elif 'pink' in request.POST: 
        color_tag = "pink"
        Tag_type = "matplot"
    elif 'spring' in request.POST: 
        color_tag = "spring"
        Tag_type = "matplot"
    elif 'summer' in request.POST: 
        color_tag = "summer"
        Tag_type = "matplot"
    elif 'autumn' in request.POST: 
        color_tag = "autumn"
        Tag_type = "matplot"
    elif 'winter' in request.POST: 
        color_tag = "winter"
        Tag_type = "matplot"
    elif 'cool' in request.POST: 
        color_tag = "cool"
        Tag_type = "matplot"
    elif 'Wistia' in request.POST: 
        color_tag = "Wistia"
        Tag_type = "matplot"
    elif 'hot' in request.POST: 
        color_tag = "hot"
        Tag_type = "matplot"
    elif 'afmhot' in request.POST: 
        color_tag = "afmhot"
        Tag_type = "matplot"
    elif 'gist_heat' in request.POST: 
        color_tag = "gist_heat"
        Tag_type = "matplot"
    elif 'copper' in request.POST: 
        color_tag = "copper"
        Tag_type = "matplot"
    elif 'binary_r' in request.POST: 
        color_tag = "binary_r"
        Tag_type = "matplot"
    elif 'gist_yarg_r' in request.POST: 
        color_tag = "gist_yarg_r"
        Tag_type = "matplot"
    elif 'gist_gray_r' in request.POST: 
        color_tag = "gist_gray_r"
        Tag_type = "matplot"
    elif 'gray_r' in request.POST: 
        color_tag = "gray_r"
        Tag_type = "matplot"
    elif 'bone_r' in request.POST: 
        color_tag = "bone_r"
        Tag_type = "matplot"
    elif 'pink_r' in request.POST: 
        color_tag = "pink_r"
        Tag_type = "matplot"
    elif 'spring_r' in request.POST: 
        color_tag = "spring_r"
        Tag_type = "matplot"
    elif 'summer_r' in request.POST: 
        color_tag = "summer_r"
        Tag_type = "matplot"
    elif 'autumn_r' in request.POST: 
        color_tag = "autumn_r"
        Tag_type = "matplot"
    elif 'winter_r' in request.POST: 
        color_tag = "winter_r"
        Tag_type = "matplot"
    elif 'cool_r' in request.POST: 
        color_tag = "cool_r"
        Tag_type = "matplot"
    elif 'Wistia_r' in request.POST: 
        color_tag = "Wistia_r"
        Tag_type = "matplot"
    elif 'hot_r' in request.POST: 
        color_tag = "hot_r"
        Tag_type = "matplot"
    elif 'afmhot_r' in request.POST: 
        color_tag = "afmhot_r"
        Tag_type = "matplot"
    elif 'gist_heat_r' in request.POST: 
        color_tag = "gist_heat_r"
        Tag_type = "matplot"
    elif 'copper_r' in request.POST: 
        color_tag = "copper_r"
        Tag_type = "matplot"

    #   Diverging
    elif 'PiYG' in request.POST: 
        color_tag = "PiYG"
        Tag_type = "matplot"
    elif 'PRGn' in request.POST: 
        color_tag = "PRGn"
        Tag_type = "matplot"
    elif 'BrBG' in request.POST: 
        color_tag = "BrBG"
        Tag_type = "matplot"
    elif 'PuOr' in request.POST: 
        color_tag = "PuOr"
        Tag_type = "matplot"
    elif 'RdGy' in request.POST: 
        color_tag = "RdGy"
        Tag_type = "matplot"
    elif 'RdBu' in request.POST: 
        color_tag = "RdBu"
        Tag_type = "matplot"
    elif 'RdYlBu' in request.POST: 
        color_tag = "RdYlBu"
        Tag_type = "matplot"
    elif 'RdYlGn' in request.POST: 
        color_tag = "RdYlGn"
        Tag_type = "matplot"
    elif 'Spectral' in request.POST: 
        color_tag = "Spectral"
        Tag_type = "matplot"
    elif 'coolwarm' in request.POST: 
        color_tag = "coolwarm"
        Tag_type = "matplot"
    elif 'bwr' in request.POST: 
        color_tag = "bwr"
        Tag_type = "matplot"
    elif 'seismic' in request.POST: 
        color_tag = "seismic"
        Tag_type = "matplot"
    elif 'PiYG_r' in request.POST: 
        color_tag = "PiYG_r"
        Tag_type = "matplot"
    elif 'PRGn_r' in request.POST: 
        color_tag = "PRGn_r"
        Tag_type = "matplot"
    elif 'BrBG_r' in request.POST: 
        color_tag = "BrBG_r"
        Tag_type = "matplot"
    elif 'PuOr_r' in request.POST: 
        color_tag = "PuOr_r"
        Tag_type = "matplot"
    elif 'RdGy_r' in request.POST: 
        color_tag = "RdGy_r"
        Tag_type = "matplot"
    elif 'RdBu_r' in request.POST: 
        color_tag = "RdBu_r"
        Tag_type = "matplot"
    elif 'RdYlBu_r' in request.POST: 
        color_tag = "RdYlBu_r"
        Tag_type = "matplot"
    elif 'RdYlGn_r' in request.POST: 
        color_tag = "RdYlGn_r"
        Tag_type = "matplot"
    elif 'Spectral_r' in request.POST: 
        color_tag = "Spectral_r"
        Tag_type = "matplot"
    elif 'coolwarm_r' in request.POST: 
        color_tag = "coolwarm_r"
        Tag_type = "matplot"
    elif 'bwr_r' in request.POST: 
        color_tag = "bwr_r"
        Tag_type = "matplot"
    elif 'seismic_r' in request.POST: 
        color_tag = "seismic_r"
        Tag_type = "matplot"
    
    # Qualitative
    elif 'Pastel1' in request.POST: 
        color_tag = "Pastel1"
        Tag_type = "matplot"
    elif 'Pastel2' in request.POST: 
        color_tag = "Pastel2"
        Tag_type = "matplot"
    elif 'Paired' in request.POST: 
        color_tag = "Paired"
        Tag_type = "matplot"
    elif 'Accent' in request.POST: 
        color_tag = "Accent"
        Tag_type = "matplot"
    elif 'Dark2' in request.POST: 
        color_tag = "Dark2"
        Tag_type = "matplot"
    elif 'Set1' in request.POST: 
        color_tag = "Set1"
        Tag_type = "matplot"
    elif 'Set2' in request.POST: 
        color_tag = "Set2"
        Tag_type = "matplot"
    elif 'Set3' in request.POST: 
        color_tag = "Set3"
        Tag_type = "matplot"
    elif 'tab10' in request.POST: 
        color_tag = "tab10"
        Tag_type = "matplot"
    elif 'tab20' in request.POST: 
        color_tag = "tab20"
        Tag_type = "matplot"
    elif 'tab20b' in request.POST: 
        color_tag = "tab20b"
        Tag_type = "matplot"
    elif 'tab20c' in request.POST: 
        color_tag = "tab20c"
        Tag_type = "matplot"
    elif 'Pastel1_r' in request.POST: 
        color_tag = "Pastel1_r"
        Tag_type = "matplot"
    elif 'Pastel2_r' in request.POST: 
        color_tag = "Pastel2_r"
        Tag_type = "matplot"
    elif 'Paired_r' in request.POST: 
        color_tag = "Paired_r"
        Tag_type = "matplot"
    elif 'Accent_r' in request.POST: 
        color_tag = "Accent_r"
        Tag_type = "matplot"
    elif 'Dark2_r' in request.POST: 
        color_tag = "Dark2_r"
        Tag_type = "matplot"
    elif 'Set1_r' in request.POST: 
        color_tag = "Set1_r"
        Tag_type = "matplot"
    elif 'Set2_r' in request.POST: 
        color_tag = "Set2_r"
        Tag_type = "matplot"
    elif 'Set3_r' in request.POST: 
        color_tag = "Set3_r"
        Tag_type = "matplot"
    elif 'tab10_r' in request.POST: 
        color_tag = "tab10_r"
        Tag_type = "matplot"
    elif 'tab20_r' in request.POST: 
        color_tag = "tab20_r"
        Tag_type = "matplot"
    elif 'tab20b_r' in request.POST: 
        color_tag = "tab20b_r"
        Tag_type = "matplot"
    elif 'tab20c_r' in request.POST: 
        color_tag = "tab20c_r"
        Tag_type = "matplot"

    # Miscellaneous
    elif 'flag' in request.POST: 
        color_tag = "flag"
        Tag_type = "matplot"
    elif 'prism' in request.POST: 
        color_tag = "prism"
        Tag_type = "matplot"
    elif 'ocean' in request.POST: 
        color_tag = "ocean"
        Tag_type = "matplot"
    elif 'gist_earth' in request.POST: 
        color_tag = "gist_earth"
        Tag_type = "matplot"
    elif 'terrain' in request.POST: 
        color_tag = "terrain"
        Tag_type = "matplot"
    elif 'gist_stern' in request.POST: 
        color_tag = "gist_stern"
        Tag_type = "matplot"
    elif 'gnuplot' in request.POST: 
        color_tag = "gnuplot"
        Tag_type = "matplot"
    elif 'gnuplot2' in request.POST: 
        color_tag = "gnuplot2"
        Tag_type = "matplot"
    elif 'CMRmap' in request.POST: 
        color_tag = "CMRmap"
        Tag_type = "matplot"
    elif 'cubehelix' in request.POST: 
        color_tag = "cubehelix"
        Tag_type = "matplot"
    elif 'brg' in request.POST: 
        color_tag = "brg"
        Tag_type = "matplot"
    elif 'hsv' in request.POST: 
        color_tag = "hsv"
        Tag_type = "matplot"
    elif 'gist_rainbow' in request.POST: 
        color_tag = "gist_rainbow"
        Tag_type = "matplot"
    elif 'rainbow' in request.POST: 
        color_tag = "rainbow"
        Tag_type = "matplot"
    elif 'jet' in request.POST: 
        color_tag = "jet"
        Tag_type = "matplot"
    elif 'nipy_spectral' in request.POST: 
        color_tag = "nipy_spectral"
        Tag_type = "matplot"
    elif 'gist_ncar' in request.POST: 
        color_tag = "gist_ncar"
        Tag_type = "matplot"
    elif 'flag_r' in request.POST: 
        color_tag = "flag_r"
        Tag_type = "matplot"
    elif 'prism_r' in request.POST: 
        color_tag = "prism_r"
        Tag_type = "matplot"
    elif 'ocean_r' in request.POST: 
        color_tag = "ocean_r"
        Tag_type = "matplot"
    elif 'gist_earth_r' in request.POST: 
        color_tag = "gist_earth_r"
        Tag_type = "matplot"
    elif 'terrain_r' in request.POST: 
        color_tag = "terrain_r"
        Tag_type = "matplot"
    elif 'gist_stern_r' in request.POST: 
        color_tag = "gist_stern_r"
        Tag_type = "matplot"
    elif 'gnuplot_r' in request.POST: 
        color_tag = "gnuplot_r"
        Tag_type = "matplot"
    elif 'gnuplot2_r' in request.POST: 
        color_tag = "gnuplot2_r"
        Tag_type = "matplot"
    elif 'CMRmap_r' in request.POST: 
        color_tag = "CMRmap_r"
        Tag_type = "matplot"
    elif 'cubehelix_r' in request.POST: 
        color_tag = "cubehelix_r"
        Tag_type = "matplot"
    elif 'brg_r' in request.POST: 
        color_tag = "brg_r"
        Tag_type = "matplot"
    elif 'hsv_r' in request.POST: 
        color_tag = "hsv_r"
        Tag_type = "matplot"
    elif 'gist_rainbow_r' in request.POST: 
        color_tag = "gist_rainbow_r"
        Tag_type = "matplot"
    elif 'rainbow_r' in request.POST: 
        color_tag = "rainbow_r"
        Tag_type = "matplot"
    elif 'jet_r' in request.POST: 
        color_tag = "jet_r"
        Tag_type = "matplot"
    elif 'nipy_spectral_r' in request.POST: 
        color_tag = "nipy_spectral_r"
        Tag_type = "matplot"
    elif 'gist_ncar_r' in request.POST: 
        color_tag = "gist_ncar_r"
        Tag_type = "matplot"
    else:
        color_tag = "19"
        Tag_type = "opencv"    
    
        
    
    # print('image is ',image)
    print("searchWord",color_tag)
    print("Tag_type",Tag_type)
    fs = FileSystemStorage()
    filename = fs.save(image.name,image)
    fileurl = fs.open(filename)
    templateurl = fs.url(filename)

    # print('image.name',image.name)
    print('file raw url',filename)
    print('file full url', fileurl)
    print('template url',templateurl)
    
    # out= run([sys.executable,'C://Users//Admin//XLA//DA_XLA//test.py',inp],shell=False,stdout=PIPE)
    image= run([sys.executable,'C://Users//Admin//XLA//django_project//image.py',str(fileurl),str(filename),str(color_tag),str(Tag_type),str(left_eye_thres),str(right_eye_thres)],shell=False,stdout=PIPE)#
    # print(out)
    print('raw_url',templateurl)
    # print("C:/Users/Admin/XLA/django_project"+templateurl)
    return render(request,'blog/home.html',{'raw_url':templateurl,'edit_url':"/static/output/result.jpg"})#'data':out.stdout, "/result.jpg"
