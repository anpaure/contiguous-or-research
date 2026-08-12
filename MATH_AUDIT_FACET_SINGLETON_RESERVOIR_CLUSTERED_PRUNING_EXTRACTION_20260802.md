# Independent audit: singleton-reservoir clustered pruning

Date: 2026-08-02  
Audit target: Section 9 of
`MATH_THEOREM_FACET_FIXED_BASE_COLLISION_TENSOR_AND_WHOLE_FRAME_NOGO_20260802.md`  
Verdict: **GO** for the stated owner/named-target packing theorem.  The
source/buffer and chronology exclusions are necessary and correctly stated.

## 0. Audited claim

In the canonical range put

\[
 Q=q+1,\qquad n=k-Q,\qquad a_0=c-1=r-q,
 \qquad M_1=\binom n{a_0}.
\]

A singleton-base frame has support

\[
 A=\{\beta\}\dot\cup V,\qquad |A|=Q,
\]

and one module for every `X in binom([k]-A,a_0)`.  The audited theorem
samples `Theta(2^q/q^2)` such frames and deletes every module occurrence
which has any owner or named-target collision with another sampled frame.
It claims that `Omega(W/q^2)` modules remain.

The proof is valid.  The central saving is exactly one factor `q`: one
whole occurrence of a second frame fixes one trace of `X` on the
second-only support, regardless of which first-frame occurrence supplied
the equality.

## 1. Literal cylinder normalization

For one first-frame module `X`, every resource in its complete named deck
has the form

\[
                         S=X\dot\cup R,                    \tag{1.1}
\]

where `R subseteq A` is one of the following occurrence footprints:

\[
 \{w\},\quad \{\beta,h\},\quad
 \{\beta\}\cup J\ (2\le |J|\le q-2),\quad
 A-\{v\}.                                                \tag{1.2}
\]

These are respectively the primitive `P`, primitive `H`, all cyclic high
targets, and all owners.  Their total occurrence count is

\[
                  L=1+1+q(q-3)+q=q^2-2q+2.               \tag{1.3}
\]

The same representation holds in a second frame with support `A'`, module
index `X'`, and footprint `R' subseteq A'`.  Since `X' cap A'=empty`, an
equality `X union R=X' union R'` necessarily satisfies

\[
                         (X\cup R)\cap A'=R'.              \tag{1.4}
\]

Put `E=A'-A`.  Because `E cap A=empty`, restricting (1.4) gives the exact
trace condition

\[
                         X\cap E=R'\cap E.                 \tag{1.5}
\]

There is an additional compatibility condition on `A cap A'`, and equality
also forces the two resources to have the same rank.  Dropping either
condition only enlarges the counted bad set, so the theorem's upper bound
is proof-safe.

Most importantly, after `R'` is fixed, changing the first footprint `R`
does not change (1.5).  Thus union bounding over the `L` second-frame
occurrences is complete; multiplying by another `L` (or even another `q`)
would be an overcount, not a missing factor.

## 2. Exact trace count and its uniform bound

Let

\[
                         b=|E|,qquad T=R'\cap E,quad t=|T|.
\]

Exactly

\[
                         \binom{n-b}{a_0-t}                \tag{2.1}
\]

first-frame module indices have trace `X cap E=T`.  Therefore

