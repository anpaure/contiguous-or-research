# R2 theorem: full K17 immediate-upper circulation, licensed seams, and Benders oracle

**Date:** 2026-08-02  
**Status:** exact full-19,448 augmenting criterion and completeness-safe
ordinary/exceptional master, plus an independently replayed connected full
factor whose rank-ten coverage is ordinary-root-only and 19,448/19,448,
together with its literal primary complement. Residence, ranks 11--17,
source, compiler and a word remain outside scope.

## 1. The full immediate-upper palette

Put

\[
 \mathcal U_{10}={{[17]}\choose10},\qquad
 |\mathcal U_{10}|=19{,}448.
\]

For the fixed exceptional rank-eight root `D`, split

\[
 \mathcal U_{\neg D}=\{U:D\nsubseteq U\},
 \qquad |\mathcal U_{\neg D}|=19{,}412,
\]

\[
 \mathcal U_D=\{D\cup\{a,b\}:a,b\notin D, a\ne b\},
 \qquad |\mathcal U_D|={9\choose2}=36.              \tag{1.1}
\]

Let the opened owner chronology be `T_0,...,T_(N-1)`. Consecutive owners
share a rank-eight root, so their union has rank ten.

### Lemma 1 (rank-ten intervals are adjacent-pair values)

Every rank-ten OR of a nontrivial consecutive owner interval equals the OR
of its first adjacent owner pair. Hence the complete rank-ten interval deck
is exactly the set of adjacent-pair unions.

#### Proof

If an interval begins with `T_i,T_(i+1)`, their union already has rank ten.
If the full interval union also has rank ten, it contains and therefore
equals that first union. \(\square\)

The opened h1 chronology has 24,309 adjacent pairs: 24,308 ordinary-root
diamonds and one internal pass through `D`. The physical cycle has one
additional closing pair.

## 2. Ordinary-root-only full circulation

For an ordinary factor `F`, let `m_F^ord(U)` count its ordinary-root
diamonds of colour `U`. A root switch with unchanged owner `P_L` is the
contracted arc

\[
 a=(T^-\to T^+;L,P_L),qquad
 o(a)=P_L\cup T^-,\quad n(a)=P_L\cup T^+.          \tag{2.1}
\]

For binary arc variables `xi_a`, impose owner conservation and root
simplicity:

\[
 \sum_{a:T^-(a)=T}\xi_a=
 \sum_{a:T^+(a)=T}\xi_a,                           \tag{2.2}
\]

\[
 \sum_{a:L(a)=L}\xi_a\le1.                        \tag{2.3}
\]

Define

\[
 \Delta_\xi^{ord}(U)=\sum_a\xi_a
 \bigl(\mathbf1_{n(a)=U}-\mathbf1_{o(a)=U}\bigr). \tag{2.4}
\]

### Theorem 1 (ordinary full-palette augmenting criterion)

Within the declared one-endpoint-per-root contracted-arc class, a guarded
root-simple ordinary circulation is a loss-safe full-palette augmentation
exactly when its final factor is zero-one, degree-exact, protected and
connected after adjoining the exceptional bank, and

\[
 \boxed{m_F^{ord}(U)+\Delta_\xi^{ord}(U)\ge1
        \quad(U\text{ currently covered}),}        \tag{2.5}
\]

while at least one current hole has positive final multiplicity. To protect
the authenticated core independently of any seam recourse, retain the hard
rows

\[
 m_F^{ord}(U)+\Delta_\xi^{ord}(U)\ge1
        \qquad(U\in\mathcal U_{\neg D}).            \tag{2.6}
\]

For terminal completion replace “currently covered” in (2.5) by every
`U in U_10`.

#### Proof

Equations (2.2)--(2.3) are exactly the alternating-incidence degree ledger
for this contracted-arc class; they are not asserted to encode every
arbitrary ordinary option replacement. Equation (2.4) is the simultaneous
multiplicity change. Thus (2.5) is equivalent to retaining the current
support, and the strict-hole condition is equivalent to a support gain. The
remaining properties are literal hard guards. \(\square\)

Forcing an arc with `n(a)=U` for a missing target turns pricing into an
owner-return problem. Duplicate capacities and singleton debts must be
aggregated over the complete circuit. A shortest path or bounded debt
automaton is a pricing accelerator only; final replay of (2.5) is the
acceptance oracle.

