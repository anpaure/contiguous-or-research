# Lane X audit: the exact U7 repair ledger and the multiscale ceiling

Date: 2026-07-25

## 0. Verdict

The displayed formula

\[
D_R(d)=d(R+1)(R-d+1)+\frac{d(d^2-1)}6
\tag{0.1}
\]

is correct for the complement of the **certified U7 support** at depth
\(d\), and its cumulative sum is correct.  One scope correction is
important: the proof identifies the complement of the selected certified
target family.  It does not prove that no other, incidental interval of the
full word represents one of those targets.  Thus \(D_R(d)\) is an exact
literal-repair upper ledger, not an architecture-free lower bound on the
true hole set of the word.

Within that certified-support/literal-repair architecture, the threshold is
sharp:

\[
\frac{\mathcal D_R(H)}{M_R}
=\frac{3H(H+1)}{4R}
 \left(1+O\left(\frac HR+\frac1R\right)\right)
\qquad(H=o(R)),
\tag{0.2}
\]

where \(M_R=w([0,R]^4)\).  In particular, at
\(H\sim c\sqrt R\) the literal repair alone costs
\((3c^2/4+o(1))M_R\).

Neither regrouping the shell radii nor recursively repairing only the small
shell caps changes this threshold.  The cap contribution is the lower-order
term \((A^2-A)/6\); the dominant large-shell shoulder contribution remains
\(\sim H^2R^2/2\).

For a fixed four-block Boolean SCD, the positive-mass parents have scale
\(R=\Theta(\sqrt k)\).  Consequently a boxwise U7 construction with literal
completion has the Boolean ceiling

\[
H=o(k^{1/4}),
\tag{0.3}
\]

not \(H=\sqrt k\,\omega(k)\).  Atypically taller chain parents carry
vanishing width mass and cannot change that bulk conclusion.

The only surviving upgrade is a genuine cross-shell/cross-parent recoding
which represents the shoulder complement on the width baseline itself.  It
cannot be a thin multiscale seam hierarchy: the already proved equal-shell
endpoint theorem forces surface-scale, high-degree sharing.  No such
recoding is currently constructed, so this lane does not prove the
constant-one theorem.

---

## 1. Independent verification of the exact formula

At global depth \(d\), the large shells \(r\ge d\) have certified deficit

\[
n_r(d)-f_r(d)=d(2r+1-d).
\tag{1.1}
\]

The smaller shell caps \(\lceil d/2\rceil\le r<d\) have size

\[
n_r(d)=(2r-d+1)^2.
\tag{1.2}
\]

The shell decomposition is disjoint, so the complement of the certified
support is the sum of these cardinalities.  The first sum is

\[
\begin{aligned}
\sum_{r=d}^R d(2r+1-d)
&=d(R-d+1)(R+1).
\end{aligned}
\tag{1.3}
\]

If \(d=2s\), the second sum is
\(1^2+3^2+\cdots+(2s-1)^2\).  If \(d=2s+1\), it is
\(2^2+4^2+\cdots+(2s)^2\).  In both cases it equals

\[
\frac{d(d^2-1)}6.
\tag{1.4}
\]

Equations (1.3)--(1.4) prove (0.1).

Put

\[
A=\frac{H(H+1)}2,
\qquad
B=\frac{H(H+1)(2H+1)}6.
\tag{1.5}
\]

Then direct summation gives

\[
\boxed{
\mathcal D_R(H)
=(R+1)((R+1)A-B)+\frac{A^2-A}{6}.}
\tag{1.6}
\]

This also verifies that the last summand is the complete small-cap
contribution, rather than an error term introduced by asymptotics.

---

## 2. Sharp literal-repair threshold

The equal four-box width is

\[
M_R=\frac{2R^3+6R^2+7R+3}{3}.
\tag{2.1}
\]

Since

\[
\frac BA=\frac{2H+1}{3},
\tag{2.2}
\]

equation (1.6) can be written

\[
\mathcal D_R(H)
=(R+1)A\left(R+1-\frac{2H+1}{3}\right)
 +\frac{A^2-A}{6}.
\tag{2.3}
\]

Uniformly for \(H=o(R)\),

\[
\mathcal D_R(H)
=R^2A\left(1+O\left(\frac HR+\frac1R\right)\right),
\tag{2.4}
\]

and division by (2.1) proves (0.2).  Therefore:

