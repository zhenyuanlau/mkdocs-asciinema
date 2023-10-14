from mkdocs.plugins import BasePlugin

from bs4 import BeautifulSoup
from mkdocs.config import config_options


class MkdocsAsciinemaPlugin(BasePlugin):
    # speed="2" theme="solarized-light" rows="20"
    config_scheme = (
        ("speed", config_options.Type(str)),
        ("theme", config_options.Type(str, default="solarized-light")),
        ("rows", config_options.Type(str)),
    )

    def on_post_page(self, output_content, config, page, **kwargs):
        if 'alt="asciicast"' not in output_content:
            return output_content
        soup = BeautifulSoup(output_content, "html.parser")
        asciicast_elements = soup.findAll("img", {"alt": "asciicast"})
        asciicasts = []
        asciicast_settings = ""
        asciicast_settings += (
            'theme:"{}",'.format(self.config["theme"])
            if "theme" in self.config
            else " "
        )
        asciicast_settings += (
            'speed:"{}",'.format(self.config["speed"])
            if "speed" in self.config
            else " "
        )
        asciicast_settings += (
            'rows:"{}",'.format(self.config["rows"]) if "rows" in self.config else " "
        )
        for idx, element in enumerate(asciicast_elements):
            asciicast_id = f"asciicast-{idx}"
            asciicast_src = element.attrs["src"]
            div_tag = soup.new_tag("div", id=asciicast_id)
            element.replace_with(div_tag)
            ascii_create_state = 'AsciinemaPlayer.create("{}", document.getElementById("{}"), {{{}}});'.format(
                asciicast_src,
                asciicast_id,
                asciicast_settings,
            )
            asciicasts.append(ascii_create_state)
        asciicast_script = soup.new_tag("script")
        asciicast_script.append("\n".join(asciicasts))
        soup.body.append(asciicast_script)
        return str(soup)
