# Angle-prediction
The main goal of this project is to build a tensorflow model which predicts an angle of an image rotation. This model takes RGB image with rotated rectangles on it as input and gives this angle of rotatin as output.
# Description of the input images:
  1.The size of the an input image is 128x128
  2.Training set has 10000 images
  3.Each image has from 1 to 10 rectangles
  4.The width and height of each rectangle ranges from 0.1 to 1 of width and height of the initial image
  5.Width of the rectangle's borders ranges between 1 and 5 pixels
  6.The center of each rectangle can be in any pixel of the initial image
  7.The pattern of this rectangles randomly rotates between -10 and 10 degrees

