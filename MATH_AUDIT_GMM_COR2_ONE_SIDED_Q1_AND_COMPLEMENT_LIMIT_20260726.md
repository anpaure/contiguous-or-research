# Audit of the GMM Corollary 2 depth-one interface

Date: 2026-07-26

Method: pure mathematics; no computation or external search.

## 0. Verdict

Gregor--Mička--Mütze, Corollary 2, does give an unconditional one-sided
depth-one owner cycle, in two related but logically distinct forms.

1. Its **saturating cycle** between ranks \(m-1,m\) projects to a simple
   Johnson cycle on exactly
   \(N_-:=\binom n{m-1}\) distinct rank-\(m\) owners.  Its intersection
   colours are all rank-\((m-1)\) sets, exactly once.
2. Its separately asserted **tight enumeration** of the same two ranks
   contracts to a Hamilton cycle on all
   \(W:=\binom n m\) rank-\(m\) owners.  Every rank-\((m-1)\) target occurs
   as an intersection colour, but the theorem gives no control on which
   \(W-N_-\) lower colours are repeated.

In neither form does Corollary 2 bound the number of repeated upper-union
colours.  Reversal changes neither colour multiset.  On the even ground
\(n=2m\), complementation converts the lower-complete cycle into a generally
different upper-complete cycle; it does not make the original cycle
two-sided.  On the odd ground \(n=2m+1\), complementation does not even
preserve the rank-\(m\) owner layer.

The exact missing assertion for the projected saturating core is the
near-injectivity of the second-window map

\[
 i\longmapsto R_{i-1}\cup R_i\cup R_{i+1}.
\]

No such assertion occurs in Corollary 2.

## 1. The exact published statement used

The local primary-source file `tmp/central/gmlc2.tex` states:

> For any \(n\geq1\) and \(1\leq\ell\leq n+1\), the subgraph of the
> \(n\)-cube induced by any sequence of \(\ell\) consecutive levels has
> both a saturating cycle and a tight enumeration.

Here a saturating cycle is a cycle visiting every vertex of the smaller
bipartition class.  A tight enumeration is a cyclic listing of every vertex
whose total Hamming distance is the number of vertices plus the difference
of the two bipartition sizes.

The word "both" is existential: the corollary supplies a saturating cycle
and a tight enumeration.  It does not state that one cyclic object has both
properties.

Throughout the nondegenerate discussion below assume \(m\geq2\) and
\(n\in\{2m,2m+1\}\), and put

\[
 W=\binom n m,
 \qquad N_-=\binom n{m-1},
 \qquad N_+=\binom n{m+1},
 \qquad E=W-N_-.
\tag{1.1}
\]

The exact values are

\[
\begin{array}{c|c|c|c}
n&N_-&N_+&E\\ \hline
2m&\dfrac m{m+1}W&\dfrac m{m+1}W&\dfrac W{m+1}\\[2mm]
2m+1&\dfrac m{m+2}W&W&\dfrac{2W}{m+2}.
\end{array}
\tag{1.2}
\]

In particular \(E=o(W)\), and \(HE=o(W)\) whenever \(H=o(m)\).

## 2. Projection of the saturating cycle

### Theorem 2.1 (exact lower-rainbow core)

There is a cyclic incidence sequence

\[
 R_0,X_0,R_1,X_1,\ldots,R_{N_--1},X_{N_--1},R_0,
\tag{2.1}
\]

where the \(R_i\)'s are all rank-\((m-1)\) sets, the \(X_i\)'s are
\(N_-\) distinct rank-\(m\) sets, and

\[
 R_i\subset X_i\supset R_{i+1}.
\tag{2.2}
\]

Consequently \(P=(X_0,\ldots,X_{N_--1})\) is a simple cycle in
\(J(n,m)\), with

\[
 X_{i-1}\cap X_i=R_i.
\tag{2.3}
\]

Thus its lower colours are all distinct and exhaust
\(\binom{[n]}{m-1}\).  Its owner leave is exactly \(E\).

#### Proof

Apply Corollary 2 to levels \(m-1,m\).  Rank \(m-1\) is the smaller
bipartition class, so a simple saturating cycle visits every one of its
\(N_-\) vertices.  Bipartite alternation forces the cycle to use exactly
\(N_-\) distinct rank-\(m\) vertices, giving (2.1).

At \(R_i\), the incident owners \(X_{i-1},X_i\) are distinct rank-\(m\)
supersets of the same rank-\((m-1)\) set.  Their intersection is therefore
exactly \(R_i\), proving (2.3).  The remaining count is (1.2). \(\square\)

