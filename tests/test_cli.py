import unittest
from src.cli import parse_args
import sys

class TestCLI(unittest.TestCase):
    def test_merge_args(self):
        # Mock sys.argv for merge command
        # Note: audio is now a list due to nargs='+'
        sys.argv = ['combine', 'merge', '-v', 'v.mp4', '-a', 'a.mp3', '-o', 'out.mp4']
        args = parse_args()
        self.assertEqual(args.command, 'merge')
        self.assertEqual(args.video, 'v.mp4')
        self.assertEqual(args.audio, ['a.mp3'])
        self.assertEqual(args.output, 'out.mp4')
        self.assertEqual(args.quality, 'fast')

    def test_info_args(self):
        # Mock sys.argv for info command
        sys.argv = ['combine', 'info', '-i', 'v.mp4']
        args = parse_args()
        self.assertEqual(args.command, 'info')
        self.assertEqual(args.input, 'v.mp4')

    def test_batch_args(self):
        # Mock sys.argv for batch command
        sys.argv = ['combine', 'batch', '-d', './raw', '-o', './out']
        args = parse_args()
        self.assertEqual(args.command, 'batch')
        self.assertEqual(args.dir, './raw')
        self.assertEqual(args.output_dir, './out')

if __name__ == '__main__':
    unittest.main()
