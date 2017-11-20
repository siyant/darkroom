#!/usr/bin/env python

import argparse
import os
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('outputFolder', nargs='?', default='edited', help='name of output folder (must not be created yet)')
parser.add_argument('-rs', '--resize', metavar='maxDim', dest='maxDim', type=int, help='max dimension in px')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

# print(vars(args))

def main():
  if not args.maxDim: # no optional arguments entered
    parser.print_help()
    return

  if os.path.isdir(args.outputFolder):
    print('Error: Output folder %s already exists' % args.outputFolder)
    return

  os.mkdir(args.outputFolder)

  for f in os.listdir(os.getcwd()):
    if os.path.isfile(f) and any(f.lower().endswith(k) for k in [".jpg", ".jpeg", ".png"]):
      name, ext = os.path.splitext(f)
      img = Image.open(f)
      origWidth, origHeight = img.size
      img = img.copy()

      if args.maxDim:   # resize to maxDim
        img.thumbnail((args.maxDim, args.maxDim))
        newWidth, newHeight = img.size
      
      new_filename = name + ext

      img.save(args.outputFolder + '/' + new_filename)

      if args.maxDim and args.verbose:
        print("resized %s from %dx%d to %dx%d" % (f, origWidth, origHeight, newWidth, newHeight))

main()