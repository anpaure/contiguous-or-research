# Direction phases and the cost of near-maximal geodesics

Date: 2026-09-07.  This note complements
`PHASE_DIRECTED_ADJACENT_SKELETON_20260907.md`.  It gives a quantitative
limitation of any construction which assigns each centered-square trace a
balanced direction phase.  It is not a lower bound for unrestricted OR
words, and it does not obstruct path-specific or mixed-support directions.

Put

\[
 W={2b\choose b},\qquad B_1={2b\choose {b-1}}={b\over b+1}W.
\]

## 1. Direction phases make traces geodesic

Fix a balanced split `Omega=P dotcup Q`.  Orient a Johnson edge from `S`
to `S-p+x` when `p in P cap S` and `x in Q setminus S`.  Along every
directed path the level `|S cap Q|` increases by one.  No deleted coordinate
can reappear and no inserted coordinate can later disappear.  Hence every
such path is geodesic and its antipodal fold is the middle trace of a
centered square pair.

Thus phase-labelled in/out slots are a valid local way to enforce
geodesicity.  The issue below is how many phases a near-extremal long-trace
cover needs.

## 2. The adjacent ledger forces near-maximal traces at fine accuracy

Consider centered square pairs of side lengths `1<=ell_i<=b`.  Write

\[
 M=2\sum_i\ell_i,\qquad t=\#\{i\}.
\]

Every pair has `2 ell_i` middle occurrences and exactly
`2(ell_i-1)` occurrences at each adjacent rank.  Therefore the total
adjacent occurrence volume is

\[
                         M-2t.                       \tag{1}
\]

Suppose the family misses `h` distinct rank-`b-1` targets.  Distinct
coverage is no larger than occurrence volume, so

\[
                         M-2t\ge B_1-h.              \tag{2}
\]

The optimal centered-square fractional charge for exact adjacent coverage
is

\[
 M_c={b\over b-1}B_1={b^2\over b^2-1}W,
 \qquad t_c={M_c\over2b}.
\]

Put `e=M-M_c` (which may be negative when `h>0`).  Equations (2) and
`M<=2bt` imply

\[
 {M\over2b}\le t\le t_c+{e+h\over2}.                \tag{3}
\]

More importantly, the total side deficiency satisfies the exact bound

\[
 \boxed{
 D:=\sum_i(b-\ell_i)=bt-{M\over2}
 \le {(b-1)e+bh\over2}.}                            \tag{4}
\]

Indeed, insert the upper bound for `t` from (2) and use
`(b-1)M_c=bB_1`.  The right side is automatically nonnegative whenever
such a family exists.

Consequently, if

\[
 |M-M_c|+h=o(W/b),                                  \tag{5}
\]

then `D=o(W)` and `t=(1+o(1))W/(2b)`.  Choose any
`delta_b -> 0` slowly enough that `D/(delta_b W)->0`.  At most
`D/(delta_b b)=o(t)` traces have side below `(1-delta_b)b`.  Thus all but
`o(t)` traces are near-maximal.  This conclusion uses only the adjacent
rank ledger; it assumes no randomness.

The scale in (5) is deliberately explicit.  An ordinary `o(W)` hole
statement is not strong enough to imply near-maximal sides.

## 3. Endpoint entropy forces exponentially many phases

Assume now that the middle traces are simple: no folded middle target occurs
in two traces.  Assign every trace a balanced phase in which it is directed
as in Section 1.

A phase-directed trace of side `ell` visits `ell` consecutive levels.  If
`ell>=(1-delta)b`, one endpoint has a representative `S` satisfying

\[
                  |S\cap Q|\le\delta b+1.           \tag{6}
\]

For one phase the number of possible folded endpoints in (6) is at most

\[
 N_\delta(b)=\sum_{r=0}^{\lfloor\delta b+1\rfloor}{b\choose r}^2. \tag{7}
\]

Simplicity makes these endpoints distinct among traces assigned to the
same phase.  Hence a catalogue of `q` phases supports at most
`q N_delta(b)` such long traces.

For fixed `0<delta<1/2`, the elementary entropy bound gives

\[
 \log_2N_\delta(b)\le2bH_2(\delta)+o(b),             \tag{8}
\]

where `H_2` is binary entropy.  Combining (5)--(8), any phase catalogue
supporting the resulting `(1-o(1))W/(2b)` near-maximal traces must satisfy

\[
 \boxed{
 \log_2q\ge2b\bigl(1-H_2(\delta_b)\bigr)-o(b).}      \tag{9}
\]

In particular, when `delta_b->0`, one needs
`q>=2^{(2-o(1))b}` phases.  A polynomial or subexponential direction
palette cannot realize this fine-accuracy regime.

At exact side `b` there is an even simpler statement.  A directed trace has
levels `0,...,b-1` or `1,...,b`, so it contains the folded antipodal target
`[P]=[Q]`.  Middle simplicity therefore permits at most one side-`b` trace
per phase, and exact side-`b` decompositions require at least
`W/(2b)` phases.

## 4. Scope and theorem-interface warning

The positive single-phase construction in the companion note remains
valid and gives geodesic components of diverging average length.  The
present result says that driving the adjacent error down to the much finer
scale (5) would force those components to be almost full-length and would
simultaneously destroy any small shared phase catalogue.

Bundling whole geodesics as hyperedges does not currently have a licensed
black-box matching step.  The standard Pippenger theorem used for the
four-uniform adjacent skeleton fixes the uniformity, whereas a
Gaussian-depth bundle has growing uniformity.  The conflict-free matching
theorem of Glock--Joos--Kim--Kuehn--Lichev
<https://arxiv.org/abs/2205.05564> also does not apply to the original
adjacent skeleton merely by declaring long bad histories as conflicts.  In
that skeleton `n=exp(Theta(b))`, `d=Theta(b^2)`, and
`Delta_2=Theta(b)`.  The theorem's codegree hypothesis permits at best
`epsilon=1/2+o(1)`, while its stated size hypothesis is
`n<=exp(d^(epsilon^3))`.  Even with fixed conflict size two, the right-hand
exponent is only `b^(1/4+o(1))`, much smaller than
`log n=Theta(b)`.  Moreover the theorem fixes the maximum conflict size,
so it does not directly encode a forbidden history whose length grows with
`b`.  This is a failure of a specific theorem's hypotheses, not a
nonexistence theorem for a tailored rounding argument.

The conclusions above concern centered-square traces carrying fixed
balanced direction phases and, in Section 3, a simple middle trace family.
They do not apply to unrestricted set-valued words, mixed-support
fragments, dynamically changing directions inside a trace, or a refinement
which splits and recombines columns.
