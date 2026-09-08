# Exact subcube run-credit envelope

## 1. Setup

Let `A=(A_1,...,A_n)` be a zero-free universal contiguous-OR word on
`[k]`.  Fix `r`, put

\[
M=\binom kr,\qquad d=n-M\ge1,
\]

and, for each `R in binom([k],r)`, set

\[
P_R=\{i:A_i\subseteq R\},\qquad p_R=|P_R|.
\]

The containment-multiplicity theorem implies that every run of `P_R` has
length at most `d+1`.  Let `q_R` be the number of its runs of length `d+1`;
equivalently, the number of physical length-`d+1` intervals whose OR is
exactly `R`.

For `1<=ell<=d+1`, define

\[
f_d(\ell)=\sum_{j=1}^{d}(\ell-j+1)_+.
\]

This is the exact number of intervals of length at most `d` contained in a
run of length `ell`.

## 2. Exact capacity envelope

For integers `p,q>=0`, define

\[
F_d(p,q)=\max\left\{
  \sum_t f_d(\ell_t):
  \sum_t\ell_t=p,
  1\le\ell_t\le d+1,
  |\{t:\ell_t=d+1\}|=q
\right\},
\]

with value `-infinity` when no such partition exists.  Define the exact
credit function

\[
\gamma_{r,d}(p)=\min\left\{q\ge0:
 F_d(p,q)\ge 2^r-2+\mathbf1_{\{q=0\}}
\right\},                                                    \tag{2.1}
\]

and put `gamma=+infinity` when the set is empty.

### Theorem 2.1 (exact run-credit theorem)

Every universal word in the setup above satisfies

\[
\boxed{q_R\ge\gamma_{r,d}(p_R)\quad\text{for every }R,}     \tag{2.2}
\]

and consequently

\[
\boxed{
 \sum_{R\in\binom{[k]}r}\gamma_{r,d}(p_R)\le\binom kr.}     \tag{2.3}
\]

Let

\[
L=\sum_{s=1}^{r-1}\binom ks,
\qquad
\sigma=dM+\binom{d+1}{2}-L                              \tag{2.4}
\]

be the residual number of width-`d` short-band cells after one witness for
every lower-rank target is selected.  Then the second, independent credit
budget is

\[
\boxed{
 \sum_R(\gamma_{r,d}(p_R)-1)_+\le\sigma.}                  \tag{2.5}
\]

#### Proof

Write the `P_R`-run lengths as `ell_1,...,ell_t`.  Every nonempty proper
subset of `R` has OR-rank below `r`, hence has a witness of length at most
`d`, wholly inside one of these runs.  The witnesses of the `2^r-2` proper
targets are different physical intervals.  Therefore

\[
\sum_t f_d(\ell_t)\ge2^r-2.                                \tag{2.6}
\]

If `q_R=0`, no length-`d+1` interval has OR `R`; the containment theorem then
forces a witness for `R` itself to have length at most `d`.  This adds one
more distinct required short interval, so the right side of (2.4) is
`2^r-1`.

The actual run partition is feasible in the maximization defining
`F_d(p_R,q_R)`.  Hence

\[
F_d(p_R,q_R)\ge2^r-2+\mathbf1_{\{q_R=0\}},
\]

which is exactly (2.2).

There are `n-d=M` physical intervals of length `d+1`.  Every one has
OR-rank at least `r`; a rank-`r` interval contributes to exactly one `q_R`
and a higher-rank interval contributes to none.  Thus `sum_R q_R<=M`.
Summing (2.2) proves (2.3).  QED.

To prove (2.5), let `z=|{R:q_R=0}|`, let `H` be the number of physical
length-`d+1` windows having rank greater than `r`, and put

\[
D=\sum_R(q_R-1)_+.
\]

There are `M-H` rank-`r` long windows and `M-z` distinct `r`-sets occurring
among them, so exact multiplicity accounting gives

\[
D=(M-H)-(M-z)=z-H\le z.                                  \tag{2.7}
\]

Every one of the `z` missing long-row targets must use a distinct witness of
length at most `d`.  Such a rank-`r` interval is not among the selected
lower-rank witnesses, so it occupies one of the `sigma` residual short-band
cells.  Hence `z<=sigma`.  Finally, (2.2) gives

\[
(\gamma_{r,d}(p_R)-1)_+\le(q_R-1)_+.
\]

Summing and applying (2.6) proves (2.5).

The earlier linear deficiency law

\[
\sum_R(c_{r,d}-p_R)_+\le M
\]

is a relaxation of (2.3): it replaces the exact integer run envelope by one
supporting line.  Equation (2.3) can therefore be strictly stronger even
when both give the same minimum first moment.

## 3. Closed evaluation for `d=3`

In fact the capacity envelope has a closed form for every `d`.  Fix `p,q`
and write

\[
s=p-q(d+1)=ad+b,\qquad 0\le b<d.
\]

