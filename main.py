from energy_calculator import best_server_location


if __name__ == "__main__":
    print(
        best_server_location(
            {"AT", "CH", "DE", "DK", "ES", "FI", "FR", "GR", "IE", "NO"},
        )
    )
    print(
        best_server_location(
            {"AT", "CH", "DE", "DK", "ES", "FI", "FR", "GR", "IE", "NO"},
            nuclear_is_green=True,
        )
    )
