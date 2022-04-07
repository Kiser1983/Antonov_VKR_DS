import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from model import model


app = Flask(__name__)


def get_prediction(X_test):
    prediction = model.predict(X_test)
    return str(prediction)


#@app.route('/')
#def index():

 #   return model


@app.route('/predict/', methods=['post', 'get'])
def index():
    message = ''
    if request.method == 'POST':
        var1 = request.form.get('Плотность, кг/м3')
        var2 = request.form.get('модуль упругости, ГПа')
        var3 = request.form.get('Количество отвердителя, м.%')
        var4 = request.form.get('Содержание эпоксидных групп,%_2')
        var5 = request.form.get('Температура вспышки, С_2')
        var6 = request.form.get('Поверхностная плотность, г/м2')
        #  var7 = request.form.get('Модуль упругости при растяжении, ГПа')
      #  var8 = request.form.get('Прочность при растяжении, МПа')
        var9 = request.form.get('Потребление смолы, г/м2')
        var10 = request.form.get('Угол нашивки, град')
        var11 = request.form.get('Шаг нашивки')
        var12 = request.form.get('Плотность нашивки')
        X_test = pd.DataFrame([[var1, var2, var3, var4,
                           var5, var6, 0.0, 0.0, var9, var10, var11,var12]])

        scaler = trans.transform(X_test)
        standart = df_standart.transform(scaler)
        PCA = pca.transform(standart)
        df_pca_new= pca.inverse_transform(PCA)
        df_pca = pd.DataFrame(df_pca_new, columns=X_test.columns)

        message = 'Соотношение матрица-наполнитель:', get_prediction(df_pca)

    return render_template('login.html', message=message)


if __name__ == '__main__':
    model = keras.models.load_model('Models/model11.h5')

    app.run()
