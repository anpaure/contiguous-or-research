# Sprinkled erosion forests and the multidepth splice barrier

## Verdict

The proved Johnson-path erosion transfer and the all-depth singleton
sprinkling construction combine into one exact theorem.  In even dimension
`n=2m`, let `W=C(2m,m)`.  If a family of vertex-disjoint middle-level paths
has `c` components, total two-sided shadow defect `M_q^-+M_q^+` through
depth `H`, and `rho_H` short internal coordinate runs, then

\[
\begin{aligned}
\nu(2m)\le{}&W+Hc+
 \sum_{q=1}^{H}(M_q^-+M_q^+)+(H^2+2H)\rho_H\\
&+(4m-2)T
 +2\sum_{q=H+1}^{m-1}N_q(1-2m/N_q)^T,
\end{aligned}
\tag{0.1}
\]

where `N_q=C(2m,m-q)` and `T>=1` is arbitrary.  Choosing

\[
 H=(1+o(1))\sqrt{m\log\log m}
\]

and a suitable `T=o(W/m)` makes the second line `o(W)`.  Consequently,
within this combined construction, it is sufficient to prove

\[
 Hc+
 \sum_{q=1}^{H}(M_q^-+M_q^+)
 +(H^2+2H)\rho_H=o(W).
\tag{0.2}
\]

This is a rigorous reduction, not a proof of coefficient one.  Neither the
current cyclic-strip cover, the depth-one rainbow forest, nor the current
fixed-radius queue packing supplies (0.2) at this depth.

There is also a precise reason that simply appending the all-depth blocks to
any of those three central constructions does not close the gap.  Under the
existing black-box accounting, the first rank below the controlled band is
completely absent, and filling that rank costs another `(1-o(1))W`.  Beating
this barrier requires deliberate use of intervals crossing block seams.

## 1. The even all-depth singleton block

Let `n=2m`, and let

\[
 \pi=(x_0,x_1,\ldots,x_{n-1})
\]

be a cyclic order.  Define

\[
 \mathcal S(\pi)=
 \{x_0\},\ldots,\{x_{n-1}\},
 \{x_0\},\ldots,\{x_{n-3}\}.
\tag{1.1}
\]

This is a literal nonzero OR word of length `2n-2=4m-2`.  Every proper
cyclic interval in `pi` is a contiguous union in (1.1).  The only boundary
case is the length-`n-1` interval beginning at `x_(n-1)`, and it is the
contiguous segment

\[
 \{x_{n-1}\},\{x_0\},\ldots,\{x_{n-3}\}.
\]

The first `n` entries have union `[n]`, so the full set is covered as well.
The empty set is not required.

For a uniformly random cyclic order modulo rotation, a fixed proper
`r`-set is a cyclic interval with probability exactly

\[
 \frac{r!(n-r)!}{(n-1)!}
 =\frac{n}{\binom nr}.
\tag{1.2}
\]

Thus `T` independent blocks leave a fixed rank-`r` target uncovered with
probability

\[
 \left(1-\frac n{\binom nr}\right)^T.
\tag{1.3}
\]

## 2. Erosion data for a middle-level path forest

Let `F` be a family of vertex-disjoint paths in the Johnson graph on the
rank-`m` sets.  Write `c` for its number of nonempty components.  For
`1<=q<=H`, let

\[
 \mathcal L_q(F)=
 \left\{\bigcap_{j=0}^{q}T_{i+j}:
          T_i,\ldots,T_{i+q}\text{ lie consecutively in one component}
 \right\},
\]

and define `\mathcal U_q(F)` analogously with unions.  Put

\[
 M_q^-=N_q-|\mathcal L_q(F)|,
 \qquad
 M_q^+=N_q-|\mathcal U_q(F)|.
\tag{2.1}
\]

Repeated values are counted only once in these supports.  Omitted middle
vertices are allowed; they are paid inside the baseline `W` below.

Let `rho_H` be the number of internal coordinate one-runs of lengths at most
`H` in the original path family.  Cut immediately before every such run.
The cut-repair erosion theorem gives a literal word covering every selected
middle vertex and every member of the supports in (2.1), with literal
completion cost at most

\[
 W+Hc+
 \sum_{q=1}^{H}(M_q^-+M_q^+)
 +(H^2+2H)\rho_H.
\tag{2.2}
\]

