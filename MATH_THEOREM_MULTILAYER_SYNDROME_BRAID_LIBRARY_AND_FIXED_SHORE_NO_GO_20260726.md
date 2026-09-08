# Multilayer syndrome braids create exponential order entropy, but not a usable double factor

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The only plausible escape from the finite-order-library ceiling is real:
many syndrome-(Q_4) braid banks can be composed on an already mixed
factor.  With (L) phase-disjoint braid layers one obtains an exact
common-phase isometric (C_{2h})-factor with as many as

\[
                              2^L                            \tag{0.1}
\]

cyclic direction-order types.  Taking (L=2d) supplies the order entropy
required by the aligned depth-(d) counting bound.  Thus owner support and
common phase do **not** keep the library subexponential.

There is nevertheless a rigorous obstruction to feeding this **one-bit,
phase-disjoint** library into the affine double-factor compiler.  Its
global same-vertex direction permutation is a product of one transposition
per active quartet.  It fixes at least half of all
directions.  The affine context trace then has an invisible parity subgroup
on a positive fraction of every collection of cyclic windows.  At every
depth (d\to\infty), at least (1/3-o(1)) of all aligned starts remain in
nontrivial fibres, even though the order library is exponential.

So the exact verdict is two-sided:

* **positive:** a dense multilayer braid network defeats the order-library
  ceiling;
* **negative:** this one-bit phase-disjoint use of the (Q_4) generator
  cannot simultaneously give
  the nearly fixed-point-free shore permutation needed by the parity
  complete-mapping trace code.

A later four-shore audit exhibits a second independent twist on (Q_4),
whose opposite shore is fixed-point-free.  That result lies outside the
one-bit atlas proved here: both twists cannot be installed as disjoint
four-letter syndrome blocks, because the two equal-column relations make
the four-column syndrome sum zero and repeat a phase.  A surviving compiler
therefore needs an overlapping composition theorem for that four-shore
primitive, or a non-affine ownership identity which has no fixed-(S)
invisible subgroup.

## 1. Syndrome coordinates and many independent braid generators

Let (h=2^t), and enumerate (mathbb F_2^t) as

\[
                         g_0,g_1,\ldots,g_{h-1},qquad g_0=0.       \tag{1.1}
\]

Use the standard syndrome map

\[
\begin{aligned}
 \phi(e_j)&=(g_j+g_{j-1},0) &&(1\le j<h),\\
 \phi(e_h)&=(g_{h-1},1),
\end{aligned}                                                    \tag{1.2}
\]

and put (K=\ker\phi).  Then

\[
                         |K|=\frac{2^h}{2h}.                      \tag{1.3}
\]

The standard translates of the cycle with word
(1,2,\ldots,h,1,2,\ldots,h), indexed by (K), form an exact
isometric (C_{2h})-factor.

Choose (L) disjoint consecutive ordered quartets

\[
 Q_s=(\alpha_s,\beta_s,\gamma_s,\delta_s),qquad 1\le s\le L,   \tag{1.4}
\]

away from direction (h), and arrange the enumeration so that

\[
                  \phi(e_{\beta_s})=\phi(e_{\delta_s}).          \tag{1.5}
\]

Then

\[
                         v_s=e_{\beta_s}+e_{\delta_s}\in K       \tag{1.6}
\]

is the translation pairing for a literal common-phase (Q_4) braid.
Within (Q_s), that braid replaces

\[
 \alpha_s,\beta_s,\gamma_s,\delta_s
 \quad\hbox{by}\quad
 \alpha_s,\delta_s,\gamma_s,\beta_s.                            \tag{1.7}
\]

The (v_s)'s are linearly independent because they have disjoint
supports.

### Lemma 1.1 (existence of (h/4-O(1)) layers)

The enumeration in (1.1) can be chosen so that (1.5) holds for every

\[
                         L\le h/4-1.                              \tag{1.8}
\]

#### Proof

Fix a two-dimensional subspace (U\le\mathbb F_2^t).  Its nonzero
cosets give (h/4-1) disjoint affine planes.  The four elements of every
affine plane have sum zero.  Put the four elements of (L) such planes
in the positions

