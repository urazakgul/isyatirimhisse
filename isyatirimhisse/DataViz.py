import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def visualize_data(df=None, plot_type='1', normalization=False, language='en', **kwargs):

    error_messages = {
        'tr': {
            'df_none': 'DataFrame (df) parametresi belirtilmelidir.',
            'df_pd_dataframe': 'DataFrame (df) parametresi bir pandas DataFrame olmalıdır.',
            "df_empty": "DataFrame (df) boş olmamalıdır.",
            "plot_type": "Geçersiz çizim türü. '1', '2' veya '3' olmalıdır.",
            "normalization": "Normalizasyon parametresi bir boolean (True/False) değeri olmalıdır."
        },
        'en': {
            'df_none': 'The DataFrame (df) parameter must be specified.',
            'df_pd_dataframe': 'The DataFrame (df) parameter must be a pandas DataFrame.',
            "df_empty": "The DataFrame (df) must not be empty.",
            "plot_type": "Invalid plot type. It must be '1', '2', or '3'",
            "normalization": "The normalization parameter must be a boolean (True/False) value."
        }
    }

    plot_titles = {
        'tr': {
            'line_plot': 'Seçilen Hisse Senetlerinin Zaman Serileri',
            'heatmap': 'Seçilen Hisse Senetleri Arasındaki Korelasyonlar',
            'scatter_matrix': 'Hisse Senetlerinin İlişkileri ve Dağılımları'
        },
        'en': {
            'line_plot': 'Time Series of Selected Stocks',
            'heatmap': 'Correlations Between Selected Stocks',
            'scatter_matrix': 'Relationships and Distributions of Selected Stocks'
        }
    }

    annotation_text = {
        'tr': {
            'normalization_text': 'Veriler normalize edilmiştir.'
        },
        'en': {
            'normalization_text': 'The data are normalized.'
        }
    }

    if df is None:
        raise ValueError(error_messages[language]['df_none'])

    if not isinstance(df, pd.DataFrame):
        raise ValueError(error_messages[language]['df_pd_dataframe'])

    if df.empty:
        raise ValueError(error_messages[language]['df_empty'])

    if not isinstance(normalization, bool):
        raise ValueError(error_messages[language]['normalization'])

    df = df.set_index('Date')

    if normalization:
        df = (df - df.min()) / (df.max() - df.min())

    figsize = kwargs.get('figsize', (10, 6))

    if plot_type == '1':

        plt.figure(figsize=figsize)
        for column in df.columns:
            sns.lineplot(
                x=df.index,
                y=df[column],
                label=column,
                linewidth=kwargs.get('linewidth', 1.5)
            )
        plt.title(f"{plot_titles[language]['line_plot']}, {df.index.min().strftime('%d/%m/%Y')} - {df.index.max().strftime('%d/%m/%Y')}", fontsize=kwargs.get('fontsize', 12))
        plt.xlabel('')
        plt.ylabel('')
        plt.legend(fontsize='small')
        if normalization:
            plt.text(
                0.99,
                -0.05,
                annotation_text[language]['normalization_text'],
                ha='right',
                va='bottom',
                transform=plt.gcf().transFigure,
                color='gray',
                fontsize=10,
                style='italic'
            )
        plt.show()

    elif plot_type == '2':

        plt.figure(figsize=figsize)
        sns.heatmap(
            df.corr(),
            annot=True,
            cmap=kwargs.get('cmap', 'coolwarm'),
            fmt='.2f',
            vmin=kwargs.get('vmin', -1),
            vmax=kwargs.get('vmax', 1),
            mask=np.triu(df.corr())
        )
        plt.title(plot_titles[language]['heatmap'], fontsize=kwargs.get('fontsize', 12))
        if normalization:
            plt.text(
                0.99,
                -0.05,
                annotation_text[language]['normalization_text'],
                ha='right',
                va='bottom',
                transform=plt.gcf().transFigure,
                color='gray',
                fontsize=10,
                style='italic'
            )
        plt.show()

    elif plot_type == '3':

        sns.pairplot(
            df,
            kind='reg',
            corner=True,
            plot_kws={'scatter_kws': {'alpha': .5}},
            height=kwargs.get('height', 2.5),
            aspect=kwargs.get('aspect', 1)
        )
        plt.suptitle(plot_titles[language]['scatter_matrix'], fontsize=kwargs.get('fontsize', 12))
        if normalization:
            plt.text(
                0.99,
                -0.05,
                annotation_text[language]['normalization_text'],
                ha='right',
                va='bottom',
                transform=plt.gcf().transFigure,
                color='gray',
                fontsize=10,
                style='italic'
            )
        plt.show()

    else:
        raise ValueError(error_messages[language]['plot_type'])