# Phase-one shadow barrier for the pair-omission physical spine

Date: 2026-07-25

Method: pure mathematics only. No search, solver, finite computation, or
external source is used.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom{2m+1}{m}.
\]

The pair-omission token-spine data do **not** imply

\[
\sum_{q\le H}(\widehat M_q^-+\widehat M_q^+)=o(W).
\tag{0.1}
\]

There is an explicit asymptotic counterexample to that implication. Take
the canonical MSW exact factor in every local universe, and then make the
coordinate relabellings supplied by the proved run-thinning theorem. The
resulting pair-omission spine has

\[
J=O(W/m),
\tag{0.2}
\]

but already at the first upper depth

\[
\boxed{\widehat M_1^+\ge(1/64-o(1))W.}
\tag{0.3}
\]

Consequently, for every \(1\le H=o(m)\), including

\[
H=\sqrt m\,\omega(m),\qquad
\omega(m)\longrightarrow\infty,\qquad
\omega(m)=o(\sqrt m),
\]

one has

\[
HJ=o(W)
\quad\text{but}\quad
\sum_{q\le H}(\widehat M_q^-+\widehat M_q^+)=\Omega(W).
\tag{0.4}
\]

Thus no deterministic lemma which charges full-corridor holes only to the
\(O(W/m)\) initial support loss and to \(O(HJ)\) selected/unselected
crossing windows or run endpoints can be valid.

This does not disprove the existence of a different, globally chosen exact
local factor satisfying (0.1). It proves that such a result must contain a
new multidepth near-rainbow exact-factor theorem. It cannot follow from the
pair-omission matching, the run count, row-coherent orientation, or expanded
collars alone.

## 1. The phase-one sector is an immutable local interval shadow

Let \(P_1\) be the first pair in the priority order and

\[
Q_1=[n]\setminus P_1,\qquad |Q_1|=2m-1.
\]

Let \(F_1\) be the exact local factor on \(Q_1\). For every integer \(r\),
write

\[
\mathcal I_r(F_1)
=\{I_\pi(i,r):\pi\in F_1,\ i\in\mathbb Z_{2m-1}\}
\]

for its actual cyclic interval support, and put

\[
h_q(F_1)
=\binom{2m-1}{m-q-1}
 -|\mathcal I_{m-q-1}(F_1)|.
\tag{1.1}
\]

### Proposition 1.1 (exact phase-one sector identity)

For every \(1\le q\le m-2\), the upper targets of rank \(m+q\) which
avoid \(P_1\) and occur in the complete physical corridor of the selected
pair-omission spine are exactly

\[
\mathcal I_{m+q}(F_1).
\tag{1.2}
\]

Consequently

\[
\boxed{\widehat M_q^+\ge h_q(F_1).}
\tag{1.3}
\]

#### Proof

Every start of every phase-one row is selected, because its lower
\((m-1)\)-set avoids \(P_1\). The complete upper corridor through these
starts consists of all length-\((m+q)\) cyclic intervals of the rows of
\(F_1\).

If a start is selected in a later phase, its lower \((m-1)\)-set meets
\(P_1\), by the first-avoided-pair rule. Every upper corridor target
through that owner contains this lower set and therefore also meets
\(P_1\). Hence no later phase adds a target avoiding \(P_1\).

Complementation inside \(Q_1\) bijects length-\((m+q)\) intervals with
length

\[
(2m-1)-(m+q)=m-q-1
\]

intervals. The number of missing targets in the \(P_1\)-free sector is
therefore exactly (1.1), proving (1.2)--(1.3). \(\square\)

This is stronger than orientation invariance: later phases are
set-theoretically unable to fill the missing sector.

## 2. An exact canonical factor with a macroscopic first shadow

Let \(r\ge3\), let

\[
A_r=\binom{2r+1}{r},\qquad
N_r=\binom{2r+1}{r-1}=\frac r{r+2}A_r,
\]

and let \(F_r^{\rm can}\) be the canonical MSW exact factor on \(2r+1\)
coordinates. For a rank-\((r-1)\) target \(S\), let \(\mu(S)\) be its
number of cyclic occurrences, and let

\[
h_1(F_r^{\rm can})=|\{S:\mu(S)=0\}|.
\]

We use here the previously proved algebraic exactness theorem for the
canonical rows indexed by Dyck roots; no probabilistic or finite input is
involved. The new ingredient needed for the present obstruction is the
marked-gap shadow count, whose insertion--erasure proof is given below.

The following algebraic marked-gap lemma is included so that the obstruction
does not rest on finite data.

### Lemma 2.1 (marked-gap collision family)

The canonical factor contains

\[
K_r=(2r-3)\operatorname {Cat}_{r-2}
\tag{2.1}
\]

pairs of distinct pointed first-shadow occurrences such that the two
occurrences in every pair have the same target and no pointed occurrence
is used twice.

#### Proof

Let \(R\) be a Dyck word of semilength \(r-2\), let \(g\) be one of its
\(2r-3\) gaps, and insert at that gap either

\[
d_0=1100\qquad\text{or}\qquad d_1=1010.
\tag{2.2}
\]

