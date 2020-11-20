from celluloid import Camera
import matplotlib.pyplot as plt

fig = plt.figure()
camera = Camera(fig)
for i in range(10):
    for j in range(10):
        plt.scatter(i, j)
        camera.snap()
a = camera.animate()
a.save('out.mp4')
