#!/usr/bin/env python3

import argparse
import math
import random

import bpy


def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)


def add_material(obj, name, color):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
    obj.data.materials.append(mat)


def add_reference_head():
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.9, location=(0, 0, 0.9))
    obj = bpy.context.active_object
    obj.name = "HeadReference"
    return obj


def add_hair_card(location, rotation, scale, color):
    bpy.ops.mesh.primitive_plane_add(size=1.0, location=location)
    obj = bpy.context.active_object
    obj.name = "HairCard"
    obj.rotation_euler = rotation
    obj.scale = (scale, scale, scale)
    add_material(obj, "HairMaterial", color)
    return obj


def build_hairstyle(style, density, length, width, color):
    clear_scene()
    add_reference_head()

    for i in range(density):
        angle = (i / max(1, density)) * math.tau
        radial = random.uniform(0.15, 0.9)
        x = math.cos(angle) * radial * 0.7
        y = math.sin(angle) * radial * 0.7
        z = random.uniform(0.2, 1.2) * length

        location = (x, y, z)

        pitch = random.uniform(-0.9, 0.8)
        yaw = random.uniform(-math.pi, math.pi)
        roll = random.uniform(-1.2, 1.2)
        rotation = (pitch, yaw, roll)

        scale = random.uniform(width * 0.6, width * 1.8)
        add_hair_card(location, rotation, scale, color)

    # Add a simple crown clump for more style structure.
    crown_center = (0.0, 0.0, 1.5 * length)
    crown_rotation = (0.0, 0.0, 0.0)
    add_hair_card(crown_center, crown_rotation, width * 3.5, color)


def parse_args():
    parser = argparse.ArgumentParser(description="Generate a stylized Roblox hairstyle setup in Blender.")
    parser.add_argument("--style", default="classic bob", help="Hairstyle mood/name")
    parser.add_argument("--density", type=int, default=180, help="Number of hair cards")
    parser.add_argument("--length", type=float, default=1.1, help="General hair length multiplier")
    parser.add_argument("--width", type=float, default=0.18, help="Hair card width multiplier")
    parser.add_argument("--color", type=str, default="(0.34, 0.14, 0.08, 1.0)", help="Hair color in RGBA")
    return parser.parse_args()


def color_from_string(value):
    try:
        color_tuple = eval(value, {"__builtins__": {}}, {})
        if isinstance(color_tuple, (tuple, list)) and len(color_tuple) == 4:
            return tuple(float(c) for c in color_tuple)
    except Exception:
        pass

    defaults = {
        "brown": (0.34, 0.14, 0.08, 1.0),
        "black": (0.06, 0.06, 0.06, 1.0),
        "blonde": (0.85, 0.72, 0.44, 1.0),
        "red": (0.67, 0.17, 0.12, 1.0),
        "purple": (0.46, 0.23, 0.7, 1.0),
    }
    return defaults.get(value.lower(), (0.34, 0.14, 0.08, 1.0))


def main():
    args = parse_args()
    hair_color = color_from_string(args.color)
    build_hairstyle(args.style, args.density, args.length, args.width, hair_color)
    print(f"Created a stylized '{args.style}' hairstyle setup with {args.density} cards.")


if __name__ == "__main__":
    main()
