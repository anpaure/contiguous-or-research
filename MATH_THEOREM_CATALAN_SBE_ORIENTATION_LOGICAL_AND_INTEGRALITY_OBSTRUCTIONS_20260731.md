# Logical and integrality obstructions in the SBE endpoint-orientation system

Date: 2026-07-31  
Status: dimension-free fractional separation and bounded-cut-width theorem;
exact independently reconstructed obstructions on the authenticated chained
structural forests at `n=3,4`.  This note complements, and does not replace,
`MATH_THEOREM_THREAD_D_CATALAN_SBE_ENDPOINT_ORIENTATION_CUT_SYSTEM_20260731.md`.

## 0. Result

For a fixed undirected Catalan forest, simultaneous SBE is an exact Boolean
endpoint-cut system.  Its continuous relaxation still has two ordinary
min-cut separation oracles, but it is not integral in general.

On the authenticated `n=3` forest, the half-endpoint point is feasible on
both shores while no Boolean orientation is feasible.  More sharply, the
upper shore alone has two cuts which force `x_1=1` and `x_1=0`; the lower
shore has the dual contradiction on `x_0`.

On the authenticated `n=4` forest, the `475` effective feasible endpoint
states (or `7600` advertised orientations after four dummy singleton bits)
are not closed under AND, OR, coordinatewise majority, or ternary XOR.
Consequently this natural relation is respectively not Horn, dual-Horn,
bijunctive/2-SAT, or affine.  Its endpoint transversals also violate ordinary
matroid basis exchange.  Thus the exact generic algorithm exposed by the
orientation theorem is Boolean branch-and-cut with two min-cut separators,
not one 2-SAT, one ordinary min-cut, or one matroid-base computation.

There is a sharp positive face.  If every nontrivial endpoint cut sees at
most two path endpoint pairs asymmetrically, then every row is unary or
binary and the complete orientation problem is exactly 2-SAT.  This is the
largest universal cut-width bound with that conclusion: at width three a
row may already be a genuine three-literal clause.

None of these statements involves `Q`.  The correct order remains

\[
 F_{\rm undirected}\longrightarrow x_{\rm endpoints}
 \longrightarrow Q\longrightarrow \hbox{SDRs/rooted support}.
\]

## 1. Continuous endpoint-cut polytope

Use the notation and bit convention of the endpoint-orientation theorem.
For a non-singleton path with stored endpoints `(u_j,v_j)`, extend an
orientation bit to `0 <= x_j <= 1`.  Put upper terminal mass `x_j` at `u_j`
and `1-x_j` at `v_j`; put the complementary masses below.  A singleton
endpoint has terminal mass one, independently of its dummy bit.  Let
`z_x^sigma(D)` be the resulting terminal mass at middle vertex `D`.

Define

\[
 \mathcal P(F)=\left\{x\in[0,1]^K:
 R|\Gamma^\sigma(A)|+
 C\sum_{D\in\Gamma^\sigma(A)}z_x^\sigma(D)
 \ge N|A|
 \quad(\sigma\in\{-,+\},A\subseteq O^\sigma)
 \right\}.                                             \tag{1.1}
\]

### Theorem 1.1 (fractional separation)

Membership in `P(F)` has two polynomial min-cut separation oracles, one per
shore.  For fixed fractional `x`, give a middle vertex capacity

\[
             R+Cz_x^\sigma(D).                         \tag{1.2}
\]

Use source-to-outer capacity `N`, infinite outer-to-neighbour capacity, and
the capacities (1.2) to the sink.  A minimum cut is feasible exactly when
all rows in (1.1) hold; otherwise its source-side outer bank is a violated
row.

#### Proof

The maximum-weight-closure calculation used for an integral orientation
does not require integral sink capacities.  Choosing an outer family earns
`N|A|` and forces its entire neighbourhood, whose exact cost is the left
side of (1.1).  The maximum positive closure value is therefore the maximum
cut violation.  There are only two networks. `square`

The total middle capacity remains `NP`: every path contributes terminal
mass one, so

\[
 RM+CK=R(N+K)+CK=N(R+K)=NP.                           \tag{1.3}
\]

Hence (1.1) is precisely the continuous common-density face, not merely a
capacity relaxation with surplus mass.

### Theorem 1.2 (the cut-width-two 2-SAT face)

For one endpoint cut let its **Boolean boundary width** be the number of
non-singleton paths for which exactly one endpoint belongs to the cut
neighbourhood.  If every nontrivial row on both shores has boundary width
at most two, then simultaneous SBE is exactly a 2-SAT instance, including
the possibilities of a tautological row or immediate infeasibility.

