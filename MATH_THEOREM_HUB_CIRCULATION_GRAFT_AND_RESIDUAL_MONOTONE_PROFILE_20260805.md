# Hub-cycle grafting: exact state balance and the residual monotone profile

**Date:** 2026-08-05  
**Method:** circulation addition and a direct monotone-polytope calculation;
no computation  
**Status:** unconditional fractional graft theorem and exact conditional
integral splice theorem.  The protected coloured hub cycle can be reserved
before rounding without reopening the stationary age-state or rank-marginal
gate.  Named-target one-copy rounding of the residual circulation remains
open.

## 0. Outcome

Let

\[
 r=\lceil k/2\rceil,\qquad
 W={k\choose r},
\]

let \(d=d(k)\), and let

\[
 N_s={k\choose s}-b_s
 \qquad(1\le s<r)                                    \tag{0.1}
\]

be the integral residual rank demands after the optimal triangular Ferrers
boundary.  Thus

\[
 q_s={N_s\over W}
\]

is nondecreasing, lies in \([0,1]\), and satisfies

\[
                         \sum_{s<r}q_s\le d.          \tag{0.2}
\]

Put

\[
 v_H(s)={\bf1}_{\{r-d,\ldots,r-1\}}(s),              \tag{0.3}
\]

the complete rank profile of one occurrence of the hub type

\[
                         H=(r-d,1,\ldots,1).
\]

Reserve a literal hub cycle of length \(L=O(d)\), marking all of its
proper suffix ranks.  It contributes exactly \(Lv_H\) to the rank ledger
and is an integer circulation by itself.

The residual normalized vector is

\[
 q^{\rm res}_s
 ={N_s-Lv_H(s)\over W-L}.                            \tag{0.4}
\]

The main result is:

\[
                         q^{\rm res}\in M_{r,d}       \tag{0.5}
\]

for every sufficiently large \(k\).  Hence the monotone-rotor theorem gives
a stationary literal residual circulation on the remaining owner mass.
Adding the protected hub cycle preserves divergence zero at every age state
and restores exactly the original integral rank totals \(N_s\).

This closes the fractional functional predecessor/state-balance gate after
the coloured reset.  It does not make the residual named-target loads
integral.

## 1. An exact cycle-grafting lemma

Let \(D=(V,E)\) be any directed literal-state graph.  For an arc multiset
\(x\), write \(\partial x\in\mathbb Z^V\) for head count minus tail count.
Let \(w:E\to\mathbb Z^a\) be any additive resource profile.

### Lemma 1.1 (zero-boundary graft)

Suppose \(x_R\) and \(x_H\) are nonnegative integral arc multisets with

\[
                         \partial x_R=0,
 \qquad
                         \partial x_H=0.              \tag{1.1}
\]

Then

\[
                         x=x_R+x_H                   \tag{1.2}
\]

is an integral circulation and

\[
                         w(x)=w(x_R)+w(x_H).          \tag{1.3}
\]

The same statement holds for nonnegative rational circulations.

#### Proof

Both assertions follow by linearity of \(\partial\) and \(w\). \(\square\)

Although elementary, this is the correct quantifier for the hub reset.
The hub is a complete directed cycle, so it exports no state boundary.
It may therefore be reserved before the residual stationary factor is
chosen.

A post hoc instruction to “replace \(L/(d+1)\) canonical cycles” is not
proof-safe when \(L\not\equiv0\pmod{d+1}\): the displayed number of donor
cycles is then not integral.  One must subtract \(L\) *role occurrences*
and solve the residual circulation, as in (0.4).

## 2. Exact residual-polytope criterion

Recall

\[
 M_{r,d}=
 \left\{
 x:\ 0\le x_1\le\cdots\le x_{r-1}\le1,\
 \sum_{s<r}x_s\le d
 \right\}.                                           \tag{2.1}
\]

### Theorem 2.1 (hub subtraction preserves monotonicity)

Assume

\[
\begin{aligned}
 N_s&\ge L
       &&(r-d\le s<r),\\
 W-N_s&\ge L
       &&(1\le s<r-d),\\
 N_{r-d}-N_{r-d-1}&\ge L
       &&\text{when }r-d-1\ge1.
\end{aligned}                                        \tag{2.2}
\]

Then the vector \(q^{\rm res}\) in (0.4) belongs to \(M_{r,d}\).

#### Proof

For \(s<r-d\),

\[
                         q^{\rm res}_s={N_s\over W-L}.
\]

The second line of (2.2) gives \(q^{\rm res}_s\le1\); nonnegativity is
automatic.  For \(s\ge r-d\),

\[
                         q^{\rm res}_s={N_s-L\over W-L}.
\]

The first line of (2.2) gives nonnegativity, and \(N_s\le W\) gives the
upper bound one.

Within the low band and within the high band, monotonicity follows from
the monotonicity of \(N_s\), because the same affine formula is used
throughout each band.  At the unique interface, the final line of (2.2)
gives

\[
 {N_{r-d-1}\over W-L}
 \le
 {N_{r-d}-L\over W-L}.                               \tag{2.3}
\]