The equivalent lower-layer description is also useful.  From (2.2),

\[
 X_i=R_i\cup R_{i+1}.
\tag{2.4}
\]

Hence \((R_i)\) is a Hamilton cycle of \(J(n,m-1)\) with distinct edge
unions \((X_i)\).  This is precisely the first-order rainbow property
delivered by the theorem.

### Proposition 2.2 (the exact unproved second-order property)

The upper colour on the owner edge \(X_{i-1}X_i\) is

\[
 U_i=X_{i-1}\cup X_i
     =R_{i-1}\cup R_i\cup R_{i+1}.
\tag{2.5}
\]

Define the upper collision excess

\[
 c_+(P):=N_--|\{U_i:i\in\mathbb Z/N_-\mathbb Z\}|.
\tag{2.6}
\]

Then the exact number of missing upper targets is

\[
 M_+(P)=N_+-N_-+c_+(P).
\tag{2.7}
\]

Thus:

* on \(n=2m\), the core is two-sided exact if and only if the map in
  (2.5) is injective;
* on \(n=2m+1\), even an injective map must miss exactly
  \(N_+-N_-=E\) upper targets, and it is asymptotically two-sided if and
  only if \(c_+(P)=o(W)\).

#### Proof

Equation (2.5) follows from (2.4).  The cycle has \(N_-\) upper-colour
occurrences and exactly \(N_--c_+(P)\) distinct upper colours.  Subtract
this number from \(N_+\). \(\square\)

Corollary 2 controls neither (2.5) nor (2.6).  A purely pointwise bound is
far too weak: for fixed \(U\), all owner vertices incident with an edge of
union colour \(U\) are facets of \(U\).  There are \(m+1\) such facets, and
the edges of a proper subcycle induced on them form paths, so \(U\) can
occur at most \(m\) times.  This yields only

\[
 |\{U_i\}|\geq N_-/m,
\tag{2.8}
\]

which is nowhere near the required \(N_--o(W)\).

## 3. What the tight enumeration additionally supplies

### Theorem 3.1 (contraction of a tight two-level enumeration)

A tight enumeration of levels \(m-1,m\) contracts to a Hamilton cycle
\(P^{\rm tight}\) of \(J(n,m)\) on all \(W\) middle owners.  Exactly
\(N_-\) owner edges arise by contracting a unique intervening
rank-\((m-1)\) vertex, and the other exactly \(E=W-N_-\) owner edges are
direct rank-\(m\)-to-rank-\(m\) steps.  Every lower target occurs at least
once as an intersection colour of \(P^{\rm tight}\).

#### Proof

Let \(a,b,c\) count, respectively, cross-rank, lower--lower, and
middle--middle consecutive pairs in the cyclic enumeration.  Counting the
two incidences at every listed vertex gives

\[
 2N_-=a+2b,
 \qquad
 2W=a+2c,
 \qquad
 c-b=W-N_-=E.
\tag{3.1}
\]

Every cross-rank pair has Hamming distance at least one, and every pair of
distinct equal-rank vertices has distance at least two.  Therefore the
total number of flipped bits is at least

\[
 a+2b+2c=2W+2b.
\tag{3.2}
\]

Tightness says that this total is

\[
 (W+N_-)+(W-N_-)=2W.
\tag{3.3}
\]

Consequently \(b=0\), and equality holds in every local distance lower
bound.  Thus every lower vertex is flanked by two incident middle vertices,
and every direct middle--middle pair is a Johnson edge.  Also (3.1) gives
\(a=2N_-\) and \(c=E\).

Delete each lower vertex from the cyclic list.  The surviving order uses
every middle vertex exactly once.  A pair formerly separated by a lower
vertex has that vertex as its intersection; a formerly direct pair differs
in exactly two coordinates.  Hence the surviving order is a Hamilton
Johnson cycle.  Every lower vertex appeared once in the enumeration, so all
lower targets occur among its intersection colours. \(\square\)

The theorem does **not** say that the extra \(E\) lower-colour occurrences
are assigned injectively, or that the lower loads are floor/ceiling
balanced.  It also gives no upper-union estimate.

The saturating cycle of Theorem 2.1 and the tight enumeration of Theorem 3.1
are separate outputs of Corollary 2.  One must not transfer structural
features from one to the other without an additional construction.

## 4. Complement and reversal audit

For any rank-\(m\) Johnson cycle \(P\), let \(L(P)\) and \(U(P)\) denote
its intersection- and union-colour multisets.

### Lemma 4.1 (reversal is ledger-neutral)

For the reversed cyclic order \(P^{-1}\),

