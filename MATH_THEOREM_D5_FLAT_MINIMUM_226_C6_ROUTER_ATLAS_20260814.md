# The frozen D5 permutation has a flat minimum 226-router C6 atlas

**Date:** 2026-08-14  
**Status:** exact algebraic theorem with independent H100 replay.  It
strictly improves the serial-site profile of the earlier one-pivot minimum
atlas.  A literal cut-open Johnson compiler, q1 refill, crossing q2 audit,
residence and the final factor traversal remain open.

## 0. Outcome

The frozen D5 head permutation on 477 logical tokens has a minimum
factorization into 226 three-cycles in which no token occurs in more than
three factors.  The exact occurrence histogram is

```text
appearances 1: 292 tokens
appearances 2: 169 tokens
appearances 3:  16 tokens.
```

Thus a serial C6-router compiler needs at most three distinct attachment
sites on any logical strand.  This replaces the earlier minimum
factorization's pivot-heavy maximum of nine without increasing the number
of routers, owner charge, or total number 678 of port attachments.

The improvement is purely algebraic but directly strengthens the live
physical interface.  It does **not** assert that the frozen factor already
contains the required distinct phase-common cuts, or that 226 relabelled
router banks can be planted simultaneously.

## 1. Flat factorization of one odd cycle

Use the convention that the rightmost factor acts first.  For an odd cycle

\[
 C=(v_1\ v_2\ \cdots\ v_{2r+1}),
\]

put

\[
 F_j=(v_{2j-1}\ v_{2j}\ v_{2j+1}),
 \qquad 1\le j\le r.                               \tag{1.1}
\]

Then

\[
             C=F_1F_2\cdots F_r.                  \tag{1.2}
\]

Indeed, `v_(2j-1)` is sent successively to `v_(2j)` and
`v_(2j+1)` is passed to the next overlapping triple; the last point is sent
back through the overlap chain to `v_1`.  Equivalently, direct evaluation
gives `v_i -> v_(i+1)` for `i<2r+1` and `v_(2r+1) -> v_1`.

The factor count is the minimum `(2r+1-1)/2=r`.  Every non-junction token
occurs once, and the overlap tokens

\[
                 v_3,v_5,\ldots,v_{2r-1}
\]

occur twice.  Hence the maximum exposure is two.

## 2. Flat factorization of a pair of even cycles

Let

\[
 A=(u_1\cdots u_{2r}),\qquad B=(w_1\cdots w_{2s})
\]

be disjoint even cycles.  Apply Section 1 to the odd prefixes

\[
 A_0=(u_1\cdots u_{2r-1}),\qquad
 B_0=(w_1\cdots w_{2s-1}).
\]

Writing

\[
 a=u_{2r-1},\ b=u_{2r},\ c=w_{2s-1},\ d=w_{2s},
\]

gives

\[
 A=A_0(a\ b),\qquad B=B_0(c\ d).                  \tag{2.1}
\]

The two residual transpositions satisfy

\[
        (a\ b)(c\ d)=(a\ c\ b)(a\ c\ d).        \tag{2.2}
\]

Consequently `AB` uses

\[
       (r-1)+(s-1)+2=r+s
\]

three-cycles, which is again the minimum.  Ordinary chain junctions occur
twice.  Only `a` and `c`, the two penultimate endpoints of the paired even
cycles, occur three times: once in their prefix chain and twice in `(2.2)`.
All other tokens occur at most twice.

## 3. Application to the frozen D5 permutation

The 41 disjoint target cycles have length histogram

```text
9:6, 10:6, 11:11, 12:6, 13:4, 14:3, 15:4, 16:1.
```

There are 25 odd and 16 even cycles.  Factor each odd cycle by Section 1
and pair the 16 even cycles arbitrarily for Section 2.  The total number of
factors is

\[
 \frac{477-25}{2}=226.                              \tag{3.1}
\]

This is globally minimum: start at the target and multiply by inverse
three-cycles to return to the identity.  One multiplication can increase
the number of odd cycles by at most two, while the target has 25 odd cycles
on its 477-point support and the identity has 477.

There are eight even-cycle pairs, so exactly 16 penultimate endpoints may
occur three times.  Independent replay of the literal frozen selection
gives the exact histogram in Section 0 and verifies the ordered product on
all 477 tokens.

## 4. Consequence for a cut-open C6 compiler

Replacing every algebraic factor by one certified 18-owner resident C6
router still has the exact budget

```text
226 routers
4068 router owners
678 logical port attachments.
```

The stronger scheduling requirement is now:

```text
292 strands need one cut site,
169 strands need two ordered cut sites,
 16 strands need three ordered cut sites.
```

No strand needs four or more.  This eliminates high-pivot congestion as a
reason to abandon a minimum atlas.

The following are still separate physical gates.

1. Realize each logical token as a cut-open strand carrying its one to three
   attachment sites in decreasing certificate index along the traversal
   direction.  This is the spatial order that implements the certificate's
   rightmost-factor-first convention.
2. At every site, choose a phase-common router cut and a context cut whose
   two cross pairs are Johnson edges.
3. Refill every removed immediate-lower and immediate-upper occurrence and
   prove equality and simplicity of the complete q1 and q2 decks, including
   crossing windows.
4. Prove owner and immediate-upper residence across every collar.
5. Suppress the full installed atlas and verify the intended old factor and
   the new `372 -> 1` component traversal.

Thus the theorem solves the router-count and serial-exposure optimization,
not the cut-open compiler.

## 5. H100 provenance

```text
constructor
  scratch/build_t2_suffix_d5_flat_minimum_c6_atlas_20260814.py
  SHA256 d7639744e5d8ce497a5b7d9cf71c99e769bb62e96326c7fc28014797b9441013

certificate
  scratch/build_t2_suffix_d5_flat_minimum_c6_atlas_20260814.h100.out
  SHA256 2b7bc68cb4559696c0dcf6bc0f7464c8dbe0d7d398dfab2b0996282a7f419dcc

independent replay
  scratch/audit_t2_suffix_d5_flat_minimum_c6_atlas_independent_20260814.py
  SHA256 67bbc59ade5abc2bf869f4daf888fe72809ddd72e35e49a8d05ddb00af89a40c

independent output
  scratch/audit_t2_suffix_d5_flat_minimum_c6_atlas_independent_20260814.h100.out
  SHA256 a5f21662d08da89dddbf6e3d14225557d078e28aff8a3f9224aa9ab5056b4ff0

frozen D5 selector
  scratch/solve_t2_suffix_d5_topology_cegar_20260814.h100.out
  SHA256 94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32
```

All construction, replay and hashing were run through SSH on H100.  The
local Mac was used only to edit, transfer and operate Git.
