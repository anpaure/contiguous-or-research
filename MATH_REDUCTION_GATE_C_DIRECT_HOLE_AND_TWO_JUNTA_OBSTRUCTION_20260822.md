# Gate C: the direct band-hole gate and a balanced two-junta obstruction

**Status (2026-08-22).**  Every assertion in this note is proved.  The
multiscale fragment compiler does not actually require stagewise balanced
colour quotas.  Its exact input is only that the union of the selected
tokens misses `o(W)` targets in aggregate over the central band.  This is a
strict weakening of the aggregate-overflow premise.

The weakening does not close Gate C.  The coordinate-star obstruction has a
stronger, previously unrecorded form.  For any two coordinates `z,y`, the
middle sets in which `z` and `y` have equal membership form a
complement-closed exact one-design of density

\[
                         {b-1\over 2b-1}\sim {1\over2},
\]

but contain no phase fragment of length `b+1`.  Intersecting disjoint such
pair equalities gives complement-closed, point-balanced, fragment-free
families of every polynomial density `b^{-gamma+o(1)}`.  Hence neither
coordinate balance nor complement symmetry is a sufficient reachable-
residual invariant.  A positive recursive theorem must preserve genuinely
second-order anti-junta information (or a stronger direct track-expansion
property).

## 1. The phase-fragment model

Let

\[
 b=2h+1\ge5,\qquad |\Omega|=2b,\qquad
 {\cal V}={\Omega\choose b},\qquad W=|{\cal V}|.             \tag{1.1}
\]

Split `Omega=A dotcup B`, with both shores of size `b`.  On each shore fix a
directed cyclic order.  Repeat the type period

\[
                 B,A,B,A,\ldots,B,A,B,                         \tag{1.2}
\]

of length `b`; at an event of one type emit the next coordinate of that
shore's cyclic stream.  A phase-refined atom is the resulting cyclic word
`(w_t)_(t in Z_(b^2))`, and its middle windows are

\[
                         C_t=\{w_t,\ldots,w_{t+b-1}\}.          \tag{1.3}
\]

These `b^2` middle windows are pairwise distinct.  To see this, a window
contains `h` consecutive `A` coordinates and `h+1` consecutive `B`
coordinates, so it determines the two cyclic-stream starts.  Write
`t=qb+r`, `0<=q,r<b`, and let `p(r)` be the pair of type counts in the
first `r` positions of one type period.  The two starts at time `t` are

\[
                         q(h,h+1)+p(r)\pmod b.                 \tag{1.3a}
\]

The functional `phi(x,y)=(h+1)x-hy mod b` kills `(h,h+1)`.  Each `A`
step changes `phi` by `h+1`, and each `B` step changes it by `-h`; these
increments are equal modulo `b=2h+1`.  Hence
`phi(p(r))=-hr mod b`.  Since `gcd(h,b)=1`, the start pair determines `r`;
then it determines `q`, because `(h,h+1)` has order `b`.  This proves the
claim.

The `h` events of type `A` and the `h+1` events of type `B` in one
period advance their respective streams.  Every block of at most `2b-2`
emissions is injective.  Indeed, such a block contains at most `b`
consecutive emissions from either shore, and one complete turn through a
shore stream has no repetition.  This argument is independent of the
origin chosen for the type period and of the two stream origins.  In
particular every window in (1.3), and every token of rank at most `2b-2`
below, is a genuine set.

For `1<=L<=b^2`, a labelled core fragment of length `L` and start `a` is

\[
                         F_L(a)=\{C_a,\ldots,C_{a+L-1}\}.       \tag{1.4}
\]

For every token rank `s` in a fixed band, its designated tokens are

\[
 T_s(a,j)=\{w_{a+j},\ldots,w_{a+j+s-1}\},
                         \qquad 0\le j<L.                       \tag{1.5}
\]

Only the following elementary compiler facts are used below: different
selected cores are disjoint, a fragment block costs `L+g-1` letters when
tokens through rank `g` are retained, and every target not supplied by a
token can be appended as one set-valued letter.

