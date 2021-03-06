#coding: utf-8

# The background image
img = "/home/tribo/Code/crappy/data/Pad.png"
# The points and their labels
points = [
    ("T1", (185,430)),
    ("T2",(145, 320)),
    ("T3",(105, 220)),
    ("T4",(720, 370)),
    ("T5",(720, 250)),
    ("T6",(720, 125)),
    ("T7",(1220, 410)),
    ("T8",(1260, 320)),
    ("T9",(1300, 230)),
]


coord_disc = [
    ('T12',(100,800)),
    ('T13',(100,920)),
]

trange = [20,300] # Temperature scale

options = [{'type':'dot_text',
            'coord':pos,
            'text':l+' = %.1f',
            'label':l} for l,pos in points]

options += [{'type':'text',
            'coord':pos,
            'text':l+' = %.1f',
            'label':l} for l,pos in coord_disc]


def get_drawing(labels):
  #from crappy.blocks import Drawing
  i = 0
  while i < len(options):
    if options[i]['label'] in labels:
      i += 1
    else:
      del options[i]
  from crappy import blocks
  return blocks.Drawing(img,options, crange=[20,300],
      title="Temperatures",backend="qt4agg")
