# Independent audit: crossed common-neighbour splitter closes the four coatom-screen collisions

Date: 2026-08-01  
Lane: independent topology/owner audit  
Status: exact dimension-uniform local theorem; no Pascal embedding or compiler theorem

## 0. Verdict

The four repeated full-filler screens in
`MATH_THEOREM_COATOM_SCREEN_TENSOR_RESIDENT_ECO_PACKET_20260801.md`
are not a regenerative sidecar.  They can be removed inside the same
`12d+35` owner slots.

Keep the displayed active cut and the common coatom order

\[
 C_0,C_1,\ldots,C_{n-1},\qquad n=d+2,
\]

in every block.  At the four zero-based active-edge positions

\[
                         J=\{1,3,5,7\},                         \tag{0.1}
\]

replace the full-filler intersection screen by the other non-block common
Johnson neighbour.  For every `d>=1`, and for each of the three authenticated
positive ECO rows, the resulting two expanded words are simple Johnson
paths with:

* common endpoints and exactly the same owner set;
* pointwise equal prefix-OR and suffix-OR chains;
* exactly equal internal interval-OR support;
* no internal positive run shorter than `d+1`; and
* the same complete clipped boundary state, including the whole-fragment
  flag.

Thus the owner/topology state is the singleton transition `0 -> 0`; no
four-token owner sidecar has to regenerate under `k -> k+2`.  The remaining
compiler and Pascal-host conditions are separate and are not proved here.

No reroot, active-word cut change, coatom rotation, length increase, or
owner deletion is needed.

## 1. The second common neighbour

Suppress the fixed core `K`.  Let consecutive active triples be

\[
 V=I\sqcup\{x\},\qquad W=I\sqcup\{y\},
\]

and put `F={f_0,...,f_(n-1)}`.  The terminal and initial block owners are

\[
 L=V\cup(F-\{f_{n-1}\}),\qquad
 R=W\cup(F-\{f_0\}).                                    \tag{1.1}
\]

Besides the old screen

\[
 S^\cap=I\cup F,
\]

the two endpoints have the common neighbour

\[
 S^\cup=(V\cup W)\cup(F-\{f_0,f_{n-1}\}).                \tag{1.2}
\]

Both have rank `n+2`.  From `L` to `S^cup` one deletes `f_0` and inserts
`y`; from `S^cup` to `R` one deletes `x` and inserts `f_(n-1)`.  Hence (1.2)
is a literal two-edge Johnson bridge.

## 2. The finite active ledger