These are two distinct Dyck roots of semilength \(r\). In the canonical
omitted-label permutation, the four inserted labels form one consecutive
block for both roots, the outside label order is the same, and the block
occupies the same position.

For completeness, this follows by induction from the defining recursion

\[
\rho(1u0v)
=\bigl(a,\ a-\rho(\mu u),\ 1,\ a+\rho(v)\bigr),
\qquad a=|u|+2,
\tag{2.3}
\]

where \(\mu\) is reverse-complement. Both words in (2.2) are fixed by
\(\mu\), and the empty-root base is

\[
\rho(1100)=(4,2,3,1),\qquad
\rho(1010)=(2,1,4,3).
\]

We also use the immediate concatenation law

\[
\rho(PQ)=(\rho(P),\,|P|+\rho(Q))
\tag{2.3a}
\]

for Dyck words \(P,Q\). Number the gaps of \(R\) by
\(g=0,\ldots,|R|\). There are three cases.

* If \(g=0\), the inserted word is \(d_iR\), and (2.3a) puts the four
  new labels in one initial block while leaving the outside order equal
  to \(\rho(R)\).
* If \(g\ge a\), the insertion lies in \(v\), at local gap \(g-a\).
  The induction hypothesis in the last block of (2.3), followed by the
  affine shift \(a+\rho(v)\), preserves the common inserted block and
  outside order.
* If \(1\le g<a\), the insertion lies in \(u\), at local gap \(g-1\).
  Reverse-complement reflects this to gap \(|u|-(g-1)\) in \(\mu u\).
  The induction hypothesis and the affine map \(z\mapsto a+4-z\) in the
  second block of (2.3) preserve consecutiveness. Erasing the four new
  labels changes the new closing label \(a+4\) back to \(a\), changes
  every suffix label \(a+4+z\) back to \(a+z\), and restores
  \(a-\rho(\mu u)\) on the interior block.

The boundary gap \(g=a\) is the suffix case with local gap zero. These
cases prove that erasing the four-label block recovers \(\rho(R)\), with
the same block position for \(d_0,d_1\).

After appending the distinguished omitted label and rotating to the
inserted block, the two rows have the forms

\[
q(R^{(i)})=(\pi_i,t_0,t_1,\ldots,t_{2r-4}),
\qquad |\pi_i|=4,
\]

with the same outside word.  In the omitted-label word
\(q=(q_0,\ldots,q_{2r})\), the physical rank-\(s\) interval at a pointed
cut is

\[
 I_i^{(s)}(q)=\{q_i,q_{i+2},\ldots,q_{i+2s-2}\},
\tag{2.3b}
\]

because multiplication by two permutes the positions modulo the odd
length \(2r+1\).  Thus the pointed first-shadow dictionary reads the
alternating outside positions at the cut after \(\pi_i\). Their first
lower shadow is therefore the common target

\[
\{t_0,t_2,\ldots,t_{2r-4}\}.
\]

This gives one collision pair for each \((R,g)\), hence (2.1).

The pointed occurrences are all distinct. From a pointed physical slot,
the inverse of the step-two correspondence (2.3b) recovers the omitted-
label \(q\)-order.  The four labels preceding its cut in that order recover
the inserted label set and hence the gap \(g\); their order distinguishes
\(d_0\) from \(d_1\); deleting them recovers \(R\). Thus no pointed slot
is reused. \(\square\)

### Theorem 2.2 (macroscopic canonical first-shadow defect)

For every \(r\ge3\),

\[
\boxed{
h_1(F_r^{\rm can})
\ge
(2r-3)\operatorname {Cat}_{r-2}
-\frac{2A_r}{r+2}.}
\tag{2.4}
\]

In particular,

\[
h_1(F_r^{\rm can})\ge(1/16-o(1))A_r.
\tag{2.5}
\]

#### Proof

Let

\[
D_1=\sum_S(\mu(S)-1)_+
\]

be the duplicate excess. Since the collision pairs in Lemma 2.1 use
disjoint pointed occurrences, a target of multiplicity \(t\) supports at
most \(\lfloor t/2\rfloor\) of those pairs. Hence

\[
K_r
\le\sum_S\left\lfloor\frac{\mu(S)}2\right\rfloor
\le D_1.
\tag{2.6}
\]

There are \(A_r\) first-shadow slots and \(N_r\) possible targets. Exact
occurrence counting gives

\[
D_1=A_r-(N_r-h_1)
=\frac{2A_r}{r+2}+h_1.
\tag{2.7}
\]

Combining (2.1), (2.6), and (2.7) proves (2.4). Finally,

\[
\frac{K_r}{A_r}
=\frac{r(r+1)}{4(2r-1)(2r+1)}
\longrightarrow\frac1{16},
\]

whereas \(2/(r+2)\to0\), proving (2.5). \(\square\)

No finite example or numerical trend enters this proof.

## 3. The exact obstruction in the pair-omission parameters

Apply Theorem 2.2 with

\[
r=m-1,\qquad A_r=\binom{2m-1}{m-1}=:A_m.
\]

