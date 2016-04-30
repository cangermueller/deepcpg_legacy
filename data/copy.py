#!/usr/bin/env python

import argparse
import sys
import logging
import os.path as pt
import h5py as h5


class App(object):

    def run(self, args):
        name = pt.basename(args[0])
        parser = self.create_parser(name)
        opts = parser.parse_args(args[1:])
        return self.main(name, opts)

    def create_parser(self, name):
        p = argparse.ArgumentParser(
            prog=name,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description='Description')
        p.add_argument(
            'in_file',
            help='Input file')
        p.add_argument(
            '-o', '--out_file',
            help='Output file')
        p.add_argument(
            '--nb_sample',
            type=int,
            help='Number of samples')
        p.add_argument(
            '--verbose',
            help='More detailed log messages',
            action='store_true')
        p.add_argument(
            '--log_file',
            help='Write log messages to file')
        return p

    def main(self, name, opts):
        logging.basicConfig(filename=opts.log_file,
                            format='%(levelname)s (%(asctime)s): %(message)s')
        log = logging.getLogger(name)
        if opts.verbose:
            log.setLevel(logging.DEBUG)
        else:
            log.setLevel(logging.INFO)
        log.debug(opts)

        in_file = h5.File(opts.in_file, 'r')
        out_file = h5.File(opts.out_file, 'w')
        nb_sample = opts.nb_sample
        if nb_sample is None:
            nb_sample = in_file['pos'].shape[0]

        in_file.copy('targets', out_file)
        for g in ['pos', 'data']:
            log.info(g)
            ig = in_file[g]
            og = out_file.create_group(g)
            for x in ig.keys():
                og[x] = ig[x][:nb_sample]

        in_file.close()
        out_file.close()

        return 0


if __name__ == '__main__':
    app = App()
    app.run(sys.argv)
