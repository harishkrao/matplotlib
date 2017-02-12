import pandas as pd
import warnings
import matplotlib.patches as mpatches 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white",color_codes=True)

grad_students = pd.read_csv("/Users/Harish/Documents/HK_Work/Machine Learning/fivethirtyeight/data/college-majors/grad-students.csv")

sorted_desc_grad_total = grad_students.sort_values(by='Grad_total',ascending=0)

#print(sorted_desc_grad_total.head())

sns.FacetGrid(sorted_desc_grad_total.head(n=10),hue="Major")\
.map(plt.bar,"Major_code","grad_studentstotal")\
.add_legend()

#plt.tight_layout()
plt.show()
