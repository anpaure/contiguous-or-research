# Recursive paired-order complete mappings and the first trace interface

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Outcome

The corrected antipodal \(Q_4\) braid does more than supply one affine
complete mapping.  It satisfies a predecessor-square identity which makes
the double-factor construction recursively closed.

Starting from the two corrected \(Q_4\) factors with words

\[
                         1234\,1234,
 \qquad                  1432\,1432,                 \tag{0.1}
\]

one obtains, for every

\[
                         r=4\cdot2^t,                 \tag{0.2}
\]

two common-phase isometric \(C_{2r}\)-factors of \(Q_r\), related
pointwise by one involutory coordinate permutation.  Applying the parity
complete-mapping lift at every stage gives an exact factor on \(Q_{2r}\)
whose physical directions occur in adjacent pairs

\[
                         b_i,a_i.                     \tag{0.3}
\]

Both row permutations and every column complete-mapping equation remain
exact.  Thus ownership, physical isometry, common phase, and adjacent pair
clustering all recurse without a rounding step.

This natural recursion does **not** solve the OR trace gate.  It preserves
the number of cyclic half-order types instead of increasing it.  The
corrected \(Q_4\) seed has one order type, so every recursively produced
factor still has one order type, with its letters replaced recursively by
adjacent pairs.  Context changes only the cyclic starting phase.

There is an exact entropy obstruction.  If the coarse factors used by the
parity lift have at most \(K\) cyclic half-order types, then at aligned
completed-pair depth \(d<r\) their signed physical trace code has at most

\[
                         Kr\,2^{2(r-d)}               \tag{0.4}
\]

values on \(2^{2r-1}\) even-context starts.  Hence its collision excess is
at least

\[
 \boxed{
  2^{2r-1}-Kr\,2^{2(r-d)}.}                          \tag{0.5}
\]

Near-injective trace recovery therefore requires

\[
 \boxed{
 K\ge(1-o(1)){2^{2d-1}\over r}.}                    \tag{0.6}
\]

At Gaussian depth, exponentially many context-coded order types are
necessary.  A recursion which adds only \(O(1)\) braid bits at each of
\(O(\log r)\) doubling levels supplies only polynomially many orders and
cannot work.

On the positive side, Section 5 gives an explicit quartet Latin order array
which recovers both erased bits per completed direction exactly, provided
the local round is known.  Sections 8--10 then audit overlapping braid
layers.  Arbitrary first-layer bits destroy the next translation pairing,
but coset-invariant comparator bits preserve an entire bounded \(Q_4\)
sorting network and give exponentially many cycle-specific orders.

A final exact kernel remains.  If a completed set \(J\) overlaps the image
\(S(J)\) of the paired-factor permutation in \(t\) coordinates, its trace
has multiplicity at least \(2^{t-1}\).  The single-transposition \(Q_4\)
partner is therefore too sparse.  The first unresolved interface is to
combine the Latin interval code with a large partner involution satisfying
\(|J\cap S(J)|=O(1)\) at every protected window.  The row and column
complete mappings are no longer the missing equation.

## 1. Recursively admissible double factors

Let \(G^0,G^1\) be neighbor permutations of \(Q_r\), with direction
functions

\[
 G^\epsilon(y)=y\oplus e_{\delta_\epsilon(y)}.
                                                               \tag{1.1}
\]

Call \((G^0,G^1,S,c)\) a **recursive paired factor** when:

1. every orbit of both \(G^0,G^1\) is an isometric \(C_{2r}\);
2. \(S\in\operatorname {Sym}([r])\) is an involution and

   \[
                         \delta_1(y)=S\delta_0(y)      \tag{1.2}
   \]

   at every common owner \(y\);
3. \(c:Q_r\to\mathbb Z_{2r}\) is common phase:

   \[
                         c(G^\epsilon y)=c(y)+1;       \tag{1.3}
   \]

4. the incoming \(G^0\)-direction agrees at the two predecessors:

   \[
 \boxed{
  \delta_0((G^0)^{-1}z)=\delta_0((G^1)^{-1}z)
  \quad(z\in Q_r).}                                  \tag{1.4}
   \]

Condition (1.4) is the extra identity needed to make the paired relation
survive at odd states of the parity lift.

### Lemma 1.1 (square form of the predecessor identity)

Put \(i=\delta_0(y)\).  Under (1.2), equation (1.4) is equivalent to