The factor \(F_{m-1}^{\rm can}\) is an admissible exact local factor on
\(Q_1\). Proposition 1.1 and (2.4) give

\[
\boxed{
\widehat M_1^+
\ge
(2m-5)\operatorname {Cat}_{m-3}
-\frac{2}{m+1}\binom{2m-1}{m-1}.}
\tag{3.1}
\]

Since

\[
\frac{A_m}{W}
=\frac{m+1}{2(2m+1)}
\longrightarrow\frac14,
\tag{3.2}
\]

(3.1) yields

\[
\widehat M_1^+\ge(1/64-o(1))W.
\tag{3.3}
\]

Coordinate relabelling preserves every interval-support cardinality. We
may therefore take a canonical factor in every local pair complement and
then apply the proved independent-relabelling run theorem. It supplies a
deterministic relabelling for which \(J=O(W/m)\), while (3.1) remains
unchanged in phase one. This proves (0.2)--(0.4).

### Corollary 3.1 (endpoint/crossing charge no-go)

There is no universal deterministic estimate of the form

\[
\sum_{q\le H}(\widehat M_q^-+\widehat M_q^+)
\le C\left(\frac Wm+HJ\right)+o(W)
\tag{3.4}
\]

with an absolute constant \(C\), valid for all exact local factors and all
first-avoided pair-omission spines, whenever \(H=o(m)\).

#### Proof

For the construction above, the right side of (3.4) is

\[
O(W/m)+O(HW/m)+o(W)=o(W),
\]

whereas its left side is at least (3.3). \(\square\)

In particular, assigning \(O(1)\) charge per selected/unselected crossing
at each depth cannot prove (0.1). Phase one has no such crossings at all;
its obstruction is carried by collisions strictly inside full selected
rows.

## 4. Positive-density stability

The obstruction also survives sparse replacement of canonical rows.

### Proposition 4.1 (row-distance stability)

Let \(F'\) be an exact factor on \(2r+1\) coordinates and put

\[
 b=\frac12|F'\triangle F_r^{\rm can}|,
\]

so exactly \(b\) canonical rows have been replaced. Then

\[
\boxed{
h_1(F')\ge
\left[
(2r-3)\operatorname {Cat}_{r-2}
-(r-1)b-\frac{2A_r}{r+2}
\right]_+.}
\tag{4.1}
\]

Consequently \(h_1(F')=o(A_r)\) requires

\[
b\ge(1/8-o(1))\operatorname {Cat}_r.
\tag{4.2}
\]

#### Proof

A canonical row participates in one marked-gap certificate for each
occurrence of \(1100\) or \(1010\) in its Dyck root. Two such occurrences
cannot begin at consecutive positions, so one row destroys at most \(r-1\)
certificates. At least \(K_r-(r-1)b\) disjoint-pointed collision pairs
remain. Repeating (2.6)--(2.7) proves (4.1).

There are \(\operatorname {Cat}_r=A_r/(2r+1)\) canonical rows, and

\[
K_r=(1/16-o(1))A_r.
\]

Dividing the number of pairs which must be destroyed by \(r-1\) gives
(4.2). \(\square\)

Thus row rotations, endpoint orientations, collars, coordinate
relabellings, and \(o(\operatorname {Cat}_r)\) row switches cannot turn the
canonical phase-one factor into the required near-rainbow object. A
successful repair must replace a positive density of its rows or begin
with a different global factor.

## 5. Exact remaining theorem

Define the local growing-window near-rainbow condition

\[
\mathrm{NR}_H(F_m):\qquad
\sum_{q=1}^H
\left[
\binom{2m-1}{m-q-1}
-|\mathcal I_{m-q-1}(F_m)|
\right]
=o\!\left(\binom{2m-1}{m-1}\right).
\tag{5.1}
\]

Because \(A_m\sim W/4\), Proposition 1.1 proves:

> Every first-avoided pair-omission proof of (0.1) must construct an exact
> local factor satisfying \(\mathrm{NR}_H\) at phase one.

This is only a necessary condition; factors in later phases must still cover
the sectors meeting earlier pairs. But it is already a new exact-factor
theorem, not a consequence of the token spine.

The canonical factor violates (5.1) by a fixed positive fraction at
\(q=1\), and Proposition 4.1 shows that a sparse canonical perturbation
also violates it. Therefore the smallest live positive gate is

\[
\boxed{
\text{Construct a genuinely noncanonical exact factor satisfying }
\mathrm{NR}_H
\text{ for }H=\sqrt m\,\omega(m)=o(m).}
\tag{5.2}
\]

Any deterministic charged crossing-window lemma capable of proving (5.2)
must charge internal marked-gap collisions and must use cancellation or
rebundling across a positive density of exact-factor rows. Boundary-only
charges are ruled out by Corollary 3.1.

This report obstructs the requested full-corridor estimate for the present
canonical/spine input. It neither disproves a different near-rainbow exact
factor nor proves the constant-one theorem. It also does not rule out
additional OR witnesses which happen to cross concatenation seams; its
statement concerns exactly the full-corridor hole functional
\(\widehat M_q^\pm\) requested here.