With the min-cut separator, this face can be decided by a 2-SAT
branch-and-cut procedure using at most `O(K^2)` distinct clauses.

#### Proof

After the contributions from pairs with zero or two endpoints in the
neighbourhood are removed, a cut is

\[
                 \ell_1+\cdots+\ell_b\ge d,           \tag{1.4}
\]

where the `ell_i` are signed Boolean literals and `b<=2`.  For `b=0` the
row is constant.  For `b=1` it is tautological, contradictory, or a unit
clause.  For `b=2`, the only nontrivial cases are one binary disjunction or
two unit clauses.  Thus every row is 2-CNF.  Conversely every failed
integral candidate returns one of these clauses.  There are only
`O(K^2)` distinct unary/binary clauses, so the separation loop cannot add
more. `square`

Boundary width three is the first point where (1.4) can contain
`ell_1+ell_2+ell_3>=1`, whose satisfying relation is not closed under
majority and is not bijunctive.  Thus width two is the maximal universal
arity guarantee; special wider systems may of course still simplify.

## 2. Exact `n=3` integrality obstruction

Here

\[
 (M,N,P,C,R,K)=(20,15,6,14,1,5),                     \tag{2.1}
\]

and paths `3,4` are singletons.  Let `x_0,x_1,x_2` be the three effective
orientation bits.

### Proposition 2.1 (two-cut contradiction on either shore)

On the upper shore take the following two outer families:

\[
\begin{aligned}
 A_1&=\{1f,2f,37,3b,3e\}_{16},\\
 A_2&=\{2f,37,3b,3d,3e\}_{16}.
\end{aligned}                                         \tag{2.2}
\]

Both have five outer vertices and seventeen middle neighbours.  Four path
endpoint pairs lie wholly in each neighbourhood.  In the first cut only
the bit-one endpoint of path `1` is additionally present, while in the
second only its bit-zero endpoint is present.  The two SBE rows are

\[
\begin{aligned}
 17+14(4+x_1)&\ge75 &&\Longleftrightarrow&
 x_1&\ge1/7,\\
 17+14(5-x_1)&\ge75 &&\Longleftrightarrow&
 x_1&\le6/7.
\end{aligned}                                         \tag{2.3}
\]

For Boolean `x_1`, the first row forces `x_1=1` and the second forces
`x_1=0`.  Thus no orientation is upper SBE.

The lower shore has the exact dual contradiction on `x_0`, using

\[
 \{01,02,04,08,20\}_{16},\qquad
 \{02,04,08,10,20\}_{16}.                            \tag{2.4}
\]

#### Proof

The neighbourhood and endpoint-incidence counts are direct reconstruction
from the two occurrence graphs.  Substitution into the scaled Hall row
gives (2.3); (2.4) gives the same two inequalities in reverse order for
`x_0`. `square`

### Proposition 2.2 (literal fractional point)

The midpoint

\[
                    (x_0,x_1,x_2)=(1/2,1/2,1/2)      \tag{2.5}
\]

lies in `P(F)`.  Exhaustion of all `2^6` outer families on each shore gives
minimum slack zero.  Nevertheless Proposition 2.1 shows

\[
                \mathcal P(F)\cap\{0,1\}^5=\varnothing. \tag{2.6}
\]

Thus the endpoint-cut polytope is not integral, even though it has a
min-cut separation oracle.  In particular, total-unimodularity or a raw
generalized-polymatroid integrality argument cannot solve the unrestricted
orientation gate.

## 3. Exact `n=4` logical obstructions

There are ten effective path bits and four singleton dummy bits.  Exact
enumeration gives `475` effective simultaneous-SBE states, hence `7600`
advertised bitstrings.

Let a decimal mask record the full stored path order, with singleton bits
zero in the witnesses below.  Every listed input mask is feasible.

### Proposition 3.1 (failure of the four standard closure classes)

The following are exact:

\[
\begin{array}{c|c|c}
\text{closure}&\text{feasible inputs}&\text{infeasible output}\\ \hline
\wedge&16,8192&16\wedge8192=0\\
\vee&16,8200&16\vee8200=8216\\
\operatorname{maj}&16,147,573&\operatorname{maj}=17\\
\oplus_3&16,18,19&16\oplus18\oplus19=17.
\end{array}                                           \tag{3.1}
\]

Consequently the natural feasible-orientation relation is not Horn,
dual-Horn, bijunctive, or affine, respectively.

