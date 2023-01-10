import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'{name}Bar.png')
    print(f"La ruta es {name}Bar.png")
    plt.close()


def generate_pie_chart(name,labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    print(f"La ruta es {name}Pie.png")
    plt.savefig(f'{name}Pie.png')


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    generate_bar_chart('Bar',labels, values)
    generate_pie_chart('Pie',labels,values)
