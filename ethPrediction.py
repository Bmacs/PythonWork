import pandas as pd
from prophet import prophet


df .rename(columns={'Date': 'ds', 'Price (Close)': 'y'}, inplace=True)
df = pd .to_datetime(df, errors='coerce', utc=True )
df = df.dt.strftime('%Y-%m-%d %H:%M')
df .rename(columns={'Date': 'ds', 'Value': 'y'}, inplace=True)

m = Prophet(seasonality_mode='multiplicative')
m.add_seasonality(name='monthly', period=30.5, fourier_order=5)

m.fit( df )
future = m.make_future_dataframe(periods=30*96, freq='15min')
forecast = m.predict(future)
m.plot(forecast)
m.plot_components(forecast)
from fbprophet.plot import add_changepoints_to_plot
fig = m.plot(forecast)
add_changepoints_to_plot(fig.gca(), m, forecast)
plt .show(trend=True)