\[
 (g_{4s-3},g_{4s-2},g_{4s-1},g_{4s}),qquad1\le s\le L,          \tag{1.9}
\]

and fill the unused positions arbitrarily with the remaining group
elements.  For the corresponding direction quartet,

\[
 (g_{4s-2}+g_{4s-3})
 =(g_{4s}+g_{4s-1}),                                               \tag{1.10}
\]

which is exactly (1.5).  \(\square\)

## 2. Coset-constant composition

Put

\[
                         V=\langle v_1,\ldots,v_L\rangle\le K.   \tag{2.1}
\]

For every coset (c\in K/V), choose an arbitrary word

\[
                         \varepsilon(c)\in\mathbb F_2^L.         \tag{2.2}
\]

At layer (s), switch **all** (v_s)-paired braid components inside the
coset (c) if and only if (arepsilon_s(c)=1).  Do this in both
antipodal halves of the standard direction word.

### Theorem 2.1 (multilayer braid composition)

The choices (2.2) produce one exact common-phase factor of (Q_h) into
isometric (C_{2h})'s.  A cycle whose phase-zero syndrome index lies in
(c) has half-order obtained from (1,2,\ldots,h) by applying exactly
the local substitutions (1.7) with (arepsilon_s(c)=1).  Consequently
the number of order types is

\[
 \boxed{
 K_{\rm ord}=|\{\varepsilon(c):c\in K/V\}|
 \le\min\{2^L,|K/V|\}.}                                         \tag{2.3}
\]

In particular, if

\[
                         2L\le h-t-1,                             \tag{2.4}
\]

then the assignment can realize all (2^L) order types.

#### Proof

At each of the two affected boundaries inside quartet (s), the new
matching on the cycle-index set (K) is either the identity or translation
by (v_s), restricted to one (V)-coset.  It is a perfect matching because
the decision is constant on that coset, hence in particular constant on
every (v_s)-pair.  The first translation enters the other row of the
literal two-row braid and the second leaves it; the net cycle-index
displacement across the quartet is

\[
                              v_s+v_s=0.                         \tag{2.5}
\]

Different layers use disjoint phase boundaries, so all their physical
edge replacements are simultaneously valid.  Every layer has returned to
the original cycle index before the next quartet is entered, and the
antipodal half repeats the same decisions.  Thus the path closes after
(2h) steps.  In each half,
every physical direction is used exactly once: (1.7) changes only the
order within a quartet.  Hence the two half-words agree and form a
doubled permutation, proving isometry and exact cycle length.

Every phase class is unchanged and every phase-to-phase matching is
perfect, so the cycles cover every owner exactly once.  Distinct bit
words in (2.2) change different disjoint local quartets and hence give
distinct cyclic orders.  Finally,

\[
 |K/V|=2^{h-t-1-L},                                                \tag{2.6}
\]

so (2.4) is exactly the condition (|K/V|\ge2^L).  \(\square\)

### Corollary 2.2 (the entropy ceiling can be met)

For (d=o(h)), take (L=2d).  Conditions (1.8) and (2.4) hold for all
sufficiently large (h), and the factor has (4^d) order types.  This
meets, up to the harmless factor (2h), the necessary order-library size
(4^d/(2h)) from the aligned trace ceiling.

This also answers the composition question literally: later layers remain
legal on factors already mixed by earlier layers because all layer
translations commute inside (V), and every switching decision is
constant on the whole (V)-coset.

## 3. The induced double factor

Complement all (L) braid bits:

\[
                         \varepsilon'(c)=\varepsilon(c)+\mathbf1. \tag{3.1}
\]