If `s<0`, the pair `(p,q)` is infeasible.  Otherwise

\[
\boxed{
F_d(p,q)=q\frac{d(d+3)}2+a\frac{d(d+1)}2+\frac{b(b+1)}2.} \tag{3.1}
\]

Indeed, after the prescribed `q` runs of length `d+1` are removed, every
remaining part is at most `d` and has value `f_d(ell)=ell(ell+1)/2`.
Convexity shows that transferring one unit from a smaller nonzero part to a
larger part weakly increases the sum.  Repeating this operation leaves `a`
parts of length `d` and one part of length `b`, proving (3.1).

For `d=3`,

\[
f_3(1)=1,\quad f_3(2)=3,\quad f_3(3)=6,\quad f_3(4)=9.
\]

At fixed `p,q`, after the `q` four-runs are removed, capacity is maximized by
using as many three-runs as possible and one residual run.  If

\[
s=p-4q=3a+b,\qquad 0\le b<3,
\]

then

\[
F_3(p,q)=9q+6a+\binom{b+1}{2},                              \tag{3.2}
\]

provided `0<=q<=floor(p/4)`; when `q=0` there are, by definition, no
four-runs.

## 4. The exact `k=11` deficiency law

For `k=11,n=465,r=6`, one has `M=462`, `d=3`, and every six-set support
already satisfies `p_U>=28`.  Equations (2.1) and (3.2) give

\[
\begin{array}{c|ccccc}
p&28&29&30&31&\ge32\\ \hline
\gamma_{6,3}(p)&7&5&3&1&0.
\end{array}                                                \tag{4.1}
\]

For example, at `p=28` six four-runs leave four positions, whose best legal
split is `3+1`; this supplies only

\[
6\cdot9+6+1=61
\]

short intervals, fewer than the 62 proper targets.  Seven four-runs supply
63.  The other three entries of (4.1) follow identically.

Writing

\[
a_j=|\{U\in\binom{[11]}6:p_U=j\}|,
\]

Theorem 2.1 yields the strictly stronger distributional cut

\[
\boxed{7a_{28}+5a_{29}+3a_{30}+a_{31}\le462.}              \tag{4.2}
\]

Here `sigma=369`, so the residual budget (2.5) also gives

\[
\boxed{6a_{28}+4a_{29}+2a_{30}\le369.}                    \tag{4.3}
\]

In particular,

\[
a_{28}\le61,\qquad
|\{U:p_U\le29\}|\le92,\qquad
|\{U:p_U\le30\}|\le154.                                  \tag{4.4}
\]

The previous linear-credit theorem gave coefficients `4,3,2,1` and bounds
`115,154,231`.  Thus (4.2) contains genuinely more individual-subcube
information, although its best aggregate first-moment consequence remains
`sum_U p_U>=31*462`.

## 5. Scope

### Boundary--core strengthening at `k=11`

The same exact envelope applies inside the boundary--core decomposition.
Every proper subset of a six-set has its witness wholly in the rank-at-most-
five core, so the core runs must supply all 62 proper targets regardless of
whether the six-set itself is a literal boundary entry.  Formally this uses
the proper-subset credit function

\[
\eta_{r,d}(p)=\min\{q:F_d(p,q)\ge2^r-2\},
\]

rather than `gamma`, whose `q=0` branch also charges `R` itself.  For
`r=6,d=3` and `28<=p<=32`, both functions have the same values
`7,5,3,1,0`.  If `p_U^C` is the core support and
`a_j^C=|{U:p_U^C=j}|`, then

\[
7a_{28}^C+5a_{29}^C+3a_{30}^C+a_{31}^C
 \le 462-h_6,                                             \tag{5.1}
\]

where `h_6` is the number of literal six-set boundary entries.  Boundary
rigidity gives `h_6 in {0,1}`.  Thus the two unrestricted branches satisfy

\[
\begin{array}{ll}
h_6=0:&7a_{28}+5a_{29}+3a_{30}+a_{31}\le462,\\[2mm]
h_6=1:&7a_{28}^C+5a_{29}^C+3a_{30}^C+a_{31}^C\le461.
\end{array}                                               \tag{5.2}
\]

Unlike a linearized interface-credit inequality, (5.2) needs no exception
for the boundary value at core support 31: zero long core runs can supply at
most 61 short intervals on 31 support positions, so one core length-four run
is still forced solely by its 62 proper subsets.

The theorem is unrestricted: it assumes no fixed derivative row, Johnson
path, grading, or prescribed witnesses beyond the standard equal-rank
antichain selection used for the containment cap.  It remains a necessary
condition.  It does not by itself construct a word or exclude length 465.

The next non-scalar step is to combine (2.3) with the exact nesting

\[
P_R\cap P_S=P_{R\cap S}
\]

and with coordinate pin survival.  Treating the `p_R` independently would
again discard the ordered geometry that the theorem exposes.
