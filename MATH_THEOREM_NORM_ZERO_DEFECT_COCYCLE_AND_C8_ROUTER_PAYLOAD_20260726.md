# Norm-zero defect cocycles and a bounded \(C_8\) router--payload atom

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

A formal twisted splice is governed by a semidirect-product cocycle.
Write it as

\[
                         A=(\tau,\varepsilon,\ell,\delta),       \tag{0.1}
\]

where:

* \(\tau\) is its endpoint monodromy;
* \(\varepsilon\) is its signed \(X/Y\)-ownership defect;
* \(\ell\) is its row-length defect; and
* \(\delta\) is its protected carrier increment.

All four objects must be expressed in the incoming port frame.  If
\(\tau\) has order \(h\), \(h\) coherent serial copies have identity
endpoint monodromy and accumulated defects

\[
                 N_\tau\varepsilon,\qquad N_\tau\ell,\qquad
                 N_\tau\delta,
 \qquad
                 N_\tau=1+\tau_*+\cdots+\tau_*^{h-1}.            \tag{0.2}
\]

Thus exact serial closure requires

\[
                         N_\tau\varepsilon=0,\qquad
                         N_\tau\ell=0,                            \tag{0.3}
\]

in addition to literal exact seams.  Productivity requires a positive
invariant projection of \(N_\tau\delta\).

There is a nontrivial bounded-row formal atom satisfying these equations.
It is a disjoint router--payload sum of two genuine \(C_8\) switches.

1. The audited rank-three star \(C_8\) is an order-four endpoint router
   with
   \[
                   \tau=(123\ 124\ 125\ 135),                    \tag{0.4}
   \]
   zero \(X/Y\) defect, and length defect
   \[
                   \ell=(-3,-1,0,4)                              \tag{0.5}
   \]
   on this orbit.  Hence \(N_\tau\ell=0\).
