import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize


class SamplePdf():

  k = 0  # number of samples
  uni_sample = np.array([])  # array containing the uniform samples
  pdf_sample = np.array([])  # array containing the new samples of the pdf

  # function that is called by the root function
  def cdf_root(self, x, sample):
    # TODO: add the correct function here, note that we can not formulate the solving in terms of F(x)=y but rather F(x,y)=0 (solved for x)
    root = x - sample  # modify this line
    return root

  def __init__(self, k=1000):
    self.k = k
    self.uni_sample.resize(k)
    self.pdf_sample.resize(k)

  def sample_pdf(self, uni_sample):
    self.uni_sample = uni_sample
    # loop through all samples
    for i in range(self.uni_sample.size):
      # We have to invert the CDF function to get the new sample.
      # As there is no analytical solution we can use the scipy.optimize function root
      # Generally the root function looks for the root of the input function F(x), i.e. F(x) = 0 is solved for x
      # if we want to have an additional argument to the function that is not optimized for we pass it using the 'args' setting we can set
      # so passing y to the args setting of the root function we can solve F(x,y) = 0 for x

      # TODO add the correct call of the scipy.optimize.root(...) function
      root = 0  # modify this line

      self.pdf_sample[i] = root.x

  # plot the results in a histogram
  def plot_result(self):
    if self.pdf_sample.size == 0:
      print("First sample_pdf needs to be called")
      return
    # for a nicer plot only show the values between -5 and 10
    cond1 = self.pdf_sample >= 10
    cond2 = self.pdf_sample <= -5
    # get index for elements statisfying condition 1 or 2
    index = [i for i, v in enumerate((cond1 | cond2)) if v]

    # remove elements with the given index and plot as histogram
    plt.hist(np.delete(self.pdf_sample, index), bins=100, normed=True)

    # plot the reference plot
    x = np.arange(-5.0, 10.0, 0.01)
    # TODO: calculate the values of f(x)
    y = x  # modify this line
    plt.plot(x, y)

    plt.show()
    return
