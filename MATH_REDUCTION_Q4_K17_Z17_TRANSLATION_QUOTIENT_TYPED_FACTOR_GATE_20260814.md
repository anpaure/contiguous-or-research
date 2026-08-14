# The `Z_17` quotient reduces a typed `q4` owner factor to 1,430 exact rows

**Date:** 2026-08-14
**Status:** exact finite reduction.  It proves what a quotient certificate
would imply and gives the complete internal ticket loads through `q3`.  It
does **not** assert that the resulting exact-cover system is feasible.

## 0. Outcome

Put the ground on `Z_17`, let the owner rank be `R=9`, and use pure rails
with

\[
                         q=4,\qquad c=5,\qquad N=10.             \tag{0.1}
\]

Every nonempty proper subset of `Z_17` has a free translation orbit.  In
particular, the rank-nine owner layer has

\[
                    {1\over17}{17\choose9}=1430                 \tag{0.2}
\]

orbits.  A period-ten pure rail whose ten owners belong to distinct
translation orbits therefore gives one ten-set quotient column.  An exact
cover by `143` such columns develops to `143*17=2431` legal closed rails
which partition all `24,310` rank-nine owners.

The same column has canonical internal lower and upper tickets.  Requiring
its ten rank-eight lower tickets to cover the `1,430` rank-eight orbits
exactly once gives, after development, a complete simple lower-`q1`
palette.  Requiring the rank-ten upper ticket loads to lie in `{1,2}` gives
complete upper-`q1` support, with exactly `286` quotient targets doubled.
The corresponding sharp load ranges through `q3` are forced by counting
and are displayed in Section 4.

Thus one finite `Z_17` master can close the owner and immediate-lower
factor rows simultaneously.  Component fusion, residence, external seam
tickets, the proper-upper continuation, and the terminal common cap remain
separate.

## 1. Quotient columns

Choose

\[
 C\in{\mathbb Z_{17}\choose5},\qquad
 \sigma=(s_0,\ldots,s_9),                           \tag{1.1}
\]

where the `s_i` are distinct and avoid `C`.  Indices below are modulo ten.
The pure rail has owners

\[
                  O_i=C\cup\{s_i,s_{i+1},s_{i+2},s_{i+3}\}.
                                                               \tag{1.2}
\]

Every consecutive pair is a Johnson edge, including the wrap edge.  Call
the rail **quotient-simple** when the ten sets `O_i` lie in ten distinct
translation orbits.  Its owner quotient column is then

\[
                  E_{\rm own}(C,\sigma)
                    =\{[O_0],\ldots,[O_9]\}.        \tag{1.3}
\]

For `1<=j<=4`, the intersection and union of `j` consecutive owners are

\[
\begin{aligned}
 L_i^{(j)}
   &=\bigcap_{t=0}^{j-1}O_{i+t}
     =C\cup\{s_{i+j-1},\ldots,s_{i+3}\},\\
 U_i^{(j)}
   &=\bigcup_{t=0}^{j-1}O_{i+t}
     =C\cup\{s_i,\ldots,s_{i+j+2}\}.
                                                               \tag{1.4}
\end{aligned}
\]

Hence their ranks are respectively

\[
                         |L_i^{(j)}|=10-j,
             \qquad      |U_i^{(j)}|=8+j.            \tag{1.5}
\]

The identities in `(1.4)` are literal, including every cyclic wrap.  They
are therefore sufficient to rebuild every internal typed ticket through
`q3` without reconstructing a physical developed factor.

## 2. Exact owner-factor equivalence

Let `Q` be any family of quotient-simple columns and let `x_Q in {0,1}`.
For a rank-nine translation orbit `A`, impose

\[
             \sum_Q 1[A\in E_{\rm own}(Q)]x_Q=1.    \tag{2.1}
\]

### Theorem 2.1

The selected columns develop under all seventeen translations to a simple
factor of the complete rank-nine owner layer if and only if `(2.1)` holds
for all `1,430` owner orbits.

