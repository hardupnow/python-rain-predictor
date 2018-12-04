import RainPredictor
import seaborn as sns
import matplotlib.pyplot as plt
import re


def test_rain_predictor_file_read():
    rain_predictor = RainPredictor.RainPredictor('../data/Weather Dataset_Filtered.csv')
    dataframe = rain_predictor.read_file(column_indices=[8, 10, 15])
    dataframe = rain_predictor.rename_columns(dataframe, ['isRain', 'temperature', 'humidity'])
    dataframe = rain_predictor.replace_data_regex(dataframe, 'isRain', re.compile('^.*(RA|SN|DN|PL).*$'), 'Yes')
    dataframe = rain_predictor.replace_data_regex(dataframe, 'isRain', re.compile('^(?!.*Yes).*$'), 'No')
    # sns.countplot(y=dataframe['isRain'], data=dataframe)
    # plt.show()
    (logistic, x_test, y_test) = rain_predictor.prediction_logic(dataframe[['humidity']+['temperature']], dataframe[['isRain']])
    # c_matrix = rain_predictor.get_confusion_matrix(logistic, x_test, y_test)
    # rain_predictor.display_confusion_matrix(c_matrix)
    print(rain_predictor.get_rain_prediction(logistic, [[24.4, 90]]))


test_rain_predictor_file_read()
