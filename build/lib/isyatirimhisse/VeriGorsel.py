import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def veri_gorsel(df=None, gorsel_turu='1', normalizasyon=False, **kwargs):
    """
    Veri çerçevesindeki hisse senetlerini görselleştirir.

    Parametreler:
        df (pandas DataFrame, varsayılan None): Hisse senedi verilerinin bulunduğu pandas DataFrame.
        gorsel_turu (str, varsayılan '1'): Görselleştirme türü.
            '1': Çizgi Grafiği
            '2': Korelasyon Isı Matrisi
            '3': Dağılım Matrisi
        normalizasyon (bool, varsayılan False): Veriler normalize (0-1 arasında ölçeklendirme) edilecek mi?
        **kwargs: Görselleştirme türlerine özel ek seçenekler. Örneğin, '1' türü için `linewidth` gibi.
        Görselleştirme Türleri için **kwargs Parametreleri:
            '1' (Çizgi Grafiği):
                linewidth (float, varsayılan 1.5): Çizgi kalınlığı.

            '2' (Korelasyon Isı Matrisi):
                cmap (str, varsayılan 'coolwarm'): Renk haritası.
                vmin (float, varsayılan -1): Renk haritasındaki en küçük değer.
                vmax (float, varsayılan 1): Renk haritasındaki en büyük değer.

            '3' (Dağılım Matrisi):
                kind (str, varsayılan 'scatter'): Görselleştirme türü ('scatter' veya 'reg').
                alpha (float, varsayılan 0.5): Nokta şeffaflığı.
    """

    if df is None:
        raise ValueError("Veri çerçevesi (df) parametresi belirtilmelidir.")

    if not isinstance(df, pd.DataFrame):
        raise ValueError("Veri çerçevesi (df) parametresi bir pandas DataFrame olmalıdır.")

    if df.empty:
        raise ValueError("Veri çerçevesi (df) boş olmamalıdır.")

    if not isinstance(normalizasyon, bool):
        raise ValueError("Normalizasyon parametresi bir bool (True/False) değeri olmalıdır.")

    df = df.set_index('Tarih')

    if normalizasyon:
        df = (df - df.min()) / (df.max() - df.min())

    figsize = kwargs.get('figsize', (10, 6))

    if gorsel_turu == '1':

        plt.figure(figsize=figsize)
        for column in df.columns:
            sns.lineplot(
                x=df.index,
                y=df[column],
                label=column,
                linewidth=kwargs.get('linewidth', 1.5)
            )
        plt.title("Hisse Senetleri, {}/{}/{} - {}/{}/{}".format(
            df.index.min().strftime('%d'), df.index.min().strftime('%m'), df.index.min().strftime('%Y'),
            df.index.max().strftime('%d'), df.index.max().strftime('%m'), df.index.max().strftime('%Y')
        ))
        plt.xlabel('')
        plt.ylabel('')
        plt.legend(fontsize='small')
        if normalizasyon:
            plt.text(
                0.99,
                -0.05,
                'Veriler normalize edilmiştir.',
                ha='right',
                va='bottom',
                transform=plt.gcf().transFigure,
                color='gray',
                fontsize=10,
                style='italic'
            )
        plt.show()

    elif gorsel_turu=='2':

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
        plt.title('Hisse Senetleri Arasındaki Korelasyonlar')
        if normalizasyon:
            plt.text(
                0.99,
                -0.05,
                'Veriler normalize edilmiştir.',
                ha='right',
                va='bottom',
                transform=plt.gcf().transFigure,
                color='gray',
                fontsize=10,
                style='italic'
            )
        plt.show()

    elif gorsel_turu=='3':

        plt.figure(figsize=figsize)
        sns.pairplot(
            df,
            kind='reg',
            corner=True,
            plot_kws={'scatter_kws': {'alpha': kwargs.get('alpha', .5)}}
        )
        plt.suptitle('Hisse Senetlerine Ait Dağılımlar')
        if normalizasyon:
            plt.text(
                0.99,
                -0.05,
                'Veriler normalize edilmiştir.',
                ha='right',
                va='bottom',
                transform=plt.gcf().transFigure,
                color='gray',
                fontsize=10,
                style='italic'
            )
        plt.show()

    else:
        raise ValueError("Geçersiz görselleştirme türü. '1', '2' veya '3' olmalıdır.")