class Helper:

    def __init__(self, testval=None):
        self.testval = 10
        self.numerical_features_list = [
                    'propertyTaxRate', 
                    'garageSpaces', 
                    'parkingSpaces', 
                    'numOfPhotos', 
                    'numOfAccessibilityFeatures',
                    'numOfAppliances',
                    'numOfParkingFeatures',
                    'numOfPatioAndPorchFeatures',
                    'numOfSecurityFeatures',
                    'numOfWaterfrontFeatures',
                    'numOfWindowFeatures',
                    'numOfCommunityFeatures',
                    'lotSizeSqFt',
                    'livingAreaSqFt',
                    'numOfPrimarySchools',
                    'numOfElementarySchools',
                    'numOfMiddleSchools',
                    'numOfHighSchools',
                    'avgSchoolDistance',
                    'avgSchoolRating',
                    'avgSchoolSize',
                    'MedianStudentsPerTeacher',
                    'numOfBathrooms',
                    'numOfBedrooms',
                    'numOfStories']
        self.categorical_features_list = [
                        'hasAssociation',
                        'hasCooling',
                        'hasGarage',
                        'hasHeating',
                        'hasSpa',
                        'hasView',
                        ]

    def get_test_val(self):
        return self.testval