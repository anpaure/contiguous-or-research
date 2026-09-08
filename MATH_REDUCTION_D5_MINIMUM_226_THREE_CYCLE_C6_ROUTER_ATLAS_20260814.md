# The frozen D5 head permutation has a minimum 226-router C6 atlas reduction

**Date:** 2026-08-14  
**Status:** exact algebraic decomposition and physical interface reduction.
The 226 three-cycle product is verified on all 477 logical head tokens.
Legal Johnson collars, complete q1 refill, global resource simplicity and
the final factor traversal are still open physical compilation gates.

## 0. Outcome

The frozen D5 head permutation is even and has a minimum factorization into
226 three-cycles.  A marked-C6 router realizes each full three-cycle on 18
resident owners, without a fixed tail, auxiliary-port suppression or cable.
Consequently the row-private 212-transposition route can be replaced
algebraically by an atlas with

```text
226 routers,  4068 new router owners,  678 logical port attachments.
```

The number `678` is important: the factorization acts on 477 logical tokens,
but 41 pivot tokens occur in more than one factor.  A physical atlas must put
repeated appearances at distinct serial occurrences on the same logical
strand; it cannot identify them as one degree-four owner.

## 1. Exact minimum three-cycle decomposition

The 477 changed head tokens in the frozen selection lie on 41 disjoint
target cycles with length histogram

```text
9:6, 10:6, 11:11, 12:6, 13:4, 14:3, 15:4, 16:1.
```

There are 25 odd cycles and 16 even cycles.  The sign exponent is 436, so the
target permutation is even.

An odd cycle of length `l` is a product of `(l-1)/2` three-cycles.  The 25
odd cycles contribute 131 factors.  Pair the 16 even cycles.  Factoring each
even cycle down to one residual transposition and replacing two disjoint
residual transpositions by two three-cycles contributes another 95 factors.
With rightmost factors acting first, the identities used by the constructor
are

```text
(a b)(a c) = (a c b),
(a b)(c d) = (a c b)(a c d)
```

for distinct `a,b,c,d`.  Thus the residual transpositions from each paired
even-cycle pair are composed in the same convention as the odd-cycle
factors.
The frozen certificate therefore gives

```text
131 + 95 = 226 three-cycles.
```

This is minimum.  Start at the target and multiply by the inverse factors
to return to the identity.  The target has 25 odd cycles on its 477-point
support, while the identity has 477; multiplication by one three-cycle can
increase the number of odd cycles by at most two.  Hence every three-cycle
factorization has at least

```text
(477 - 25)/2 = 226
```

factors.  The H100 constructor explicitly multiplies the displayed 226
factors, with rightmost factor acting first, and checks the target image of
all 477 tokens.

## 2. Cut-open C6-router atlas interface

For each factor `gamma_j=(p q r)`, allocate one owner-disjoint copy of the
18-owner C6 router.  Its old first-return action on its three ports is the
identity and its new action is `gamma_j` after orienting the port labels.

At each of its three phase-common central edges, cut one router edge and one
edge on the corresponding logical token strand, then perform an ordinary
degree-two two-edge splice.  Thus one router uses three owner-disjoint
splices.  Across the atlas this requires

```text
3*226 = 678 splices,
2*678 = 1356 deleted edges, and
2*678 = 1356 added Johnson cross edges
```

when counting both the router and strand edge removed by each splice.

Fix the traversal direction on every logical strand.  Because the
certificate writes the product with the rightmost factor acting first, put
the attachment sites encountered by a traveller in decreasing certificate
index, `gamma_226,...,gamma_1` (omitting factors not incident with that
strand).  Suppressing the router interiors makes every old box the identity
wire and every new box its listed three-cycle.  Therefore the suppressed new
atlas has monodromy

```text
gamma_1 gamma_2 ... gamma_226,
```