Finally,

\[
\begin{aligned}
 \sum_{s<r}q^{\rm res}_s
  &={\sum_{s<r}N_s-Ld\over W-L}\\
  &\le {dW-Ld\over W-L}=d,                           \tag{2.4}
\end{aligned}
\]

using (0.2).  This proves every inequality in (2.1). \(\square\)

### Corollary 2.2 (the criterion holds for the \(O(d)\) reset)

Let \(L=O(d)\), with \(d=O(\sqrt k)\), and use the left-filled Ferrers
boundary, so \(b_1\ge b_2\ge\cdots\ge0\) and \(b_s\le d\).  Then (2.2)
holds for every sufficiently large \(k\).

#### Proof

The first line follows from

\[
 N_{r-d}\ge {k\choose r-d}-d,
\]

which grows exponentially in \(k\), whereas \(L+d=O(\sqrt k)\).
For the second line it is enough to check the largest low rank:

\[
 W-N_{r-d-1}
 \ge {k\choose r}-{k\choose r-d-1},
\]

again exponentially larger than \(L\).

At the interface, monotonicity of the Ferrers correction gives

\[
\begin{aligned}
 N_{r-d}-N_{r-d-1}
 &=
 {k\choose r-d}-{k\choose r-d-1}
   +b_{r-d-1}-b_{r-d}\\
 &\ge
 {k\choose r-d}-{k\choose r-d-1},                   \tag{2.5}
\end{aligned}
\]

and the positive adjacent-binomial difference is exponentially larger than
\(L\).  These estimates prove (2.2) for all sufficiently large \(k\).
\(\square\)

No asymptotic subtlety is hidden here: one may use (2.2) itself as the exact
finite-dimensional aperture test.

## 3. Stationary graft theorem

### Theorem 3.1 (fractional protected-hub graft)

Assume (2.2), and reserve the literal length-\(L\) hub necklace from
MATH_THEOREM_COLOURED_HUB_NECKLACE_AND_PROTECTED_OWNER_MATCHING_20260805.md.
Then there is a stationary literal marked-trace circulation with:

1. total owner mass \(W\);
2. the protected hub necklace occurring with integral multiplicity one;
3. total marked rank-\(s\) mass exactly \(N_s\) for every \(s<r\); and
4. zero divergence at every literal age state.

#### Proof

Theorem 2.1 gives \(q^{\rm res}\in M_{r,d}\).  The monotone-rotor theorem
therefore supplies a normalized stationary literal circulation with marked
rank vector \(q^{\rm res}\).  Scale it by \(W-L\).  Its marked rank totals
are

\[
                         (W-L)q^{\rm res}
                         =N-Lv_H.                    \tag{3.1}
\]

The protected necklace is one directed literal cycle, so it is an integral
circulation.  Every one of its \(L\) occurrences has the complete hub mark
vector \(v_H\), and hence its total is \(Lv_H\).  Lemma 1.1 now gives a
stationary circulation with total marks \(N\) and zero divergence at every
state.  Its owner mass is \((W-L)+L=W\). \(\square\)

The residual circulation can be placed on the owner fibres not used by the
hub because the fractional labelled-lift theorem is valid on every fixed
rank-\(r\) owner separately.  This gives owner mass one on each fibre.
It does **not** make the residual named-target distribution uniform after
the explicitly named hub targets have been deleted; that is the remaining
coloured rounding problem.

### Theorem 3.2 (exact integral splice, conditional only on the residual)

Suppose, stronger, that the remaining owner and target roles admit an
integral stationary literal factor with exact marked rank totals

\[
                         N-Lv_H.                     \tag{3.2}
\]

Then adjoining the protected hub necklace gives an integral stationary
factor with exact totals \(N\), and it changes no in/out balance at any
residual age state.

#### Proof

Apply the integral form of Lemma 1.1.  The two factors may be taken on
disjoint owner-labelled state fibres, so even their vertex supports need
not interact. \(\square\)

Thus the hub itself creates no functional-predecessor debt.  All integral
difficulty is concentrated in constructing the residual factor (3.2).

## 4. What remains after the graft

The following rows are not consequences of stationary balance.

1. **Named-target deletion.**  The residual demand is zero on the \(Ld\)
   explicit hub targets and one on every other required target.  The
   monotone-rotor theorem controls rank marginals, not this nonuniform named
   vector.
2. **One-copy integral rounding.**  The residual circulation in Theorem 3.1
   is rational and may repeat owner and target labels.
3. **Component fusion.**  Lemma 1.1 deliberately leaves the hub as one
   protected Euler component.  Joining it to the residual component while
   preserving owner colours and payloads is a separate rainbow-fusion gate.
4. **Linear opening and upper guards.**  Opening the cyclic hub and
   protecting all exterior upper witnesses remain chronology questions.

The exact gain is nevertheless substantial: reserving the coloured
holonomy reset is compatible with the optimal fractional lower ledger and
with literal state balance.  Neither the rank polytope nor the de Bruijn
circulation has to be reopened.

