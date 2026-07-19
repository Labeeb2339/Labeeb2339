"""Build the crisp, transparent Espeon loop used by the profile README."""

from __future__ import annotations

import math
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image


SOURCE_COMMIT = "6c9d4efd1662ad363a5b2b64b64d048a7f394013"
SOURCE_URL = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/"
    f"{SOURCE_COMMIT}/sprites/pokemon/versions/generation-v/"
    "black-white/animated/196.gif"
)
OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "espeon-loop.gif"
CANVAS_SIZE = (360, 280)
SCALE = 4


def load_source() -> Image.Image:
    request = Request(SOURCE_URL, headers={"User-Agent": "profile-asset-builder"})
    with urlopen(request, timeout=30) as response:
        return Image.open(BytesIO(response.read()))


def build_frames(source: Image.Image) -> tuple[list[Image.Image], list[int]]:
    frames: list[Image.Image] = []
    durations: list[int] = []

    for index in range(source.n_frames):
        source.seek(index)
        sprite = source.convert("RGBA")
        sprite = sprite.resize(
            (sprite.width * SCALE, sprite.height * SCALE),
            Image.Resampling.NEAREST,
        )

        # A small horizontal drift makes the loop immediately legible as motion
        # without blurring the source pixel art.
        phase = 2 * math.pi * index / source.n_frames
        drift_x = round(7 * math.sin(phase))
        canvas = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))
        position = (
            (CANVAS_SIZE[0] - sprite.width) // 2 + drift_x,
            (CANVAS_SIZE[1] - sprite.height) // 2,
        )
        canvas.alpha_composite(sprite, position)
        frames.append(canvas)
        durations.append(source.info.get("duration", 100))

    return frames, durations


def main() -> None:
    source = load_source()
    frames, durations = build_frames(source)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        OUTPUT,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        disposal=2,
        optimize=True,
    )
    print(f"wrote {OUTPUT} ({len(frames)} frames)")


if __name__ == "__main__":
    main()
