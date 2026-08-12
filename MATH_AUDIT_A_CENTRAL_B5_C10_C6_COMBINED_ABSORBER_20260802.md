# Audit: central `B_5` `C10` compressor, Boolean `C6` opener, and the exact combined absorber

**Date:** 2026-08-02  
**Status:** independent proof audit plus one new literal local synthesis.  No
handoff or research-index entry is made here.  No global central-bank,
reset, residence, upper-shadow, source, or compiler existence theorem is
claimed.

## 0. Verdict

The following three ingredients are sound, with the scopes stated in their
source notes.

1. A saturated nontrivial `B_5` fibre has exactly two phases with the same
   lower and upper palettes.  Their physical symmetric difference is one
   alternating `C10`; hence every nonidentity frozen-fibre replacement
   changes all five diamonds.
2. Two copies joined by the fixed vertical matching give the exact topology
   change `5 C4 -> C20`.  This is a cycle compressor, not a forest maker.
3. The Boolean ternary hex is an exact `3 <-> 3` four-resource circuit.
   Its cycle mode opens one cycle using two distinct path components.  The
   star-centred-square theorem excludes every nonidentity `2 <-> 2`
   four-resource circuit, so `C6` is support-minimal globally.  The separate
   `C6/C8` no-go in the five-fibre note is only a frozen-fibre statement.

The graphic identity

\[
 \beta(B-R+A)-\beta(B)
   =\rho_{B-R}(R)-\rho_{B-R}(A)
\]

is exact.  The atlas sink/plateau criterion is also exact, but conditional:
it characterizes a supplied atlas and does not prove Boolean circuit supply.
The matroid-intersection row is conditional on an exact protected matroidal
lift, which the natural four resource rows do not presently supply.

There is, however, a stronger literal local consequence not stated in the
three input notes: for every `m >= 5`, one `C10` compressor and one cross-
fibre Boolean `C6` opener form an exact four-resource `5-cycle -> forest`
absorber.  The construction and its strict scope are below.

## 1. Independent `B_5` classification check

Let `K=Z_5`,

\[
 U_i=\{i,i+1,i+2\},\qquad
 p_i=\{i,i+1\},\qquad d_i=\{i,i+2\}.
\]

If singleton `i` is assigned to `U_(i+x_i)`, then
`x_i in {0,-1,-2}`.  Unique use of `{i,i+1}` gives

\[
 1_{x_i\ne-2}+1_{x_{i+1}\ne0}=1.                 \tag{1.1}
\]

If some `x_i=0`, (1.1) propagates `x=0` cyclically.  Otherwise an occurrence
of `-1` forces the next value to be zero, so every value is `-2`.  Thus the
only phases are

\[
 E^+=\{p_i d_i:i\in Z_5\},\qquad
 E^-=\{p_i d_{i-1}:i\in Z_5\}.                    \tag{1.2}
\]

Their union is the alternating cycle

\[
 p_0,d_0,p_1,d_1,\ldots,p_4,d_4,p_0.             \tag{1.3}
\]

This proves both uniqueness and the absence of frozen-fibre `C6` or `C8`
replacements.  Complementation gives the rank-`2,3,4` fibre.  This argument
does not exclude cross-fibre `C6/C8` circuits.

## 2. Exact literal `C10+C6` forest absorber

### Theorem 2.1 (one socket absorbs all five local cycles)

For every `m >= 5`, there is a partial two-bank central table with 22
diamonds and four injective typed resource rows (lower, upper, tail, head)
having the following two resource-equivalent realizations:

* the old realization has five `C4` cycle components and two isolated-edge
  path components;
* the new realization is a forest with component vertex sizes `22` and `2`.

The transformation is the composition of one five-diamond frozen-fibre
`C10` switch and one three-diamond cross-fibre Boolean `C6` switch.  It
preserves every named resource in all four typed rows and preserves both
bank matching constraints.

#### Construction

Choose disjoint data

\[
 |C|=m-3,\quad K=Z_5,\quad a,b,c\notin C\cup K,
\]

and choose `q in C`.  This uses `m+5 <= 2m` coordinates.  Form the two
`B_5` fibres with cores `C+a` and `C+b`:

\[
 \mathcal Q_x^+=\{[C+x+i,C+x+U_i]:i\in Z_5\},\qquad
 \mathcal Q_x^-=\{[C+x+i,C+x+U_{i-2}]:i\in Z_5\}, \tag{2.1}
\]

for `x in {a,b}`, together with the vertical bank

\[
 \mathcal R=\{[C+X,C+\{a,b\}+X]:X\in {K\choose2}\}. \tag{2.2}
\]

Orient the `a`-fibre from every `p_i` to `d_i`, the `b`-fibre in the
opposite direction, the `p`-verticals from the `b` copy to the `a` copy,
and the `d`-verticals from the `a` copy to the `b` copy.  Hence every old
`C4`, and the compressed `C20`, is a directed cycle and each tail/head row
is injective.

The coordinate budget is exact for this realization.  The two-fibre socket
uses `(m-3)+5+2=m+4` coordinates, and `c` is chosen outside that complete
support.  Such a fresh coordinate exists exactly when `m+5 <= 2m`, namely
`m >= 5`.  Also `C` is then nonempty, so the required `q in C` exists.

Take `X=d_0`, put `L=C+X`, `S=L-q`, and use the vertical atom

\[
 e=(L,L+\{a,b\},L+a,L+b).                          \tag{2.3}
\]

as the target of the Boolean hex with theorem parameters
`alpha=b`, `delta=a`, `b_parameter=q`, and `c_parameter=c`.  Its two other
old atoms are

\[
\begin{aligned}
 o_1&=(S+b,\ S+\{a,b,c\},\ S+\{a,b\},\ S+\{b,c\}),\\
 o_2&=(S+c,\ S+\{q,a,c\},\ S+\{a,c\},\ S+\{q,c\}),
\end{aligned}                                      \tag{2.4}
\]

and its new phase is

\[
\begin{aligned}
 n_1&=(S+b,\ L+\{a,b\},\ S+\{a,b\},\ L+b),\\
 n_2&=(S+c,\ S+\{a,b,c\},\ S+\{a,c\},\ S+\{b,c\}),\\
n_3&=(L,\ S+\{q,a,c\},\ L+a,\ S+\{q,c\}).
\end{aligned}                                      \tag{2.5}
\]

Keep the bank labels fixed and define

\[
\begin{array}{ll}
 B_0^{\rm old}=\mathcal Q_a^+\mathbin{\dot\cup}\mathcal Q_b^+,
 &B_0^{\rm new}=\mathcal Q_a^-\mathbin{\dot\cup}\mathcal Q_b^+,\\[2mm]
 B_1^{\rm old}=\mathcal R\mathbin{\dot\cup}\{o_1,o_2\},
 &B_1^{\rm new}=(\mathcal R-\{e\})
                  \mathbin{\dot\cup}\{n_1,n_2,n_3\}.
\end{array}                                        \tag{2.6}
\]

The fresh coordinate `c` and the missing core coordinate `q` show directly
that every resource of `o_1,o_2` outside (2.3) is disjoint from the
two-fibre socket resources.  The four external physical endpoints are also
distinct and outside the socket.  Thus `o_1,o_2` are two isolated old path
edges and may be adjoined to the vertical bank.  Consequently every one of
the four sets in (2.6) is a physical matching in its declared bank.

For completeness, every socket middle vertex contains all of `C`, exactly
one of `a,b`, and two points of `K`.  The four new exterior middle vertices
are

\[
 S+\{a,b\},\quad S+\{b,c\},\quad
 S+\{a,c\},\quad S+\{q,c\};                        \tag{2.7}
\]

the first three omit `q`, and the last contains the fresh `c`.  Hence none
is a socket vertex.  The same missing-`q`/fresh-`c` signatures separate the
two exterior lower and upper colours from the socket palettes.  Within the
six-vertex hex, distinctness is the Boolean-hex matching identity.

#### Proof of the topology and resource claims

With both fibres in phase `E^+`, their union with the vertical bank (2.2)
gives `5 C4`.  Replacing the
`a`-fibre by `E^-` gives one `C20`, without changing any lower, upper, tail,
or head resource: orienting both phases from the `p` shore to the `d` shore
makes the tail and head sets identical.

The atom `e` remains an edge of that `C20`, while `o_1,o_2` lie in two
different path components.  The Boolean-hex identity gives

