#MenuTitle: Change LayerColor to Brown

#MenuTitle: Change LayerColor to Green
# -*- coding: utf-8 -*-

font = Glyphs.font

selectedLayers = font.selectedLayers
for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	thisGlyph.layers[font.selectedFontMaster.id].color = 2