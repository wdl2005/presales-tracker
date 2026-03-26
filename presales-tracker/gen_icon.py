#!/usr/bin/env python3
"""Generate simple PNG icons for PWA manifest."""
import struct
import zlib
import os

def create_png(width, height, color=(37, 99, 235), text="售前"):
    """Create a simple PNG with colored background and text."""
    def make_chunk(chunk_type, data):
        chunk_len = struct.pack('>I', len(data))
        chunk_crc = struct.pack('>I', zlib.crc32(chunk_type + data) & 0xffffffff)
        return chunk_len + chunk_type + data + chunk_crc

    # PNG signature
    png = b'\x89PNG\r\n\x1a\n'

    # IHDR chunk
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    png += make_chunk(b'IHDR', ihdr_data)

    # IDAT chunk (image data)
    raw_data = b''
    r, g, b = color
    # Simple solid color with text representation (we'll just make solid color for now)
    for y in range(height):
        raw_data += b'\x00'  # filter byte
        for x in range(width):
            # Create a gradient-like effect
            factor = 1.0 - (abs(x - width//2) / width * 0.3)
            raw_data += bytes([
                min(255, int(r * factor)),
                min(255, int(g * factor)),
                min(255, int(b * factor))
            ])
    
    compressed = zlib.compress(raw_data, 9)
    png += make_chunk(b'IDAT', compressed)

    # IEND chunk
    png += make_chunk(b'IEND', b'')
    return png

def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Generate 192x192 icon
    icon_192 = create_png(192, 192)
    with open(os.path.join(out_dir, 'icons', 'icon-192.png'), 'wb') as f:
        f.write(icon_192)
    print("Created icon-192.png")
    
    # Generate 512x512 icon  
    icon_512 = create_png(512, 512)
    with open(os.path.join(out_dir, 'icons', 'icon-512.png'), 'wb') as f:
        f.write(icon_512)
    print("Created icon-512.png")

if __name__ == '__main__':
    main()
