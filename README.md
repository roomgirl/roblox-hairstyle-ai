# Roblox Hairstyle AI for Blender

This project is a practical starter kit for building a Roblox hairstyle workflow in Blender.
It gives you:
- prompt generation for hairstyle style directions
- a Blender Python script that creates hair cards / stylized strands
- a Roblox export checklist for making the results usable in-game

The goal is not to replace human artistry. It is to give you a faster visual ideation and asset-generation workflow.

## What this project does

1. Helps you describe a hairstyle in a structured way.
2. Builds a prompt or style brief for the haircut.
3. Generates a Blender scene with simple hair cards.
4. Prepares the asset for Roblox adaptation.

## Project layout

- `scripts/hair_style_prompt_builder.py` – creates hairstyle briefs and prompts
- `scripts/blender_generate_hair.py` – Blender script to generate a stylized hair setup
- `docs/roblox_blender_pipeline.md` – Roblox export and optimization guide

## Quick workflow

### 1) Generate a hairstyle brief

```bash
python3 scripts/hair_style_prompt_builder.py --style "afro puff" --length medium --parting center --mood clean
```

This prints a prompt and technical notes like:
- silhouette
- face shape
- volume
- colors
- Blender approach

### 2) Build a basic hairstyle in Blender

In Blender:

```bash
blender --background --python scripts/blender_generate_hair.py -- --style "afro puff" --density 260 --length 1.2 --width 0.18
```

This generates:
- a simple scalp guide
- hair cards distributed around the head
- randomized rotations for a more natural look

### 3) Refine and export for Roblox

Use the export checklist in `docs/roblox_blender_pipeline.md`.

## Example style ideas

- curly bob
- afro puff
- layered wolf cut
- straight ponytail
- bubble braid
- short pixie
- long wavy hair
- anime bangs

## Recommended Blender workflow

- Start with hair cards, not full scalp geometry.
- Keep the silhouette simple and readable from a distance.
- Use flat or slightly curved planes for Roblox-friendly stylized hair.
- Export as FBX or OBJ with a clean transform.
- Keep UVs easy and avoid unnecessary sub-division.

## Roblox-specific notes

For Roblox, hair usually works best when:
- the silhouette is simple
- the top is a bit flatter than real-life hair
- the volume is readable from front and side views
- the model is low-poly and cleanly weighted or attached

## Next upgrades

Possible future upgrades for this repo:
- generate a proper UV layout for hair cards
- support texture generation for different hair colors
- create a Blender add-on UI
- export a full package for Roblox Studio use

## License

This project is intentionally lightweight and open for you to remix for your own creative workflow.