#### Proof

The exact two-min-cut replay accepts every input and rejects every output.
Horn solution relations are closed under AND; dual-Horn under OR;
bijunctive relations under coordinatewise majority; affine relations under
ternary XOR.  These closure properties persist under the introduction and
existential projection of auxiliary variables.  Therefore (3.1) excludes
the four representations on the natural endpoint relation. `square`

In particular, the majority counterexample rules out 2-SAT even with
existential auxiliary variables.  The AND/OR pair also shows that the
feasible family is not the minimizer lattice of one ordinary submodular
set function in the natural variables.  This does not contradict the two
min-cuts used to **separate one fixed orientation**.

### Proposition 3.2 (ordinary matroid basis exchange fails)

View an orientation as the `K`-element endpoint transversal which chooses
one endpoint of every path.  Masks `16` and `8192` are feasible.  Exchange
the path-4 endpoint selected by mask `16`.  The only exchange which remains
an endpoint transversal is its opposite endpoint, producing mask `0`,
which is infeasible.  Choosing an endpoint belonging to another path would
leave one path empty and another doubled.  Hence the feasible endpoint
transversals are not the bases of one matroid.

This assertion is deliberately narrow.  It does not rule out a more
elaborate extended formulation or a special recursive algorithm; it rules
out identifying the supplied feasible transversals themselves with one
matroid base family.

## 4. The literal `n=4` repair clause

Here

\[
                 (N,R,C)=(56,14,42).                 \tag{4.1}
\]

On the upper shore, take all twenty-eight rank-six outer masks except
`0x7d` and `0xed`.  Its neighbourhood has order `67`.  Twelve path pairs
have both endpoints in the neighbourhood, paths `4` and `13` contribute
only their bit-one endpoints, and no path contributes a bit-zero-only
endpoint.  Its row is

\[
 14\cdot67+42(12+x_4+x_{13})\ge56\cdot26,             \tag{4.2}
\]

or

\[
                   x_4+x_{13}\ge1/3.                 \tag{4.3}
\]

For Boolean orientations this is exactly

\[
                         x_4\lor x_{13}.              \tag{4.4}
\]

It is obeyed by all `475` feasible effective states.  The two stored paths
are the one-edge paths with endpoints

\[
 (0x4d,0x5c),\qquad(0xa9,0xe8).                      \tag{4.5}
\]

Thus (4.4) is a literal Hall-cut explanation for both known one-component
repairs of the stored orientation.  The earlier stored minimum cut gives a
weaker six-literal clause; (4.4) is the sharp global two-literal row.

## 5. Relation to `Q` and rooted/no-empty support

The endpoint-cut polytope is defined by the undirected structural forest
and its two fixed occurrence graphs.  Neither `Q` nor a side representative
appears.  When an integral orientation passes both shores, SBE puts the
constant point in both pulled-back strict base polytopes and only then
supplies a common `Q` by matroid-intersection integrality.

The rooted/no-empty and source-ear rows are later physical conditions on
that `Q` and its two representative banks.  They cannot repair a failed
orientation cut.  Conversely a component flip changes the terminal
injections, so an old `Q` is not automatically retained even though both
occurrence graphs and the undirected forest are unchanged.

Therefore a recursive preservation proof must export either:

1. an integral solution of the endpoint-cut master for its new structural
   forest; or
2. a narrower structural invariant, such as the cut-width-two face, that
   guarantees one can be found.

It must not charge an SBE failure to later `Q` selection.  The guarded
isolated `c`-rail filler remains outside this orientation system.

## 6. Exact audit and scope

The independent audit is

```text
scratch/audit_catalan_sbe_orientation_integrality_obstructions_20260731.py
scratch/catalan_sbe_orientation_integrality_obstructions_20260731.audit.json
```

It authenticates the chained witness, reconstructs both occurrence graphs,
enumerates all effective `n=3,4` orientations with an independent Dinic
implementation, checks every fractional `n=3` cut exactly over rational
numbers, and replays every closure and literal-cut witness above.

At freeze time the canonical JSON payload is

```text
e971ca294e9332ccd23612e1971624e6d7fcb2d9b99125bb96132c798c02c494
```

The finite obstructions concern these authenticated forests only.  They do
not prove that every higher-dimensional Catalan forest has a hard
orientation system, nor that every wider-cut system is intractable.  They
prove that integrality, 2-SAT, one-submodular-mincut, and one-matroid-base
claims are unavailable without an additional structural invariant.