\[
 \operatorname{res}\{o_1,o_2,e\}
   =\operatorname{res}\{n_1,n_2,n_3\}              \tag{2.8}
\]

in all four typed rows.  Its cycle-mode theorem therefore replaces the
`C20` and the two isolated edges by two paths.  In this literal choice the
path vertex sizes are `22` and `2`.  Both phases of the hex are matchings on
the same six middle vertices, so the vertical-bank matching row also
survives.  The fibre switch similarly uses every one of its ten middle
vertices once in both phases.

More explicitly, each of the old and new total tables in (2.6) has 22
atoms, and each of its lower, upper, tail, and head rows consists of 22
pairwise distinct literal resources.  Equality of the old/new lower and
upper rows follows from the two palette identities; equality of tail and
head rows follows from the `p`-to-`d` orientation of the `C10` and (2.8).
Thus the assertion is stronger than equality of undirected middle degrees:
the two bank labels and all four ordered resource rows survive literally.

The contracted-rank ledger is also sharp.  Regard the composite as an
eight-edge replacement and let `T` be the support after deleting its eight
old edges.  Those old edges meet all five old cycles, so

\[
 \rho_T(R)=8-5=3.
\]

The final graph is a forest, hence all eight new edges are independent over
`T` and \(\rho_T(A)=8\).  The graphic identity therefore gives
\(\Delta\beta=3-8=-5\), exactly the five destroyed cycles.  This proves the
theorem.  \(\square\)

### Corollary 2.2 (protected version)

The same construction is valid in an ambient table provided its complete
old/new footprint is disjoint from every protected or forbidden literal
resource and the 22 local resources are unused outside the displayed
socket.  It removes five cycle components and creates none.  It does not
make an arbitrary ambient atlas circuit-complete: the theorem supplies one
explicit socket, not a theorem planting such a socket through every
residual cycle.

### Corollary 2.3 (disjoint-product hypercube absorber)

Let

\[
             (\mathcal M_t^{0},\mathcal M_t^{1}),
             \qquad 1\le t\le s,                  \tag{2.9}
\]

be `s` planted copies of Theorem 2.1, where superscripts `0,1` denote the
old and new modes.  Require their **complete footprints** to be pairwise
disjoint: no lower, upper, tail, head, bank-middle, protected, forbidden,
or declared guard resource occurring in either mode of one copy occurs in
either mode of another.  In particular, their physical middle-vertex sets
are disjoint.  If an extra guard or state row is part of the intended face,
additionally require it to be mode-transparent inside each copy; footprint
disjointness alone does not imply this.  For `epsilon in {0,1}^s`, put

\[
                 \mathcal M(\epsilon)
                    =\mathop{\dot\bigcup}_{t=1}^s
                       \mathcal M_t^{\epsilon_t}.   \tag{2.10}
\]

Then:

1. every `M(epsilon)` has exactly the same four typed resource rows and
   satisfies the same two bank-matching constraints (and preserves any
   extra row explicitly assumed mode-transparent);
2. the exchange graph under one-module composite `C10+C6` toggles is the
   hypercube `Q_s`;
3. if `z(epsilon)=|{t:epsilon_t=0}|`, then
   \[
                \beta(\mathcal M(\epsilon))=5z(\epsilon);      \tag{2.11}
   \]
4. the all-new state `M(1,...,1)` is a forest, namely the disjoint union of
   `s` copies of \(P_{22}\mathbin{\dot\cup}P_2\).

Thus the composite circuit is a monotone circuit-complete absorber on this
planted disjoint-module face: toggling any old coordinate raises graphic
rank by five, and at most `s` composite toggles reach the forest.

#### Proof

Theorem 2.1 gives equality of the four central resource rows and fixed bank
labels inside each coordinate.  Complete-footprint disjointness makes
choices in different coordinates independent, so the `2^s` states are all
legal and two states are adjacent exactly when their bit strings differ in
one coordinate.  This is `Q_s`.  Physical disjointness makes graphic
nullity additive.  An old module has five cyclic components and a new
module has none, proving (2.11) and the forest assertion.  \(\square\)

The same conclusion remains true after adjoining a fixed forest background
whose complete footprint is disjoint from every module.  Without this
disjointness, cross-module or background paths can alter the graphic rank
delta, so Corollary 2.3 gives no conclusion.  In particular, it proves
circuit completeness only for the prescribed `2^s` module modes, not for
the entire named-resource fibre and not for an unplanted central table.

