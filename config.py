BATCH_SIZE = 64
EPOCHS = 135
WARMUP_EPOCHS = 0
LEARNING_RATE = 1E-4

EPSILON = 1E-6
IMAGE_SIZE = (448, 448)

S = 8       # Divide each image into a SxS grid, max width divisible by 8
B = 23       # Number of bounding boxes to predict, if we have 23 that's all the possible objects in the image. so we don't run into not having enough boxes to allocate to each object.
C = 3      # Number of classes in the dataset