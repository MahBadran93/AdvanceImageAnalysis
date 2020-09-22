import numpy as np

# Create class to do the convolution process. 
class ConvolutionOps:
    
    
    # Constructor 
    def __init__(self):
        pass
        
        
    # Convolution Function     
    def convolve(self, signal, kernel):
        # Find number of shifting (Row and Column), no padding
        numOfRowShift = np.abs(signal.shape[0]-kernel.shape[0]) + 1 
        numOfColumnShift = np.abs(signal.shape[1]-kernel.shape[1]) + 1 
        flippedKernel = self.flipFilter(kernel)
        # Start Convolution Process. 
       
        
    #Flipping the Kernel 180 degree for convolution     
    def flipFilter(self, kernelTest): 
        
        firstFlippedKernel = np.zeros((kernelTest.shape[0],kernelTest.shape[1])) # temp variable 
        finalFlippedKernel = np.zeros((kernelTest.shape[0],kernelTest.shape[1])) # flipped kernel
        
        # First flipping operation, inverse clock wise 90 degree
        lastIndexRow = kernelTest.shape[0]-1
        lastIndexColumn = kernelTest.shape[1]-1
        for i in range(kernelTest.shape[1]):
            for j in range(kernelTest.shape[0]):
                firstFlippedKernel[lastIndexRow-j,i] = kernelTest[i,j]
                
        # Second Flipping Operation, inverse clock wise 90 degree 
        lastIndexFlippedRow = firstFlippedKernel.shape[0]-1
        lastIndexFlippedColumn = firstFlippedKernel.shape[1]-1
        for i in range(firstFlippedKernel.shape[1]):
            for j in range(firstFlippedKernel.shape[0]):
                finalFlippedKernel[lastIndexFlippedRow-j,i] = firstFlippedKernel[i,j]
                
        return finalFlippedKernel 
    
    
    
startConv = ConvolutionOps()

kernel = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

flippedKernel = startConv.flipFilter(kernel)
    
print(flippedKernel)    
    
    
        