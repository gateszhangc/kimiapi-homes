#!/usr/bin/env python3
"""Generate an elegant Kimi API logo with a modern 'K' symbol."""

from PIL import Image, ImageDraw, ImageFont
import math
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def draw_rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle."""
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_logo():
    w, h = 512, 512
    img = Image.new('RGBA', (w, h), (10, 10, 15, 255))
    draw = ImageDraw.Draw(img)

    cx, cy = w // 2, h // 2

    # Subtle radial glow
    for r in range(220, 0, -1):
        alpha = max(0, int(12 * (1 - r / 220)))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(108, 92, 231, alpha))

    # Outer ring
    draw.ellipse(
        [cx - 155, cy - 155, cx + 155, cy + 155],
        outline=(108, 92, 231, 50),
        width=1,
    )

    # Inner ring
    draw.ellipse(
        [cx - 140, cy - 140, cx + 140, cy + 140],
        outline=(108, 92, 231, 25),
        width=1,
    )

    # Orbital dots on outer ring
    dot_count = 8
    for i in range(dot_count):
        angle = (i / dot_count) * 2 * math.pi - math.pi / 2
        dx = cx + math.cos(angle) * 155
        dy = cy + math.sin(angle) * 155
        r = 4 if i == 0 else 2.5
        alpha = 255 if i == 0 else 80
        draw.ellipse([dx - r, dy - r, dx + r, dy + r], fill=(108, 92, 231, alpha))

    # Central circle accent
    draw.ellipse(
        [cx - 80, cy - 80, cx + 80, cy + 80],
        fill=(108, 92, 231, 15),
    )

    # K letter - designed as clean geometric shapes
    k_color = (235, 235, 245, 255)
    accent = (108, 92, 231, 255)

    # Main vertical bar
    bar_w = 28
    bar_x = cx - 55
    draw.rounded_rectangle(
        [bar_x, cy - 112, bar_x + bar_w, cy + 100],
        radius=6,
        fill=k_color,
    )

    # Upper arm
    arm_w = 18
    arm_h = 28
    # Upper diagonal
    pts_upper = [
        (bar_x + bar_w - 2, cy - 15),
        (cx + 100, cy - 110),
        (cx + 100 + arm_w, cy - 110 - arm_h + 30),
        (cx + 100 + arm_w - 15, cy - 110 - arm_h + 30 + 15),
        (bar_x + bar_w + 10, cy - 5),
    ]
    draw.polygon(pts_upper, fill=k_color)

    # Lower diagonal
    pts_lower = [
        (bar_x + bar_w - 2, cy + 15),
        (cx + 100, cy + 112),
        (cx + 100 + arm_w, cy + 112 + arm_h - 30),
        (cx + 100 + arm_w - 15, cy + 112 + arm_h - 30 - 15),
        (bar_x + bar_w + 10, cy + 5),
    ]
    draw.polygon(pts_lower, fill=k_color)

    # Small accent diamond/dot near top right
    dot_r = 7
    draw.ellipse(
        [cx + 92, cy - 102, cx + 92 + dot_r * 2, cy - 102 + dot_r * 2],
        fill=accent,
    )

    # "KIMI API" text below
    # We'll keep it minimal - just the logo mark is enough

    path = os.path.join(OUTPUT_DIR, 'logo.png')
    img.save(path, 'PNG')
    print(f'Logo saved: {path}')
    return path


def draw_favicon():
    w, h = 64, 64
    img = Image.new('RGBA', (w, h), (10, 10, 15, 255))
    draw = ImageDraw.Draw(img)

    cx, cy = w // 2, h // 2

    # Subtle glow
    for r in range(30, 0, -1):
        alpha = max(0, int(8 * (1 - r / 30)))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(108, 92, 231, alpha))

    # K letter
    k_color = (235, 235, 245, 255)
    accent = (108, 92, 231, 255)

    # Vertical bar
    bar_w = 6
    bar_x = cx - 12
    draw.rounded_rectangle(
        [bar_x, cy - 24, bar_x + bar_w, cy + 22],
        radius=2,
        fill=k_color,
    )

    # Upper arm
    pts_upper = [
        (bar_x + bar_w - 1, cy - 2),
        (cx + 22, cy - 24),
        (cx + 24, cy - 22),
        (bar_x + bar_w + 3, cy),
    ]
    draw.polygon(pts_upper, fill=k_color)

    # Lower arm
    pts_lower = [
        (bar_x + bar_w - 1, cy + 2),
        (cx + 22, cy + 26),
        (cx + 24, cy + 24),
        (bar_x + bar_w + 3, cy),
    ]
    draw.polygon(pts_lower, fill=k_color)

    # Accent dot
    draw.ellipse([cx + 20, cy - 22, cx + 24, cy - 18], fill=accent)

    path = os.path.join(OUTPUT_DIR, 'favicon.png')
    img.save(path, 'PNG')
    print(f'Favicon saved: {path}')
    return path


if __name__ == '__main__':
    draw_logo()
    draw_favicon()
    print('All assets generated!')
