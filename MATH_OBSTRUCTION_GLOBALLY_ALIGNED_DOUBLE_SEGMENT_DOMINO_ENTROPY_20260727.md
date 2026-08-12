# Globally aligned domino bad segments: the double-segment entropy obstruction

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver,
probabilistic black box, or web input is used.

Local inputs audited:

- `MATH_THEOREM_MACRO_OVERLAP_QUARANTINE_BY_CONFLICT_THINNING_20260727.md`;
- `MATH_AUDIT_DOMINO_TWIN_SLOW_BITE_TILTED_SPECTRUM_AND_HEREDITY_GATE_20260727.md`;
- `MATH_THEOREM_DOMINO_TWIN_FACTORIAL_OVERLAP_BOUND_20260727.md`; and
- `MATH_THEOREM_ANNULAR_PACKET_COMMON_INTERVAL_ENERGY_AND_PAIR_GADGET_GATE_20260727.md`.

## 0. Outcome

Put

\[
 n=2m,\qquad R=2r+1=m-q_0,
 \qquad h:=m-2r=q_0+1.
\tag{0.1}
\]

At the Gaussian annulus, \(h=\Theta(\sqrt m)\).  A simple domino-twin
packet is the disjoint union of \(m\) four-target cells indexed by a
cyclic domino necklace.  If two packets miss at most \(s=o(m)\) common
targets, the existing alignment theorem puts all complete common cells
at the same global indices.  The remaining inverse count cannot,
however, have a uniform entropy coefficient below \(1/2\).

### Theorem A (two independently repartitioned aligned segments)

Fix one packet.  Choose two length-\(\ell\) domino segments whose initial
indices differ by \(r\), and independently repartition the labels inside
each segment into an ordered list of unordered dominoes.  If

\[
 1\ll\ell,\qquad \ell+h<r,
\tag{0.2}
\]

then the resulting family has at least

\[
 \boxed{
 {1\over2m}\left({(2\ell)!\over2^\ell}\right)^2}
\tag{0.3}
\]

distinct simple packet supports.  Every member shares at least

\[
 K-4b_\ell
 \quad\text{targets with the original packet},
 \qquad K=4m,
\tag{0.4}
\]

where

\[
 \boxed{
 b_\ell\le
 2(\ell-1)+\min\{\ell-1,h\}+4.}
\tag{0.5}
\]

Thus all these packets lie in the conflict neighbourhood
\(\Gamma_{s_\ell}\), with

\[
 \boxed{
 s_\ell=8\ell+4\min\{\ell,h\}+O(1).}
\tag{0.6}
\]

Their logarithmic entropy is

\[
 \boxed{
 \log |{\cal F}_\ell|=4\ell\log\ell+O(\ell+\log m).}
\tag{0.7}
\]

Consequently the effective power coefficient is

\[
 c_\ell=
 {4\ell\over8\ell+4\min\{\ell,h\}}+o(1)
 = {1\over 2+\min\{1,h/\ell\}}+o(1).
\tag{0.8}
\]

It equals \(1/3+o(1)\) for \(\ell\le h\), and tends to \(1/2\) when
\(\ell/h\to\infty\).

### Corollary B (the desired uniform inverse exponent is false)

No estimate uniform for \(s=o(m)\) of the form

\[
 \#\{G:|F\cap G|\ge K-s\}
 \le \exp(O(m))m^{cs}
\tag{0.9}
\]

can hold with a fixed \(c<1/2\).  Indeed take

\[
                         \ell={m\over\sqrt{\log m}}.
\tag{0.10}
\]

Then \(h=o(\ell)=o(m)\), the \(O(m)\) term in (0.9) is negligible,
and (0.3)--(0.8) force \(c\ge1/2-o(1)\).

In particular, the proposed targets \(c=1/3\) and
\(c=1/4+o(1)\) are false for the globally aligned packet family.  The
one-contiguous-segment construction giving \(1/4\) is sharp only when a
single bad-front pair is allowed.  It is not sharp after two segments
at the natural displacement \(r\) are independently active.

This obstruction is at exactly the survivor threshold \(c=1/2\).  It
does not by itself refute a bound specialized to
\(s=Cm/\log m\) with a sufficiently explicit \(\exp(C_0m)\) constant,
because at that scale both the double-segment entropy and the prefactor
are exponential in \(m\).  It does refute the sought uniform
power-saving inverse theorem and the proposed terminal comparison based
only on raw missing-target count.

## 1. Domino cells and global alignment

Let

\[
                         B_0,B_1,\ldots,B_{m-1}
\tag{1.1}
\]

be the cyclic list of unordered dominoes of a fixed simple twin packet,
with indices in \(\mathbb Z_m\).  Put