For `U subseteq V`, let `H_(b,L)[U]` denote the induced labelled fragment
hypergraph: a labelled phase/start pair is an edge precisely when all of
its `L` consecutive middle windows lie in `U`.  Thus `H_(b,L)[U]` is
edge-free exactly when no phase-refined atom has a length-`L` interval of
middle windows wholly contained in `U`.

## 2. Balanced quotas are not the exact compiler gate

Choose fragments in stages `j`, with `1<=L_j<=b^2` and `t_j`
fragments, and suppose that all middle cores are mutually disjoint.  Put

\[
 M_j=L_jt_j,\qquad M=\sum_jM_j.                                \tag{2.1}
\]

At rank `s`, let

\[
 A_s(T)=\#\{(j,F,u):F\hbox{ is selected at stage }j,
                         \ T_s(F,u)=T\},                        \tag{2.2}
\]

and let

\[
 I_s=\{T:A_s(T)>0\},\qquad h_s=N_s-|I_s|,qquad
                         N_s={2b\choose s}.                     \tag{2.3}
\]

Thus `h_s` is the literal number of missing rank-`s` targets.

### Theorem 2.1 (direct band-hole compiler)

For any integer `0<=H<=b-2` and `g=b+H`,

\[
 \boxed{
 \nu(2b)\le
 M+(g-1)\sum_j{M_j\over L_j}
 +\sum_{s=b-H}^{b+H}h_s
 +\sum_{|s-b|>H}{2b\choose s}.}                                \tag{2.4}
\]

Consequently, the three conditions

\[
 M=(1-o(1))W,\qquad
 {g\over W}\sum_j{M_j\over L_j}=o(1),\qquad
 \sum_{s=b-H}^{b+H}h_s=o(W),                                   \tag{2.5}
\]

together with a binomial tail `sum_(|s-b|>H) N_s=o(W)`, imply

\[
                         \nu(2b)=(1+o(1))W.                    \tag{2.6}
\]

#### Proof

All unqualified rank sums in this theorem range over the nonempty ranks
`1<=s<=2b`.  The restriction `H<=b-2` gives `g<=2b-2`, so every designated
token is a genuine set of its displayed rank by Section 1.

Linearize each selected fragment as

\[
 \{w_a\},\{w_{a+1}\},\ldots,\{w_{a+L_j+g-2}\}.               \tag{2.7}
\]

Every token (1.5) in the band is a consecutive union in its own block.
The blocks cost

\[
 \sum_jt_j(L_j+g-1)=M+(g-1)\sum_j{M_j\over L_j}.               \tag{2.8}
\]

Append each target absent from `I_s` as a single set-valued letter, and do
the same at every rank outside the band.  This gives (2.4).  Under (2.5)
and the tail assumption its right side is `(1+o(1))W`.

Conversely, at one fixed word position, all interval unions ending there
form an inclusion chain.  At most one middle target can be charged to that
endpoint, so every universal word has at least `W` positions.  This proves
(2.6).  \(\square\)

The theorem contains no quota vector.  The quota-overflow statement used in
the earlier compiler is a sufficient way to upper-bound `h_s`, but it is not
the object required by the word construction.

For completeness, this distinction has an exact finite formulation.  Fix
one rank, write `N=N_s`, and let `A(T)` be any nonnegative integer load of
total `M`.  Put `M=aN+r`, `0<=r<N`, and arrange the loads as

\[
                         A_{(1)}\ge\cdots\ge A_{(N)}.            \tag{2.9}
\]

Among all balanced integer quotas `Q`, whose entries are `a` or `a+1` and
whose total is `M`, the minimum overflow is

\[
 \boxed{
 V_{\min}(A)=
 \sum_{i=1}^{r}(A_{(i)}-a-1)_+
 +\sum_{i=r+1}^{N}(A_{(i)}-a)_+.}                              \tag{2.10}
\]

Indeed an exchange puts every high quota on one of the `r` largest loads,
and then the displayed expression is forced.  When `M<=N`, (2.10) becomes

\[
                         V_{\min}(A)=M-|I|,                     \tag{2.11}
\]

and hence

\[
                         h=(N-M)+V_{\min}(A).                   \tag{2.12}
\]