#### Proof

Translation is free on every rank-nine set.  One occurrence of an orbit in
a selected quotient column develops to all seventeen members of that orbit,
once each.  Quotient simplicity prevents a single developed column from
using an orbit twice.  Thus `(2.1)` is equivalent orbit by orbit to every
physical owner occurring exactly once.  Conversely, any collision or hole
in the developed deck projects to a load different from one in `(2.1)`.
\(\square\)

Summing `(2.1)` gives

\[
                       10\sum_Qx_Q=1430,
              \qquad   \sum_Qx_Q=143.              \tag{2.2}
\]

The development therefore has `2,431` rails and `24,310` owners.  Each
coordinate lies in exactly

\[
                         9\cdot1430=12870            \tag{2.3}
\]

developed owners.  This point regularity is automatic: one developed orbit
of rank `r` contains each coordinate exactly `r` times.

## 3. Immediate-lower exactness and immediate-upper support

For a rank-eight orbit `A`, impose

\[
       \sum_Q\#\{i:[L_i^{(2)}]=A\}\,x_Q=1.          \tag{3.1}
\]

There are again `1,430` rows.  Under `(2.1)` and `(3.1)`, the developed
factor has a complete simple immediate-lower palette: every rank-eight set
occurs exactly once as an edge intersection.  This follows by the same free
orbit argument as Theorem 2.1.  Its point degree is automatically

\[
                         8\cdot1430=11440.           \tag{3.2}
\]

For a rank-ten orbit `B`, impose instead

\[
       1\le\sum_Q\#\{i:[U_i^{(2)}]=B\}\,x_Q\le2.    \tag{3.3}
\]

Since

\[
                  {1\over17}{17\choose10}=1144,     \tag{3.4}
\]

the `1,430` quotient occurrences in `(3.3)` force exactly

\[
                      286\text{ loads }2,
              \qquad  858\text{ loads }1.           \tag{3.5}
\]

After development, `(3.3)` is exactly complete immediate-upper support
with physical multiplicity at most two.  No additional point-balance row is
needed: translation development makes its point degree

\[
                        10\cdot1430=14300.           \tag{3.6}
\]

## 4. Sharp internal loads through `q3`

The orbit counts in the relevant ranks are

\[
\begin{array}{c|rrrrrrrrrrr}
r&5&6&7&8&9&10&11&12&13&14&15\\ \hline
{17\choose r}/17&364&728&1144&1430&1430&1144&728&364&140&40&8.
\end{array}                                                        \tag{4.1}
\]

Every selected depth has exactly ten occurrences per quotient column and
hence `1,430` occurrences in total.  Consequently the narrowest two-level
support ranges and their forced histograms are:

\[
\begin{array}{c|c|c}
\text{ticket}&\text{allowed loads}&\text{forced histogram}\\ \hline
L^{(2)},\ r=8&\{1\}&1430\times1\\
U^{(2)},\ r=10&\{1,2\}&858\times1, 286\times2\\
L^{(3)},\ r=7&\{1,2\}&858\times1, 286\times2\\
U^{(3)},\ r=11&\{1,2\}&26\times1, 702\times2\\
L^{(4)},\ r=6&\{1,2\}&26\times1, 702\times2\\
U^{(4)},\ r=12&\{3,4\}&26\times3, 338\times4.
                                                               \tag{4.2}
\end{array}
\]

For completeness, the longer internal upper windows have the analogous
balanced ranges

\[
\begin{array}{c|c|c}
r=13&\{10,11\}&110\times10, 30\times11\\
r=14&\{35,36\}&10\times35, 30\times36\\
r=15&\{170,180\}&1\times170, 7\times180.
                                                               \tag{4.3}
\end{array}
\]

