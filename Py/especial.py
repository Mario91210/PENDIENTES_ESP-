import openpyxl
import PIL
import pandas
import matplotlib

workbook = "proyectoespecial.xlsx"
df = pd.read_excel(workbook)

print(df.head())

valores = df[["Pendiente","Porcentaje"]]
print(valores)

ax = valores.plot.bar(x = "Pendiente", y = "Porcentaje", rot = 0)
plt.show()

#Si desea ver la imagen del �rea de estudio indique "y"
run = raw_input("Desea ver el Ejido de estudio y/n\n")


from PIL import Image


#Para que la imagen pueda ser expuesta deber� de indicarse con el nombre de la imagen
def show(path_name):
    image = ()
image.open(path_name)=
    image.show()
show()
