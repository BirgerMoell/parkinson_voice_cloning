import tortoise as tts  # Importing the Tortoise TTS library
import tortoise.utils as utils  # Importing utility functions


clips_paths = "data/young_control"

text = "Il ramardo della zia, il papà, o il babbo come dice il piccolo dado, era sull'etto, sotto di lui accanto al lago sediva Gigi, detto Ciccio, cocco della mamma e della nonna, vicino ad un sasso c'era una rossa rossa, vivo e lo sciocco vedendo la vole per la zia."

reference_clips = [utils.audio.load_audio(p, 22050) for p in clips_paths]
tts = api.TextToSpeech()
pcm_audio = tts.tts_with_preset(text, voice_samples=reference_clips, preset='fast')