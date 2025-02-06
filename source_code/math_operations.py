class basic_math:

    # create add function
    def add(*numbers):
        sumall = 0
        for number in numbers:
            sumall += number
    
        return sumall
    #If you want to indent all, select lines --> "Ctrl + ]"

    # create multiply function
    def multiply(*numbers):
        productall = 1
        for number in numbers:
            productall *= number
    
        return productall

class plotting:

    def plot_graph(x, y):
        
        from matplotlib import pyplot as plt
        from matplotlib import style

        style.use('ggplot')
        fig, ax = plt.subplots()
        ax.plot(x, y, 'g', label='line1', linewidth=5)
        ax.set_title('CHEE 412-005')
        ax.set_ylabel('moola')
        ax.set_xlabel('products')
        
        ax.legend()
        ax.grid(True, color='k')
        #plt.savefig('moola.png')
        return(ax)