### Exact ordinary target rows

For `U in U_10`, every pair `{a,b} subset U` gives the diamond

\[
 L=U-\{a,b\},\qquad T=U-\{a\},\qquad H=U-\{b\}.
\]

The ordinary provider row is

\[
 \boxed{
 \sum_{\substack{\{a,b\}\subset U\\U-\{a,b\}\notin\{M,D\}}}
 p_{U-\{a,b\},\{U-\{a\},U-\{b\}\}}\ge1.}         \tag{2.7}
\]

Its width is

\[
 45-\mathbf1_{D\subset U}-\mathbf1_{M\subset U}.  \tag{2.8}
\]

Among the 36 `D`-superset rows, 28 have width 44 and the eight containing
`B=M union D` have width 43. Requiring all rows (2.7) is stronger than a
chosen opening: it is independent of both licensed orientations and uses no
exceptional provider.

## 3. Licensed `D/M` seam states

In the normalized face

\[
 D=255,\qquad M=383,\qquad B=511,
\]

and `M--B` is protected. Let the three selected neighbours of `D` be

\[
 D+t,\qquad D+s,\qquad D+h,
\]

where the unique `M`-to-`D` tail enters through `D+t`. The two licensed
orientations traverse the cycle from `D` through `D+s` or through `D+h`.
Their internal opened and cyclic-closing occurrences are

\[
 I_0=D\cup\{t,s\},\qquad C_0=D\cup\{8,h\},
\]

\[
 I_1=D\cup\{t,h\},\qquad C_1=D\cup\{8,s\}.         \tag{3.1}
\]

Thus orientation recourse has factor-incidence support zero but currents

\[
 \Delta^{open}_{0\to1}=[I_1]-[I_0],                \tag{3.2}
\]

\[
 \Delta^{cyc}_{0\to1}=[I_1]+[C_1]-[I_0]-[C_0].    \tag{3.3}
\]

Let

\[
 m^{open}_{F,o}(U)=m_F^{ord}(U)+\mathbf1_{I_o=U},  \tag{3.4}
\]

\[
 m^{cyc}_{F,o}(U)=m_F^{ord}(U)
   +\mathbf1_{I_o=U}+\mathbf1_{C_o=U}.             \tag{3.5}
\]

The closing occurrence is not consecutive in the opened chronology and
must not appear in (3.4). Full physical-cycle rank ten does not imply full
opened rank ten.

### Theorem 2 (seam-aware loss-safe criterion)

For mode `chi in {open,cyc}`, an ordinary circulation `z` and final licensed
orientation `o'` are a loss-safe augmentation exactly when all factor,
guard and topology rows hold and