in the certificate's rightmost-first convention.  If the cut-open strands
and final closure are the literal frozen-D5 darts, this recovers the exact
frozen head permutation.

The local owner cost and **closed-router** typed-bank budget before the
three cuts are

```text
18*226 = 4068 owners,
18*226 = 4068 lower-q1 occurrences,
18*226 = 4068 upper-q1 occurrences,
18*226 = 4068 lower-q2 occurrences,
18*226 = 4068 upper-q2 occurrences.
```

Each closed router has zero old/new q2 occurrence current and exact
residence minima `(3,3)` on owners and `(4,2)` on immediate-upper traces.
These facts are internal: after the cuts, the deleted internal windows and
all crossing q1/q2 windows belong to the open collar audit.  Pairwise
simplicity of the 226 relabelled banks and all 678 crossing collars remain
to be selected.

## 3. Logical tokens are not single physical occurrences

The verified token-appearance histogram is

```text
appearances 1: 436 tokens
appearances 4:   6 tokens
appearances 5:  11 tokens
appearances 6:  10 tokens
appearances 7:  10 tokens
appearances 8:   3 tokens
appearances 9:   1 token.
```

Thus all 436 nonpivot tokens appear once, while one pivot from each of the 41
target cycles is reused.  Total port appearances are

```text
436 + 4*6 + 5*11 + 6*10 + 7*10 + 8*3 + 9 = 678.
```

There are 201 appearances beyond the first occurrence of each logical token.
This does not obstruct a serial atlas: a logical token is a strand, and each
appearance is a distinct cut site on that strand.  It does rule out the
stronger claim that all 477 ports can be identified one-for-one with router
port owners.  Such identification would create reused or degree-four owner
occurrences.

The pivot-heavy factorization is algebraically minimum, not chronology-
optimal.  A later atlas optimizer may trade more than 226 routers for lower
maximum token exposure, or seek another minimum factorization with a flatter
appearance distribution.

## 4. Remaining physical theorem

The exact global atlas theorem still has to provide:

1. 477 oriented cut-open strands whose suppressed labels are the frozen D5
   head darts, with 678 distinct serial attachment sites in the certified
   product order;
2. for every attachment, a phase-common router cut and strand cut whose two
   cross pairs are Johnson edges;
3. pairwise-simple owner/lower-q1/upper-q1/lower-q2/upper-q2 banks, including
   every crossing window, and exact refill of the q1 resources removed from
   the frozen factor;
4. owner and immediate-upper collar residence across every new join; and
5. a complete traversal showing that the old atlas is the original factor
   and the new atlas has the required `372 -> 1` component topology.

A selector for 226 private router relabellings addresses only item 3's
internal-resource part.  It does not by itself provide the ordered strands,
crossing q1/q2 windows or global topology.

## 5. H100 provenance

```text
selection SHA-256
94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32

constructor/verifier SHA-256
9f90f2e382fbdfd5735041bdfe6584617b54c7f84c8a9111c291ad813413e725
  scratch/build_t2_suffix_d5_global_c6_decomposition_20260814.py

certificate SHA-256
66a0e8eb4ee478108ce7a7638a3ee2bb8380db0119942b64366b933542efc4a4
  scratch/build_t2_suffix_d5_global_c6_decomposition_20260814.h100.out

independent replay SHA-256
0b41e3c50680d001dca1edbc2ad0e892f5cd7655110141d60cef22bd66f9fd81
  scratch/audit_t2_suffix_d5_global_c6_decomposition_independent_20260814.py
20713675439b3d4d17df698a1c5ad14c7e853e8bdc05000a2e3af6b7cb6f4540
  scratch/audit_t2_suffix_d5_global_c6_decomposition_independent_20260814.h100.out
```

The frozen output records all 226 ordered factors and their source-cycle
provenance, not only the aggregate counts.  The independent replay imports
none of the constructor code and separately verifies the product, lower
bound, provenance partition and complete port-appearance histogram.
