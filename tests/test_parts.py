from source.image_reader import *
from matplotlib import pyplot as plt

calibrantExternalPicture = Measurement('pictureOnly','measurement')

testImagePath = measurement_storage+'/test_raw.jpg'

profile = calibrantExternalPicture.profile(testImagePath, (135,150),(135,300),25)

polifit = calibrantExternalPicture.fit_profile(profile)

print (polifit)

plt.plot(profile)
plt.show()