For `M>N`, small hole count is strictly weaker than small balanced
overflow.  For example, with `M=2N` and `N` even, a load equal to `3` on
half the targets and `1` on the other half has no holes but has minimum
balanced overflow `N/2`.  Thus replacing aggregate quota overflow by the
literal hole sum in (2.5) is a genuine logical weakening.

### Corollary 2.2 (smaller exact Gate-C premise)

In the density-adapted multiscale schedule, it is enough to construct
residual-disjoint core fragments which leave `o(W)` middle vertices, have
`o(W)` total seam cost, and satisfy

\[
 \boxed{
 \sum_{s=b-H}^{b+H}
 \left|{\Omega\choose s}\setminus
       \{T_s(F,u):F\hbox{ selected},\ 0\le u<|F|\}
 \right|=o(W).}                                                \tag{2.13}
\]

No stagewise quota choice and no balanced load upper bound is needed.
Equation (2.13) is still open; it is a simultaneous near-surjectivity
problem for the actual fragment tokens.

## 3. A complement-closed point-balanced obstruction

Fix two distinct coordinates `z,y in Omega`, and define the equality junta

\[
 {\cal E}_{z,y}=\{C\in{\cal V}:\mathbf1_{z\in C}
                                  =\mathbf1_{y\in C}\}.         \tag{3.1}
\]

### Theorem 3.1 (balanced two-junta obstruction)

The family (3.1) has the following three properties.

1. Its exact size is

   \[
   |{\cal E}_{z,y}|=2{2b-2\choose b-2},\qquad
   {|{\cal E}_{z,y}|\over W}={b-1\over2b-1}.                  \tag{3.2}
   \]

2. It is closed under complementation, and for every coordinate `u`,

   \[
   |\{C\in{\cal E}_{z,y}:u\in C\}|={1\over2}|{\cal E}_{z,y}|.
                                                                    \tag{3.3}
   \]

3. On every phase-refined atom, the cyclic runs of starts `t` for which
   `C_t in E_(z,y)` have length at most `b`.  Consequently

   \[
                    {\cal H}_{b,L}[{\cal E}_{z,y}]
                    \text{ is edge-free for }b+1\le L\le b^2. \tag{3.4}
   \]

#### Proof

A member of (3.1) contains both distinguished coordinates or neither.  The
two cases give

\[
 {2b-2\choose b-2}+{2b-2\choose b}
                         =2{2b-2\choose b-2},                   \tag{3.5}
\]

and division by `binom(2b,b)` gives (3.2).  Complementation preserves
equality of the two membership bits.  It pairs every member with a distinct
complement, exactly one of which contains a prescribed coordinate `u`.
This proves (3.3).

It remains to prove the run bound.  Suppose, to the contrary, that

\[
                         C_t,C_{t+1},\ldots,C_{t+b}             \tag{3.6}
\]

all belong to (3.1).  In the transition from `C_(t+i)` to
`C_(t+i+1)`, the word removes `w_(t+i)` and inserts `w_(t+i+b)`.
These are distinct, and neither occurs elsewhere in the relevant middle
window.  If exactly one of these two letters is `z` or `y`, equality of the
two membership bits is toggled.  If the two letters are `z` and `y`, one is
removed and the other inserted, so the membership bits are unequal both
before and after the transition.  Both alternatives contradict (3.6).
Hence neither `z` nor `y` occurs among

\[
                         w_t,w_{t+1},\ldots,w_{t+2b-1}.          \tag{3.7}
\]

But (3.7) consists of exactly two whole type periods.  It contains `b-1`
consecutive emissions of the `A` stream, hence `b-1` distinct coordinates
of `A`, and `b+1` consecutive emissions of the `B` stream, hence every
coordinate of `B`.  Thus it contains exactly `2b-1` distinct coordinates
and omits only one coordinate of `Omega`.  It cannot omit both `z` and
`y`, a contradiction.  Therefore an equality run has length at most `b`,
which proves (3.4).  The reasoning used only a length-`2b` interval of the
periodic type stream, so it applies without change at every phase origin,
including intervals crossing the chosen end of the displayed cyclic word.
\(\square\)

This obstruction survives precisely the most natural repair of the
coordinate-star example: (3.3) gives exact, not approximate, point balance.

## 4. Polynomial-density balanced obstructions

