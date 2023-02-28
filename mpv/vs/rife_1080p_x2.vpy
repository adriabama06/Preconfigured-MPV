import vapoursynth as vs
from vapoursynth import core

FPS_multiply = 2
FPS_den = 1
GPU_ID = 0
GPU_THREAD = 2

input = video_in
colorlv = input.get_frame(0).props._ColorRange
fmt_fin = input.format.id

if container_fps > 31:
	raise Exception("FPS > 30 fps, the framerate is to fast")


# Make sure the input is not a duplicated frame
sc_clip = core.misc.SCDetect(clip=input, threshold=0.15)

#                                 1920x1080
if (input.width * input.height) > 2073600:
	sc_clip = sc_clip.resize.Bicubic(width=1920, height=1080, format=vs.RGBS, matrix_in_s="709")
else:
	sc_clip = sc_clip.resize.Bilinear(format=vs.RGBS, matrix_in_s="709")

# you can change the arguments and use this:
# model=9, multiplier=2
# fps_num=48, fps_den=1

interpolated = core.rife.RIFE(clip=sc_clip, model=9, factor_num=FPS_multiply, factor_den=FPS_den, gpu_id=GPU_ID, gpu_thread=GPU_THREAD, sc=True, skip=True, skip_threshold=60.0)

out = interpolated.resize.Bilinear(format=fmt_fin, matrix_s="709", range=1 if colorlv == 0 else None)

out.set_output()