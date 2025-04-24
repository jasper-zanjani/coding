import drawsvg as draw

d = draw.Drawing(61,51, origin=(0,0))

d.append(draw.Lines(0,0, 60,0, 60,0, 30,-50, close=True, fill='transparent', stroke='black'))

d.save_svg('00.svg')