The first two rows are the narrowest integer ranges allowed by the total
occurrence count.  The rank-fifteen row has an additional exact structural
constraint.  Once an interval has seen all ten active labels, all ten cyclic
starts have the same value `C union {s_0,...,s_9}`.  A selected quotient
column therefore contributes load ten to one rank-fifteen orbit.  The most
balanced possible distribution of 143 such column choices over eight target
orbits is consequently one load `170` and seven loads `180`, not the
unattainable scalar range `{178,179}`.  Formula `(4.3)` remains an occurrence
budget, not a claim that a chosen factor attains any displayed balanced
range.

Equivalently, a rank-fifteen orbit is the cyclic distance class
`delta in {1,...,8}` of the two labels omitted by `C union supp(sigma)`.
If `n_delta` selected columns omit a pair of distance `delta`, then its
rank-fifteen occurrence load is exactly `10 n_delta`.  Complete rank-fifteen
support is therefore the eight elementary inequalities `n_delta>=1`; the
balanced row of `(4.3)` is the histogram `n_delta in {17,18}`.

The lower rank-five intersection is different: every five-owner window of
one rail has the same core `C`.  Thus 143 selected quotient columns can use
at most 143 of the 364 core orbits.  The pure internal deck cannot by itself
cover all rank-five targets.  Any complete construction must obtain those
targets from the external strict-lower compiler, exactly as required by the
deadline architecture.

## 5. Finite typed master

The strongest direct quotient master suggested by the reduction is:

1. the `1,430` exact owner rows `(2.1)`;
2. the `1,430` exact lower-`q1` rows `(3.1)`;
3. the `1,144` upper-`q1` support/capacity rows `(3.3)`;
4. optionally, the four `q2/q3` support/capacity families in `(4.2)`; and
5. any protected reserve columns fixed in advance, with their occupied
   orbit rows deleted from the residual right side.

Every row is finite and translation invariant.  A certificate consists
only of the selected `(C,sigma)` columns; Theorems 2.1--3.1 then expand it
deterministically to the literal physical factor.

An owner-only solution proves overlapping-core positive factorization but
not typed occurrence alignment.  A solution of rows 1--3 proves the exact
owner/lower-`q1` factor and complete immediate-upper support.  Rows 4--5
are the direct route to coinstantiating the local q4 common reserve without
losing the already required typed tickets.

## 6. Exact remaining scope

This reduction removes neither chronology nor topology.  Translation
development initially produces seventeen copies of every selected base
rail, so the owner-only cover has `2,431` cycle components.  It still needs
literal resource-safe switches, residence, a connected nonzero-voltage
closure or equivalent fusion, external seam-current checks, and the three
terminal common-cap positions of an optimal `k=17` word.

What the reduction does prove is that overlapping-core positivity and the
first typed decks are not separate unstructured global problems: they are
one exact finite quotient cover on at most a few thousand rows.

## 7. H100 replay

The independent finite verifier enumerates all translation orbits in ranks
five through fifteen, checks freeness and point regularity orbit by orbit,
rebuilds every cyclic ticket in `(1.4)` including all wrap cases, verifies
the repeated rank-five and rank-fifteen structures, and checks every forced
histogram in `(4.2)--(4.3)`.  It does not search for a cover.

```text
scratch/verify_q4_k17_z17_translation_quotient_typed_factor_gate_20260814.py
SHA-256 186f01e3c8158ef854fac3bf4c5f2a2d532cc211bf9abe57657f772890c6694a

H100 output
scratch/verify_q4_k17_z17_translation_quotient_typed_factor_gate_20260814.h100.out
SHA-256 82b173f584825e54b170aa5a2b7f8d093e0ca5b031c6a5e96fd437241910187d
```

Exact output:

```text
PASS k=17 q=4 period=10 owner_orbits=1430 ticket_formulas=all_wraps orbit_counts=r5..15 rank15_hist=170x1+180x7
```

All enumeration, execution, and hashing ran through SSH on H100.  The local
Mac was used only for reading, editing, transfer, and Git.