The last coefficient is exact.  A cut adds at most `H` erosion entries and
destroys at most `q` lower and `q` upper windows at each depth `q`, so

\[
 H+2\sum_{q=1}^{H}q=H^2+2H.
\]

## 3. Sprinkled erosion-forest theorem

**Theorem 3.1.**  For every family `F` as in Section 2, every
`1<=H<m`, and every integer `T>=1`, inequality (0.1) holds.

**Proof.**  Start with the literal erosion-and-repair word in (2.2).  Append
`T` all-depth blocks (1.1), choosing their cyclic orders independently and
uniformly for the moment.

For `H<q<m`, the lower and upper ranks have the same size

\[
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\]

By (1.3), the expected number of masks still missing at these two ranks is
at most

\[
 2N_q(1-2m/N_q)^T.
\]

Summing over `q`, some deterministic choice of the same `T` cyclic orders
has total outer defect at most the last sum in (0.1).  Append those remaining
masks literally.  The full set is already covered inside every block (1.1),
and ranks one and `2m-1` are included at `q=m-1`.  This proves (0.1).  \(\square\)

The expectation can also be derandomized by the usual conditional-expectation
potential; no independence is needed after the orders have been fixed.

## 4. The outer threshold

Put

\[
 \mu_q=\frac{W}{N_q}.
\]

Let `a_m->infinity` with

\[
 \log a_m=o(\log\log m),
\]

let `H` be the least depth for which

\[
 \mu_H\ge 3a_m\log m,
\tag{4.1}
\]

and take

\[
 T=\left\lceil\frac{W}{2ma_m}\right\rceil.
\tag{4.2}
\]

Uniformly for `q=O(sqrt(m log m))`,

\[
 \log\mu_q
 =\sum_{i=0}^{q-1}\log\frac{m+i+1}{m-i}
 =\frac{q^2}{m}+O\left(\frac{q^3}{m^2}+\frac qm\right).
\tag{4.3}
\]

Consequently

\[
 H=(1+o(1))\sqrt{m\log\log m}.
\tag{4.4}
\]

The singleton-block cost is

\[
 (4m-2)T\le \frac{2W}{a_m}+O(m)=o(W).
\tag{4.5}
\]

Since `mu_q` is increasing and `2mT/W>=1/a_m`, the expected outer defect is
at most

\[
 \begin{aligned}
 2\sum_{q=H+1}^{m-1}\frac{W}{\mu_q}
       \exp\left(-\frac{2mT}{W}\mu_q\right)
 &\le \frac{2mW}{\mu_H}\exp(-\mu_H/a_m)\\
 &=o(W)
 \end{aligned}
\tag{4.6}
\]

by (4.1).  Substituting (4.5)--(4.6) into Theorem 3.1 proves the sufficient
condition (0.2).

## 5. A black-box append barrier

The following statement is deliberately about a **block-preserving proof
architecture**, not about all possible OR words.

Suppose an inner word has no witness for any target in one rank of size `N`.
Append `T` intact singleton blocks (1.1), and then append `R` targets
literally.  If the proof credits only witnesses internal to the old word,
internal to one singleton block, or singleton literal witnesses, then one
block supplies at most `n` targets in the chosen rank.  Hence

\[
 nT+R\ge N.
\tag{5.1}
\]

The added word length satisfies

\[
 (2n-2)T+R\ge nT+R\ge N.
\tag{5.2}
\]

For a near-central rank, `N=(1-o(1))W`.  Therefore this black-box append
costs a second asymptotic baseline.

Intervals crossing the seams between blocks are excluded from this ledger.
They may help, but exploiting them is a new braid theorem rather than an
application of the existing sprinkling theorem.

### 5.1 Cyclic strips

In the even cyclic-strip construction through depth `J`, every literal entry
has rank `m-J`.  Every nonempty interval consequently has rank at least
`m-J`, so the word contains no rank-`m-J-1` target.  If `J=o(sqrt m)`, then

\[
 \binom{2m}{m-J-1}=(1-o(1))W.
\]

Equations (5.1)--(5.2) show that appending the existing all-depth sprinkling
completion to this word costs another `(1-o(1))W` under the black-box
accounting.

### 5.2 The depth-one rainbow word

Every entry in the proved depth-one rainbow-forest word has rank `m-1` or
`m`.  It therefore has no rank-`m-2` target.  Since