* \(H=o(\sqrt R)\) gives \(\mathcal D_R(H)=o(M_R)\);
* \(H/\sqrt R\to c\in(0,\infty)\) gives
  \(\mathcal D_R(H)/M_R\to3c^2/4\);
* \(H/\sqrt R\to\infty\), while \(H=o(R)\), gives
  \(\mathcal D_R(H)/M_R\to\infty\).

This is an if-and-only-if threshold for the particular operation “append
every target outside the certified atlas support once literally.”  It is
not a lower bound for a different recoding.

For later use, when \(d/R\to x\in[0,1]\), (0.1) also gives

\[
\frac{D_R(d)}{R^3}
\longrightarrow x(1-x)+\frac{x^3}{6}.
\tag{2.5}
\]

Thus at every fixed positive relative depth the certified complement in a
single rank is already a positive fraction of the width scale.  Any
successful fixed-relative-depth construction must alter the atlas support,
or prove that its unadvertised intervals supply most of this complement;
literal repair cannot be negligible.

---

## 3. Shell-cap recursion does not touch the dominant term

Split (1.6) as

\[
\mathcal D_R(H)
=\mathcal S_R(H)+\mathcal C_R(H),
\tag{3.1}
\]

where

\[
\mathcal S_R(H)
=\sum_{d=1}^H\sum_{r=d}^R d(2r+1-d)
=(R+1)((R+1)A-B)
\tag{3.2}
\]

is the large-shell shoulder deficit, and

\[
\mathcal C_R(H)
=\sum_{d=1}^H\sum_{\lceil d/2\rceil\le r<d}(2r-d+1)^2
=\frac{A^2-A}{6}
\tag{3.3}
\]

is the small-shell cap deficit.

### Proposition 3.1 (cap-only recursion ceiling)

Suppose an iterated construction repairs every target in
\(\mathcal C_R(H)\) at zero cost but retains the U7 certified support on
all large shells.  Its remaining literal-repair ledger is exactly
\(\mathcal S_R(H)\), and for \(H=o(R)\)

\[
\frac{\mathcal S_R(H)}{M_R}
=\frac{3H(H+1)}{4R}
\left(1+O\left(\frac HR+\frac1R\right)\right).
\tag{3.4}
\]

Hence perfect recursive cap completion leaves the same
\(H=o(\sqrt R)\) threshold.

The proof is immediate from (3.2).  Notice also that (3.2) is additive in
the shell radius \(r\).  Partitioning the radii among any number of
multiscale groups, or arranging those groups in any fusion tree, leaves
the sum unchanged.  A regrouping can help only if it creates new
cross-shell witnesses for the shoulder targets; relabelling the same
literal repairs cannot help.

---

## 4. Boolean scaling for boxwise use

The following statement records the exact scope in which the local ledger
has a Boolean consequence.

### Theorem 4.1 (boxwise U7 ceiling)

Let the Boolean dimension \(k\) be split into four equal blocks and fix an
SCD in each block.  Consider a compact positive window of four chain
heights.  Inside every selected product parent, use a centred equal
four-box core \([0,R]^4\) with

\[
a\sqrt k\le R\le b\sqrt k
\tag{4.1}
\]

for fixed \(0<a<b<\infty\).  Suppose the core middle widths have total
mass at least \(\beta W(k)\), where \(\beta>0\), and every core is
serviced independently by the U7 atlas followed by literal repair of the
complement of its certified upper-band support.

For \(1\le H\le a\sqrt k/2\), the total literal repair is at least

\[
c_{a,b}\,\beta W(k)\frac{H^2}{\sqrt k}
\tag{4.2}
\]

for an absolute positive \(c_{a,b}\).  Consequently this architecture can
have total length \(W(k)+o(W(k))\) only if

\[
H=o(k^{1/4}).
\tag{4.3}
\]

#### Proof

For \(H\le R/2\), (3.2) gives

\[
\mathcal D_R(H)\ge\mathcal S_R(H)
\ge \frac{R^2H(H+1)}4.
\tag{4.4}
\]

Since \(M_R=\Theta(R^3)\), uniformly on (4.1),

\[
\mathcal D_R(H)
\ge c\,M_R\frac{H^2}{R}
\ge c_b M_R\frac{H^2}{\sqrt k}.
\tag{4.5}
\]