For row 1, the active words are

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab.
```

At `J`, the four active unions are

\[
\begin{array}{c|c|c}
 &P&Q\\ \hline
j=1&45&43\\
j=3&57&57\\
j=5&46&46\\
j=7&43&45
\end{array}                                                \tag{2.1}
\]

so both phases have the same four distinct crossed labels

\[
                           \{43,45,46,57\}.                \tag{2.2}
\]

At the seven uncrossed positions, both phases have the same seven distinct
intersection labels

\[
                           \{3,5,9,17,34,36,40\}.          \tag{2.3}
\]

The other two positive ECO rows are coordinate relabellings and obey the
same ledger.  The independent replay checks them literally rather than
assuming the relabelling.

Every block owner is identified by its active triple and omitted filler
coordinate, so all `12n` block owners are distinct.  The three owner types
are mutually disjoint:

\[
\begin{array}{c|c|c}
\text{type}&\text{active rank}&\text{number of omitted fillers}\\ \hline
\text{block}&3&1\\
S^\cap&2&0\\
S^\cup&4&2.
\end{array}                                                \tag{2.4}
\]

Equations (2.2)--(2.4) prove simplicity.  The active vertex sets, (2.2),
and (2.3) are common between phases, so they also prove exact owner current.
The common first and last active triples prove common physical endpoints.

There is also a sharp finite characterization inside this repair fibre.
Choose exactly one occurrence from each of the four doubled intersection
screens to cross in each phase.  Exhausting the resulting `16 x 16` pairs
gives exactly three solutions, in all three active rows:

\[
 \{1,3,5,7\},\qquad \{2,5,8,10\},\qquad \{3,4,7,10\}.    \tag{2.5}
\]

The crossed sets agree phase by phase.  Thus (0.1) is one of exactly three
fixed-cut, fixed-block-order zero-defect repairs in this natural fibre.

## 3. Prefix and suffix chains

The filler word is positionwise identical between phases.  Inside block
`j`, the active part of a prefix is the contracted prefix through `V_j`.
At an uncrossed screen it remains that prefix, while at a crossed screen it
is the contracted prefix through `V_(j+1)`.  The base ECO rows have equal
contracted prefix chains, and the crossed-position vector is common, so the
expanded prefix chains agree pointwise.  Reversal gives the suffix claim.

This proof is independent of `n`.

## 4. Exact interval-deck formula

Let

* `A(W)` be the support of active contiguous-interval unions;
* `I_cap` be the seven labels in (2.3);
* `U_cross` be the four labels in (2.2);
* `C_t=F-{f_t}`; and
* `D=F-{f_0,f_(n-1)}`.

After restoring `K`, the complete internal interval-OR support of either
expanded word is exactly the union of

\[
\begin{aligned}
 &\{K\cup V\cup C_t:V\text{ is an active owner},\ 0\le t<n\},\\
 &\{K\cup U\cup D:U\in U_{\rm cross}\},\\
 &\{K\cup U\cup C_0,
       K\cup U\cup C_{n-1}:U\in U_{\rm cross}\},\\
 &\{K\cup I\cup F:I\in I_{\rm cap}\},\\
 &\{K\cup A\cup F:A\in\mathcal A(W)\}.                 \tag{4.1}
\end{aligned}
\]

Indeed, two different coatoms already cover `F`.  An interval whose filler
union is smaller than `F` is therefore exactly one of: one block cell; one
crossed screen; the terminal block cell followed by a crossed screen; or a
crossed screen followed by the next initial block cell.  These are the
first three lines of (4.1).  A singleton uncrossed screen gives line four.
Every remaining interval has full filler and its active part is a
contiguous active interval union, giving line five; conversely every such
union is realised.

The base active interval supports are equal, and Section 2's three finite
label banks are equal.  Formula (4.1) therefore proves the full deck equality
for every `n>=3`, not just for the audited depths.

## 5. Residence

Every active-coordinate occurrence at a screen touches a containing
adjacent active block.  Hence every internal active positive run contains a
whole block of length `n=d+2`.

For a middle filler `f_t`, `1<=t<=n-2`, every screen contains `f_t`; between
successive block zeros its run has length `n`.  For `f_0`, a crossed screen
separates a suffix of `n-1` ones from the next block's initial zero.  For
`f_(n-1)`, it separates the preceding terminal zero from a prefix of `n-1`
ones.  An uncrossed screen increases either length to `n`.  Thus

\[
                \min\{\text{internal positive run}\}=n-1=d+1. \tag{5.1}
\]

The first and last active triples and the first and last coatom blocks are
common.  The complete leading/trailing states, clipped at `d+1`, therefore
agree.  Core coordinates are whole-fragment coordinates in both phases;
all other whole-fragment flags also agree.

## 6. Independent replay

The dependency-free audit is

```text
scratch/audit_coatom_screen_cross_splitter_independent_20260801.py
scratch/coatom_screen_cross_splitter_independent_20260801.audit.json
```

It hard-codes the three active rows instead of reading either previous
tensor payload.  It checks:

1. all `16 x 16` choices in the finite fibre and the exact three-solution
   catalogue (2.5);
2. literal ranks, Johnson adjacency, endpoints, simplicity, and owner
   counters;
3. pointwise prefix/suffix chains and complete interval-OR support;
4. clipped boundary states with whole-fragment flags; and
5. every internal run,

for every row and every `1<=d<=16`.  The symbolic arguments above extend
the finite replay to every `d>=1`.

This audit does not assert trace-guarded compiler invariance, unused-basis
Hall, macro abundance, or a same-parity Pascal embedding.