\[
 B({\cal R},{\cal R}')
 \le\sum_{R'}\binom{n-b}{a_0-|R'\cap E|}.                \tag{2.2}
\]

After division by `M_1`, one summand is exactly the probability that a
uniform `a_0`-subset of an `n`-set has one prescribed binary trace on a
fixed `b`-set:

\[
 {\binom{n-b}{a_0-t}\over\binom n{a_0}}
 ={(a_0)_t(n-a_0)_{b-t}\over(n)_b}.                      \tag{2.3}
\]

Here `a_0/n=1/2+O(1/q)` and `b<=q+1`.  Consequently

\[
 {\binom{n-b}{a_0-t}\over\binom n{a_0}}
 \le 2^{-b}\exp(O(b/q+b^2/n))
 \le C_0 2^{-b},                                        \tag{2.4}
\]

with an absolute `C_0`, uniformly in the supports, overlap, row, and trace.
This verifies that the constant in the main proof does not depend on `k`
or on an occurrence type.

## 3. Support-overlap moment

For independent uniform `Q`-sets `A,A'`, let `Z=|A cap A'|`.  Since
`b=Q-Z`, the required moment is

\[
 \mathbb E 2^{-b}=2^{-Q}\mathbb E2^Z.                    \tag{3.1}
\]

The subset expansion gives the exact identity

\[
 \mathbb E2^Z
 =\sum_{t=0}^{Q}\binom Qt{(Q)_t\over(k)_t}.              \tag{3.2}
\]

Termwise,

\[
 \binom Qt{(Q)_t\over(k)_t}
 \le {1\over t!}\left({Q^2\over k-Q+1}\right)^t.
\]

Thus

\[
 \mathbb E2^Z\le
 \exp\left({Q^2\over k-Q+1}\right)=O(1),                \tag{3.3}
\]

because `Q^2/k=Theta(1)` canonically.  No independence approximation for
the individual support coordinates is used.

Combining (1.3), (2.2), (2.4), and (3.3) yields

\[
 \mathbb E B({\cal R},{\cal R}')
       \le C_1 M_1 {q^2\over2^q}                         \tag{3.4}
\]

for an absolute `C_1`.

## 4. Deletion accounting

Sample independently

\[
                         R_0=\left\lfloor
                 {2^q\over4C_1q^2}\right\rfloor          \tag{4.1}
\]

frames.  Let `Z_bad` be the number of module occurrences which collide
with at least one occurrence in another sampled frame.  Counting an
occurrence once for every opposing frame can only overcount, so

\[
 Z_{bad}\le\sum_{i\ne j}B({\cal R}_i,{\cal R}_j).         \tag{4.2}
\]

Using (3.4),

\[
 \mathbb E Z_{bad}
 \le R_0(R_0-1)C_1M_1{q^2\over2^q}
 \le {R_0M_1\over4}.                                    \tag{4.3}
\]

Hence some outcome retains at least `3R_0M_1/4` good module occurrences.
Two retained modules in different frames cannot share a resource, because
that would have made both bad.  Internal frame simplicity handles modules
from the same frame.  Duplicate sampled supports or frames are harmless:
their coincident modules are simply bad under the same definition.

Finally, the independently proved sharp asymptotic

\[
                         M_1\sim
       2^{-(q+1)}e^{-\pi/16}W                           \tag{4.4}
\]

turns (4.1)--(4.3) into

\[
                         {3R_0M_1\over4}=\Omega(W/q^2). \tag{4.5}
\]

The leading constant may be reduced arbitrarily by sampling fewer frames,
and surplus modules may be discarded.  The proof does not assert an
arbitrary prescribed leading constant near the scalar ceiling.

## 5. Weighted protected-bank extension

The same experiment gives a protected-bank version which was not needed in
the main theorem.  Choose the support, base point, cyclic order, and the two
low tags from a distribution invariant under `Sym([k])`.  Let

\[
 {cal D}_u\subseteq\binom{[k]}u
\]

be a preused or forbidden bank at every resource rank, and define

\[
 \Psi({\cal D})=
 { |{cal D}_c|\over\binom{k}{c}}
 +{ |{cal D}_{c+1}|\over\binom{k}{c+1}}
 +q\sum_{j=2}^{q-2}{|{cal D}_{c+j}|\over\binom{k}{c+j}}
 +q{|{cal D}_r|\over W}.                                \tag{5.1}
\]

### Corollary 5.1 (weighted robust clustered pruning)

For every fixed `psi<1`, if `Psi(D)<=psi`, then the sampling constant in
(4.1) can be chosen so that clustered pruning, followed by deletion of
every module meeting `D`, still leaves `Omega(W/q^2)` pairwise
resource-disjoint modules avoiding `D`.

### Proof

One full singleton reservoir has exactly `M_1` resources at ranks `c` and
`c+1`, and exactly `qM_1` resources at every high rank and at the owner
rank.  By permutation invariance, a fixed rank-`u` resource has the same
probability of appearing as every other resource of that rank.  Therefore
the expected number of incidences between one random reservoir and the
forbidden bank is exactly

\[
                         M_1\Psi({\cal D}).                  \tag{5.2}
\]

Inside one reservoir every named resource belongs to a unique module, so
the number of modules killed by the bank is at most the incidence count.
For `R_0` sampled reservoirs its expectation is at most
`R_0M_1 psi`.

In (4.1), replace the constant `1/(4C_1)` by any sufficiently small
positive constant `epsilon` satisfying

\[
                         \epsilon C_1+\psi<1.               \tag{5.3}
\]

The expected cross-frame deletion fraction is at most `epsilon C_1`, while
the bank deletion fraction is at most `psi`.  Some outcome therefore leaves
a positive constant fraction of `R_0M_1=Theta(W/q^2)` modules.  Deleting
bank incidences cannot create a new collision. \(\square\)

This extension requires a weighted-small forbidden bank.  It makes no
claim for `Psi>=1`, even if the raw cardinality of the bank looks small in
an unweighted aggregate.

## 6. Exact aggregate occurrence reservation

The selected modules do not require an additional matching to create their
own local source occurrences: every retained module already comes with the
literal length-`q=d+2` cycle from the sharp buffered one-copy theorem.  It
contains one `P`, one distinguished primitive `H`, and `d` short-buffer
`H` occurrences.  Thus its aggregate age-signature vector is exactly

\[
                         e_{d+1}+(q-1)e_{d-1}.              \tag{6.1}
\]

There is nevertheless a real residual-inventory condition.  Let
`A=(A_0,...,A_(r-1))` be the canonical Ferrers age-signature vector, put

\[
 E=L-H,
 \qquad {cal Q}=Q_{r,d}
\]

for the resource slack and conductor quantum in the aggregate semigroup
theorem, and define

\[
 T_{\rm sock}=\min\left\{
 A_{d+1}-{cal Q}-1,
 \left\lfloor{A_{d-1}-{cal Q}-1\over q-1}\right\rfloor,
 \left\lfloor{E\over d}\right\rfloor
 \right\}.                                                \tag{6.2}
\]

Negative entries make `T_sock` zero.

### Corollary 6.1 (aggregate socket reservation)

Assume `d>=4`, `d+1<r`, and the unchanged coordinates satisfy

\[
 A_{d-3},A_{d-2}\ge{cal Q}+1.                            \tag{6.3}
\]

Then every integer `0<=t<=T_sock` can be reserved for `t` literal buffered
facet modules, and the residual age-signature vector still has an exact
integral short/long/mixed rotor decomposition.

### Proof

Subtract the `t` module vectors:

\[
 A'=A-t e_{d+1}-(q-1)t e_{d-1}.                          \tag{6.4}
\]

Its total occurrence mass is `W-qt`.  The low-minus-high resource slack is

\[
                         E'=E-dt\ge0,                     \tag{6.5}
\]

because one primitive pair is balanced and its `d` short buffers each
contribute one low unit.  Definition (6.2) gives

\[
 A'_{d-1},A'_{d+1}\ge{cal Q}+1,
\]

while (6.3) supplies the other two coordinates.  The exact buffered
semigroup criterion applies to `A'`, proving the residual decomposition.
Restoring the `t` explicit literal module cycles gives the original vector
`A`. \(\square\)

For the canonical vector, the aggregate semigroup theorem proves (6.3)
for all sufficiently large dimensions (and checks the finite conductor
range separately).  Also

\[
 {q^2\over W}{A_{d-1}\over q-1}
 \longrightarrow {\pi\over2}e^{-\pi/4}>0.               \tag{6.6}
\]

Therefore the two coordinate rows in (6.2) permit a sufficiently small
constant multiple of `W/q^2`.  The independent slack row may not: if
`E=o(W/q)`, and in particular if `E=0`, this specific one-primitive
buffered family cannot occur at order `W/q^2`.  Random support pruning
cannot repair that scalar obstruction.  One must then use an unbuffered
multi-primitive cycle or another role package.

Corollary 6.1 is an aggregate occurrence theorem, not a physical-position
embedding.  Coordinate relabelling is transitive on named subsets, which is
why Section 5 admits a weighted forbidden-bank calculation.  It is not
transitive on the positions, predecessor/successor arcs, or component
ports of a fixed chronology.  Randomizing frame supports leaves those
positional constraints unchanged.  Hence no analogous density-only formula
can reserve physical sockets without an additional host distribution or a
literal fusion/embedding theorem.

## 7. Exact scope

The audit verifies simultaneous distinctness of exactly these actual named
resources:

* all rank-`r` owners;
* the primitive targets at ranks `c` and `c+1`;
* all `q` cyclic targets at each rank `c+2,...,r-1`.

It does **not** allocate the separate source-occurrence rows.  In
particular, every retained module still requires one primitive `P`, one
primitive `H`, and `d` short `H` buffers, subject to

\[
 t\le A_{d+1},\qquad (q-1)t\le A_{d-1},\qquad
 dt\le L-H.                                               \tag{7.1}
\]

Nor does it serialize the component cycles, establish arbitrary exterior
upper shadows, global residence, protected pins, or compiler/common-cap
feasibility.  Corollary 5.1 handles a preused named-resource bank only when
its exact weighted load is bounded away from one; it does not protect
physical positions or later compiler incidences.  Corollary 6.1 reserves
aggregate occurrence types with conductor margin, but does not embed or
fuse their positions in one chronology.

Therefore the audited theorem closes the previously missing
owner/named-target **order-of-magnitude packing gate**, but it is not by
itself a construction of a universal OR word or a proof of
`nu(k)=B(k)+O(1)`.
