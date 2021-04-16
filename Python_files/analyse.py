

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.preprocessing import MinMaxScaler
import warnings
import scipy.stats as st
import statsmodels as sm


def analyse(df_input,df_all_input):
    df = df_input
    fig, ax = plt.subplots(figsize=(17,8))
    plt.scatter(df['num_pages'],df['num_ratings'],
            label = 'books',
            color = 'lightpink', 
            edgecolor = 'darkviolet')
    plt.xlabel('num_pages', fontsize=20,labelpad=20)
    plt.ylabel('num_ratings', fontsize=20,labelpad=20)
    plt.title('2D Scatterplot', fontsize=38,y=1.15)
    plt.xlim(0,1900)
    plt.xticks(np.arange(0,1900,100),fontsize=14, rotation=45)
    #plt.ylim(0,max(df['num_ratings']))
    plt.yticks(np.arange(0,max(df['num_ratings']),1000000),fontsize=14)
    plt.grid(True,linestyle='dashed')
    plt.show()

# 3
    x=df['num_pages']
    y=df['num_ratings']
    # Pearson 
    pearson = st.pearsonr(x, y)
    print(f'Pearson: Correlation= {pearson[0]} , p-value= {pearson[1]}')
    # Spear
    spear = st.spearmanr(x, y)
    print(f'Spear: Correlation= {spear[0]} , p-value= {spear[1]}')
    # Kendal
    kendal = st.kendalltau(x,y)
    print(f'Kendal: Correlation= {kendal [0]} , p-value= {kendal [1]}')
    # python
    python_corr = df['num_pages'].corr(df['num_ratings'])
    print(f'Correlation= {python_corr}')


