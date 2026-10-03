#!/usr/bin/env python3

import argparse
import json


def build_prompt(style, length, parting, mood, face_shape):
    length_map = {
        "short": "short and clean",
        "medium": "medium length with soft movement",
        "long": "long and flowing",
        "extra-long": "very long with dramatic volume"
    }

    parting_map = {
        "center": "center part",
        "side": "deep side part",
        "middle": "soft middle part",
        "none": "no visible part"
    }

    mood_map = {
        "clean": "clean and polished",
        "wild": "chaotic and expressive",
        "cute": "cute and playful",
        "edgy": "edgy and bold",
        "soft": "soft and romantic"
    }

    data = {
        "style": style,
        "description": f"{style} hairstyle, {length_map.get(length, 'medium length')} with a {parting_map.get(parting, 'center part')}, {mood_map.get(mood, 'clean and polished')}, tailored for a {face_shape} face shape.",
        "silhouette": "clear front silhouette with readable volume from the crown to the ends",
        "volume": "balanced volume with controlled puff and movement",
        "color_direction": "solid vibrant tone with subtle variation for depth",
        "blender_approach": "generate layered hair cards, randomized clipping, and controlled curls or flattening for Roblox readability",
        "roblox_notes": "Low-poly silhouette, simple separation, good top volume, clean front view readability"
    }

    return data


def main():
    parser = argparse.ArgumentParser(description="Generate hairstyle design prompts for Blender and Roblox.")
    parser.add_argument("--style", default="bob cut", help="Hairstyle style")
    parser.add_argument("--length", default="medium", choices=["short", "medium", "long", "extra-long"], help="Hair length")
    parser.add_argument("--parting", default="center", choices=["center", "side", "middle", "none"], help="Hair parting")
    parser.add_argument("--mood", default="clean", choices=["clean", "wild", "cute", "edgy", "soft"], help="Overall vibe")
    parser.add_argument("--face-shape", default="oval", help="Face shape")
    args = parser.parse_args()

    prompt = build_prompt(args.style, args.length, args.parting, args.mood, args.face_shape)
    print(json.dumps(prompt, indent=2))


if __name__ == "__main__":
    main()
