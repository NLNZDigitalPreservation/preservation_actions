import moviepy.editor as mp
import os


# in_ = r"\\wlgprdfile13\NDHA\ndha\atl\pre-deposit\processing_copies\Abi\blog_mp4"
# out_ = r"\\wlgprdfile13\NDHA\ndha\atl\pre-deposit\processing_copies\Abi\Blog_GIFs"


in_ = r"Z:\temp"
out_ = r"Z:\temp2"


for f in os.listdir(in_):
    print (f)
    in_f = os.path.join(in_, f)
    print (in_f) 
    out_f = os.path.join(out_, f.replace(".gif", ".mp4")) 
    clip = mp.VideoFileClip(in_f)
    print (out_f)
    clip.write_videofile(out_f)
