# -*- coding: utf-8 -*-
"""
Created on Sun May 14 20:39:09 2023

@author: doank
"""
import os
import pandas as pd 
import matplotlib.pyplot as plt
import random 


target = r' INSERT YOUR DIRECTORY LOCATION HERE '
os.chdir(target)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
for root, dirname, files in os.walk(target): 

	for x in files:
        #looks for the file with the correct name 
		if x.endswith('.xlsx'):
                    #Opens the files and reads the csv
                    with open(os.path.join(x),"r")as f:
                        df2=pd.read_excel(x)
                        df2=df2.sort_values(by='avg cost/share',ascending=False)
                
                       
                        #Total amount 
                        portfolio_total_amount= sum(df2['avg cost/share'] *df2['Shares'])
                        portfolio_total_amount= round(portfolio_total_amount,2)
                        print(portfolio_total_amount)
                        
                        
                        #Visually Show porfolio
                
                        stock_ticker=df2['Ticker'].values
                        sizes= df2['avg cost/share'] *df2['Shares']
                        # Makes Random part of Pie chart explode everytime 
                        listofZeros=[0]*df2.shape[0]
                        n= random.randint(0,df2.shape[0]-1)
                        listofZeros[n]=0.1
                        explode=listofZeros
                        
                        #Make figure
            
                        
                        #plot figure
                        ax1.pie(sizes,labels=stock_ticker, autopct='%.2f%%', shadow='True', startangle=360,explode=explode)
                        
                        
                        #title 
                        ax1.set_title('Portfolio Pie Chart',color='Black',fontsize=24)
                        label= sizes.values
                        #Add text to visual
                        x=-2.2
                        y=1
                        ax1.text(x,y, 'Overview:', fontsize=24, color='purple')
                        y_counter=0.12
                        ax1.text(x,y-y_counter, 'Total:$ '+ str(portfolio_total_amount), fontsize=15, color='blue')
                       
                        for i in range(0,df2.shape[0]):
                            ax1.text(x,0.88-y_counter, stock_ticker[i] +':$'+ str( round(label[i],2)), fontsize=14, color='Black')
                            y_counter=y_counter+0.12
                            
                        #Display Chart
                        ax1
                      
                    #split between diffrent categories of invesstmnets
                    
                    Category=df2['Category'].value_counts()
                    Investment_count=df2['Category'].count()
                
                   
            
                    #plot figure
                    ax2.pie(Category,labels=Category.index, autopct='%.2f%%', shadow='True',startangle=360)
                    
                    #figure labels
                    ax2.set_title('Portfolio Divison', color='Black', fontsize=24)
                    #Add text to visual
                    x2 = -1.5
                    y2 = 1
                    y2_counter = 0.1
                    ax2.text(x2,y2, 'Overview:', fontsize=24, color='purple')
                    ax2.text(x2,y2-y2_counter, 'Investment Count: '+ str(Investment_count), fontsize=15, color='blue')
                    
                    for i in range(0,Category.shape[0]):
                        ax2.text(x2,0.9 -y2_counter,' #of in '+Category.index[i] +"'s: "+ str( Category[i]), fontsize=14, color='Black')
                        y2_counter=y2_counter+0.20
                        
                    # Display Chart 
                    ax2
                    
                    plt.show()
                  
                #Source for most of the Coding:  https://www.youtube.com/watch?v=X349OK519Aw&ab_channel=ComputerScience    
                    
                    
                        
                        
                        
                        
                    
                    