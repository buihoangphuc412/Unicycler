import unittest
import os
import unicycler.cpp_function_wrappers
import unicycler.read_ref
import unicycler.alignment

class TestSemiGlobalAlignment(unittest.TestCase):
    pass


class TestFullyGlobalAlignment(unittest.TestCase):
    pass


class TestPathAlignment(unittest.TestCase):
    pass


class TestMultipleSequenceAlignment(unittest.TestCase):

    def setUp(self):
        test_fastq = os.path.join(os.path.dirname(__file__), 'test_2.fastq')
        self.read_dict, self.read_names, _ = unicycler.read_ref.load_long_reads(test_fastq, 0)
        self.scoring_scheme = unicycler.alignment.AlignmentScoringScheme('3,-6,-5,-2')
        self.seqs = [self.read_dict[name].sequence for name in self.read_names]
        self.quals = [self.read_dict[name].qualities for name in self.read_names]
        self.original_seq = self.seqs[0]

    def test_consensus_with_subs(self):
        seqs = self.seqs[1:4]
        quals = self.quals[1:4]
        consensus, scores = unicycler.cpp_function_wrappers.consensus_alignment(seqs, quals,
                                                                                self.scoring_scheme)
        self.assertEqual(consensus, self.original_seq)

    def test_consensus_with_deletions(self):
        seqs = self.seqs[4:7]
        quals = self.quals[4:7]
        consensus, scores = unicycler.cpp_function_wrappers.consensus_alignment(seqs, quals,
                                                                                self.scoring_scheme)
        self.assertEqual(consensus, self.original_seq)

    def test_consensus_with_insertions(self):
        seqs = self.seqs[7:10]
        quals = self.quals[7:10]
        consensus, scores = unicycler.cpp_function_wrappers.consensus_alignment(seqs, quals,
                                                                                self.scoring_scheme)
        self.assertEqual(consensus, self.original_seq)

    def test_consensus_with_deletions_and_insertions(self):
        seqs = self.seqs[4:10]
        quals = self.quals[4:10]
        consensus, scores = unicycler.cpp_function_wrappers.consensus_alignment(seqs, quals,
                                                                                self.scoring_scheme)
        self.assertEqual(consensus, self.original_seq)

    def test_consensus_with_all(self):
        seqs = self.seqs[1:10]
        quals = self.quals[1:10]
        consensus, scores = unicycler.cpp_function_wrappers.consensus_alignment(seqs, quals,
                                                                                self.scoring_scheme)
        self.assertEqual(consensus, self.original_seq)