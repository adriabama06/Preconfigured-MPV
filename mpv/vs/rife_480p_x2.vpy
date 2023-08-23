import vapoursynth as vs
from vapoursynth import core

FPS_multiply = 2
FPS_den = 1
GPU_ID = 0
GPU_THREAD = 2

input = video_in
colorlv = input.get_frame(0).props._ColorRange
fmt_fin = input.format.id

if container_fps > 61:
	raise Exception("FPS > 60 fps, the framerate is to fast")


# Make sure the input is not a duplicated frame
sc_clip = core.misc.SCDetect(clip=input, threshold=0.15)

#                                 853x480
if (input.width * input.height) > 409440:
	aspect_radio = input.width / input.height
	sc_clip = sc_clip.resize.Bicubic(width=int(480 * aspect_radio) if aspect_radio != (16/9) else 853, height=480, format=vs.RGBS, matrix_in_s="709")
else:
	sc_clip = sc_clip.resize.Bilinear(format=vs.RGBS, matrix_in_s="709")

# you can change the arguments and use this:
# model=9, multiplier=2
# fps_num=48, fps_den=1

interpolated = core.rife.RIFE(clip=sc_clip, model=9, factor_num=FPS_multiply, factor_den=FPS_den, gpu_id=GPU_ID, gpu_thread=GPU_THREAD, sc=True, skip=True, skip_threshold=60.0)

out = interpolated.resize.Bilinear(format=fmt_fin, matrix_s="709", range=1 if colorlv == 0 else None)

out.set_output()