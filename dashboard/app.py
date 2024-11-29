from faicons import icon_svg
import pandas as pd
import pyarrow as pa
from shinyswatch import theme 
import plotly.express as px
import scipy 
import shiny
import shinylive
from shinywidgets import render_widget, render_plotly
from pathlib import Path

# Import data from shared.py
from shiny import reactive
from shiny.express import input, render, ui

#ui.page_opts(
#    title="This is Bananas!", 
 #   theme=theme.minty, 
  #  style="text-align: center; font-size: 30px; font-weight: bold;")
    
with ui.sidebar(title="Filter Controls", bg="#8D6B94"):
    options = ["Brazil", "Colombia", "Costa Rica", "Ecuado", "Guatemala", "Honduras", "India", "Philippines"]
    ui.input_checkbox_group(
        "selected_region_list",
        "Select Region",
        choices = ["Brazil", "Colombia", "Costa Rica", "Ecuado", "Guatemala", "Honduras", "India", "Philippines"],
        selected=["Brazil", "Colombia", "Costa Rica", "Ecuado", "Guatemala", "Honduras", "India", "Philippines"],
    )
    #ui.input_checkbox("Region_select_all", "Select All", value=True),

    ui.input_selectize(
    "selected_variety_list",
    "Choose banana variety(ies)",
    ["Burro", "Cavendish", "Fehi", "Manzano", "Plantain"],
    multiple=True,
    selected="Burro",
    options=(
        {
            "placeholder": "Enter text",
            "render": ui.js_eval(
                '{option: function(item, escape) {return "<div><strong>Select " + escape(item.label) + "</strong></div>";}}'
            ),
            "create": True,
        }
    ),    
)
    ui.div(
            ui.hr(),  # Use ui.hr() to add a horizontal rule to the sidebar 
            style="border-top: 2px solid #495569; margin: 10px 0;"  # Custom style for the horizontal rule
        )     
    ui.h4("Interactive Scatterplot")
    
    # Dropdown for selecting x and y axes for the scatter plot
    ui.input_selectize("x_column_scatter", "Select X Variable:", ["quality_score", "weight_g", "length_cm"])
    ui.input_selectize("y_column_scatter", "Select Y Variable:", ["quality_score", "weight_g", "length_cm"], selected="weight_g")
    @render.text
    def select():
        return f"{input.selectize()}"  

with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header(
            "This is Bananas!",
            style="background-color: #F7FA4F; color: #1D1F21; text-align: center; font-size: 36px;",
        )
        ui.p(
        "Check out the Banana Quality data set on ",
        ui.a("Kaggle", href="https://www.kaggle.com/datasets/mrmars1010/banana-quality-dataset/data", target="_blank", style="color: #007BFF; text-decoration: underline;"),
        ".",
        style="text-align: center; font-size: 16px;"
    )
        ui.p(
        "Learn how this app was built at Melissa's ",
        ui.a("GitHub", href="https://github.com/meldstonerogers/cintel-06-custom", target="_blank", style="color: #007BFF; text-decoration: underline;"),
        ".",
        style="text-align: center; font-size: 16px;"
    )
        
with ui.layout_column_wrap(fill=False):
    with ui.value_box(showcase=icon_svg("thumbs-up"), style="background-color: #F7936B"):
        "Average Quality Score (out of 4)"

        @render.text
        def ave_quality():
            return f"{filtered_data()['quality_score'].mean():.1f}"

    with ui.value_box(showcase=icon_svg("weight-hanging"), style="background-color: #F7936B"):
        "Average Banana Weight"

        @render.text
        def ave_weight():
            return f"{filtered_data()['weight_g'].mean():.1f} g"

    with ui.value_box(showcase=icon_svg("ruler-vertical"), style="background-color: #F7936B"):
        "Average Banana Length"

        @render.text
        def age_length():
            return f"{filtered_data()['length_cm'].mean():.1f} cm"

with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header(
            "Plotly Bananas Scatterplot",
            style="background-color: #25CED1; color: ##1D1F21;",
        )

        @render_widget
        def banana_scatterplot():
            x_column_name = input.x_column_scatter()
            y_column_name = input.y_column_scatter()
    
            # Filter the penguins dataset based on selected species
            bananas_df = filtered_data().dropna(subset=[x_column_name, y_column_name])
    
            # Create scatter plot
            scatterplot = px.scatter(
                data_frame = filtered_data(),
                x=x_column_name,  # X-axis based on user selection
                y=y_column_name,  # Y-axis based on user selection
                color="region",  # Color points by species
                title=f"{x_column_name} vs {y_column_name}",
                labels={x_column_name: x_column_name, y_column_name: y_column_name},  # Custom labels for axes
                color_discrete_sequence=["#FF0000", "#0000FF", "#008000", "#FFFF00", "#FFFF00", "#FF00FF", "#FFA500", "#800080"],  # Custom colors
                
            ).update_layout(
                title={"text": f"{x_column_name} vs {y_column_name}", "x": 0.5},
                yaxis_title=y_column_name,
                xaxis_title=x_column_name,
            )
    
            return scatterplot

    with ui.card(full_screen=True):
        ui.card_header(
            "B-A-N-A-N-A-S Data",
            style="background-color: #25CED1; color: ##1D1F21;",
        )
        @render.data_frame
        def summary_statistics():
            cols = [
                "region",
                "variety",
                "quality_score",
                "weight_g",
                "length_cm",
            ]
            return render.DataGrid(filtered_data()[cols], filters=True)


#ui.include_css(app_dir/ "docs" / "styles.css")

bananas_df = pd.read_csv("/Users/melissastonerogers/Documents/cintel-06-custom/dashboard/banana_quality_dataset.csv")

@reactive.calc
def filtered_data():
    isFilterMatch = (
        bananas_df["region"].isin(input.selected_region_list()) &
        bananas_df["variety"].isin(input.selected_variety_list())
    )
    return bananas_df[isFilterMatch]

# Reactive logic for "Select All" functionality
@reactive.calc
def updated_region_selection():
    selected = input.selected_region_list()  # Get selected options

    # If "Select All" is selected, return all options
    if "Select All" in selected:
        return options
    return selected

# Display the selected regions
#@render.text
#def update_region():
    selected_regions = updated_region_selection()
    return f"Selected regions: {', '.join(selected_regions)}"