## 3. Minimality and the exact connected-exchange conclusion

The `C10` is forced inside a saturated frozen `B_5` fibre by Section 1.
The global Boolean `C6` is support-minimal because any outer `K_(2,2)`
square has the common middle vertex

\[
 L_0\cup L_1=U_0\cap U_1,
\]

and the two crossed diamonds cannot reproduce the other typed middle
resources unless the two phases are identical.  Thus no nonidentity exact
`2 <-> 2` four-resource replacement exists.  Nothing here excludes a
global `4 <-> 4` circuit; the `C8` rigidity claim is only fibre-local.

Let an atlas contain protected instances of the `C10`, the cross-fibre
`C6`, and any other declared literal circuits.  The strongest unconditional
exchange statement about that supplied atlas is:

* an equal-size trade improves topology exactly when its new half has
  greater graphic rank after contraction of the untouched support;
* the atlas is a monotone forest absorber exactly when every sink strongly
  connected component of its nondecreasing-rank state graph has full
  graphic rank.

A useful sufficient specialization is: from every sub-full plateau, a
sequence of rank-neutral legal phase moves reaches an applicable `C6` whose
old target edge lies on a cycle and whose two old partner edges lie in two
distinct path components.  Then the `C6` raises graphic rank by one and
escapes that plateau.  Repetition reaches a forest in at most the initial
cycle-nullity many strict moves.  This is a theorem once the stated socket
supply is proved; it is not supplied merely by the `3/4` five-fibre density.

There is an independent determinant-sign boundary.  On a fixed oriented
tail/head resource fibre, a `C_(2r)` toggle changes the tail-to-head
bijection by an `r`-cycle.  Both circuits used above have odd `r` (`r=5`
and `r=3`) and hence preserve its sign.  Therefore `C6+C10` is not a Markov
basis for a fixed resource fibre whenever both signs occur.  The first
sign-changing Boolean trade is the `C8` (`r=4`), and the exact `B_5`
classification shows that it requires one aperture: neither of its phases
extends to a saturated five-diamond fibre.  The one-socket absorber of
Theorem 2.1 is unaffected—it starts and ends in the same sign—but a global
connected exchange theorem must either plant protected `C8` apertures or
allow a move that changes the fixed tail/head/core fibre.

There is also a free core-flux obstruction to staying inside the frozen
five-coordinate fibres: fibre-local circuits preserve, for every core
pattern `P`, the difference between its lower and upper target counts, while
the full central demand has a nonzero difference.  A nonzero *simple-core*
cross-fibre circuit needs at least three core states.  This qualifier is
essential: a literal two-state circuit may have zero simple-core projection
by exchanging parallel columns.  Thus neither the `C10` hypercube nor the
local forest socket completes the missing central quarter.

## 4. Common-base/reset interface

The local construction is exact on the four central resource rows.  It can
be used before state insertion.  It may be used after state insertion only
if old and new roles have identical Cartesian menus and protected boundary
ledger, or if the exact Hoffman cuts are rebuilt for the new table.

Likewise, the conditional matroid-intersection criterion

\[
 r_M(Y)+r_G(E-Y)\ge q\qquad(Y\subseteq E)
\]

becomes an exact existence theorem only after an exact protected matroidal
lift has been proved.  The four natural partition rows do not themselves
form that lift.  Neither the local `C10+C6` absorber nor the Dong--Mao
`3/4` bank proves reset/history transparency, residence, deeper upper
support, source chronology, or a common compiler.

## 5. Regression

The new verifier

```text
scratch/a_central_b5_c10_c6_combined_absorber_20260802/
  audit_a_central_b5_c10_c6_combined_absorber_20260802.py
```

replays the literal construction for every `5 <= m <= 20`.  It checks all
four typed resource rows, both bank matchings, the `5 C4 + 2 K2` old graph,
the `C20 + 2 K2` intermediate graph, and the final `P22 + P2` forest.

The pre-existing independent regressions also pass:

```text
scratch/a_five_fibre_c10_cycle_compressor_20260802/
  audit_a_five_fibre_c10_cycle_compressor_20260802.py
scratch/audit_boolean_hex_ternary_four_resource_absorber_20260801.py
```
