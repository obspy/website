"""
Effortlessly read and write various waveform file formats

>>> import obspy
>>> st = obspy.read("BW.FURT..EH.D.2010.005")
>>> print st
3 Trace(s) in Stream:
BW.FURT..EHE | 2010-01-05T00:00:00 - 2010-01-06T00:00:00 | 200.0 Hz, 17280068 samples
BW.FURT..EHN | 2010-01-05T00:00:00 - 2010-01-06T00:00:00 | 200.0 Hz, 17280068 samples
BW.FURT..EHZ | 2010-01-05T00:00:00 - 2010-01-06T00:00:00 | 200.0 Hz, 17280068 samples
>>> st.filter("lowpass", freq=1.0)
>>> st.write("BW.FURT..EH.D.2010.005", format="sac")
"""
