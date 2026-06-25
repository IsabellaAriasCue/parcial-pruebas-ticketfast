from playwright.sync_api import Page, expect


def test_reserva_vip(page: Page):

    page.goto("http://localhost:4200/reservas")


    page.get_by_test_id("input-email-cliente").fill("cliente@correo.com")
    page.get_by_test_id("select-zona-evento").select_option("VIP")
    page.get_by_test_id("input-cantidad-asientos").fill("1")


    page.get_by_test_id("btn-confirmar-reserva").click()


    expect(
        page.get_by_test_id("seccion-resumen-total")
    ).to_contain_text("150.000")