class MainMenu:
    @staticmethod
    def start(value):
        config = {
            'highlightthickness': 0,
            'bg': '#5159a7',  # background color
            'width': 800,
            'height': 40
        }
        return config.get(value)