\[
 \delta_0(y\oplus e_i\oplus e_{S i})=i.              \tag{1.5}
\]

#### Proof

Let \(z=G^0y=y\oplus e_i\).  Its \(G^1\)-predecessor must have
\(G^0\)-label \(i\), by (1.4), and hence \(G^1\)-direction \(S i\).
That predecessor is necessarily

\[
 z\oplus e_{S i}=y\oplus e_i\oplus e_{S i},
\]

which proves (1.5).  Reversing the argument proves equivalence.
\(\square\)

### Lemma 1.2 (the corrected \(Q_4\) seed is recursive)

Let \(G^0\) be the corrected factor with word \(1234\,1234\), let
\(G^1\) be the antipodally doubled braid with word \(1432\,1432\), and put

\[
                         S=(2\ 4).                    \tag{1.6}
\]

Then \((G^0,G^1,S,c)\) is a recursive paired factor.

#### Proof

The independent \(Q_4\) audit verifies exact ownership, isometry, the
common column phase \(c\), and (1.2).  At a vertex of phase \(j\),
\(\delta_0\) is the \(j\)-th letter of \(1234\,1234\).  Both predecessors
of a phase-\(j\) vertex have common phase \(j-1\).  Their \(\delta_0\)
values are therefore equal, proving (1.4). \(\square\)

## 2. The double parity lift

Write the coordinates of \(Q_{2r}\) as

\[
                         (a_i,b_i),\qquad i\in[r],    \tag{2.1}
\]

and use

\[
                         x_i=a_i,\qquad
                         p_i=a_i\oplus b_i.           \tag{2.2}
\]

For every even \(p\) and every \(x\), put

\[
 y=Sp\oplus x,\qquad
 d_p^0(x)=\delta_0(y),\qquad
 d_p^1(x)=S\delta_0(y)=\delta_1(y).                  \tag{2.3}
\]

Define the coarse row maps

\[
 F_p^\epsilon(x)=x\oplus e_{d_p^\epsilon(x)}.        \tag{2.4}
\]

### Lemma 2.1 (both row and both column systems)

For every even \(p\), both \(F_p^0,F_p^1\) are permutations.  For every
\(x\), both maps

\[
 T_x^\epsilon(p)=p\oplus e_{d_p^\epsilon(x)}         \tag{2.5}
\]

are bijections from the even to the odd parity shore.

#### Proof

Under the affine change \(y=Sp\oplus x\),

\[
 Sp\oplus F_p^0(x)=G^0(y),\qquad
 Sp\oplus F_p^1(x)=G^1(y),                           \tag{2.6}
\]

which proves both row assertions.  Since \(S^2=1\),

\[
\begin{aligned}
 S T_x^0(p)\oplus x&=y\oplus e_{S\delta_0(y)}=G^1(y),\\
 S T_x^1(p)\oplus x&=y\oplus e_{\delta_0(y)}=G^0(y).
\end{aligned}                                         \tag{2.7}
\]

Both column maps are therefore affine conjugates of neighbor
permutations. \(\square\)

Apply the parity lift separately to the two systems in Lemma 2.1.  Denote
the resulting neighbor permutations of \(Q_{2r}\) by \(L^0,L^1\).
At an even context, \(L^\epsilon\) first toggles
\(b_{d_p^\epsilon(x)}\); at the routed odd context it toggles the matching
\(a_{d_p^\epsilon(x)}\).

Let \(\widetilde S\) be the coordinate permutation

\[
 \widetilde S(a_i)=a_{S i},\qquad
 \widetilde S(b_i)=b_{S i}.                          \tag{2.8}
\]

### Theorem 2.2 (recursive paired-order lift)

If \((G^0,G^1,S,c)\) is a recursive paired factor on \(Q_r\), then

\[
                         (L^0,L^1,\widetilde S,\widetilde c)           \tag{2.9}
\]

is a recursive paired factor on \(Q_{2r}\).  Every physical direction
word is obtained from a coarse word by the adjacent substitution

\[
                         i\longmapsto b_i,a_i.        \tag{2.10}
\]

#### Proof

For fixed even \(p\), two steps of \(L^\epsilon\) induce the row
permutation \(F_p^\epsilon\).  Hence a coarse \(C_{2r}\) becomes a
physical \(C_{4r}\).  If its coarse word is \(\pi\pi\), its physical word
is the adjacent expansion of \(\pi\pi\), again a doubled permutation.
Thus every orbit is isometric.