Choose `m` disjoint coordinate pairs

\[
                         (z_1,y_1),\ldots,(z_m,y_m)              \tag{4.1}
\]

and put

\[
                         {\cal E}_m=\bigcap_{i=1}^m
                                           {\cal E}_{z_i,y_i}. \tag{4.2}
\]

### Theorem 4.1 (all polynomial residual scales)

For `m=o(sqrt(b))`,

\[
 {|{\cal E}_m|\over W}
                         =2^{-m}\exp\!\left(O(m^2/b)\right).   \tag{4.3}
\]

The family `E_m` is complement-closed, satisfies the exact point balances
(3.3), and is edge-free in `H_(b,L)` for every `b+1<=L<=b^2`.  In particular,
for every fixed `gamma>0`, taking

\[
                         m=\lfloor\gamma\log_2b\rfloor         \tag{4.4}
\]

gives a point-balanced fragment-free residual of size

\[
                         |{\cal E}_m|=b^{-\gamma+o(1)}W.        \tag{4.5}
\]

#### Proof

The exact enumerator is

\[
 |{\cal E}_m|=[x^b](1+x^2)^m(1+x)^{2b-2m}.                    \tag{4.6}
\]

Equivalently, expose the membership pattern on the `2m` distinguished
coordinates.  A fixed pattern with `a` ones has probability

\[
 { {2b-2m\choose b-a}\over {2b\choose b}}
 ={(b)_a(b)_{2m-a}\over(2b)_{2m}}
 =2^{-2m}\exp\!\left(O(m^2/b)\right),                          \tag{4.7}
\]

uniformly in `0<=a<=2m`, where `(x)_j=x(x-1)...(x-j+1)`.  Indeed,
`log((x)_j/x^j)=sum_(ell<j) log(1-ell/x)=O(j^2/x)` uniformly for
`j=O(m)=o(sqrt(b))`.  Exactly `2^m` patterns obey all pair equalities.
Summing (4.7) proves (4.3).

Complementation preserves every equality in (4.2), so the complement
pairing proves exact point balance.  Also `E_m` is a subset of
`E_(z_1,y_1)`, and Theorem 3.1 proves edge-freeness.  Finally (4.3)--(4.4)
give (4.5).  \(\square\)

The obstruction therefore exists not only at density `1/2`, but at the
same polynomial scales at which the multiscale schedule seeks to stop.

## 5. A necessary quantitative anti-two-junta invariant

The preceding proof yields a useful necessary condition, rather than only
an edge-free example.  In any binary interval of length `L` whose runs of
ones have length at most `b`, the number of zeros is at least

\[
                         \left\lfloor{L\over b+1}\right\rfloor. \tag{5.1}
\]

Indeed `k` zeros can separate at most `k+1` one-runs and hence support at
most `b+k(b+1)` total positions; (5.1) is the equivalent integer bound.

Let `U subseteq V`, and suppose a length-`L` core matching inside `U`, with
`1<=L<=b^2`, covers at least `theta|U|` vertices.  If it has `t` cores,
the distinctness proved after (1.3) gives `tL>=theta|U|`.  Applying (5.1)
to every matched fragment, and then using core disjointness, gives at least
`t floor(L/(b+1))` distinct vertices outside any fixed equality junta.
Consequently, for every pair `z!=y`,

\[
 \boxed{
 {|U\setminus{\cal E}_{z,y}|\over|U|}
 \ge {\theta\over L}\left\lfloor{L\over b+1}\right\rfloor.} \tag{5.2}
\]

Thus a recursive proof must prevent the actual residual from concentrating
inside any equality junta.  Point balance and complement closure do not do
so, by Theorem 4.1.  Condition (5.2) is necessary but is not asserted to be
sufficient; a complete positive theorem must additionally prove genuine
track supersaturation and the direct band near-surjectivity (2.13).

The exact Gate-C target is therefore smaller and sharper than the earlier
quota formulation:

* construct the residual-disjoint density-adapted fragments;
* preserve enough higher-order anti-junta/track expansion to continue the
  recursion, at least beyond the necessary tests (5.2); and
* prove the literal aggregate band-hole bound (2.13).

No balanced stage-quota construction is independently required.
