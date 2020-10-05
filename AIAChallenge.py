import numpy as np

# Create class to do the convolution process. 
class ConvolutionOps:
    
    
    # Constructor 
    def __init__(self):
        pass
    
    def convolution1D(self, signal, kernel, paddingType="zeroPadding"):
        # Condition for zero padding 
        if paddingType == "zeroPadding":
            # initalised a padded signal depends on the filter(kernel) size
            newPaddedSignal = np.zeros((signal.shape[0] + (kernel.shape[0]-1),))
            # Add the content of signal to the padded signal with
            # keeping the padded element of zero value.
            # kernel.shape[1]-1) this to know how many elements to add  
            # at the end and at the start of the signal
            for i in range(newPaddedSignal.shape[0]):
                if i < ((kernel.shape[0]-1) /2):
                    newPaddedSignal[i] = 0
                elif i > ((newPaddedSignal.shape[0]-1) - (kernel.shape[0]-1) /2):
                    newPaddedSignal[i] = 0
                else :
                    index = int(i- ((kernel.shape[0]-1) /2))
                    newPaddedSignal[i] = signal[index]
            print("zero padded signal:", newPaddedSignal)            
        # Condition for symmetric padding 
        if paddingType == "Symmetric":
            # initalised a symmetry padded signal depends on the filter(kernel) size
            newPaddedSignal = np.zeros((signal.shape[0] + (kernel.shape[0]-1),))
            # use lastIndexSignal to know the last index of my signal to fill
            # the symmetric values in the padded indecies 
            lastIndexSignalFirstCond = signal.shape[0]-1 
            lastIndexSignalSecCond = signal.shape[0]-1 
            # Add the content of signal to the padded signal with
            # keeping the padded element of zero value.
            # kernel.shape[1]-1) this to know how many elements to add  
            # at the end and at the start of the signal
            for i in range(newPaddedSignal.shape[0]):
                s = int((((kernel.shape[0]-1) /2)-1))
                if i < ((kernel.shape[0]-1) /2):
                    newPaddedSignal[s-i] = signal[i] 
                    lastIndexSignalFirstCond = lastIndexSignalFirstCond -1
                elif i > ((newPaddedSignal.shape[0]-1) - (kernel.shape[0]-1) /2):
                    newPaddedSignal[i] = signal[lastIndexSignalSecCond]
                    lastIndexSignalSecCond = lastIndexSignalSecCond -1
                else :
                    index = int(i- ((kernel.shape[0]-1) /2))
                    newPaddedSignal[i] = signal[index]
            print("padded symmety", newPaddedSignal)
            
        #....................... Flip the 1D kernel ..............................
        
        # initalize a flipped kernel 
        flipped1DKernel = np.zeros((kernel.shape[0],))
        kernelLastIndex = kernel.shape[0]-1 
        for i in range (kernel.shape[0]):
            # swap operation(sorting) 
            flipped1DKernel[i] = kernel[kernelLastIndex - i]
        #................ start the convolution process ............................ 
        # the newly convolved signal size will be the same as the original signal 
        # because of the padding.
        # initalize a covolved signal 
        newConvoledSignal = np.zeros((signal.shape[0], ))
        sumRes = 0
        for i in range(newConvoledSignal.shape[0]):
            for j in range(flipped1DKernel.shape[0]):
                sumRes = sumRes + (flipped1DKernel[j] * newPaddedSignal[i+j])
            newConvoledSignal[i] = sumRes
            sumRes = 0
        return newConvoledSignal   
        
        
    # ............................2D Convolution Function, no padding      
    def convolve2D(self, signal, kernel):
        # Find number of shifting (Row and Column), no padding
        # shift horizentally: column filter - column signal
        # shift vertically: row filter - row signal 
        numOfRowToShift = np.abs(signal.shape[0]-kernel.shape[0]) + 1 
        numOfColumnToShift = np.abs(signal.shape[1]-kernel.shape[1]) + 1 
        flippedKernel = self.flipFilter(kernel)
        convolvedSignal = np.zeros((numOfRowToShift,numOfColumnToShift ))
        sumRes = 0
    
          # Start Convolution Process. 
        for m in range(numOfColumnToShift):
            for s in range(numOfRowToShift):
                for i in range(flippedKernel.shape[0]):
                    for j in range(flippedKernel.shape[1]):
                        sumRes = sumRes + (flippedKernel[i,j] *
                                           signal[i+m,j+s])
                convolvedSignal[s, m] = sumRes
                
        return convolvedSignal 
    
    #Flipping the Kernel 180 degree for convolution     
    def flipFilter(self, kernelTest): 
        
        firstFlippedKernel = np.zeros((kernelTest.shape[0],kernelTest.shape[1])) # initialize fipped kernel, first flip 
        finalFlippedKernel = np.zeros((kernelTest.shape[0],kernelTest.shape[1])) # initalize flipped kernel, second flip 
        
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
    
    
 #................................... Testing............................... 
# Create Object Of Convolution class   
startConv = ConvolutionOps()

# ...................Testing Convolution 2D function .....................
print('......Test 2D Convolution...........')
signal = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
kernel = np.array([[1,0,1],
                  [0,1,1],
                  [0,1,1]])
print('Signal:\n',signal)
print('Filter:\n', kernel)
# First Flip the kernel , call flip function
flippedKernel = startConv.flipFilter(kernel)  
# CAll the 2d Conv function 
print('Convolved Signal 2D \n', startConv.convolve2D(signal,flippedKernel) )
print('........Test 1D convolution..............')
#............. Testing Convolution 1D ......................

signal3 = np.array([1,2,3,4])
kernel4 = np.array([0,1,1])

# Print the signal,Filter we are testing on, change in the values
# to check my function compared with numpy function 
print('Signal:',signal3)
print('Filter:', kernel4)
print('Results.........................')
# call the conv 1D fucntion, kernel should be of odd size, sym padding  
print('Convolved Signal 1D with sym padding, my function:', startConv.convolution1D(signal3,kernel4,"Symmetric"))

# call the conv 1D fucntion, kernel should be of odd size, 0 padding  
print('Convolved Signal 1D with zero padding, my function:', startConv.convolution1D(signal3,kernel4,"zeroPadding"))


print('convolved Signal using numpy function',np.convolve(signal3,kernel4))

    
        