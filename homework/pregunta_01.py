# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import os

import matplotlib.pyplot as plt
import pandas as pd


def pregunta_01():
        """
        El archivo `files//shipping-data.csv` contiene información sobre los envios
        de productos de una empresa. Cree un dashboard estático en HTML que
        permita visualizar los siguientes campos:

        * `Warehouse_block`

        * `Mode_of_Shipment`

        * `Customer_rating`

        * `Weight_in_gms`

        El dashboard generado debe ser similar a este:

        https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

        Para ello, siga las instrucciones dadas en el siguiente video:

        https://youtu.be/AgbWALiAGVo

        Tenga en cuenta los siguientes cambios respecto al video:

        * El archivo de datos se encuentra en la carpeta `data`.

        * Todos los archivos debe ser creados en la carpeta `docs`.

        * Su código debe crear la carpeta `docs` si no existe.

        """
        os.makedirs("docs", exist_ok=True)

        data = pd.read_csv("files/input/shipping-data.csv")

        plt.style.use("ggplot")

        fig, ax = plt.subplots(figsize=(8, 4.5))
        data["Warehouse_block"].value_counts().sort_index().plot(kind="bar", ax=ax, color="#4c78a8")
        ax.set_title("Shipping by Warehouse Block")
        ax.set_xlabel("Warehouse block")
        ax.set_ylabel("Number of shipments")
        fig.tight_layout()
        fig.savefig("docs/shipping_per_warehouse.png")
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(8, 4.5))
        data["Mode_of_Shipment"].value_counts().sort_index().plot(kind="bar", ax=ax, color="#f58518")
        ax.set_title("Shipping by Mode of Shipment")
        ax.set_xlabel("Mode of shipment")
        ax.set_ylabel("Number of shipments")
        fig.tight_layout()
        fig.savefig("docs/mode_of_shipment.png")
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(8, 4.5))
        data.groupby("Warehouse_block")["Customer_rating"].mean().sort_index().plot(kind="bar", ax=ax, color="#54a24b")
        ax.set_title("Average Customer Rating by Warehouse Block")
        ax.set_xlabel("Warehouse block")
        ax.set_ylabel("Average customer rating")
        ax.set_ylim(0, 5)
        fig.tight_layout()
        fig.savefig("docs/average_customer_rating.png")
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(8, 4.5))
        ax.hist(data["Weight_in_gms"], bins=20, color="#e45756", edgecolor="white")
        ax.set_title("Weight Distribution")
        ax.set_xlabel("Weight in gms")
        ax.set_ylabel("Frequency")
        fig.tight_layout()
        fig.savefig("docs/weight_distribution.png")
        plt.close(fig)

        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Shipping Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 24px;
            background: #f4f7fb;
            color: #1f2937;
        }
        h1 {
            margin-top: 0;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
        }
        .card {
            background: white;
            border-radius: 12px;
            padding: 16px;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
        }
        img {
            width: 100%;
            display: block;
        }
    </style>
</head>
<body>
    <h1>Shipping Dashboard</h1>
    <div class="grid">
        <div class="card"><img src="shipping_per_warehouse.png" alt="Shipping per warehouse"></div>
        <div class="card"><img src="mode_of_shipment.png" alt="Mode of shipment"></div>
        <div class="card"><img src="average_customer_rating.png" alt="Average customer rating"></div>
        <div class="card"><img src="weight_distribution.png" alt="Weight distribution"></div>
    </div>
</body>
</html>
"""

        with open("docs/index.html", "w", encoding="utf-8") as file_object:
                file_object.write(html)
