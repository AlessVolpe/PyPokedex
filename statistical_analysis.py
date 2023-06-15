class statistical_analysis:
    def max_stats(df, col_list):
        message = ''
        
        for col in col_list:
            stat = df[col].max()
            name = df[df[col] == df[col].max()]["Name"].values[0]
            message += name + ' has the greatest ' +  col + ' stat of ' + str(stat) + '\n'
        
        return message
    
    def min_stats(df, col_list):
        message = ''
        for col in col_list:
            stat = df[col].min()
            name = df[df[col]==df[col].min()]['Name'].values[0]
            message += name +' has the worst ' + col + ' stat of ' + str(stat) + '.\n'
            
        return message
    
    def barh_stats(df, types, colors):
        import pandas as pd
        import matplotlib.pyplot as plt
        
        i = 0
        plt.figure(figsize=(15,5))
        plt.suptitle('Statistics', fontsize=15)
        
        for t in types:
            i+=1   
            plt.subplot(121)
            plt.title('Mean')
            pd.to_numeric(df[df['Type'] == t]).mean(axis = 0).plot(kind='barh', color = colors[i])
            
            plt.subplot(122)
            plt.title('Standard Deviation')
            pd.to_numeric(df[df['Type'] == t]).std().plot(kind='barh', color = colors[i])
        
        #Add list of Pokemon Type to legend
        plt.legend(types, bbox_to_anchor=(1.3, 1.1))

