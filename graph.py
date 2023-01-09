import matplotlib as plt 

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'/{name}Bar.png')
    print(f"La ruta es imgs/{name}Bar.png")
    plt.close()


def generate_pie_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('imgs/chart_pie_final.png')