\[
 \binom{2m}{m-2}=(1-o(1))W,
\]

the same black-box append again costs another asymptotic baseline.

### 5.3 Fixed-radius queue words

One fixed-radius queue atom consists of a prefix of `2d` singleton entries
followed by cores of rank `m-d`.  In a concatenation of intact atoms, any
interval avoiding every core lies inside one singleton prefix and has rank at
most `2d`; every other interval has rank at least `m-d`.  If

\[
 m-d-1>2d,
\]

the complete inner word has no target of rank `m-d-1`.  For `d=o(sqrt m)`,
this rank has `(1-o(1))W` targets, so the same block-preserving append barrier
applies.

## 6. Exact erosion/splice conservation

Let

\[
 T_0,T_1,\ldots,T_{L-1}
\]

be a geodesic middle-level Johnson path, and let `1<=d<L`.  It has exactly
`L-q` consecutive windows of `q+1` vertices.  Hence endpoint-capped erosion
supplies exactly

\[
 L-q
\]

canonical lower `q`-windows and the same number of upper `q`-windows.  Its
literal erosion word has length `L+d`.

By comparison, a lossless fixed-radius queue atom supplies `L` advertised
masks in every signed depth and has word length `L+2d`.  The erosion word
saves `d` physical entries but loses `q` slots on each side at depth `q`.
The total slot loss is therefore

\[
 2\sum_{q=1}^{d}q=d(d+1).
\tag{6.1}
\]

Now join two path segments, each having more than `d` vertices, by one
Johnson edge.  At depth `q<=d`, exactly `q` new consecutive windows cross
the splice, on each of the lower and upper sides.  Thus one splice creates
exactly

\[
 2\sum_{q=1}^{d}q=d(d+1)
\tag{6.2}
\]

new shadow slots.  Slot counts therefore balance perfectly: the physical
`d`-entry saving is available only when a segment boundary is replaced by a
multidepth splice.

If `p` such segments are joined by a linear forest into `c` components, then
`p-c` splices recover `(p-c)d(d+1)` slots, leaving precisely

\[
 c\,d(d+1)
\tag{6.3}
\]

boundary slots relative to a lossless per-centre profile.  Equations
(6.1)--(6.3) count physical windows only.  They do not assert that the new
window labels are distinct or that they avoid the old labels.  Those are
the multidepth-rainbow conditions still missing.

## 7. The precise splice gate

The current queue theorem gives short, pairwise mask-disjoint geodesic
segments through a polylogarithmic depth.  To combine it with Theorem 3.1,
one must splice those segments into a final Johnson path forest `F` while
retaining their internal windows and controlling all new crossing windows.
At the threshold (4.4), the sufficient conditions are exactly

\[
 c=o(W/H),
\tag{7.1}
\]

\[
 \sum_{q=1}^{H}(M_q^-+M_q^+)=o(W),
\tag{7.2}
\]

and

\[
 \rho_H=o(W/H^2).
\tag{7.3}
\]

Condition (7.2) includes both the unresolved intermediate annulus and the
requirement that crossing windows replace the endpoint slots counted in
Section 6 without destructive label collisions.

For the explicit current queue segment length

\[
 L_0\asymp\sqrt{\frac{\log m}{\log\log m}},
\]

there are `p=(1+o(1))W/L_0` initial segments.  Condition (7.1) requires the
average final component to contain

\[
 \frac pc=\omega(H/L_0)
 =\omega\left(
   \frac{\sqrt m\,\log\log m}{\sqrt{\log m}}
  \right)
\tag{7.4}
\]

initial queue segments.  The presently proved depth-one rainbow forest has
only an unquantified `c=o(W)` component bound and does not imply (7.1).

## 8. Scope

Theorem 3.1 and its threshold corollary are unconditional.  The append
barrier in Section 5 is a theorem about the existing block-preserving
accounting, not a lower bound against constructions that exploit cross-seam
intervals.  The conservation law in Section 6 is an exact slot ledger, not a
distinct-colour theorem.

No coefficient-one construction is proved here.  The remaining new task is
an integral multidepth splice theorem: join almost all current queue segments
into very long Johnson paths, keep the total two-sided shadow support defect
`o(W)` through (4.4), and create only `o(W/H^2)` short coordinate runs.
