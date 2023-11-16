# Imports
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------- DATA WRANGLING --------#

# Function to map column to bucket
def map_to_bucket(col: str, categories_dictionary: dict) -> None:
    '''
    '''
    for bucket, categories in categories_dictionary.items():
        if col in categories:
            return bucket
    return None


def create_bucket_df(df: pd.DataFrame, categories_dictionary: dict) -> pd.DataFrame:
    '''
    '''
    # Create a DataFrame to store bucketed columns
    bucketed_df = pd.DataFrame(index=df.index)

    # Iterate over the columns and map them to buckets
    for col in df.columns[14:]:
        bucket = map_to_bucket(col, categories_dictionary)
        if bucket:
            # If the bucket already exists in the DataFrame, add the column to it
            if bucket in bucketed_df:
                bucketed_df[bucket] += df[col]
            else:
                # Otherwise, create a new bucket column
                bucketed_df[bucket] = df[col]

    final_df = pd.concat([df.iloc[:, :14], bucketed_df], axis=1)

    return final_df


# -------- EDA --------#

def central_tendency_spread(df:pd.DataFrame, col:str, table:bool) -> dict:
    '''
    '''
    mean, median, std, var = df[col].mean(), df[col].median(), df[col].std(), df[col].var()
    range_value = df[col].max() - df[col].min()
    Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    IQR = Q3 - Q1

    return_dict = {
        'mean_value': mean,
        'median_value': median,
        'std_value': std,
        'var_value': var,
        'range_value': range_value,
        'Q1_value': Q1,
        'Q3_value': Q3,
        'IQR_value': IQR
    }

    if table:
        print(f'<--- {col} Statistics --->')
        print(pd.DataFrame([return_dict], index=None))
        print("")

    return return_dict


def plot_histogram(df:pd.DataFrame, col:str, graph_data:dict) -> None:
    '''
    '''
    stats_dict = central_tendency_spread(df, col, table=False)
    
    mean_value = stats_dict['mean_value']
    median_value = stats_dict['median_value']
    std_value = stats_dict['std_value']
    var_value = stats_dict['var_value']
    range_value = stats_dict['range_value']
    IQR_value = stats_dict['IQR_value']

    # Set the aesthetic style of the plots
    sns.set(style="whitegrid")

    # Histogram
    plt.figure(figsize=(10, 6))

    sns.histplot(df[col], 
                bins=15, 
                kde=True, 
                color='skyblue')

    # Annotating statistics
    plt.axvline(mean_value, color='red', linestyle='--', label=f'Mean: {mean_value:.2f}')
    plt.axvline(median_value, color='green', linestyle=':', label=f'Median: {median_value:.2f}')
    plt.text(mean_value, plt.gca().get_ylim()[1]*0.9, f'Std: {std_value:.2f}', color='black')
    plt.text(mean_value, plt.gca().get_ylim()[1]*0.85, f'Var: {var_value:.2f}', color='black')
    plt.text(mean_value, plt.gca().get_ylim()[1]*0.80, f'Max: {range_value:.2f}', color='black')
    plt.text(mean_value, plt.gca().get_ylim()[1]*0.75, f'IQR: {IQR_value:.2f}', color='black')

    plt.title(graph_data['Title'], fontsize=16)
    plt.xlabel(graph_data['x_label'], fontsize=12)
    plt.ylabel(graph_data['y_label'], fontsize=12)

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

    return None


