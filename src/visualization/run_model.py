from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from src.model.gmu_social import GmuSocial


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.5}
    if agent.status == "home":
        portrayal["Color"] = "green"
    elif agent.status == "work":
        portrayal["Color"] = "blue"
    elif agent.status == "transport":
        portrayal["Color"] = "red"
    return portrayal


if __name__ == "__main__":
    grid_width = 80
    grid_height = 40
    grid = CanvasGrid(agent_portrayal, grid_width=40, grid_height=grid_height,
                      canvas_width=500, canvas_height=500)
    server = ModularServer(GmuSocial,
                           [grid],
                           "GMU-Social Model",
                           {"gmu_buildings_file": "data/raw/campus/Mason_bld.shp",
                            "gmu_walkway_file": "data/raw/campus/Mason_walkway_line.shp",
                            "world_size_file": "data/raw/campus/world.shp",
                            "grid_width": grid_width,
                            "grid_height": grid_height,
                            "num_commuters": 109,
                            "speed": 5.0})
    server.port = 8521  # The default
    server.launch()