#### avg_rating
    fig, ax = plt.subplots(figsize=(17,8))
    plt.hist(df.avg_rating, 
         bins = np.arange(3.5,4.65,0.1), ## change for a better bin scale
         color='cornflowerblue',
         edgecolor = "white")
    plt.xticks(np.arange(3.5,4.65,0.1),fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xlabel("Averge Rating", fontsize=20,labelpad=20)
    plt.ylabel("Books", fontsize=20,labelpad=20)
    plt.title('Distribution of avg_rating', fontsize=28,y=1.15)
    plt.grid(True,linestyle='dashed')
    plt.show()



    fig, ax = plt.subplots(figsize=(17,8))
    plt.hist(df.avg_rating, 
         bins = np.arange(3.5,4.65,0.025), ## change for a better bin scale
         color='cornflowerblue',
         edgecolor = "white")
    plt.xticks(np.arange(3.5,4.65,0.1),fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xlabel("Averge Rating", fontsize=20,labelpad=20)
    plt.ylabel("Books", fontsize=20,labelpad=20)
    plt.title('Distribution of avg_rating', fontsize=28,y=1.15)

    plt.grid(True,linestyle='dashed')
    plt.show()



    fig, ax = plt.subplots(figsize=(17,8))
    plt.hist(df.avg_rating, 
         bins = np.arange(3.5,4.65,0.01), ## change for a better bin scale
         color='cornflowerblue',
         edgecolor = "white")
    plt.xticks(np.arange(3.5,4.65,0.1),fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xlabel("Averge Rating", fontsize=20,labelpad=20)
    plt.ylabel("Books", fontsize=20,labelpad=20)
    plt.title('Distribution of avg_rating', fontsize=28,y=1.15)
    plt.grid(True,linestyle='dashed')
    plt.show()



### 4

    fig, ax = plt.subplots(figsize=(17,8))
    plt.hist(df.minmax_norm_ratings, 
         bins = np.arange(0,10,0.5), ## change for a better bin scale
         color='cornflowerblue',
         edgecolor = "white")
    plt.xticks(np.arange(0,10,1),fontsize=14, rotation=45)
    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xlabel("minmax_norm Rating", fontsize=20,labelpad=20)
    plt.ylabel("Books", fontsize=20,labelpad=20)
    plt.title('Distribution of minmax_norm_ratings', fontsize=28,y=1.15)
    plt.grid(True,linestyle='dashed')
    plt.xlim(0,10)
    plt.show()



### 4

    fig, ax = plt.subplots(figsize=(17,8))
    plt.hist(df.minmax_norm_ratings, 
            bins = np.arange(0,10,0.1), ## change for a better bin scale
            color='cornflowerblue',
            edgecolor = "white")
    plt.xticks(np.arange(0,10,1),fontsize=14, rotation=45)
    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xlabel("minmax_norm Rating", fontsize=20,labelpad=20)
    plt.ylabel("Books", fontsize=20,labelpad=20)
    plt.title('Distribution of minmax_norm_ratings', fontsize=28,y=1.15)
    plt.grid(True,linestyle='dashed')
    plt.xlim(0,10)
    plt.show()

### 5

    fig, ax = plt.subplots(figsize=(17,8))
    plt.hist(df.mean_norm_ratings, 
            bins = np.arange(0,10,0.5), ## change for a better bin scale
            color='cornflowerblue',
            edgecolor = "white")
    plt.xticks(np.arange(2,9,1),fontsize=14, rotation=45)
    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xlabel("mean_norm Rating", fontsize=20,labelpad=20)
    plt.ylabel("books", fontsize=20,labelpad=20)
    plt.title('Distribution of mean_norm_ratings', fontsize=28,y=1.15)
    plt.grid(True,linestyle='dashed')
    plt.xlim(2,9)
    plt.show()

    fig, ax = plt.subplots(figsize=(17,8))
    plt.hist(df.mean_norm_ratings, 
            bins = np.arange(2,9,0.1), ## change for a better bin scale
            color='cornflowerblue',
            edgecolor = "white")

    plt.xticks(np.arange(0,10,1),fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xlabel("mean_norm Rating", fontsize=20,labelpad=20)
    plt.ylabel("books", fontsize=20,labelpad=20)
    plt.title('Distribution of mean_norm_ratings', fontsize=28,y=1.2)
    plt.grid(True,linestyle='dashed')
    plt.xlim(2,9)
    plt.show()

    # 6
    fig, ax = plt.subplots(figsize=(14,8))

    bins =np.arange(0,10,1)
    plt.hist([df['minmax_norm_ratings'],df['mean_norm_ratings']],
            bins,
            label=['minamx_norm_ratings','mean_norm_ratings'],
            color=['cornflowerblue','lightpink'],
            edgecolor = "white")

    plt.xticks(np.arange(0,10,0.5),fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xlabel("norm_rating", fontsize=20,labelpad=20)
    plt.ylabel("books", fontsize=20,labelpad=20)
    plt.title('Distribution of mean_norm_ratings', fontsize=28,y=1.2)
    plt.grid(True,linestyle='dashed')
    plt.xlim(0,10)
    plt.show()



    fig, ax = plt.subplots(figsize=(17,8))

    bins =np.arange(0,10,0.5)
    plt.hist([df['minmax_norm_ratings'],df['mean_norm_ratings']],
            bins,
            label=['minamx_norm_ratings','mean_norm_ratings'],
            color=['cornflowerblue','lightpink'],
            edgecolor = "white")

    plt.xticks(np.arange(0,10,0.5),fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xlabel("norm_rating", fontsize=20,labelpad=20)
    plt.ylabel("Books", fontsize=20,labelpad=20)
    plt.title('Distribution of mean_norm_ratings', fontsize=28,y=1.2)
    plt.grid(True,linestyle='dashed')
    plt.xlim(0,10)
    plt.show()

    matplotlib.rcParams['figure.figsize'] = (18, 10)
    matplotlib.style.use('ggplot')

    # Create models from data
    def best_fit_distribution(data, bins=200, ax=None):
        """Model data by finding best fit distribution to data"""
        # Get histogram of original data
        y, x = np.histogram(data, bins=bins, density=True)
        x = (x + np.roll(x, -1))[:-1] / 2.0

        # Distributions to check
        DISTRIBUTIONS = [        
            st.alpha,st.anglit,st.arcsine,st.beta,st.betaprime,st.bradford,st.burr,st.cauchy,st.chi,st.chi2,st.cosine,
            st.dgamma,st.dweibull,st.erlang,st.expon,st.exponnorm,st.exponweib,st.exponpow,st.f,st.fatiguelife,st.fisk,
            #st.foldcauchy,st.foldnorm,st.frechet_r,st.frechet_l,st.genlogistic,st.genpareto,st.gennorm,st.genexpon,
            st.genextreme,st.gausshyper,st.gamma,st.gengamma,st.genhalflogistic,st.gilbrat,st.gompertz,st.gumbel_r,
            st.gumbel_l,st.halfcauchy,st.halflogistic,st.halfnorm,st.halfgennorm,st.hypsecant,st.invgamma,st.invgauss,
            st.invweibull,st.johnsonsb,st.johnsonsu,st.ksone,st.kstwobign,st.laplace,st.levy,st.levy_l,st.levy_stable,
            st.logistic,st.loggamma,st.loglaplace,st.lognorm,st.lomax,st.maxwell,st.mielke,st.nakagami,st.ncx2,st.ncf,
            st.nct,st.norm,st.pareto,st.pearson3,st.powerlaw,st.powerlognorm,st.powernorm,st.rdist,st.reciprocal,
            st.rayleigh,st.rice,st.recipinvgauss,st.semicircular,st.t,st.triang,st.truncexpon,st.truncnorm,st.tukeylambda,
            st.uniform,st.vonmises,st.vonmises_line,st.wald,st.weibull_min,st.weibull_max,st.wrapcauchy
        ]

        # Best holders
        best_distribution = st.norm
        best_params = (0.0, 1.0)
        best_sse = np.inf

        # Estimate distribution parameters from data
        for distribution in DISTRIBUTIONS:

            # Try to fit the distribution
            try:
                # Ignore warnings from data that can't be fit
                with warnings.catch_warnings():
                    warnings.filterwarnings('ignore')

                    # fit dist to data
                    params = distribution.fit(data)

                    # Separate parts of parameters
                    arg = params[:-2]
                    loc = params[-2]
                    scale = params[-1]

                    # Calculate fitted PDF and error with fit in distribution
                    pdf = distribution.pdf(x, loc=loc, scale=scale, *arg)
                    sse = np.sum(np.power(y - pdf, 2.0))

                    # if axis pass in add to plot
                    try:
                        if ax:
                            pd.Series(pdf, x).plot(ax=ax)
                        end
                    except Exception:
                        pass

                    # identify if this distribution is better
                    if best_sse > sse > 0:
                        best_distribution = distribution
                        best_params = params
                        best_sse = sse

            except Exception:
                pass

        return (best_distribution.name, best_params)

    def make_pdf(dist, params, size=10000):
        """Generate distributions's Probability Distribution Function """

        # Separate parts of parameters
        arg = params[:-2]
        loc = params[-2]
        scale = params[-1]

        # Get sane start and end points of distribution
        start = dist.ppf(0.01, *arg, loc=loc, scale=scale) if arg else dist.ppf(0.01, loc=loc, scale=scale)
        end = dist.ppf(0.99, *arg, loc=loc, scale=scale) if arg else dist.ppf(0.99, loc=loc, scale=scale)

        # Build PDF and turn into pandas Series
        x = np.linspace(start, end, size)
        y = dist.pdf(x, loc=loc, scale=scale, *arg)
        pdf = pd.Series(y, x)

        return pdf



    # Plot for comparison takes time
    plt.figure(figsize=(15,10))
    #ax = data.plot(kind='hist', bins=50, normed=True, alpha=0.5, color=plt.rcParams['axes.color_cycle'][1])
    ax = df.minmax_norm_ratings.hist(
        bins=20,
        alpha=0.5,
        density=True,
        color='cornflowerblue',
        edgecolor = 'white')
    # Save plot limits
    dataYLim = ax.get_ylim()

    # Find best fit distribution
    best_fit_name, best_fit_params = best_fit_distribution(df.minmax_norm_ratings, 200, ax)
    best_dist = getattr(st, best_fit_name)

    # Update plots
    ax.set_ylim(dataYLim)
    ax.set_title(u'Minmax norm rating')
    ax.set_xlabel(u'Frequency')
    ax.set_ylabel('Frequency')



    # runs fast
    plt.figure(figsize=(14,8))
    ax = pdf.plot(lw=2, label='PDF', legend=True)
    df.minmax_norm_ratings.plot(kind='hist',
                                bins=50,
                                density=True,
                                alpha=0.5,
                                label='Data',
                                color='cornflowerblue',
                                legend=True,
                                ax=ax)

    param_names = (best_dist.shapes + ', loc, scale').split(', ') if best_dist.shapes else ['loc', 'scale']
    param_str = ', '.join(['{}={:0.2f}'.format(k,v) for k,v in zip(param_names, best_fit_params)])
    dist_str = '{}({})'.format(best_fit_name, param_str)

    ax.set_title(u'minmax_norm with best fit distribution \n' + dist_str)
    ax.set_xlabel(u'norm_ratings')
    ax.set_ylabel('Frequency')


    ########## 8

    ###
    fig, ax = plt.subplots(figsize=(17,8))
    plt.hist(df.awards_count, 
            bins = np.arange(0,30,1), ## change for a better bin scale
            color='cornflowerblue',
            edgecolor = "white")

    plt.xticks(np.arange(1,30,1),fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xlabel("mean_norm awards_count", fontsize=20,labelpad=20)
    plt.ylabel("frequency", fontsize=20,labelpad=20)
    plt.title('awards_count', fontsize=28,y=1.2)
    plt.grid(True,linestyle='dashed')
    plt.xlim(1,30)
    plt.show()

    fig, ax = plt.subplots(figsize=(17,8))
    aggregate = df.groupby('original_publish_year')['awards_count'].agg('max','mean')
    plt.hist(aggregate, 
            bins = np.arange(0,30,1), ## change for a better bin scale
            color=['cornflowerblue'],
            edgecolor = "white")

    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xticks(np.arange(1,30,1),fontsize=14, rotation=45)
    plt.xlabel("mean_norm awards_count", fontsize=20,labelpad=20)
    plt.ylabel("awards", fontsize=20,labelpad=20)
    plt.title('Aggregation plot for awards', fontsize=28,y=1.2)
    plt.grid(True,linestyle='dashed')
    plt.xlim(1,30,1)
    plt.show()

    fig, ax = plt.subplots(figsize=(10,8))
    plt.boxplot(df['awards_count'])
    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xticks()
    plt.ylabel("awards", fontsize=20,labelpad=20)
    plt.title('Awards distribution', fontsize=28,y=1.2)
    plt.grid(True,linestyle='dashed')
    ax.set_xticks([])
    plt.show()

    ## 9
    year_minmax=df.groupby("original_publish_year")['minmax_norm_ratings'].mean().round(decimals=2)
    fig, ax = plt.subplots(figsize=(17,8))
    plt.plot(year_minmax,color='cornflowerblue')

    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xticks(np.arange(1900,2001,10),fontsize=14, rotation=45)
    plt.xlabel("year", fontsize=20,labelpad=20)
    plt.ylabel("aminmax_norm_ratings", fontsize=20,labelpad=20)
    plt.title('Average Ratings by Year', fontsize=28,y=1.2)
    plt.grid(True,linestyle='dashed')
    plt.xlim(1900,2000)
    plt.show()

    ##10
    fig, ax = plt.subplots(figsize=(17,8))
    plt.scatter(df['original_publish_year'],df['minmax_norm_ratings'],
                label = 'books',
                color = 'lightpink', 
                edgecolor = 'darkviolet')
    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.xticks(np.arange(1900,2001,10),fontsize=14, rotation=45)
    plt.xlabel("year", fontsize=20,labelpad=20)
    plt.ylabel("aminmax_norm_ratings", fontsize=20,labelpad=20)
    plt.title('Average Ratings by Year', fontsize=28,y=1.2)
    plt.grid(True,linestyle='dashed')
    plt.xlim(1900,2000)
    plt.show()

    df_all = df_all_input

    count_awards = len(df) #allwith awards
    count_all = len(df_all) # get all 
    #Series all
    series_count_all = df_all['series'].value_counts()
    count_have_series_all = series_count_all[True]
    count_no_series_all = series_count_all[False]
    prob_series_all=count_have_series_all/count_all
    prob_series_perc_all=round((count_have_series_all/count_all)*100,2)
    print(f'Probabilty of having a series is in all : {prob_series_perc_all} %')

    #Series in award
    series_count = df['series'].value_counts()
    count_have_series = series_count[True]
    count_no_series = series_count[False]
    prob_series=count_have_series/count_awards
    prob_series_perc=round((count_have_series/count_awards)*100,2)
    print(f'Probabilty of having a series is : {prob_series_perc} %')

    #Awards
    prob_awards=count_all/1100
    prob_awards_perc=round((count_awards/1100)*100,2)
    print(f'Probabilty of having a awards is : {prob_awards_perc} %')

    ##
    prob=round(prob_awards_perc*prob_series_perc/prob_series_perc_all,2)
    print(f'probability that a book that is part of a series has won an award is: {prob} %')