#MenuTitle: Change LayerColor to DarkBlue
# -*- coding: utf-8 -*-

font = Glyphs.font

selectedLayers = font.selectedLayers
for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	thisGlyph.layers[font.selectedFontMaster.id].color = 7
