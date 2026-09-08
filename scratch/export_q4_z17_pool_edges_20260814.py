#!/usr/bin/env python3
"""Export a q4 Z17 JSON candidate pool to a compact integer edge list."""

from __future__ import annotations

import argparse
import json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("target")
    args = parser.parse_args()
    data = json.load(open(args.source))
    edges = [candidate["edge"] for candidate in data["candidates"]]
    sizes = sorted({len(edge) for edge in edges})
    if len(sizes) != 1:
        raise ValueError(f"mixed edge sizes: {sizes}")
    with open(args.target, "w") as handle:
        handle.write(f"{data['owner_orbits']} {len(edges)} {sizes[0]}\n")
        for edge in edges:
            if len(set(edge)) != len(edge):
                raise ValueError("nonsimple edge")
            handle.write(" ".join(map(str, edge)) + "\n")
    print(
        f"PASS vertices={data['owner_orbits']} edges={len(edges)} "
        f"uniformity={sizes[0]} target={args.target}"
    )


if __name__ == "__main__":
    main()
