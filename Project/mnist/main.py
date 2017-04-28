from mnist import MNIST

mndata = MNIST('samples')

images, labels = mndata.load_training()

# index = random.randrange(0, len(images))  # choose an index ;-)
index = 100
print(mndata.display(images[index]))