2. A disjoint endpoint-inert exact two-row \(C_8\) rectangle has zero
   \(X/Y\) and length defects but a nonzero private first-shadow carrier
   \[
        \delta_\square
          =e_{K\cup\{a,b\}}-e_{K\cup\{a,b'\}}
             -e_{K\cup\{a',b\}}+e_{K\cup\{a',b'\}}.              \tag{0.6}
   \]
   The four displayed targets are distinct.

Let the router act trivially on the private payload coordinates.  The
direct-sum macro-atom has monodromy (0.4), satisfies (0.3), and obeys

\[
                   \operatorname{pr}_\square
                     (N_\tau\delta)=4\delta_\square\ne0.          \tag{0.7}
\]

For any prescribed linear carrier score nonzero on the private direction,
one of the two payload orientations is positive on (0.7).

Consequently there is no invariant obstruction for **all bounded
\(C_6/C_8\) atoms** at the formal cocycle level.  The remaining gate is
geometric: realize the router and private payload in one ambient
switch-stable serial/context chart with disjoint resources and literal
seams.  A single connected \(C_6\) or \(C_8\) carrying both jobs is not
constructed here.

## 1. The formal splice category

Let \(\Omega\) be the finite incoming port set.  Let

\[
                 L=L_X\oplus L_Y,\qquad Q,\qquad V              \tag{1.1}
\]

be respectively the integral \(X/Y\)-ledger module, the row-length
module, and the protected carrier module.  Every allowed port chart acts
on these modules by integral automorphisms.  In particular
\(\tau\in\operatorname{Sym}(\Omega)\) induces

\[
                         \tau_*:L,Q,V\longrightarrow L,Q,V.      \tag{1.2}
\]

By a formal splice we still require a root-to-sink path collection with no
detached cycle, so that its endpoint permutation is defined.  The word
*formal* allows nonzero signed ownership or length defects; it does not
discard path topology.

The defects in (0.1) are signed *new minus old* ledgers.  They include all
local contributions assigned to the splice; crossing collars not included
in the modules are an additional physical seam condition, not silently
zero.

Consider splices \(A_1,\ldots,A_k\) in serial order.  Put

\[
                         g_0=1,\qquad
                         g_j=\tau_j\tau_{j-1}\cdots\tau_1.       \tag{1.3}
\]

With the convention that the \(j\)-th local defect is transported back
through the preceding physical charts by \(g_{j-1,*}\), define

\[
\begin{aligned}
 \operatorname{Mon}(A_1,\ldots,A_k)&=g_k,\\
 \varepsilon_{\rm tot}
   &=\sum_{j=1}^k g_{j-1,*}\varepsilon_j,\\
 \ell_{\rm tot}
   &=\sum_{j=1}^k g_{j-1,*}\ell_j,\\
 \delta_{\rm tot}
   &=\sum_{j=1}^k g_{j-1,*}\delta_j.                            \tag{1.4}
\end{aligned}
\]

This is the defect-cocycle law.

### Theorem 1.1 (serial/context legality)

Assume that the slab interiors are resource-disjoint, every unchanged
connector realizes the chart used in (1.3), and all crossing collars are
included exactly once.  The serial replacement has the original endpoint
closure, exact \(X/Y\) ownership, and the original row lengths if and only
if

\[
                  g_k=1,\qquad
                  \varepsilon_{\rm tot}=0,\qquad
                  \ell_{\rm tot}=0.                              \tag{1.5}
\]

Its carrier increment is then \(\delta_{\rm tot}\).

If a context chart \(c\) conjugates an atom, its data become

\[
 (c\tau c^{-1},\,c_*\varepsilon,\,c_*\ell,\,c_*\delta).          \tag{1.6}
\]

Thus the same criterion applies to serially nested common contexts after
transporting every term to one frame.

#### Proof

After splice \(A_j\), whole outgoing tails are relabelled by \(\tau_j\).
Therefore the next local ledger is seen in the incoming frame through the
prefix transport \(g_{j,*}\).  Signed ledgers add, giving (1.4).

The final tails close onto their original endpoints exactly when \(g_k=1\).
Every \(X/Y\) owner is used once exactly when its signed total discrepancy
is zero, and every row has its old total length exactly when the
row-resolved length discrepancy is zero.  Under the stated seam
hypotheses these are the only defects.  Carrier loads are additive but are
not required to vanish, proving the last assertion.  Formula (1.6) is
ordinary change of frame. \(\square\)

### Corollary 1.2 (finite-order norm criterion)

For \(h\) coherent copies of one atom of order \(h\),

\[
                 g_h=\tau^h=1,\qquad
                 (\varepsilon_{\rm tot},\ell_{\rm tot},\delta_{\rm tot})
                  =(N_\tau\varepsilon,N_\tau\ell,N_\tau\delta). \tag{1.7}
\]

This proves (0.2)--(0.3).

## 2. Exact structure of a norm-zero defect

The relevant ledger modules have distinguished bases of tagged states,
colours, or row slots, and the monodromy acts by permuting those bases.
The norm kernel is therefore elementary but integral.

### Theorem 2.1 (augmentation-kernel theorem)

Let \(\tau\) have finite order \(h\) and act by permutation on a free
abelian group \(\mathbb Z[\mathcal B]\).  For

\[
                         x=\sum_{b\in\mathcal B}x_b e_b,          \tag{2.1}
\]

the following are equivalent:

1. \(N_\tau x=0\);
2. on every \(\tau\)-orbit \(O\subseteq\mathcal B\),
   \[
                              \sum_{b\in O}x_b=0;                \tag{2.2}
   \]
3. \(x\in(1-\tau_*)\mathbb Z[\mathcal B]\).

#### Proof

On an orbit of length \(d\mid h\), every coordinate of \(N_\tau x\)
equals

\[
                         \frac hd\sum_{b\in O}x_b.               \tag{2.3}
\]

Thus (1) and (2) are equivalent.  For a cyclically ordered orbit
\((b_0,\ldots,b_{d-1})\), every integral zero-sum vector has the telescoping
form

\[
 \sum_{i=0}^{d-1}x_{b_i}e_{b_i}
   =(1-\tau_*)\sum_{j=0}^{d-1}
        \left(\sum_{i=0}^{j}x_{b_i}\right)e_{b_j},                \tag{2.4}
\]

up to the harmless choice of cyclic orientation.  This proves (2) and
(3) equivalent. \(\square\)

Applied separately to \(L_X,L_Y,Q\), this theorem completely characterizes
formal norm-zero defects: they are integral coboundaries, not merely
rational cancellations.

There is no analogous implication for the carrier.  The invariant
projection

\[
                  \operatorname{Av}_\tau(\delta)
                       =\frac1hN_\tau\delta                       \tag{2.5}
\]

is independent of whether \(\varepsilon\) is a coboundary.  A no-go
theorem must therefore establish an additional geometric relation between
the carrier and the \(X/Y\) defect.  It cannot follow from the cocycle
formalism alone.

## 3. The explicit order-four \(C_8\) router

Use the rank-three path cover

\[
\begin{aligned}
 K_1={}&123-1236-136-1346-146-1246-126-1256-156-1456-456,\\
 K_2={}&124-1234-234-2346-236-2356-256,\\
 K_3={}&125-1235-235-2345-345-3456-346,\\
 K_4={}&135-1356-356,\\
 K_5={}&134-1345-145-1245-245-2456-246.
\end{aligned}                                                   \tag{3.1}
\]

It partitions every three-set and every four-set of \([6]\).  Its endpoint
monodromy is

\[
                         \pi=(124\ 134\ 135).                    \tag{3.2}
\]

The selected edges

\[
 1236-136,\quad2346-236,\quad3456-346,\quad1356-356              \tag{3.3}
\]

are the old half of the alternating star

\[
 136-1236-236-2346-346-3456-356-1356-136.                       \tag{3.4}
\]

They lie on the four distinct root strands

\[
                         123,\quad124,\quad125,\quad135          \tag{3.5}
\]

and all are traversed from the upper to the lower shore.  The clean
strand-splice theorem therefore shows that the toggle is again a
root-to-sink path cover and right-multiplies (3.2) by

\[
                         \tau=(123\ 124\ 125\ 135).               \tag{3.6}
\]

Both before and after the switch every \(X\)- and \(Y\)-vertex is used
once.  Hence

\[
                              \varepsilon_X=\varepsilon_Y=0.     \tag{3.7}
\]

The old row semilengths on the orbit (3.6) are

\[
                               (5,3,3,1).                         \tag{3.8}
\]

The cuts (3.3) occur after respectively \(0,1,2,0\) completed
\(X\)-transitions.  Cyclically attaching each prefix to the next suffix
gives new row semilengths

\[
                               (2,2,3,5).                         \tag{3.9}
\]

Thus the signed length defect is

\[
                         \ell=(-3,-1,0,4),                        \tag{3.10}
\]

with zero on the fixed row \(134\).  Its coordinate sum on the unique
nontrivial \(\tau\)-orbit is zero, so Theorem 2.1 gives

\[
                              N_\tau\ell=0.                       \tag{3.11}
\]

### Theorem 3.1 (four-copy formal closure)

Four coherently charted copies of the star-\(C_8\) splice have identity
endpoint monodromy, exact \(X/Y\) ledgers, and the same total row lengths
as four copies of the old packet.

#### Proof

Equations (3.6), (3.7), and (3.11) give respectively
\(\tau^4=1\), \(N_\tau\varepsilon=0\), and \(N_\tau\ell=0\).
Corollary 1.2 applies. \(\square\)

This is already a nonidentity norm-zero twisted router.  Its useful
carrier norm is not inferred from the endpoint calculation.

The path partition (3.1) and its monodromy are the rank-three witness in
MATH_ATTACK_S_PORT_PATH_FACTOR_HALL_20260726.md; the star-cycle strand
operation is independently certified in
MATH_THEOREM_C6_C8_STRAND_SPLICING_20260726.md.  Equations
(3.8)--(3.11) add the row-length cocycle audit required here.

## 4. An endpoint-inert \(C_8\) payload

An exact two-for-two MSW \(C_8\) rectangle has common
\((m-3)\)-set \(K\) and four distinct labels
\(a,a',b,b'\notin K\).  With one orientation its first-shadow increment is

\[
 \delta_\square
   =e_{K\cup\{a,b\}}-e_{K\cup\{a,b'\}}
      -e_{K\cup\{a',b\}}+e_{K\cup\{a',b'\}}.                    \tag{4.1}
\]

The four supports are distinct, so

\[
                         \delta_\square\ne0,\qquad
                         \|\delta_\square\|_1=4.                 \tag{4.2}
\]

The switch is factor-to-factor exact: it preserves the complete middle
\(X/Y\) ownership and all row lengths.  Its two-row octahedral strand
diagram has identity endpoint operation.  Consequently its formal data are

\[
                         (1,0,0,\delta_\square).                 \tag{4.3}
\]

Reversing the switch replaces \(\delta_\square\) by
\(-\delta_\square\).

For audit provenance, exact \(X/Y\) ownership, fixed ports, and identity
endpoint operation are the uniform-rectangle theorem in
MATH_THEOREM_DYCK_TRANSVERSAL_RECTANGLE_FACTOR_20260726.md and its port
audit in MATH_ATTACK_S_PORT_PATH_FACTOR_HALL_20260726.md.  The
first-shadow formula (4.1), including distinctness and
\(\ell^1\)-norm four, is the rectangle calculation in
MATH_ATTACK_R3_SHORT_CYCLE_INCREMENT_LATTICE_20260725.md.

## 5. Router--payload separation

Take the disjoint union of the star router in Section 3 and the rectangle
payload in Section 4.  The word *disjoint* means:

1. their middle \(X/Y\) resources are disjoint;
2. the router monodromy fixes the payload row labels; and
3. the protected target support of \(\delta_\square\) is private to the
   payload chart.

These are precisely the hypotheses under which two bounded local switches
compose without a hidden collar term.

### Theorem 5.1 (bounded norm-zero productive atom)

The direct-sum atom \(A\) has

\[
                   \tau_A=\tau,\qquad
                   \varepsilon_A=0,\qquad
                   \ell_A=\ell,\qquad
                   \delta_A=\delta_{\rm rt}+\delta_\square,      \tag{5.1}
\]

where \(\delta_{\rm rt}\) is the router's carrier increment.  It satisfies

\[
                         N_\tau\varepsilon_A=0,\qquad
                         N_\tau\ell_A=0,                          \tag{5.2}
\]

and

\[
                 \operatorname{pr}_\square
                   (N_\tau\delta_A)=4\delta_\square\ne0.         \tag{5.3}
\]

In particular, choose a linear score \(\Lambda\) supported on the private
payload sector with \(\Lambda(\delta_\square)>0\).  Then

\[
                              \Lambda(N_\tau\delta_A)>0.          \tag{5.4}
\]

#### Proof

Disjoint exact switches add their ledger, length, and carrier differences.
The payload has identity monodromy, so the macro-atom retains the router
monodromy \(\tau\).  Equations (3.7), (3.11), and (4.3) prove (5.1)--(5.2).

The router transport fixes the private payload chart.  Hence every one of
the four terms in the norm has payload projection
\(\delta_\square\).  The router carrier has zero projection there by
resource disjointness.  This gives (5.3); reversing the payload orientation
if necessary gives (5.4). \(\square\)

The construction uses only a bounded number of touched rows and two
\(C_8\) components, independently of the ambient rank.  It disproves a
formal invariant obstruction for all \(C_6/C_8\) atoms.

## 6. Exact scope and remaining physical gate

Theorem 5.1 is a formal local atom theorem, not yet a positive-density
constant-one construction.  Its realization in the target recursive
factor requires all of the following.

1. **One transported label.**  The four router copies must be serial
   stages on one port label.  Four independent Catalan holes act
   tensorially and do not implement \(\tau^4\).
2. **Literal seams.**  Every connector and crossing collar must realize
   the charts assumed in (1.3), with no unrecorded \(X/Y\), length, or
   carrier defect.
3. **A fixed payload sector.**  The private rectangle must remain outside
   the router's transported support, so that (5.3) is literal rather than
   a formal relabelling.
4. **Favourable ambient score.**  Reversing a formal rectangle chooses the
   sign of a linear carrier functional only when both rectangle states are
   supported in the current factor.  The canonical private \(C_8\) family
   can be anti-repair for the actual nonlinear hole functional.

For a **single clean connected** \(C_6\) or \(C_8\), with one cut on each
moved strand, every segment-additive carrier change is a coboundary:

\[
                            \delta_{\rm seg}
                                =(1-\tau_*)v,                    \tag{6.1}
\]

because the switch merely cyclically reassigns a fixed collection of old
suffix segments among the affected roots.  Therefore

\[
                            N_\tau\delta_{\rm seg}=0.             \tag{6.2}
\]

Any positive norm of one clean connected switch must come from genuinely
non-additive crossing-window or collar terms.  A folded switch, with
several cuts on one old strand, has an additional internal-segment
permutation and is not covered by (6.1).  Neither contribution is
determined by the endpoint monodromy or the \(X/Y\) defect.  The exact
remaining connected-atom target is consequently:

> Find a strand-admissible \(C_6\) or \(C_8\) for which the augmented
> crossing-carrier cocycle has nonzero invariant projection, while its
> \(X/Y\) and length defects lie in their integral augmentation kernels.

This is the only part not settled by the bounded router--payload
construction.