\[
 \boxed{
 m^\chi_{F,o}(U)+\Delta_z^{ord}(U)
 +\Delta_{o\to o'}^\chi(U)\ge1
 \quad(U\text{ currently covered}),}              \tag{3.6}
\]

with a strict gain on at least one current hole. Terminal completion uses
all `U in U_10`. The 19,412 rows (2.6) remain hard.

Both licensed orientations must be tested before asserting a positive
factor-support lower bound: (3.2) is a zero-support augmentation. At a fixed
factor the opened seam supplies at most one of the 36 exceptional targets;
the physical cycle supplies at most two.

For the authenticated q1-zero factor, the selected `D` owners are

```text
8447, 33023, 65791
```

and the tail enters through `33023`. Hence the two opened seam colours are
`41215` and `98559`; the corresponding closing colours are `66047` and
`8703`. Ordinary coverage is 19,425, so either opened orientation initially
has 22 holes and either physical cycle has 21.

## 4. Controlled exceptional incidence moves

Let `y_(M,T)` and `y_(D,T)` be the selected exceptional incidences. The
ordinary owner ledger is

\[
 \boxed{b_T^{ord}=2-y_{M,T}-y_{D,T}.}               \tag{4.1}
\]

In the normalized protected face, `y_(M,B)=1` is fixed and no `M` move is
licensed. Replacing one selected `D` incidence by another creates an owner
imbalance which must be closed by an ordinary alternating return path. Its
q1 effect is not root-local at `D`: reconstruct the final lollipop, identify
the tail incidence and recompute (3.1).

If a larger boundary branch licenses an `M` move, let its selected owner be
`A`. The internal occurrence is still the consecutive pair through `D`,
while the cyclic closing occurrence is the union of the terminal `D` owner
with `A`, counted only when it has rank ten. This is outside the frozen `MB`
face and requires separate boundary authorization.

A completeness-safe signed-incidence formulation uses `z_(L,T)` with

\[
 \sum_{T\supset L}z_{L,T}=0,qquad
 \sum_{L\subset T}z_{L,T}=0,                       \tag{4.2}
\]

\[
 -F_{L,T}\le z_{L,T}\le1-F_{L,T},                 \tag{4.3}
\]

and fixes `z=0` on protected incidences. Ordinary roots use (2.4);
exceptional colour deltas are computed only from the final licensed seam
state.

## 5. Completeness-safe full option master

Let `Omega_lic` be the complete finite set of boundary-licensed exceptional
states. A state `o` records its `M` owner `T_M(o)`, its three-owner set
`S_D(o)`, and its semantic tail, two directed `D` branches, internal
occurrence `I_o`, and (in cyclic mode) closing occurrence `C_o`. Use binary
variables:

- `y_(M,T)` for the unique `M` incidence;
- `y_(D,T)` for the three `D` incidences;
- `p_(L,{T,H})` for one owner pair at every ordinary root;
- `sigma_o` for `o in Omega_lic`;
- `h_U` for uncovered targets.

Thus `y,p,sigma,h` are all in `{0,1}`. For a linear relaxation it is enough
to retain `0 <= h_U <= 1`; `h` is never an unrestricted slack.

The exact degree rows are

\[
 \sum_{T\supset M}y_{M,T}=1,qquad
 \sum_{T\supset D}y_{D,T}=3,                       \tag{5.1}
\]

\[
 \sum_{\{T,H\}\in\mathcal O_L}p_{L,\{T,H\}}=1
        \quad(L\ne M,D),                           \tag{5.2}
\]

\[
 \sum_{\substack{L,\{T,H\}\ni T}}p_{L,\{T,H\}}
 =2-y_{M,T}-y_{D,T}.                               \tag{5.3}
\]

Choose exactly one seam state and channel it to the selected exceptional
incidences and the semantic tail/cycle roles:

\[
 \sum_{o\in\Omega_{lic}}\sigma_o=1,
 \quad y_{M,T}=\sum_{o:T_M(o)=T}\sigma_o,
 \quad y_{D,T}=\sum_{o:T\in S_D(o)}\sigma_o.       \tag{5.4}
\]

The opened coverage rows are

\[
 \boxed{
 \sum_{\substack{L,\{T,H\}\\T\cup H=U}}
 p_{L,\{T,H\}}
 +\sum_o\sigma_o\mathbf1_{I_o=U}+h_U\ge1.}        \tag{5.5}
\]

For a physical-cycle master, add
`sum_o sigma_o 1[C_o=U]`; never add it to an opened row.
Set

\[
 h_U=0\quad(U\in\mathcal U_{\neg D}),
 \qquad \min\sum_{U\in\mathcal U_D}h_U.           \tag{5.6}
\]

Terminal completion fixes every `h_U=0`.

A missing target separates precisely row (5.5). A disconnected state, or a
state whose tail/branch labels disagree with the ordinary options, returns
a semantic no-good or topology cut on the joint variables `(p,sigma)`, not
on `sigma` alone. With every finite joint topology cut admitted, this option
master is complete for its licensed boundary face. Bounded circuits and
debt automata are only column-generation views.

For compatible root-disjoint circuit packets, or a packet whose final
signature was recomputed jointly, columns `lambda_C` obey

\[
 m^\chi_{F,o}(U)+\sum_C\delta_C^\chi(U)\lambda_C
 \ge1.                                              \tag{5.7}
\]

Overlapping base-relative signatures are not additive; represent the whole
packet as one replayed column or use the final option master.

## 6. Residual Benders rows and literal complements

Let \(\mathcal R_0={{[17]}\choose8}\setminus\{M,D\}\), and let

\[
 s(T)=y_{M,T}+y_{D,T},qquad b_T^{ord}=2-s(T).
\]

Make the primary channel literal. For every ordinary option occurrence `e`,
use `x_e in {0,1}` with `x_e <= p_e`. For a licensed state use seam-provider
variables `q_o^I,q_o^C in {0,1}`:

\[
 q_o^I\le\sigma_o,\qquad
 q_o^C\le\sigma_o\quad\hbox{(cyclic mode only)}.    \tag{6.1}
\]

Writing `R(e)` for the rank-ten colour of occurrence `e`, require one actual
provider per target:

\[
 \sum_{e:R(e)=U}x_e+\sum_{o:I_o=U}q_o^I
 +\mathbf1_{\chi=cyc}\sum_{o:C_o=U}q_o^C=1
 \qquad(U\in\mathcal U_{10}).                     \tag{6.2}
\]

Let \(E_\chi\) be the selected occurrence-root set: it consists of the
24,308 ordinary occurrences and the internal seam occurrence in opened
mode, and additionally the closing seam occurrence in cyclic mode. Thus
\(|E_{open}|=24{,}309\) and \(|E_{cyc}|=24{,}310\). Let
`d_T^chi(sigma)` be the owner degree contributed by those selected seam
occurrences. The literal residual owner capacity is

\[
 c_T^\chi=2-y_{M,T}-y_{D,T}+d_T^\chi(\sigma)
           -\deg_x(T)-\deg_q(T)\ge0,              \tag{6.3}
\]

with the balanced ledger

\[
 \sum_Tc_T^\chi=2(|E_\chi|-19{,}448).              \tag{6.4}
\]

For root-injective actual-provider variables satisfying these channel and
capacity rows, let \(N(L)\) be the full owner star above \(L\), and put

\[
 w_Y(L)=\bigl(2-|N(L)\setminus Y|\bigr)_+,\qquad
 W_0(Y)=\sum_{L\in\mathcal R_0}w_Y(L),
 \qquad
 \alpha_Y(e)=|\partial e\cap Y|-w_Y(L(e)).
\]

The exact owner-shore deficiency is

\[
 \boxed{
 \Psi(Y)=W_0(Y)-2|Y|+
 \sum_{T\in Y}(y_{M,T}+y_{D,T})
 +\sum_e\alpha_Y(e)x_e.}                           \tag{6.5}
\]

For the standard residual max-flow network, the max-flow is full exactly
when

\[
 \boxed{\Psi(Y)\le0\quad\hbox{for every owner shore }Y.} \tag{6.6}
\]

Necessity is the cut bound. Sufficiency is max-flow/min-cut after the total
ledger (6.4); nonnegative capacities exclude hidden owner deficits. Thus a
maximizing shore is an exact polynomial separator for a fixed
`(p,sigma,x,q)` incumbent.

If the exceptional bank is fixed, its term moves to the right. If it
changes, its variables must remain in every Benders row and the ordinary
factor complement must be rebuilt.

An internal or closing seam occurrence is an occurrence-labelled root with
two distinct endpoint owners. For every shore its trapped-root weight is the
number of its endpoints in the shore, so eliminating that selected or
unselected occurrence gives selector coefficient zero. The seam marks
therefore change provider colours and topology but cancel from (6.5).

Suppose a full opened factor has one actual provider for every target and
the primary is channelled to those occurrences. Then:

| layer | factor edges | primary edges | residual edges | flow |
|---|---:|---:|---:|---:|
| opened path | 24,309 | 19,448 | 4,861 | 9,722 |
| physical cycle | 24,310 | 19,448 | 4,862 | 9,724 |

For the opened layer the primary forest has 4,862 components and the
residual complement has contracted rank 4,861, yielding one path. For the
cycle, the residual complement closes that path into one cycle. The literal
factor-minus-primary complement saturates every residual capacity, so the
corresponding maximum residual flow is full and every row (6.6) is
nonpositive.

Fail-closed opened acceptance is:

1. replay all incidence degrees, protected edges, guards and connectivity;
2. reconstruct the two licensed seam roles and choose one orientation;
3. replay all 19,448 opened rows (5.5), excluding the closing occurrence;
4. choose one actual provider per target and channel the primary to it;
5. build the literal opened complement and require max-flow 9,722;
6. replay contracted rank 4,861 and the single opened path.

A smaller min-cut contradicts a claimed literal complement and exposes a
channel, seam, boundary or decoder error. Without the complement channel it
is a genuine Benders separator.

## 7. Minimum support and no-go scope

### Theorem 3 (smallest nonzero incidence circuit)

A licensed orientation reversal has factor-incidence support zero. Once the
seam state is fixed, every nonzero zero-boundary simple-incidence exchange
has at least three root vertices and toggles at least six incidences.

#### Proof

Every balanced nonzero exchange decomposes into alternating cycles in the
rank-eight/rank-nine inclusion graph. Two distinct rank-eight roots have at
most one common rank-nine owner: if their union has rank nine it is the
unique common owner, and otherwise there is none. Hence the inclusion graph
has no C4; its shortest cycle is a C6, with three root vertices and three
owner vertices. Alternation toggles one old and one new incidence at each
root. A controlled D switch plus its ordinary return is subject to the same
cycle bound. In the frozen normalized MB face, M moves are not licensed.
\(\square\)

Therefore a bounded ordinary C6/C8 failure is only a bounded-class no-go. A
global no-go must test both opened orientations and every state of the
complete semantic option master, including joint \((p,\sigma)\) topology
cuts.

## 8. Independently replayed terminal closure

The frozen ordinary-only loss-safe chain from the authenticated q1-zero
factor increased ordinary coverage as follows:

~~~text
19425,19427,19429,19431,19433,19435,19437,19439,
19441,19443,19444,19445,19446,19447,19448.
~~~

The terminal model is

~~~text
/home/amodo/or15/work/root_k17_fullq1_ordinary_circulation_20260802/
  fullq1_13.best.model
SHA-256 e7ea3841cde04129e3b0af008da0ab2ca2deb8936f09ae22d43a9174ac888a31
~~~

The last augmentation is a lossless connected support-five return for mask
66047, with roots

~~~text
66011,66041,73977,73947,67803.
old incidence variables: 116042,116128,131502,131411,118942
new incidence variables: 116039,116134,131500,131415,118938
~~~

An independent search-free O3 replay in

~~~text
/home/amodo/or15/work/r2_k17_fullq1_13_independent_20260802
~~~

verified all root/owner degrees, the protected M/D bank, all 16,261 guard
clauses, one augmented incidence component, and all 19,448 ordinary provider
rows. Its audit JSON has SHA-256
469157e326d7ac75caf742ba68373fe6ceb4e7e72051adfca93c8a658e7599de;
the verifier source has SHA-256
bdd2d9f36086b7d9be8e314bd05a197fdec133aab2dc6e9fc65da252fcb32427.
The provider multiplicities are:

~~~text
m=1:15128, m=2:3816, m=3:471, m=4:30, m=5:3.
~~~

In particular all 19,412 non-D targets and all 36 D-superset targets have an
ordinary provider. The selected exceptional incidences remain

~~~text
M:[511], D:[8447,33023,65791],
~~~

but the final semantic tail enters through 8447. The two final
(internal,closing) seam pairs are

~~~text
(41215,66047), (73983,33279).
~~~

Each of these four colours already has an ordinary provider, so both
licensed opened palettes and both physical-cycle palettes are
19,448/19,448.

A second independent literal-complement replay deterministically selected
the first ordinary provider for each target. For each orientation it found:

~~~text
primary forest             19,448 edges / 4,862 components
opened residual quotient    4,861 edges / one path / flow 9,722
cyclic residual quotient    4,862 edges / one cycle / flow 9,724
~~~

Its source and audit JSON SHA-256 values are respectively
80b91e6fdf86adb981b0f830495d9575f92f26513d5f4cba985bf4c2d9fd626f
and
976c52ca38964477e933a9df9fdcee98f8e8369511133c2b1e535bcc4cc9f97e.
This is a literal witness to every residual shore row, not merely a target
count.

## 9. Exact scope

The ordinary-only terminal factor closes full rank ten for both openings
without exceptional-provider recourse. Seam-aware completion of (5.5) in
general closes only its selected opened orientation. The frozen terminal
factor is still massively nonresident, and nothing here establishes ranks
11--17, source antecedents, a lower or terminal compiler, exterior
cross-windows, regeneration, a universal word, or \(\nu(17)=24313\).
