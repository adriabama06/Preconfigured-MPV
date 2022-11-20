# Preconfigured MPV with RIFE

mpv: https://sourceforge.net/projects/mpv-player-windows/files/64bit/mpv-x86_64-20221113-git-2f74734.7z/
vapoursynth: https://github.com/vapoursynth/vapoursynth/releases/tag/R60
mpv settings edited from: https://github.com/Tsubajashi/mpv-settings
VapourSynth-RIFE-ncnn-Vulkan: https://github.com/HomeOfVapourSynthEvolution/VapourSynth-RIFE-ncnn-Vulkan/releases/tag/r9
VapourSynth-RIFE-ncnn-Vulkan models: https://github.com/HomeOfVapourSynthEvolution/VapourSynth-RIFE-ncnn-Vulkan/releases/tag/r3
inspired by: https://github.com/hooke007/MPV_lazy

# GPU:
## Recommended:
- RTX 3080
## Minimum:
- RTX 2080 ti
# Info
For RTX 3060 ti and low:
<br>
Edit `/mpv/vs/rife.vpy` and replace:
```py
#                                 1920x1080
if (input.width * input.height) > 2073600:
	clip = input.resize.Bicubic(width=1920, height=1080, format=vs.RGBS, matrix_in_s="709")
```
to
```py
#                                 1280x720
if (input.width * input.height) > 921600:
	clip = input.resize.Bicubic(width=1280, height=720, format=vs.RGBS, matrix_in_s="709")
```