The product parents and their centred cores are disjoint.  Summing (4.5)
and using the assumed core-width mass proves (4.2).

For equal coordinate blocks, the hypotheses occur on a positive-mass
compact SCD-height sector: chain heights divided by \(\sqrt k\) have a
nondegenerate Rayleigh limit, parent widths are \(\Theta(k^{3/2})\), and a
centred equal core of side \(\Theta(\sqrt k)\) has width
\(\Theta(k^{3/2})\).  Parity may be fixed by restricting to one common
height parity and changing \(R\) by at most one.

Parents with a height larger than \(T\sqrt k\) do not offer a bulk escape.
The exact SCD chain count gives a Gaussian height tail.  If \(S\) is the
sum of the four heights, then

\[
\mathbb E(S+1)^6=O(k^3),
\qquad
\Pr(\max_iL_i>T\sqrt k)\le C e^{-cT^2}.
\tag{4.6}
\]

As a four-chain box width is at most \((S+1)^3\), Cauchy--Schwarz shows
that all such tall parents have aggregate middle width

\[
O(e^{-c'T^2}W(k)).
\tag{4.7}
\]

Thus taking \(R/\sqrt k\to\infty\) sacrifices all but \(o(W(k))\) of the
bulk middle ownership.

The theorem is deliberately architecture-scoped.  A global word may share
positions between different parents; then independent summation of local
repair lengths is invalid.

---

## 5. What cross-parent fusion would have to do

The equal-shell endpoint theorem in
`MATH_ATTACK_H_MULTISCALE_THREE_FOURBOX_FUSION_20260725.md` is already
formulated for arbitrary ambient witnesses.  For a universal word of
length \(M_R+D\), it forces

\[
\mathcal C_R^{\rm share}
\ge\left(\frac{289}{3456}-o(1)\right)M_R-2D
\tag{5.1}
\]

units of same-side cross-shell endpoint sharing.  If a fusion tree has
height \(h_R\), and each node has at most \(s_R\) genuinely shared typed
sites, then near-width length requires

\[
h_Rs_R
\ge\left(\frac{289}{10368}-o(1)\right)R^2.
\tag{5.2}
\]

Moreover at least

\[
\left(\frac{289}{2592}-o(1)\right)R^2
\tag{5.3}
\]

physical positions must exhibit cross-shell reuse in the audited depth-
\(R/8\) shoulder band.  If only \(O(R^2)\) such positions are used, their
average endpoint--shell excess degree is \(\Omega(R)\).

Therefore none of the following raises the local or Boolean band:

1. regrouping the same U7 shells at several values of \(R\);
2. recursively solving only the small caps;
3. a bounded-arity, logarithmic-depth hierarchy with
   \(R\,\mathrm{polylog}(R)\)-scale interfaces;
4. independent four-box parents followed by an \(o(W)\) literal repair.

The surviving possibility is much more specific: a surface-scale set of
baseline positions must be reused with unbounded cross-shell/cross-parent
degree, and those same positions must represent the missing shoulder
targets through literal intervals.  The known wreath portal word supplies
middle-productive baseline sharing at the two central ranks, but no theorem
aligns it with these shoulder incidences.  The U7 chronology supplies
near-surjective support only for \(d=o(R)\), and no lower-half partner or
cross-parent allocation is known.

---

## 6. Exact frontier

The new constructive ledger is valid and useful, but it does not iterate to
the required Boolean depth.

* **Proved:** complete certified upper-band support with
  \(M_R+o(M_R)\) length for \(H=o(\sqrt R)\).
* **Proved:** cap-only and regrouping multiscale variants retain the same
  threshold.
* **Proved:** in the fixed four-block Boolean aggregation, boxwise literal
  completion has ceiling \(H=o(k^{1/4})\).
* **Proved:** thin multiscale cross-shell interfaces cannot supply the
  missing fixed-relative-depth shoulders.
* **Open:** a surface-scale, high-degree cross-parent braid which recodes
  the width baseline and gives distinct shoulder support on both sides.

Since the constant-one proof needs every fixed Gaussian window
\(H=A\sqrt k\), followed by diagonalization to
\(H=\sqrt k\,\omega(k)\), the U7 literal-repair theorem is still two scale
jumps short: \(k^{1/4}\) versus \(k^{1/2}\), and one-sided equal-parent
support versus a symmetric cross-parent Boolean word.
