import httpx


BASE_URL = "http://localhost:8001"


def test_calcular_total_recaudado():
    payload = {
        "cliente_email": "sistema@correo.com",
        "zona": "General",
        "cantidad": 3
    }


    response_post = httpx.post(
        f"{BASE_URL}/reservas/sistema-evento-xyz",
        json=payload
    )

    assert response_post.status_code == 201


    response_get = httpx.get(
        f"{BASE_URL}/reservas/sistema-evento-xyz/resumen"
    )

    assert response_get.status_code == 200

    resumen = response_get.json()

    assert resumen["total_recaudado"] == 150000