def plot_boxplot(df:pd.DataFrame, col:str, graph_data:dict) -> None:
    '''
    '''
    stats_dict = central_tendency_spread(df, col, table=False)

    mean_value = stats_dict['mean_value']
    median_value = stats_dict['median_value']
    Q1_value = stats_dict['Q1_value']
    Q3_value = stats_dict['Q3_value']
    IQR_value = stats_dict['IQR_value']

    # Boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(df[col], color='lightgreen')

    # Annotating statistics
    plt.text(0.07, mean_value, f'Mean: {mean_value:.2f}', verticalalignment='center', horizontalalignment='right', color='black')
    plt.text(0.07, median_value, f'Median: {median_value:.2f}', verticalalignment='center', horizontalalignment='right', color='black')
    plt.text(0.3, Q1_value, f'Q1: {Q1_value:.2f}', verticalalignment='top', horizontalalignment='right', color='black')
    plt.text(0.3, Q3_value, f'Q3: {Q3_value:.2f}', verticalalignment='center', horizontalalignment='right', color='black')
    plt.text(0.4, Q3_value/2, f'IQR: {IQR_value:.2f}', verticalalignment='center', horizontalalignment='right', color='black')

    plt.title(graph_data['Title'], fontsize=16)
    plt.xlabel(graph_data['x_label'], fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

    return None


def corr_two_var(df:pd.DataFrame, cols:list, graph_data:dict) -> pd.DataFrame:
    '''
    '''
    corr = df[cols].corr()

    ax = sns.heatmap(corr, annot=True)

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Scatterplot
    scatter = sns.scatterplot(x=cols[0], y=cols[1], 
                            data=df,
                            color='royalblue', 
                            edgecolor='black', 
                            s=50)

    # Title and Labels
    plt.title(graph_data['Title'], fontsize=18, fontweight='bold')
    plt.xlabel(graph_data['x_label'], fontsize=14)
    plt.ylabel(graph_data['y_label'], fontsize=14)

    # Additional Aesthetics
    scatter.set_facecolor("white")  # Set background to white
    plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')  # Custom grid lines
    plt.yscale('log')  # Logarithmic scale for better visibility of wide-range data
    scatter.spines['top'].set_visible(False)  # Remove top spine
    scatter.spines['right'].set_visible(False)  # Remove right spine

    # Show scatter correlation plot
    plt.show()

    return corr


def detect_outliers(df:pd.DataFrame, cols:list, plot:bool, **graph_data:dict) -> dict:
    '''
    '''

    dict_var = dict()

    for col in cols:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        dict_var[f'l_bound_{col}'] = lower_bound
        dict_var[f'u_bound_{col}'] = upper_bound

        if plot:

            plt.figure(figsize=(12, 6))

            sns.boxplot(y=df[col])
            plt.title(graph_data['Title'])
            plt.axhline(lower_bound, color='g', linestyle='--')
            plt.axhline(upper_bound, color='g', linestyle='--')
            plt.text(y=lower_bound, x=0.05, s='Lower Bound', color='g')
            plt.text(y=upper_bound, x=0.05, s='Upper Bound', color='g')

            plt.tight_layout()
            plt.show()

    return dict_var


def drop_outliers(df:pd.DataFrame, dict_bounds:dict, cols:list) -> pd.DataFrame:
    '''
    '''
    drop_out_df = df[(df[cols[0]] >= dict_bounds[f'l_bound_{cols[0]}']) & 
                    (df[cols[0]] <= dict_bounds[f'u_bound_{cols[0]}']) &
                    (df[cols[1]] >= dict_bounds[f'l_bound_{cols[1]}']) & 
                    (df[cols[1]] <= dict_bounds[f'u_bound_{cols[1]}'])
                    ]
    
    return drop_out_df


def impute_outliers_mean(df:pd.DataFrame, cols:list, dict_bounds:dict) -> pd.DataFrame:
    '''
    '''
    mean_out_df = df.copy()

    for col in cols:

        mean = df[(df[col] >= dict_bounds[f'l_bound_{col}']) & 
                  (df[col] <= dict_bounds[f'u_bound_{col}'])][col].mean()
        
        mean_out_df.loc[df[col] < dict_bounds[f'l_bound_{col}'], col] = mean
        mean_out_df.loc[df[col] > dict_bounds[f'u_bound_{col}'], col] = mean

    return mean_out_df


def cap_outliers(df:pd.DataFrame, cols:list) -> pd.DataFrame:
    '''
    '''
    cap_out_df = df.copy()

    for col in cols:

        stats_dict = central_tendency_spread(df, col, table=False)
    
        mean_value = stats_dict['mean_value']
        std_value = stats_dict['std_value']

        cap_lower = mean_value - 3 * std_value
        cap_upper = mean_value + 3 * std_value

        cap_out_df[col] = cap_out_df[col].clip(lower=cap_lower, upper=cap_upper)

    return cap_out_df


def sample_df(df:pd.DataFrame, n:int) -> pd.DataFrame:
    '''
    '''
    sampled_df = df.sample(n)
    
    return sampled_df


def filter_dataframe(df:pd.DataFrame, col:str, values:list) -> pd.DataFrame:
    '''
    '''
    filtered_df = df[df[col].isin(values)]
    
    return filtered_df


def avg_funding_days_country(df:pd.DataFrame, country:list, n:int) -> None:
    '''
    '''
    sampled_country_df = (filter_dataframe(df, 'country_code', country)\
                        .sample(n)\
                        .reset_index())
    
    days_in_avg = ((sampled_country_df['first_funding_at'] - sampled_country_df['founded_at']).dt.days).mean()
    
    print(f"<-------- Startups in {country[0]} (Samples: 100) -------->\n")
    print(f"         <---- 'funding_total_usd' ---->\n")
    print(pd.DataFrame([central_tendency_spread(sampled_country_df, 'funding_total_usd', table=False)], index=None))
    print("")
    print(f"          <---- 'funding_rounds'---->\n")
    print(pd.DataFrame([central_tendency_spread(sampled_country_df, 'funding_rounds', table=False)], index=None))
    print("")
    print(f" Days to get funding in {country[0]}: {days_in_avg} days")
    print("\n" * 2)

    return None


def probability_funding_6_months(df:pd.DataFrame, country:list, **n_count:bool) -> float:
    '''
    '''
    if country == ['All']:
        filtered_df = df.copy()
    else:
        filtered_df = filter_dataframe(df, 'country_code', country).copy()
    
    # Calculate the difference in days between founded date and first funding date
    filtered_df.loc[:, 'days_to_funding'] = (filtered_df['first_funding_at'] - filtered_df['founded_at']).dt.days

    # Filter startups that got funding within 6 months (approx 180 days)
    funded_within_6_months = filtered_df[filtered_df['days_to_funding'] <= 180]

    # Calculate probability
    probability = len(funded_within_6_months) / len(filtered_df)

    print(f"Probability of {country[0]} startups being funded within the first 6 months: %{round(probability*100, 2)}")

    return round(probability, 2)


def plot_barplot(df:pd.DataFrame, graph_data:dict) -> None:
    '''
    '''
    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x=graph_data["x_var"], y=graph_data["y_var"], data=df, palette="viridis")

    plt.title(graph_data["Title"], fontsize=15)
    plt.xlabel(graph_data["x_axis"], fontsize=12)
    plt.ylabel(graph_data["y_axis"], fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    for index, value in enumerate(df['Probability']):
        plt.text(index, value, f'{value}%', ha='center', va='bottom', fontsize=10)

    # Display the plot
    plt.show()

    return None