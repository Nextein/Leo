# Algoritmo de inversión en acciones

Producto desarrollado en conjunto por Pepe, Enrique Barragán Parrados, Rocío González Pérez y Marc Goulding Tójar.

Lee data de Interactive Brokers y scanea las acciones para encontrar señales en la gráfica diaria, semanal y mensual.


# Interactive Brokers Breakdown

Fees: Trades are usually commision-free (TDAmeritrade). IB has monthly fees based on how much you trade (per trade + data subscription for real-time and historical data).

Ease of use: Download TWS workstation. IP Gateway.

Trade anything from anywhere. They've expanded to everything.

They don't sell your order flow data. Great order execution (speed & filled price)

Advanced order types.

Loads of tools:

Research, scanners, news, fundamentals, paper trading API, backtesting, mobile app, built in charting and indicators.

Worth paying fees for quality data and order execution.

Can fire off loads of async requests in one go and continue (not wait). Handle each request as they come using callback functions to run much quicker.

