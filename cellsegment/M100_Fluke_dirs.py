""" Directorises for Fluke preparatioan and training and testing images
"""

basepath = '*'
originImages = '*'
train = '*'
validTxtFile = '*'
label = '*'
test = '*'
crop = '*'
sizeCsvFile = '*'
cropValidTxtFile  = '*'
cropTrain  = '*'
cropLabel  = '*'
model  = '*'

def set_base_path(_basepath:str):
    global basepath, originImages, train, validTxtFile, label, test, crop, sizeCsvFile, cropValidTxtFile, cropTrain, cropLabel, model

    basepath = _basepath
    originImages = basepath + '/Original'
    train = basepath + '/Fullsize/Train'
    validTxtFile =  basepath + '/Fullsize/valid.txt'
    label =  basepath + '/Fullsize/Label'
    test =  basepath + '/Fullsize/Test'
    crop =  basepath + '/Crop-200'
    sizeCsvFile =  basepath + '/file_size.csv'
    cropValidTxtFile =  basepath + '/Crop-200/valid.txt'
    cropTrain =  basepath + '/Crop-200/Train'
    cropLabel =  basepath + '/Crop-200/Label'
    model = basepath + '/models/'



def printVariables(variable_names):
    print(__doc__)
    """Renders variables and their values on the terminal."""
    max_name_len = max([len(k) for k in variable_names])
    max_val_len = max([len(str(globals()[k])) for k in variable_names])

    for k in variable_names:
        print(f'  {k:<{max_name_len}}:  {globals()[k]:{max_val_len}}')
def printdirs(d):
    ks = [k for k in d if (k[:2] != "__" and not callable(globals()[k]))]
    printVariables(ks)

if __name__ == "__main__":

    ks = [k for k in dir() if (k[:2] != "__" and not callable(globals()[k]))]

    printVariables(ks)
    # printdir()
