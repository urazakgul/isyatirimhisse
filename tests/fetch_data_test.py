import pytest
import os
import sys
import asyncio
from datetime import date
from isyatirimhisse import fetch_data

# Scenario 1: No Symbol Entered
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_no_symbol():

    async def run_test():
        start_date = '03-01-2023'

        data = await fetch_data(
            start_date=start_date
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Scenario 2: Start Date Not Entered
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_no_start_date():

    async def run_test():
        symbol='GARAN'

        data = await fetch_data(
            symbol=symbol
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Scenario 3: Incorrect Frequency Entered
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_incorrect_frequency():

    async def run_test():
        symbol='GARAN'
        start_date='01-12-2021'
        frequency='1h'

        data = await fetch_data(
            symbol=symbol,
            start_date=start_date,
            frequency=frequency
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Scenario 4: Incorrect Observation Entered
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_incorrect_observation():

    async def run_test():
        symbol='GARAN'
        start_date='02-01-2012'
        end_date='30-12-2022'
        frequency='1m'
        observation='median'

        data = await fetch_data(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            frequency=frequency,
            observation=observation
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Scenario 5: Incorrect Symbol Entered
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_incorrect_symbol():

    async def run_test():
        symbol='GARAN.IS'
        start_date='02-01-2012'
        end_date='30-12-2022'

        data = await fetch_data(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Scenario 6: Incorrect Language Entered
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_incorrect_language():

    async def run_test():
        symbol='GARAN.IS'
        start_date='02-01-2012'
        end_date='30-12-2022'
        language='de'

        data = await fetch_data(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            language=language
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Scenario 7: Incorrect Exchange Entered
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_incorrect_exchange():

    async def run_test():
        symbol='GARAN.IS'
        start_date='02-01-2012'
        end_date='30-12-2022'
        exchange='GBP'

        data = await fetch_data(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            exchange=exchange
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Scenario 8: Incorrect Boolean Value (True as String) Entered
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_incorrect_boolean_value():

    async def run_test():
        symbol='GARAN.IS'
        start_date='02-01-2012'
        end_date='30-12-2022'
        calculate_return='True'

        data = await fetch_data(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            calculate_return=calculate_return
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Scenario 9: End Date Earlier Than Start Date
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_end_date_earlier():

    async def run_test():
        symbol='GARAN.IS'
        start_date='02-01-2012'
        end_date='30-12-2021'

        data = await fetch_data(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Scenario 10: The compatibility of 'symbol' and 'stock_market_index' parameters
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_symbol_stock_market_index_compatibility():

    async def run_test():
        symbol='GARAN.IS'
        stock_market_index='XU100'
        start_date='02-01-2012'
        end_date='30-12-2021'

        data = await fetch_data(
            stock_market_index=stock_market_index,
            start_date=start_date,
            end_date=end_date
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Scenario 11: Key Value 104
# @pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_key_error_104():

    async def run_test():
        symbol=[
            'A1CAP','AEFES','AFYON','AGESA','AGHOL','AHGAZ','AKBNK','AKCNS','AKFGY','AKFYE','AKGRT','AKSA','AKSEN','AKSGY','ALARK','ALBRK','ALCTL','ALFAS','ALGYO','ALKIM',
            'ANGEN','ANHYT','ANSGR','ARASE','ARCLK','ARDYZ','ARENA','ARSAN','ASELS','ASGYO','ASTOR','ASUZU','ATAKP','ATATP','AYDEM','AYEN','AYGAZ','AZTEK','BAGFS','BARMA',
            'BASGZ','BERA','BIENY','BIGCH','BIMAS','BIOEN','BIZIM','BLCYT','BOBET','BRISA','BRKVY','BRLSM','BRSAN','BRYAT','BTCIM','BUCIM','BVSAN','CANTE','CCOLA','CEMAS',
            'CEMTS','CIMSA','CLEBI','CONSE','CUSAN','CVKMD','CWENE','DAPGM','DESA','DEVA','DGNMO','DOAS','DOHOL','DYOBY','ECILC','ECZYT','EGEEN','EGEPO','EGGUB','EGPRO',
            'EGSER','EKGYO','EKSUN','ELITE','ENJSA','ENKAI','ERBOS','ERCB','EREGL','ESCAR','ESCOM','ESEN','EUPWR','EUREN','FENER','FROTO','FZLGY','GARAN','GEDIK','GENIL',
            'GENTS','GESAN','GLCVY','GLYHO','GOKNR','GOLTS','GOODY','GOZDE','GRSEL','GRTRK','GSDHO','GSRAY','GUBRF','GWIND','HALKB','HEDEF','HEKTS','HKTM','HLGYO','HTTBT',
            'HUNER','IHAAS','IMASM','INDES','INFO','INVEO','INVES','IPEKE','ISCTR','ISDMR','ISFIN','ISGYO','ISMEN','ISSEN','IZMDC','JANTS','KAREL','KARSN','KARTN','KATMR',
            'KAYSE','KCAER','KCHOL','KERVT','KGYO','KLGYO','KLKIM','KLMSN','KLRHO','KLSER','KLSYN','KMPUR','KNFRT','KONKA','KONTR','KONYA','KOPOL','KORDS','KOZAA','KOZAL',
            'KRDMA','KRDMB','KRDMD','KRPLS','KRVGD','KTLEV','KTSKR','KZBGY','LIDER','LOGO','MACKO','MAGEN','MAKIM','MARTI','MAVI','MEDTR','MERCN','MGROS','MIATK','MNDRS',
            'MNDTR','MOBTL','MPARK','MRGYO','MTRKS','NATEN','NETAS','NTGAZ','NTHOL','NUHCM','ODAS','OFSYM','ONCSM','ORGE','OTKAR','OYAKC','OYYAT','OZKGY','PAMEL','PARSN',
            'PASEU','PENGD','PENTA','PETKM','PETUN','PGSUS','PNLSN','PNSUT','POLHO','PRDGS','PRKAB','PRKME','PSGYO','QUAGR','RUBNS','RYGYO','RYSAS','SAHOL','SARKY','SASA',
            'SAYAS','SDTTR','SELEC','SISE','SKBNK','SMRTG','SNGYO','SNICA','SOKM','SRVGY','SUNTK','SUWEN','TATGD','TAVHL','TCELL','TERA','TEZOL','THYAO','TKFEN','TKNSA',
            'TMSN','TOASO','TRCAS','TRGYO','TRILC','TSGYO','TSKB','TTKOM','TTRAK','TUKAS','TUPRS','TUREX','TURSG','ULKER','ULUUN','UNLU','VAKBN','VAKKO','VERUS','VESBE',
            'VESTL','VKGYO','YATAS','YEOTK','YGGYO','YKBNK','YKSLN','YUNSA','YYLGD','ZOREN','ZRGYO','AYES','BALAT','BASCM','CMENT','ISBIR','KENT','KLNMA','KSTUR','ORMA',
            'QNBFB','QNBFL','SNPAM','SODSN','SUMAS','TBORG','UMPAS','UZERB','YBTAS','YONGA','ATSYH','BRKO','BRMEN','CASA','DIRIT','EKIZ','EMNIS','KERVN','KUVVA','MMCAS',
            'OTTO','ROYAL','SNKRN','ACSEL','ADEL','ADESE','AGYO','AKENR','AKMGY','AKSUE','AKYHO','ALCAR','ALKA','ALMAD','ANELE','ARZUM','ATAGY','ATEKS','ATLAS','AVGYO',
            'AVHOL','AVOD','AVTUR','AYCES','BAKAB','BANVT','BAYRK','BEYAZ','BFREN','BJKAS','BMSCH','BMSTL','BNTAS','BOSSA','BRKSN','BSOKE','BURCE','BURVA','CELHA','CEOEM',
            'CMBTN','COSMO','CRDFA','CRFSA','DAGHL','DAGI','DARDL','DENGE','DERHL','DERIM','DESPC','DGATE','DGGYO','DITAS','DMSAS','DNISI','DOBUR','DOCO','DOGUB','DOKTA',
            'DURDO','DZGYO','EDATA','EDIP','EMKEL','ENSRI','EPLAS','ERSU','ETILR','ETYAT','EUHOL','EUKYO','EUYO','EYGYO','FADE','FLAP','FMIZP','FONET','FORMT','FORTE','FRIGO',
            'GARFA','GEDZA','GEREL','GLBMD','GLRYH','GMTAS','GRNYO','GSDDE','GZNMI','HATEK','HDFGS','HUBVC','HURGZ','ICBCT','ICUGS','IDEAS','IDGYO','IEYHO','IHEVA','IHGZT',
            'IHLAS','IHLGM','IHYAY','INGRM','INTEM','ISATR','ISBTR','ISGSY','ISKPL','ISKUR','ISYAT','ITTFH','IZFAS','IZINV','KAPLM','KARYE','KFEIN','KIMMR','KRGYO','KRONT',
            'KRSTL','KRTEK','KUTPO','KUYAS','LIDFA','LINK','LKMNH','LUKSK','MAALT','MAKTK','MANAS','MARKA','MEGAP','MEPET','MERIT','MERKO','METRO','METUR','MIPAZ','MRSHL',
            'MSGYO','MTRYO','MZHLD','NIBAS','NUGYO','OBASE','ORCAY','OSMEN','OSTIM','OYAYO','OYLUM','OZGYO','OZRDN','OZSUB','PAGYO','PAPIL','PCILT','PEGYO','PEKGY','PINSU',
            'PKART','PKENT','PLTUR','POLTK','PRZMA','PSDTC','RALYH','RAYSG','RNPOL','RODRG','RTALB','SAFKR','SAMAT','SANEL','SANFM','SANKO','SEGYO','SEKFK','SEKUR','SELGD',
            'SELVA','SEYKM','SILVR','SKTAS','SMART','SOKE','SONME','TDGYO','TEKTU','TETMT','TGSAS','TLMAN','TMPOL','TNZTP','TSPOR','TUCLK','TURGG','UFUK','ULAS','ULUFA','ULUSE',
            'USAK','VAKFN','VANGD','VBTYZ','VERTU','VKFYO','VKING','YAPRK','YAYLA','YESIL','YGYO','YYAPI',
        ]
        # symbol = symbol[:400]
        stock_market_index=['XU100']
        start_date='01-01-2003'
        frequency='1d'
        drop_na=False
        save_to_excel=True

        data = await fetch_data(
            symbol=symbol,
            stock_market_index=stock_market_index,
            start_date=start_date,
            frequency=frequency,
            drop_na=drop_na,
            save_to_excel=save_to_excel
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Example 1
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_example_1():

    async def run_test():
        symbol='GARAN'
        start_date='03-01-2023'

        data = await fetch_data(
            symbol=symbol,
            start_date=start_date
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Example 2
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_example_2():

    async def run_test():
        symbol=['GARAN','THYAO']
        start_date='03-01-2023'
        frequency='1w'
        observation='mean'

        data = await fetch_data(
            symbol=symbol,
            start_date=start_date,
            frequency=frequency,
            observation=observation
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Example 3
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_example_3():

    async def run_test():
        symbol=['GARAN','THYAO']
        start_date='01-12-2021'
        end_date='30-12-2022'
        frequency='1m'
        calculate_return=True
        log_return=False
        exchange='USD'

        data = await fetch_data(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            frequency=frequency,
            calculate_return=calculate_return,
            log_return=log_return,
            exchange=exchange
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Example 4
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_example_4():

    async def run_test():
        symbol=['EUPWR','THYAO']
        start_date='02-01-2012'
        end_date='30-12-2022'
        frequency='1y'
        drop_na=False
        save_to_excel=True
        language='tr'
        exchange='USD'

        data = await fetch_data(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            frequency=frequency,
            drop_na=drop_na,
            save_to_excel=save_to_excel,
            language=language,
            exchange=exchange
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

# Example 5
@pytest.mark.skip(reason="This test is currently disabled.")
@pytest.mark.asyncio
async def test_fetch_data_example_5():

    async def run_test():
        # symbol=['GARAN','THYAO']
        stock_market_index=['XU100','XU030','XBANK']
        start_date='02-01-2012'
        end_date='31-07-2023'
        frequency='1d'
        drop_na=False
        save_to_excel=True
        language='tr'
        exchange='USD'

        data = await fetch_data(
            # symbol=symbol,
            stock_market_index=stock_market_index,
            start_date=start_date,
            end_date=end_date,
            frequency=frequency,
            drop_na=drop_na,
            save_to_excel=save_to_excel,
            language=language,
            exchange=exchange
        )

        assert len(data) > 0, "No data found."

        print(data)

    await run_test()

if __name__ == "__main__":
    tests_directory = os.path.dirname(os.path.abspath(__file__))
    isyatirimanaliz_directory = os.path.abspath(os.path.join(tests_directory, '..'))
    if os.path.exists(isyatirimanaliz_directory):
        sys.path.insert(0, isyatirimanaliz_directory)
        print(sys.path)
    else:
        print(f"The directory '{isyatirimanaliz_directory}' does not exist.")

    pytest.main([__file__])