\[
 A_i=B_i\cup B_{i+1}\cup\cdots\cup B_{i+r-1}.
\tag{1.2}
\]

Its \(i\)-th four-target cell is

\[
 {\cal S}_i
 =\{A_i\cup\{x\}:x\in B_{i-1}\cup B_{i+r}\}.
\tag{1.3}
\]

The cells are disjoint and exhaust the \(K=4m\) targets.  Equality of
a complete cell in two packets recovers its core \(A_i\), its boundary
four-set, and its intrinsic cyclic index relative to every adjacent
complete cell.  The global alignment theorem in the source note then
shows that, after one dihedral alignment, every complete common cell of
two packets with \(o(m)\) missing targets has the same index.

The construction below is already presented in this globally aligned
normal form.  Thus it does not exploit independent rotations or
reflections of separate good runs.

## 2. Two segments at the core length displacement

Fix the two cyclic position intervals

\[
 I=\{0,1,\ldots,\ell-1\},
 \qquad
 J=I+r=\{r,r+1,\ldots,r+\ell-1\}.
\tag{2.1}
\]

Condition (0.2) makes them disjoint and keeps every interval calculation
below away from wraparound ambiguities.  Keep every domino outside
\(I\cup J\) fixed.  Independently do the following on \(I\) and on
\(J\): take the \(2\ell\) labels originally occupying the segment and
partition them arbitrarily into an ordered list of \(\ell\) unordered
dominoes.

One segment has

\[
                         N_\ell={(2\ell)!\over2^\ell}
\tag{2.2}
\]

ordered repartitions, so the labelled necklace count is \(N_\ell^2\).
A simple twin support recovers its unordered domino partition and cyclic
domino order.  Therefore only the global dihedral group, of size at most
\(2m\), can identify two members.  This proves (0.3).

The two choices are genuinely independent: their label sets are
disjoint, and no quotient operation exchanges labels between the two
segments.

## 3. Exact union of the bad core fronts

For a set of domino positions \(Q\), an \(r\)-core can change only when
its position interval meets \(Q\) nontrivially but does not contain all
of \(Q\).  For the segment \(I\), put

\[
                         L=\{1,2,\ldots,\ell-1\}.
\tag{3.1}
\]

The possibly changed core starts are exactly contained in

\[
                         L\cup(L-r).
\tag{3.2}
\]

The first band consists of cores whose left boundary cuts \(I\); the
second consists of cores whose right boundary cuts \(I\).  Translating
the segment by \(r\) gives

\[
                         (L+r)\cup L
\tag{3.3}
\]

for \(J\).  Hence the union of all possibly changed core starts is

\[
                         L\cup(L-r)\cup(L+r).
\tag{3.4}
\]

The first band is disjoint from the two remote bands under (0.2).  The
remote bands have length \(\ell-1\), and their relative displacement is

\[
                         2r\equiv-h\pmod m.
\tag{3.5}
\]

Therefore

\[
 \boxed{
 |L\cup(L-r)\cup(L+r)|
 =2(\ell-1)+\min\{\ell-1,h\}.}
\tag{3.6}
\]

This is the decisive overlap.  If \(2r=m\), the two remote fronts would
coincide exactly.  At the annulus they are separated only by
\(h=q_0+1=\Theta(\sqrt m)\), so long segments make them coincide up to
an \(O(h)\) fringe.

## 4. Boundary-only exceptional cells

It remains to count cells whose core contains all or none of a modified
segment but whose boundary four-set meets it.  For one segment there are
at most two:

1. the cell immediately after the segment, whose left boundary domino
   is the final modified domino; and
2. the cell whose right boundary domino is the first modified domino
   while its core ends immediately before the segment.

Thus two segments contribute at most four additional possibly changed
cells.  Every cell outside the set counted by (3.6) and these four
exceptions has both:

- the same core, because it contains all or none of each independently
  repartitioned label set; and
- the same boundary dominoes, because both boundary positions avoid the
  modified segments.

It is therefore literally the same complete four-target cell.  This
proves (0.5).

Since the cells of the original packet are disjoint, at most four
original targets are lost per possibly changed cell.  Consequently

\[
 |F\cap G|\ge K-4b_\ell.
\tag{4.1}
\]

Taking \(s_\ell=4b_\ell+1\) gives strict conflict adjacency and proves
(0.4)--(0.6).

## 5. Entropy coefficient

Stirling's formula gives

\[
 \begin{aligned}
 \log |{\cal F}_\ell|
 &\ge2\left(\log(2\ell)!-\ell\log2\right)-\log(2m)\\
 &=4\ell\log\ell+O(\ell+\log m).
 \end{aligned}
\tag{5.1}
\]

