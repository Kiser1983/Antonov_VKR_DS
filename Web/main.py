from tensorflow import keras
import numpy as np
import pandas as pd

from flask import Flask, request, render_template
from keras.models import load_model
import pandas as pd

app = Flask(__name__)


@app.route('/predict/', methods=['post', 'get'])
def compute():
    result = ''
    error = dict()
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
        input = pd.DataFrame([[var1, var2, var3, var4, var5, var6, 0.0, 0.0, var9, var10, var11,var12]])
        result = model.predict(input)[0][0]
    return render_template('index.html', result=result, error=error)


if __name__ == '__main__':
    model = load_model('Models/')
    app.run(host='localhost', port=8081, debug=True)