\[
 L(P^{-1})=L(P),
 \qquad U(P^{-1})=U(P)
\tag{4.1}
\]

as multisets.

This is immediate because reversal changes only the orientation of each
unordered Johnson edge.

### Lemma 4.2 (even-ground complementation swaps the ledgers)

Suppose \(n=2m\), and write \(\overline P\) for the cycle obtained by
complementing every owner.  Then \(\overline P\) is again a rank-\(m\)
Johnson cycle and

\[
 L(\overline P)=\{[n]\setminus U:U\in U(P)\},
 \qquad
 U(\overline P)=\{[n]\setminus L:L\in L(P)\}.
\tag{4.2}
\]

#### Proof

For an edge \(XY\), De Morgan's laws give

\[
 \overline X\cap\overline Y=\overline{X\cup Y},
 \qquad
 \overline X\cup\overline Y=\overline{X\cap Y}.
\]

Complementation preserves rank \(m\) exactly when \(n=2m\). \(\square\)

It follows that complementing the lower-complete cycle from either Section 2
or Section 3 produces an upper-complete cycle.  (The Section 2 colours are
rainbow; Section 3 asserts coverage and may have repetitions.)  However, this is generally a
different cyclic order.  Corollary 2 contains no assertion that
\(\overline P\) equals \(P\), its reversal, or a small edge modification of
either.

For the projected core in Section 2, the owner sets of \(P\) and
\(\overline P\) do at least have large overlap, for the trivial counting
reason

\[
 |V(P)\cap V(\overline P)|\geq W-2E.
\tag{4.3}
\]

This is only a vertex-set statement.  It gives no common-edge or common
cyclic-order bound, so it cannot splice the two ledgers.

There is a sharp parity warning for the strongest complement shortcut.

### Proposition 4.3 (antipodal core parity obstruction)

If the projected core \(P\) on \(N_-\) owners in \(J(2m,m)\) were invariant
under complementation as an unoriented cycle, then \(N_-\) would be even.
For every \(m=2^a-1\),

\[
 N_-=\binom{2m}{m-1}
\]

is odd.  Hence no complement-invariant projected saturating core exists in
those dimensions.

#### Proof

Complementation has no fixed rank-\(m\) set.  If it preserved the cycle, it
would induce a fixed-point-free involutive automorphism of the abstract
cycle \(C_{N_-}\).  An odd cycle has no such automorphism, so \(N_-\) must
be even.

For \(m=2^a-1\), adding \(m-1\) and \(m+1\) in base two creates no carries.
By the parity form of Kummer's theorem,
\(\binom{2m}{m-1}\) is odd. \(\square\)

This does not obstruct a non-antipodal two-sided cycle; it only proves that
"take the complement and reverse the same core" cannot be the general
argument.

When \(n=2m+1\), complementation sends a rank-\(m\) owner to rank \(m+1\),
so Lemma 4.2 is not an owner-layer operation.  Applying Corollary 2 instead
to the equal central levels \(m,m+1\) gives a Hamilton middle-levels cycle;
projecting its rank-\(m\) vertices gives a Hamilton Johnson cycle with every
upper colour exactly once.  This is a second one-sided cycle, not a coupling
to the lower-perfect cycle.

## 5. Exact boundary for the proposed upgrade

The following are the precise consequences and gaps.

1. **Projected near-factor form.**  Corollary 2 gives \(W-E\) owners,
   exact lower colours, and \(HE=o(W)\) for every \(H=o(m)\).  Two-sided
   asymptotic saturation is equivalent to the new bound
   \(c_+(P)=o(W)\) in (2.6).
2. **Full-owner form.**  A tight enumeration gives a Hamilton owner cycle
   with no missing lower target.  It remains to choose such an enumeration
   so that its union colours miss only \(o(W)\) upper targets.
3. **Exact cardinality.**  On even ground, a projected core can cover both
   adjacent layers exactly because \(N_-=N_+\).  On odd ground, a projected
   lower core has only \(N_-=W-E\) edges and therefore must miss at least
   \(E\) of the \(W\) upper targets.  A full Hamilton owner cycle has exactly
   \(W\) edges, so exact upper coverage there means every upper colour occurs
   exactly once.
4. **No complement/reversal completion.**  Reversal is ledger-neutral.
   Even-ground complement supplies the dual cycle but no shared edge order;
   odd-ground complement leaves the owner rank.  Any successful construction
   must coordinate the two ledgers rather than merely place the two
   one-sided theorems side by side.

Accordingly, Corollary 2 is a rigorous one-sided depth-one input, but it is
not yet a two-sided saturating Johnson-cycle theorem.