Let (G_0,G_1) be the two multilayer factors corresponding to
(arepsilon,arepsilon'), with their common phase colouring.  Define

\[
                         S=\prod_{s=1}^L(\beta_s\ \delta_s).     \tag{3.2}
\]

### Proposition 3.1 (exponential-library double factor)

The factors (G_0,G_1) satisfy both same-vertex relations

\[
 \delta^+_1(y)=S\delta^+_0(y),\qquad
 \delta^-_1(y)=S\delta^-_0(y).                                  \tag{3.3}
\]

They therefore meet the bidirectional hypotheses of the exact
double-factor recursion.  Both have (K_{\rm ord}) order types.

#### Proof

Within every active quartet, complementing its braid bit exchanges the
two words in (1.7), which is precisely the coordinate transposition
((\beta_s\ \delta_s)) at the same common phases.  The quartets are
disjoint, so their transpositions commute and give (3.2).  Outside the
active quartets the factors agree and (S) fixes the direction.  Shifting
one phase back proves the incoming identity.  \(\square\)

Thus exponential order entropy is compatible with exact ownership,
common phase, isometry, and the recursive double-factor equations.

## 4. The fixed-shore trace obstruction

The permutation (3.2) moves only (2L) directions.  Even at the maximum
disjoint-layer density (L=h/4-1), it fixes at least (h/2) directions:

\[
                         f:=|\operatorname {Fix}S|=h-2L\ge h/2. \tag{4.1}
\]

Apply the affine parity complete-mapping compiler to
((G_0,G_1,S)).  For a completed support (J), its physical trace fibre
contains the invisible subgroup

\[
 \{z:\ |z|\equiv0,
       \operatorname {supp}z\subseteq J\cap S^{-1}J\},           \tag{4.2}
\]

of order (2^{\max\{|J\cap S^{-1}J|-1,0\}}).  In particular every
fixed direction of (S) lying in (J) contributes to this subgroup.

### Theorem 4.1 (exponential library still has linear trace deficit)

For every (1\le d<h), at least one third of the cyclic length-(d)
windows in every order type satisfy

\[
                         |J\cap\operatorname {Fix}S|\ge d/4.    \tag{4.3}
\]

Consequently, as (d\to\infty), the aligned trace collision deficit of
the affine parity lift is at least

\[
                         \boxed{(1/3-o(1)),2^{2h-1}.}            \tag{4.4}
\]

#### Proof

Fix one cyclic order and let (k_a) be the number of fixed directions in
the length-(d) window starting at phase (a\in\mathbb Z_h).  Every fixed
direction occurs in exactly (d) windows, so

\[
                         \frac1h\sum_a k_a=\frac{df}{h}\ge d/2. \tag{4.5}
\]

If a proportion (ho) of the windows have (k_a\ge d/4), then, using
(k_a\le d),

\[
                         d/2\le \rho d+(1-\rho)d/4,
\]

and hence (ho\ge1/3).  This proves (4.3).

On every such window, (4.2) has order at least
(2^{d/4-1}).  Its action fixes the phase point (y), the completed
support, and both outside restrictions, so each orbit is contained in one
literal trace fibre and remains inside the same bad phase.  The common
phase classes are equicardinal.  Therefore at least one third of the
(2^{2h-1}) aligned starts are partitioned into trace fibres of size at
least (2^{d/4-1}).  The number of distinct traces on those starts is at
most their number divided by this quantity.  Subtraction gives (4.4).
\(\square\)

The same argument applies to upper traces and to the reversed aligned
windows.

## 5. Exact boundary

The multilayer experiment has a decisive answer.

1. There is no owner-support or common-phase invariant forcing the order
   library to be polynomial: Theorem 2.1 realizes (2^L) types.
2. Exact braid components really can be composed on an already mixed
   factor, provided the switches are phase-disjoint and their decisions
   are constant on the joint translation cosets.
3. Exponential order count alone is insufficient.  The disjoint one-bit
   (Q_4)
   atlas changes only two of four directions per layer, so its global
   shore involution fixes at least half the coordinates, and Theorem 4.1
   is statewise.

Accordingly the next finite target is not “more layers of the same
one-bit braid.”  It is an overlapping composition of the fixed-point-free
four-shore primitive.  The crossed product recursion presently proposed
for that purpose must additionally satisfy the same-owner relation; a
mere exchange of the active left/right half does not do so.
