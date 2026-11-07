import unittest

from django.test import TestCase
from django.urls import reverse

from .servicios import (
    calcular_emisiones_carbono,
    obtener_metricas_consumo
)


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_correcto(self):
        resultado = calcular_emisiones_carbono(100)

        self.assertEqual(resultado, 40)

    def test_factor_emision_personalizado(self):
        resultado = calcular_emisiones_carbono(100, 0.5)

        self.assertEqual(resultado, 50)

    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0)

        self.assertEqual(resultado, 0)

    def test_consumo_decimal(self):
        resultado = calcular_emisiones_carbono(12.5)

        self.assertEqual(resultado, 5)

    def test_consumo_negativo(self):

        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)


class TestMetricasConsumo(unittest.TestCase):

    def test_obtener_metricas(self):

        registros = [
            {"planta": "Mendoza", "consumo_kwh": 100},
            {"planta": "Mendoza", "consumo_kwh": 50},
            {"planta": "Cordoba", "consumo_kwh": 200}
        ]

        resultado = obtener_metricas_consumo(registros)

        self.assertEqual(
            resultado["emisiones_totales"],
            140
        )

        self.assertEqual(
            resultado["planta_mayor_consumo"],
            "Cordoba"
        )

        self.assertEqual(
            resultado["consumo_maximo"],
            200
        )

    def test_lista_vacia(self):

        resultado = obtener_metricas_consumo([])

        self.assertEqual(
            resultado["emisiones_totales"],
            0
        )

        self.assertIsNone(
            resultado["planta_mayor_consumo"]
        )

    def test_consumo_negativo_en_registros(self):

        registros = [
            {"planta": "Mendoza", "consumo_kwh": -10}
        ]

        with self.assertRaises(ValueError):
            obtener_metricas_consumo(registros)


class TestIntegracionPanel(TestCase):

    def test_panel_sustentabilidad(self):

        respuesta = self.client.get(
            reverse("sustentabilidad:panel")
        )

        self.assertEqual(respuesta.status_code, 200)

        self.assertTemplateUsed(
            respuesta,
            "sustentabilidad/panel.html"
        )

        self.assertIn(
            "emisiones_totales",
            respuesta.context
        )

        self.assertContains(
            respuesta,
            "Panel de Sustentabilidad"
        )