Combining this with (0.6) proves (0.8).  There are three regimes.

### 5.1 Short segments: \(\ell\le h\)

All three bad-front bands in (3.4) are essentially disjoint.  Thus

\[
                         s_\ell=12\ell+O(1),
 \qquad c_\ell={1\over3}+o(1).
\tag{5.2}
\]

This realizes the proposed \(1/3\) coefficient as a lower bound, not an
upper theorem.

### 5.2 Long sublinear segments: \(h=o(\ell)=o(m)\)

The two remote fronts overlap in all but \(O(h)\) positions.  Hence

\[
                         s_\ell=8\ell+4h+O(1),
 \qquad c_\ell={1\over2}-O(h/\ell).
\tag{5.3}
\]

Taking (0.10) makes \(s_\ell=o(m)\), while

\[
 \log |{\cal F}_\ell|
 =(4+o(1))m\sqrt{\log m},
\]

\[
 s_\ell\log m=(8+o(1))m\sqrt{\log m}.
\tag{5.4}
\]

The \(\exp(O(m))\) factor is negligible, proving Corollary B.

### 5.3 The critical terminal scale

For \(\ell=Cm/\log m\), one still has \(\ell/h\to\infty\) and the
formal coefficient tends to \(1/2\), but both
\(\log|{\cal F}_\ell|\) and an unspecified \(O(m)\) prefactor are of
order \(m\).  Thus this family does not determine the sharp additive
constant at that single scale.  Any terminal-scale rescue must expose
that constant; a statement with an opaque \(\exp(O(m))\) term cannot do
so.

## 6. Why the one-segment \(1/4\) family is not sharp

With only the segment \(I\), the two bad core fronts are
\(L,L-r\), giving \(2(\ell-1)\) possibly changed cores and at most two
boundary exceptions.  There are \((2\ell)!/2^\ell\) repartitions, so

\[
 \log |{\cal F}^{(1)}_\ell|
 =2\ell\log\ell+O(\ell),
 \qquad
 s^{(1)}_\ell=8\ell+O(1).
\tag{6.1}
\]

This gives \(c=1/4+o(1)\), exactly as in the source theorem.  The
double-segment construction has twice the independent repartition
entropy, but its four nominal fronts collapse to three for
\(\ell\le h\), and to two plus an \(h\)-fringe for \(\ell\gg h\).
Therefore the single contiguous segment does not maximize entropy at a
fixed missing-target budget.

The obstruction is not caused by independent dihedral alignment of
good runs.  Both modified segments live in one already aligned cyclic
coordinate system.  It is caused by the arithmetic relation

\[
                         2r=m-h,
\tag{6.2}
\]

which makes the two exit fronts nearly coincide.

## 7. Consequence for the annulus gate

The conflict-thinning comparison at survivor density
\(z=m^{-1/2}\) needs a strict entropy coefficient below \(1/2\).  The
double-segment family reaches \(1/2-o(1)\) while retaining
\(K-o(m)\) common targets.  Hence raw support-overlap entropy has no
strict margin at the square-root survivor tilt.

The remaining possible escapes are narrower:

1. stop at a density above \(m^{-1/2}\), as in the existing
   \(m^{-1/3}\) route;
2. prove a terminal-scale estimate with an explicit additive
   \(Cm\) constant and stop at \(s\asymp m/\log m\);
3. quotient or jointly colour the paired \(r\)-separated segment
   clusters, charging their shared bad front only once; or
4. use trajectory information showing that both independent segment
   repartitions cannot survive in the same residual link.

What is now ruled out is a purely static, uniform inverse theorem with
coefficient \(1/3\), \(1/4+o(1)\), or any fixed value below \(1/2\),
based only on the number of missing packet targets.

## 8. Exact implication boundary

Proved:

1. a globally aligned two-segment family with independent label
   repartitions;
2. its exact three-band bad-core union (3.6);
3. the boundary exception count of four;
4. the packet-overlap lower bound (0.4)--(0.6);
5. the entropy coefficient interpolation from \(1/3\) to \(1/2\);
6. failure of every uniform inverse exponent \(c<1/2\); and
7. non-sharpness of the one-segment \(1/4\) calibration.

Not proved:

1. the exact best additive \(O(m)\) constant at
   \(s=\Theta(m/\log m)\);
2. a dynamic theorem excluding simultaneous survival of both segment
   repartitions; or
3. an integral near-factor or coefficient-one annulus conclusion.

The sharp static obstruction is therefore the nearly coincident pair of
bad fronts at displacement \(r\), not the entropy of one isolated
contiguous segment.
