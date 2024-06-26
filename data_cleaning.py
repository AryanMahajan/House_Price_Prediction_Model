import pandas as pd
import seaborn as sns
from path import TRAIN_PATH

df = pd.read_csv(TRAIN_PATH)

removing_columns = ["Id","MSSubClass","MSZoning","LotFrontage","Street","Alley","LotShape","LandContour","Utilities","LotConfig","LandSlope","Neighborhood","Condition1","Condition2","BldgType","HouseStyle","OverallQual","OverallCond","YearBuilt","YearRemodAdd","RoofStyle","RoofMatl","Exterior1st","Exterior2nd","MasVnrType","MasVnrArea","ExterQual","ExterCond","Foundation","BsmtQual","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinSF1","BsmtFinType2","BsmtFinSF2","BsmtUnfSF","TotalBsmtSF","Heating","HeatingQC","CentralAir","Electrical","1stFlrSF","2ndFlrSF","LowQualFinSF","GrLivArea","KitchenAbvGr","KitchenQual","TotRmsAbvGrd","Functional","Fireplaces","FireplaceQu","GarageType","GarageYrBlt","GarageFinish","GarageCars","GarageArea","GarageQual","GarageCond","PavedDrive","WoodDeckSF","OpenPorchSF","EnclosedPorch","3SsnPorch","ScreenPorch","PoolArea","PoolQC","Fence","MiscFeature","MiscVal","MoSold","YrSold","SaleType","SaleCondition"]

df = df.drop(removing_columns, axis = 1)

df["BsmtFullBath"] = df["BsmtFullBath"] + df["BsmtHalfBath"] + df["FullBath"] + df["HalfBath"]

df = df.drop(["BsmtHalfBath","FullBath","HalfBath"], axis = 1)

df = df.rename(columns={"LotArea":"Area", "BsmtFullBath":"Bathrooms","BedroomAbvGr":"Bedrooms","SalePrice":"Sales Price"})

head = df.head()
print(head)