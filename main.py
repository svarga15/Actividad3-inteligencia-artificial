from sklearn import tree


def aprensizaje():
    # el primero valor corresponde a la altura, el segundo al peso, y el tercero a la temperatura
    caracteristicas = [[8, 0.6, 50],
                       [8, 0.6, 51],
                       [8, 0.6, 52],
                       [39, 0.8, 67],
                       [39, 0.8, 68],
                       [39, 0.8, 69]]

    # 0 corresponde a gato y 1 a perro, segun las caracteristicas anteriores
    valores = [0, 0, 0, 1, 1, 1]

    # esta funcion es la que vamos a ulitizar
    clasificaciones = tree.DecisionTreeClassifier()

    # lo podemos a entrenar todos los patrones para que hagas las predicciones
    clasificaciones.fit(caracteristicas, valores)

    respuesta = clasificaciones.predict([[39, 0.8, 67]])

    print(respuesta)


if __name__ == '__main__':
    aprensizaje()
