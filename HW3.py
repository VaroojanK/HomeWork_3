import dash
import dash_core_components as dcc
import dash_html_components as html


from Figures import gr1
from Figures import gr2
from Figures import gr3
from Figures import gr4
from Figures import data_gr5

app=dash.Dash()

app.css.append_css({"external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

	#Heading

app.layout=html.Div([

	html.Div([html.H1(children="Homework 3", style={"color":"red", "text-align":"center", "font-weight":"bold",})], className="twelve columns"),

	#First Part

	html.Div([
		html.Div([html.P("Homework 3 assumes the development of this web application using Dash and Plotly in Python.You are required to develop 6 plots (including one table) with the given layout. Subtle differences related to styling (colors etc) are allowed, yet the general layout must be kept to perceive same information as this website does. Quandl is used as a data source for 4 plots among 6, while the other 2 are based on user provided data. Some of the Quandl based plots require minor analysis using pandas. You are encouraged to follow below mentioned steps to complete the HW:",
			style={"text-align":"justify","padding-left":"10",}),
			
			html.Ol(
				[html.Li("Start from first developing the 6 plots in Jupyter Notebook,"),
				html.Li("Once plots are ready post them into the Dash app,"),
				html.Li("Add HTML components (website heading etc.),"),
				html.Li("Structure the layout of the dashboard.")], style={"padding-left":"20",}

				)], className="four columns"),

		html.Div([html.P("Graph 1", style={"font-weight":"bold",}), html.P("The graph on the right hand side is showing correlations of different variables (call them from x1 to x8) with employee churn. Data is artificial, manually inputted by the developer. Recreate the graph. Small coloring or corelation value differences will be neglected."),
			], className="four columns"),

		html.Div([
		dcc.Graph(id="Graph1", figure=gr1)],
		className="four columns")

		], className="twelve columns"),


	#Second Part


	html.Div([
		html.Div([html.P("Graph 2", style={"font-weight":"bold", "padding-left":"20",}), html.P("One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph."),
			], className="four columns"),

		html.Div([
		dcc.Graph(id="Graph2", figure=gr2)],
		className="six columns"),

		html.Div([],className="two columns")

		], className="twelve columns"),
	

	#Third Part

	html.Div([
		html.Div([html.P("Graph 3 and 4", style={"font-weight":"bold", "padding-left":"20",}), html.P("The two graphs on this row are based on Google's stock (WIKI/GOOGL) and Bitcoin's (BCHARTS/ABUCOINSUSD) prices sourced from Quandl. First, percentage changes are calculated. Then the latter is plotted using Box plot to find the distribution and outliers. In the end the first 4 percentage changes (apart from the very first one, which is N/A) are plotted in a table. Recreate similar graphs with the same values (minor styling is neglected)."),
			], className="four columns"),

		html.Div([
		dcc.Graph(id="Graph3", figure=gr3)],
		className="four columns"),


		html.Div([
		dcc.Graph(id="Graph4", figure=gr4)],
		className="four columns")

		], className="twelve columns"),

	#Fourth Part

	html.Div([
		html.Div([html.P("Graph 5", style={"font-weight":"bold", "padding-left":"20",}), html.P("Last graph is based on manually inputted data. It shows the Roadmap developed by an artificial startup. Task 1 is assumed to take the whole Janduary, while Task 2 is starting from March and ending in mid April. Afterwards, Task 3 begins and ends in the end of September. Recreate a similar Roadmap"),
			], className="four columns"),

		html.Div([
		dcc.Graph(id="Graph5", figure=data_gr5)],
		className="six columns"),


		html.Div([],
		className="two columns")

		], className="twelve columns")


	])


if __name__=='__main__':
	app.run_server(debug=True)
