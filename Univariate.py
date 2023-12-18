class Univariate():
# function for find qualitative variables (characters) and quantiative variables (numbers) append in quan and qual list.
    def quanqual(dataset):
        quan = []
        qual = []

        for ColumnName in dataset.columns:
            #print(ColumnName)

            if (dataset[ColumnName].dtype=='O'):
                #print("qual")
                qual.append(ColumnName)
            else:
                #print("quan")
                quan.append(ColumnName) 
        return quan,qual

#  find lesser and greater outliers in quan variables append in lesser and greater list. 
    def find_outliers(quan,descriptive):
    lesser = []
    greater = []

    for columnName in quan:
        if descriptive[columnName]['Min'] < descriptive[columnName]['Lesser']:
            lesser.append(columnName)
        if descriptive[columnName]['Max'] > descriptive[columnName]['Greater']:
            greater.append(columnName)
    return lesser, greater

# Replace the outliers in greater and lesser utliers list
   def replace_outliers(dataset, descriptive):
    for columnName in lesser_outliers:
        dataset[columnName][dataset[columnName] < descriptive[columnName]['Lesser']] = descriptive[columnName]['Lesser']
    
    for columnName in greater_outliers:
        dataset[columnName][dataset[columnName] > descriptive[columnName]['Greater']] = descriptive[columnName]['Greater']
    return columnName 

# Create tables with mentioned columns and caluculation of frequency's      
    def freqtable(columnName,dataset):
        freqtable = pd.DataFrame(columns=['Unique_values','Frequency','Relative frequency','Cusum'])
        freqtable['Unique_values'] = dataset[columnName].value_counts().index
        freqtable['Frequency'] = dataset[columnName].value_counts().values
        freqtable['Relative frequency'] = (freqtable['Frequency']/103)
        freqtable['Cusum'] = (freqtable['Frequency']/103).cumsum()
        return freqtable

# Create tables with mentioned coilumns and calculations of mean, median, mode, Percentile and IQR
    def Univariate(dataset, quan):
        descriptive = pd.DataFrame(index=['Mean','Median','Mode', 
                                      'Q1:25%', 'Q2:50%', 'Q3:75%','99%', 'Q4:100%',
                                      'IQR','1.5rule','Lesser','Greater','Min','Max'],columns=quan) 
        for columnName in quan:
            descriptive[columnName]['Mean'] = dataset[columnName].mean()
            descriptive[columnName]['Median'] = dataset[columnName].median()
            descriptive[columnName]['Mode'] = dataset[columnName].mode()[0]
        
            descriptive[columnName]['Q1:25%'] = dataset.describe()[columnName]['25%']
            descriptive[columnName]['Q2:50%'] = dataset.describe()[columnName]['50%']
            descriptive[columnName]['Q3:75%'] = dataset.describe()[columnName]['75%']
            descriptive[columnName]['99%'] = np.percentile(dataset[columnName],99)
            descriptive[columnName]['Q4:100%'] = dataset.describe()[columnName]['max']
        
            descriptive[columnName]['IQR'] = descriptive[columnName]['Q3:75%'] - descriptive[columnName]['Q1:25%'] 
            descriptive[columnName]['1.5rule'] = 1.5* descriptive[columnName]['IQR'] 
            descriptive[columnName]['Lesser'] = descriptive[columnName]['Q1:25%'] -  descriptive[columnName]['1.5rule']
            descriptive[columnName]['Greater'] = descriptive[columnName]['Q3:75%'] + descriptive[columnName]['1.5rule']
            descriptive[columnName]['Min'] = dataset[columnName].min()
            descriptive[columnName]['Max'] = dataset[columnName].max()
            
        return descriptive