For an even physical state, (2.3) makes the two outgoing directions
\(b_i,b_{S i}\), so they satisfy the pointwise relation (2.8).

Consider an odd state and put \(y'=Sp'\oplus x\).  The even predecessor
for \(L^0\) corresponds to \((G^1)^{-1}y'\), while the even predecessor
for \(L^1\) corresponds to \((G^0)^{-1}y'\).  The two outgoing
\(a\)-directions at the odd state are therefore

\[
 a_{\delta_0((G^1)^{-1}y')},\qquad
 a_{S\delta_0((G^0)^{-1}y')}.                       \tag{2.11}
\]

Equation (1.4) shows that these are related by \(\widetilde S\).

The common lifted phase is explicit.  At even states put

\[
                         \widetilde c(p,x)=2c(Sp\oplus x),             \tag{2.12}
\]

and at odd states put

\[
                         \widetilde c(p',x)=2c(Sp'\oplus x)-1.         \tag{2.13}
\]

Equations (2.6)--(2.7) and the common phase law (1.3) show that either
successor advances (2.12)--(2.13) by one modulo \(4r\).

It remains to verify the lifted form of (1.4).  Let \(Z\) be odd and put
\(z=Sp_Z\oplus x_Z\).  Its \(L^0\)- and \(L^1\)-predecessors are even
states corresponding respectively to \((G^1)^{-1}z\) and
\((G^0)^{-1}z\).  Evaluating the \(L^0\)-direction at them gives equal
\(b\)-directions by (1.4).

Now let \(Z\) be even and put \(z=Sp_Z\oplus x_Z\).  Its two odd
predecessors have transformed odd states

\[
 G^1(G^0)^{-1}z,\qquad G^0(G^1)^{-1}z.               \tag{2.14}
\]

At the first, the \(L^0\)-direction is
\(a_{\delta_0((G^0)^{-1}z)}\).  At the second it is

\[
 a_{\delta_0((G^1)^{-1}G^0(G^1)^{-1}z)}.
\]

Apply (1.4) first at \(G^0(G^1)^{-1}z\), and then at \(z\).  The latter
label equals \(\delta_0((G^1)^{-1}z)\), which equals
\(\delta_0((G^0)^{-1}z)\).  Thus the lifted predecessor identity holds in
both parity cases. \(\square\)

### Corollary 2.3 (exact infinite recursion)

The corrected \(Q_4\) pair recursively produces exact paired factors at
every dimension (0.2).  At every stage:

* all owners occur exactly once on each shore;
* every row and column map is bijective;
* every component is a physical isometric maximum cycle;
* the two shores have one common phase map;
* physical directions occur in adjacent pairs.

No port or collar is omitted: these are closed physical cycles.

## 3. What order information the recursion carries

For an isometric factor, call two cycles the same **order type** when their
half-words are cyclic rotations of the same permutation.  Let \(K(G)\) be
the number of order types in \(G\).

### Proposition 3.1 (order types do not grow)

In Theorem 2.2,

\[
                         K(L^0)=K(G^0),\qquad
                         K(L^1)=K(G^1).               \tag{3.1}
\]

#### Proof

For fixed \(p\), \(F_p^0\) is a translate-conjugate of \(G^0\), so its
cycles have exactly the same direction orders.  The parity lift applies
the deterministic injective substitution (2.10) to every letter.  This
neither identifies nor creates order types.  The second equality is
identical. \(\square\)

The corrected \(Q_4\) seed has \(K(G^0)=K(G^1)=1\).  Hence the infinite
recursion has one order type at every scale.  The affine context \(p\)
changes the base vertex

\[
                         y=Sp\oplus x,                \tag{3.2}
\]

and therefore changes its phase and cycle translate, but it does not change
the cyclic order type.

## 4. Exact order-entropy lower bound for trace recovery

Fix the parity lift at coarse dimension \(r\), and consider aligned
physical windows of length \(2d\), beginning at an even context.  Let

\[
 J_{p,d}(x)\subseteq[r]                               \tag{4.1}
\]

be the \(d\) completed coarse directions.  The lower or upper physical
trace determines at most

\[
 \mathcal C_d(p,x)=
 \bigl(J_{p,d}(x),x|_{J^c},p|_{J^c}\bigr).           \tag{4.2}
\]

There are \(2^{2r-1}\) pairs \((p,x)\) with \(p\) even.

### Theorem 4.1 (order-entropy obstruction)

Suppose all coarse cycles appearing among the \(F_p\)'s have at most
\(K\) cyclic half-order types.  For \(1\le d<r\), the number of possible
codes (4.2) is at most

\[
                         Kr\,2^{2(r-d)}.              \tag{4.3}
\]

Consequently the number of starts in excess of the number of distinct
aligned traces is at least (0.5), and their average trace multiplicity is
at least

\[
                         {2^{2d-1}\over Kr}.          \tag{4.4}
\]

#### Proof

For one cyclic order, a consecutive \(d\)-window has at most \(r\)
possible unordered direction sets.  Thus \(J\) has at most \(Kr\) values.
Once \(J\) is fixed, the two outside restrictions in (4.2) have at most
\(2^{r-d}2^{r-d}\) values.  This proves (4.3).

Every signed physical trace factors through (4.2), so the number of
distinct traces is no greater than (4.3).  Subtracting it from the number
of starts proves (0.5), and division proves (4.4). \(\square\)

### Corollary 4.2 (bounded-branch recursion cannot reach Gaussian depth)

If \(Kr/2^{2d-1}=o(1)\), then asymptotically every even-context start is
part of the collision excess.  Near-injectivity forces (0.6).

In particular:

1. the recursion of Corollary 2.3 fails once
   \(d-\tfrac12\log_2r\to\infty\);
2. a construction adding at most \(B\) new order choices at each doubling
   level has \(K\le B^{O(\log r)}=r^{O(1)}\), and therefore reaches only
   \(d=O(\log r)\);
3. at \(d=\Theta(\sqrt m)\), one needs
   \(\exp(\Theta(\sqrt m))\) genuinely different context-coded cyclic
   orders.

Thus a single corrected braid, or one braid bit per recursive scale, cannot
be the main OR compiler.  It can only be a sparse order absorber.

## 5. A static quartet Latin trace code

The entropy lower bound is not a set-theoretic impossibility.  There is an
explicit order array with the correct local information rate.

Partition the \(r=4n\) coarse directions into ordered quartets

\[
 B_g=\{(g,u):u\in\mathbb F_2^2\},\qquad 0\le g<n.    \tag{5.1}
\]

At direction \((g,u)\), put the hidden two-bit symbol

\[
                         z_{g,u}=(p_{g,u},x_{g,u})
                         \in\mathbb F_2^2.            \tag{5.2}
\]

For a local round \(t\in\mathbb F_2^2\), define

\[
 s_g(z)=\sum_{u\in\mathbb F_2^2}z_{g,u},\qquad
 j_{g,t}(z)=s_g(z)+t.                                 \tag{5.3}
\]

All sums are in \(\mathbb F_2^2\).  As \(t\) runs through the four
elements, \(j_{g,t}\) runs through the four directions of \(B_g\) exactly
once.  Choose any fixed cyclic listing \(t_0,t_1,t_2,t_3\) of
\(\mathbb F_2^2\), and form the round-major half-order

\[
\begin{split}
 \Lambda(z)=(&j_{0,t_0},j_{1,t_0},\ldots,j_{n-1,t_0},\\
             &j_{0,t_1},j_{1,t_1},\ldots,j_{n-1,t_1},\\
             &j_{0,t_2},\ldots,j_{n-1,t_2},\\
             &j_{0,t_3},\ldots,j_{n-1,t_3}).         \tag{5.4}
\end{split}

This is a permutation of all \(r\) directions.

### Theorem 5.1 (marked-round exact trace recovery)

Let an interval of at most \(n\) consecutive positions of (5.4) be given,
together with its round positions.  Erase the two-bit symbols on the
selected directions and retain every other symbol.  Then the interval
direction set and the retained symbols recover all erased symbols exactly.

#### Proof

A length-at-most-\(n\) interval in the round-major word meets each quartet
at most once, including across a round boundary.  Suppose it selects
direction \(j=j_{g,t}\) in quartet \(g\).  The other three symbols of that
quartet are retained, and (5.3) gives

\[
 \boxed{
 z_{g,j}=j+t+\sum_{u\ne j}z_{g,u}.}                  \tag{5.5}
\]

Thus the erased two-bit symbol is recovered independently in every touched
quartet. \(\square\)

The four choices in (5.3) are an exact local Latin transport: for fixed
outside symbols and fixed round \(t\), the map

\[
 z_{g,j}\longmapsto j_{g,t}(z)                       \tag{5.6}
\]

is a bijection between the four possible erased symbols and the four
possible selected directions.

This supplies exactly two order bits per completed physical pair, matching
the entropy demand (0.6).

## 6. Why the static array is not yet a rotor factor

Equation (5.4) assigns an order to a frozen symbol array \(z\).  Along a
coarse cube path, however, selecting direction \((g,j)\) toggles
\(x_{g,j}\), so the symbol array changes.  Recomputing (5.3) changes
\(s_g(z)\).  Therefore the next direction obtained by naively reevaluating
\(\Lambda(z)\) need not be the next unused letter of the original order.

There are three exact requirements for a rotor realization.

1. **Cycle invariance.**  The order tag used by a cycle must remain
   invariant, with the physical state determining only the advancing phase.
2. **Owner factorization.**  Cycles carrying different context-coded orders
   must be vertex-disjoint and cover \(Q_r\) exactly once.  Applying the
   fixed-order syndrome tiling separately to every order does not prove that
   mixed orders tile together.
3. **Untagged phase recovery.**  Formula (5.5) uses the round \(t\).  The
   literal lower or upper target carries no external phase tag.  The factor
   must make \(t\) recoverable from the retained physical symbols and the
   interval direction set, including intervals crossing a round seam.

The affine complete-mapping theorem addresses none of these three points:
it assumes the row factors \(G^0,G^1\) already exist.  Once they exist, it
does solve every column equation exactly.

## 7. The exact remaining compiler lemma

The first unresolved interface can be stated without asymptotic language.

### \(\mathrm{PAIR\mbox{-}LATIN}(r,H)\)

Construct a recursive paired factor \((G^0,G^1,S,c)\) on \(Q_r\) such
that, for the affine families (2.3), all maps

\[
 (p,x)\longmapsto
 \bigl(J_{p,d}(x),x|_{J^c},p|_{J^c}\bigr),           \tag{7.1}
\]

with \(p\) even and \(1\le d\le\lfloor H/2\rfloor\), are injective or
have aggregate collision excess \(o(2^{2r}/H)\).  The two half-step codes
for odd starts and odd physical depths must obey the same bound.

An equivalent constructive formulation is:

* realize at least \(2^{H-o(H)}\) cycle order types in one exact factor;
* implement a nested Latin erasure code such as (5.3)--(5.5);
* give the paired factor with (1.2), common phase, and the predecessor-square
  identity (1.4).

The corrected \(Q_4\) braid supplies the local paired transposition needed
to alter orders.  Sections 8--10 audit multilayer use of that transposition.
They show that a flag-compatible overlapping network can preserve exact
ownership and can create exponentially many whole-cycle orders.  However,
one adjacent Coxeter sweep has only polynomially many versions of any fixed
consecutive direction set.  The
missing object is therefore a genuinely mixing, owner-disjoint braid
network which realizes the Latin *interval* code, not merely many full
permutations.

Once \(\mathrm{PAIR\mbox{-}LATIN}(r,H)\) is proved, Theorem 2.2 compiles it
directly into adjacent physical direction pairs with exact row/column
bijectivity.  Until then, the multiframe interval-coded Latin rotor is the
first impossible interface; the complete-mapping and physical-suspension
gates are closed.

## 8. Exact composition of translated two-cycle braids

We now audit successive recouplings directly.

Let an isometric factor have rooted cycles \(C_a\), indexed by a torsor
\(A\) for a binary translation group.  Suppose translation by

\[
                         v=e_i+e_j                    \tag{8.1}
\]

pairs cycles:

\[
                         C_{a+v}=C_a+v,               \tag{8.2}
\]

with the same phase and half-order \(\pi_a\).  Put \(S=(i\ j)\).

### Lemma 8.1 (rooted transposition braid)

The owner union \(C_a\mathbin{\dot\cup}C_{a+v}\) has a second exact
partition into two common-phase isometric cycles whose rooted half-order is

\[
                         S\pi_a.                     \tag{8.3}
\]

#### Proof

In \(\pi_a\), suppose \(i\) occurs before \(j\).  Swapping their labels
changes every prefix vertex strictly after \(i\) and no later than \(j\)
by exactly \(e_i+e_j=v\), and leaves every other prefix unchanged.  Use
the translated prefix vertices from \(C_{a+v}\) on that interval and the
vertices of \(C_a\) elsewhere.  Do the same on the antipodal copy of the
interval.  The complementary choices give the other cycle.

At each phase the two new cycles use exactly the same two owners as the old
cycles.  Their direction words are \(S\pi_a,S\pi_a\), so they are
isometric.  Roots and phase columns are unchanged. \(\square\)

The corrected \(Q_4\) braid is the case in which the exchanged labels have
one intervening direction.  Lemma 8.1 also records exactly how to compose
such rectangles when the exchanged positions have moved farther apart.

Choose a shore bit \(\varepsilon(a)\) on every unordered pair
\(\{a,a+v\}\).  Translation by a second symmetry \(w\) remains a cycle
symmetry after this layer if and only if

\[
 \boxed{
  \varepsilon(a+w)=\varepsilon(a)\quad(a\in A).}     \tag{8.4}
\]

Indeed, translating a switched component by \(w\) gives the switched
component at \(a+w\), while translating an unswitched one gives the
unswitched component.  If their bits disagree, \(w\) sends a cycle of the
new factor to a cycle which is absent from that factor.

Thus an arbitrary first mixed layer normally destroys the component
structure needed by an overlapping second layer.  Equation (8.4) is the
exact repair; there is no probabilistic or asymptotic substitute for it.

## 9. A flag-compatible multilayer theorem

Let

\[
                         v_1,\ldots,v_L\in A          \tag{9.1}
\]

be independent translation symmetries, with
\(v_\ell=e_{i_\ell}+e_{j_\ell}\), and put
\(S_\ell=(i_\ell\ j_\ell)\).  For layer \(\ell\), choose a bit function

\[
                         \varepsilon_\ell:A\to\mathbb F_2.            \tag{9.2}
\]

### Theorem 9.1 (flag-compatible exact braid atlas)

Suppose

\[
 \varepsilon_\ell(a+v_k)=\varepsilon_\ell(a)
 \qquad(k\ge\ell).                                  \tag{9.3}
\]

Then the layers \(1,2,\ldots,L\) may be applied successively.  Every
intermediate state is an exact common-phase isometric factor, and the rooted
half-order on cycle index \(a\) at the end is

\[
 S_L^{\varepsilon_L(a)}\cdots
 S_2^{\varepsilon_2(a)}S_1^{\varepsilon_1(a)}\pi_a. \tag{9.4}
\]

#### Proof

Before layer \(\ell\), every earlier bit
\(\varepsilon_k\), \(k<\ell\), is invariant under \(v_\ell\) by (9.3).
Hence translation by \(v_\ell\) pairs current cycles with identical current
orders.  Lemma 8.1 applies componentwise.  The new layer is itself constant
on its \(v_\ell\)-pairs and, by (9.3), retains every future translation
symmetry.  Induction proves exactness and (9.4). \(\square\)

The condition is triangular, not constant.  Write
\(a=\sum_k\alpha_k(a)v_k+a_\perp\).  For example,

\[
 \varepsilon_1=0,\qquad
 \varepsilon_\ell(a)=\alpha_{\ell-1}(a)
 \quad(2\le\ell\le L)                              \tag{9.5}
\]

satisfies (9.3).  If \(S_1\cdots S_L\) is a word in distinct Coxeter
generators, its different subwords have different supports and hence give
different permutations.  Equations (9.4)--(9.5) then produce

\[
                         2^{L-1}                     \tag{9.6}
\]

cycle-specific order types in one exact factor.

### 9.1 The required translations exist in the syndrome factor

In the parity-alternating syndrome construction, the direction columns are

\[
                         w_i=u_i+u_{i+1}.             \tag{9.7}
\]

With \(u_{2j}=a_j\), \(u_{2j+1}=a_j+z\), one has

\[
                         w_{2j}=z                    \tag{9.8}
\]

for all \(j\).  Hence

\[
 e_{2j}+e_{2k}\in\ker\Psi                           \tag{9.9}
\]

for every pair of even positions.  The complement \(K_0\) to the all-one
vector may be chosen to contain the \((r/2-1)\)-dimensional span of these
weight-two vectors.  Thus the cycles of one resolution factor admit a
large translation star, and in particular a path of overlapping exact
recouplings

\[
 (e_0+e_2),(e_2+e_4),\ldots,(e_{2L-2}+e_{2L})        \tag{9.10}
\]

for every \(L<r/2\).

The associated label transpositions are adjacent generators on the
even-position direction alphabet.  Theorem 9.1 therefore gives a literal
high-rate family of exact translated two-cycle recouplings.  There is one
locality qualification: after the first label swap, the next two fixed
labels need not remain in one bounded \(Q_4\) interval.  Lemma 8.1 still
gives an exact braid, but its exchanged prefix segment may be long.

### 9.1a Keeping every layer literally \(Q_4\)-local

Let \(D\) be the set of even-position direction labels and put

\[
 V=\operatorname {span}\{e_i+e_j:i,j\in D\}\subseteq K_0.             \tag{9.10a}
\]

Require every comparator bit in every layer to be constant on the cosets
of \(V\).  Then the factor remains invariant under translation by
\(e_i+e_j\) for *every* two current labels \(i,j\in D\), not merely under
a predetermined future list.

Keep the odd-position directions fixed as separators and regard the labels
in \(D\) as movable wires.  A fixed adjacent-comparator network on these
wires now has a literal corrected \(Q_4\) realization at every comparator:
whatever labels currently occupy two neighboring wires, their pair-sum
translation lies in \(V\), and the common separator supplies the same
three-edge braid geometry as the seed.

Comparator settings may be arbitrary functions of the quotient cycle tag

\[
                         \bar a=a+V.                  \tag{9.10b}
\]

A standard fixed sorting network can therefore realize any prescribed
permutation of \(D\) for each \(\bar a\), while every intermediate shore
remains an exact common-phase isometric factor.  Since

\[
 \dim(K_0/V)=r/2-O(\log r),                           \tag{9.10c}
\]

this gives exponentially many cycle-specific pair orders using successive
bounded \(Q_4\) recouplings on overlapping direction blocks.

Thus the direct multilayer answer is positive, but only under the strong
coset condition: arbitrary componentwise first-layer bits destroy the next
layer, flag-invariant bits retain predetermined future braids, and
\(V\)-invariant bits retain an entire local comparator network.

### 9.2 Retaining the paired complete-mapping gate

Reserve one further symmetry

\[
                         v_*=e_i+e_j                 \tag{9.11}
\]

and require every layer bit to be invariant under \(v_*\).  Translation by
\(v_*\) then pairs final cycles with identical context-coded orders.  Apply
Lemma 8.1 uniformly with \(S_*=(i\ j)\) to obtain a partner factor.

The two final factors satisfy the pointwise relation
\(\delta_1=S_*\delta_0\).  Their two predecessors at a common target lie
in \(v_*\)-paired cycles of the same order and phase, so (1.4) also holds.
They are therefore a recursive paired factor, and Theorem 2.2 converts the
multilayer atlas into adjacent physical pairs with exact row and column
bijectivity.

This closes the *component-composition* part of the multilayer question.
It does not yet close trace recovery: the reserved transposition in
(9.11) is too sparse, as Theorem 10.1 below shows.

## 10. Yang--Baxter identity and the remaining interval obstruction

Let \(R_S\) denote the rooted recoupling of Lemma 8.1.  If every factor
state associated with the six elements of
\(\langle S,T\rangle\cong S_3\) is legal on the same rooted cycle index,
then the owner-level Yang--Baxter equation is simply

\[
 \boxed{
  R_SR_TR_S=R_TR_SR_T}                                \tag{10.1}
\]

because both shores have the same rooted direction order

\[
                         STS\pi=TST\pi.               \tag{10.2}
\]

The rooted isometric cycle with a given start and doubled order is unique,
so (10.2) identifies the two final owner factors.

For context-dependent bits, (10.1) is **not automatic**.  It holds exactly
when the two three-step routes give the same pointwise permutation word on
every rooted cycle index.  The bit functions must therefore satisfy the
corresponding Boolean cocycle equations, in addition to the translation
invariances (8.4).  A single \(Q_4\) involution supplies only
\(R_S^2=1\); it does not supply this context-dependent Yang--Baxter cocycle.

For a compiler with one fixed canonical layer order, Theorem 9.1 avoids the
need for path independence.  Nevertheless, its first high-rate example has
a separate exact trace defect.

Suppose the generators form one monotone adjacent Coxeter sweep

\[
 S_1=(0\ 1),\ S_2=(1\ 2),\ldots,S_L=(L-1\ L),         \tag{10.3}
\]

each used at most once.  For a base cyclic interval \(J\), its image is

\[
 S_L^{\varepsilon_L}\cdots S_1^{\varepsilon_1}(J).   \tag{10.4}
\]

A single sweep can transport a boundary letter a long distance, so it is
not true that only two switch bits are visible.  Nevertheless it has only
polynomial interval capacity.

For a prefix \(P_k=\{0,\ldots,k\}\), all switches before its unique boundary
exchange equal membership bits.  If the boundary switch is off, no later
switch changes the prefix.  If it is on, it launches one membership carrier
to the right, which advances until the first subsequent off switch.  Thus
the image of \(P_k\) is determined by one terminal position, with at most
\(L+2\) possibilities.  Every ordinary interval is the difference of two
nested prefixes, and a cyclic interval is either such an interval or its
complement.  Hence, for a fixed start and depth,

\[
\boxed{
  \#\{\text{direction sets in (10.4)}\}
  \le 2(L+2)^2.}                                     \tag{10.5}
\]

Thus the atlas of Theorem 9.1 can have \(2^{\Theta(r)}\) different full
orders while giving only \(O(\log r)\) bits of interval-set information at
a fixed window.  Substitution in Theorem 4.1 leaves exponential trace
collision whenever \(d- O(\log r)\to\infty\).

This is the precise multilayer verdict.

* Arbitrary overlapping layers fail immediately by loss of the next
  translation symmetry.
* Flag-compatible layers compose exactly and can have exponential whole
  order entropy.
* One monotone adjacent Coxeter sweep has only polynomial interval capacity
  and does not provide the
  required OR trace entropy.
* Escaping (10.5) requires several genuinely mixing frames, so that
  \(\Theta(d)\) context-controlled generators transport labels across a
  typical \(d\)-window boundary.  Their repeated or dependent translation
  layers must satisfy either a canonical flag extension of Theorem 9.1 or
  the full context-dependent Yang--Baxter cocycle (10.1).

### Theorem 10.1 (partner-overlap trace kernel)

Consider the affine complete-mapping family

\[
                         y=Sp+x,                      \tag{10.6}
\]

and one aligned completed-direction set \(J\).  Put

\[
                         t=|J\cap S(J)|.              \tag{10.7}
\]

If \(t\ge1\), then every physical trace with that \(J\) has multiplicity
at least

\[
                         2^{t-1}                     \tag{10.8}
\]

among even contexts, whenever the corresponding starts exist.

For \(t=0\), the corresponding universal bound is one.

#### Proof

Fix the outside restrictions of \(p,x\).  For every vector \(q\) supported
on

\[
                         J\cap S^{-1}(J),             \tag{10.9}
\]

replace

\[
                         p\mapsto p+q,\qquad
                         x\mapsto x+Sq.               \tag{10.10}
\]

Both changes are supported inside \(J\), and

\[
                         S(p+q)+(x+Sq)=Sp+x=y.        \tag{10.11}
\]

Therefore the factor phase, context-coded direction order, completed set
\(J\), and all retained physical symbols are unchanged.  The support in
(10.9) has dimension \(t\); imposing that \(p+q\) retain even parity removes
at most one dimension.  This gives (10.8). \(\square\)

For the reserved single transposition of Section 9.2, every window avoiding
its two moved labels has \(t=d\), and hence multiplicity at least
\(2^{d-1}\).  No amount of cycle-order entropy repairs this kernel.  More
generally, a successful partner permutation must satisfy

\[
                         |J\cap S(J)|=O(1)            \tag{10.12}
\]

for every protected consecutive set emitted by the order atlas.

Accordingly, the first open interface is now smaller and sharper than a
generic dense braid network: construct a **displaced multiframe
flag/Yang--Baxter rotor** which

1. realizes the Latin interval recovery identity (5.5);
2. has a large involutory partner \(S\) obeying (10.12), preferably a
   fixed-point-free pairing whose mates are separated by more than \(H\) in
   every emitted order;
3. retains all translations \(e_i+e_{S i}\) needed to build the partner
   factor and its predecessor identity.

The multilayer \(Q_4\) composition itself is possible.  The first unsolved
interface is simultaneous interval coding and large partner displacement.
