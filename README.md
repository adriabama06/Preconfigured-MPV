# Download:
[(click aqui)](https://github.com/adriabama06/Preconfigured-MPV/archive/refs/heads/master.zip)

# Preconfigured MPV with RIFE, FSR, Anime4k

- mpv: https://sourceforge.net/projects/mpv-player-windows/files/64bit/mpv-x86_64-20221113-git-2f74734.7z/
- vapoursynth: https://github.com/vapoursynth/vapoursynth/releases/tag/R60
- mpv settings edited from: https://github.com/Tsubajashi/mpv-settings
- VapourSynth-RIFE-ncnn-Vulkan: https://github.com/HomeOfVapourSynthEvolution/VapourSynth-RIFE-ncnn-Vulkan/releases/tag/r9
- VapourSynth-RIFE-ncnn-Vulkan models: https://github.com/HomeOfVapourSynthEvolution/VapourSynth-RIFE-ncnn-Vulkan/releases/tag/r3
- Anime4k: https://github.com/bloc97/Anime4K
- FSR: https://gist.github.com/agyild/82219c545228d70c5604f865ce0b0ce5
- FSRCNN: https://github.com/igv/FSRCNN-TensorFlow
- NIS (NVScaler): https://gist.github.com/agyild/7e8951915b2bf24526a9343d951db214
<br>Inspired by: https://github.com/hooke007/MPV_lazy

# GPU:
## Recommended (**1080p 30fps -> 1080p 60fps**):
- **RTX 3080**
## Minimum (**720p 30fps -> 720p 60fps**):
- **RTX 2080 ti**
# Info
If you have problems during playback
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
