# Odd `h=1`: rooted excursions and an all-upper guarded reversal lift

**Date:** 2026-08-02  
**Status:** exact reductions and a sufficient construction theorem.  The
results below do not prove that the required guarded reversal exists, do not
solve the lower compiler, and do not prove `nu(17)=24313`.

## 0. Outcome

There are two useful exact descriptions of the downstream gates left by the
fixed-boundary lollipop theorem.

1. After one parity matching is fixed, every lollipop is a Hamilton path in
   an `(r-1)`-regular directed **root-link graph**.  Positive residence and
   every upper target become component/excursion conditions on the same
   labelled path.  In particular, no source-age variables are needed to test
   the unmarked residence row.
2. A two-cut reversal can turn an exact-q1 cycle into the required `h=1`
   missing/duplicated-colour cycle while preserving **all** upper interval
   unions and positive residence.  The complete all-width upper condition
   is one exact prefix/suffix cross-grid containment, and residence is one
   explicit seam-aperture test.

The second result is a genuine guarded lift: once its finite port conditions
are met, neither ranks 11 through `k` nor the residence row need a later
repair.  Its existence in every dimension remains open.

## 1. The root-link digraph

Put

\[
 k=2r-1,\qquad
 \mathcal Q={{[k]}\choose {r-1}},\qquad
 \mathcal T={{[k]}\choose r},\qquad
 W=|\mathcal Q|=|\mathcal T|.
\]

Fix a perfect containment matching

\[
                     \mu:\mathcal Q\longrightarrow\mathcal T,
                     \qquad L\subset\mu(L).              \tag{1.1}
\]

Define the directed root-link graph `A_mu` on `mathcal Q` by

\[
 L\longrightarrow L'
 \quad\Longleftrightarrow\quad
 L\subset\mu(L'),\qquad L\ne L'.                         \tag{1.2}
\]

Every vertex has indegree and outdegree `r-1`.  Indeed, the owner `mu(L')`
has `r` coatoms, one of which is `L'`; and a fixed coatom `L` lies in `r`
owners, one of which is `mu(L)`.

### Theorem 1.1 (rooted Hamilton-path equivalence)

Let

\[
                         L_0\to L_1\to\cdots\to L_{W-1}    \tag{1.3}
\]

be a directed Hamilton path in `A_mu`, and put

\[
                         T_i=\mu(L_i).                       \tag{1.4}
\]

Then

\[
 T_0,L_0,T_1,L_1,\ldots,T_{W-1},L_{W-1}                   \tag{1.5}
\]

is a spanning alternating Hamilton path in the Middle Levels graph.
Conversely, colouring the incidences of any spanning alternating Hamilton
path by parity and taking its perfect parity class as `mu` gives (1.3), up
to reversing the whole path.

Moreover,

\[
                       T_i\cap T_{i+1}=L_i,                 \tag{1.6}
\]

and its immediate upper colour is

\[
                       T_i\cup T_{i+1}.                     \tag{1.7}
\]

#### Proof

The arc `L_i -> L_(i+1)` says that the nonmatching incidence
`L_i subset mu(L_(i+1))` exists.  Together with the matching incidence
`L_i subset mu(L_i)`, it expands the arc to

\[
                         T_i-L_i-T_{i+1}.
\]

The path uses every matching edge once, every root once and every owner
once.  Since the owners are distinct rank-`r` sets both containing the
rank-`(r-1)` set `L_i`, their intersection is exactly `L_i`.  This proves
(1.5)--(1.7).  Contracting the perfect parity class of an alternating
Hamilton path reverses the argument. \(\square\)

### Theorem 1.2 (fixed-boundary closure in root form)

Assume the Hamilton path (1.3) has terminal root

\[
                         L_{W-1}=M,qquad \mu(M)=B,          \tag{1.8}
\]

and initial owner

\[
                         \mu(L_0)=C.                        \tag{1.9}
\]

Suppose `B,C` are Johnson adjacent, put

\[
                         D=B\cap C,                         \tag{1.10}
\]

and assume

\[
                         D\ne M,\qquad D\ne L_0.             \tag{1.11}
\]

Then the reverse of (1.5) starts with the prescribed
edge `MB`, ends at `C`, and does not use the incidence `CD`.  Adding `CD`
therefore produces the fixed-boundary augmented lollipop.  Applying the
standard reconstruction (delete `MB`, add `DB`, and pair the two occurrences
at `D`) gives the physical owner cycle with missing colour `M`, duplicated
colour `D`, and boundary owner `B=M union D`.  Here `add DB` is an
occurrence-level operation: if the simple incidence `DB` is already selected,
the reconstruction creates the required parallel occurrence at `D`; it does
not assert insertion of a second edge into a simple graph.

The added incidence changes neither the linear owner word nor any property
computed from it.  In particular, residence and every consecutive-owner
union are exactly those of (1.4).

#### Proof

The reversed expanded path starts `M-B` by (1.8) and ends at `C` by (1.9).
Since `C=mu(L_0)` and `mu` is injective, (1.11) says that `CD` is not a
matching incidence.  Its only other possible realization in the expanded
path would be the nonmatching incidence represented by the arc
`D -> L_0`.  This arc is absent because `L_0` has indegree zero on (1.3).
Thus `CD` is absent.  The degree argument of the
fixed-boundary lollipop lemma applies after adding it.  The owner word is not
altered by adjoining the terminal incidence. \(\square\)

Conditions `D != L_0` and `D -> L_0` absent can alternatively be replaced
by the single literal hypothesis `CD notin E(H)`; this is the form to use in
an implementation.

## 2. Exact residence and upper excursions on the rooted path

For a coordinate `x`, let `P_x` be the subgraph of the path (1.3) induced
by the roots whose owner labels contain `x`:

\[
                         x\in\mu(L_i).                     \tag{2.1}
\]

For an upper target `U`, let `P[U]` be the subgraph induced by

\[
                         \mu(L_i)\subseteq U.                \tag{2.2}
\]

### Theorem 2.1 (component/excursion criterion)

1. The component orders of `P_x` are exactly the positive `x`-run lengths
   in the owner word.  Thus internal positive residence floor `h` is
   equivalent to every component of every `P_x` which avoids both path
   endpoints having order at least `h`.
2. An upper target `U` occurs as a consecutive-owner union if and only if
   some component `K` of `P[U]` satisfies

   \[
                         \bigcup_{L_i\in K}\mu(L_i)=U.       \tag{2.3}
   \]
3. For `|U|=r+1`, item 2 is equivalent to the existence of one arc
   `L_i -> L_(i+1)` with

   \[
                         \mu(L_i)\cup\mu(L_{i+1})=U.         \tag{2.4}
   \]

#### Proof

Items 1 and 2 are the maximal-run decomposition of a linear word.  An
interval has union `U` precisely when all its owners lie below `U` and their
union is `U`; enlarging it to its maximal below-`U` run proves item 2.

For item 3, (2.4) is plainly sufficient.  Conversely, scan any interval
whose union has rank `r+1`.  At its first transition the two distinct
rank-`r` owners have intersection rank `r-1`, so their union already has rank
`r+1`; being contained in `U`, that union equals `U`. \(\square\)

The path has exactly `W-1` arcs, and item 3 counts exactly those `W-1`
linear owner adjacencies.  The added closure incidence `CD`, equivalently
the omitted physical opening/wrap, is not an arc of (1.3) and supplies no
rank-`r+1` provider.  Thus (2.4) already has the correct opening semantics;
no separate subtraction row is hidden in the rooted formulation.

There is an equivalent first-arrival form.  Orient the owner path and write

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.                    \tag{2.5}
\]

Then

\[
             \bigcup_{t=p}^qT_t
                =T_p\cup\{\beta_p,\beta_{p+1},\ldots,
                                      \beta_{q-1}\}.        \tag{2.6}
\]

Thus a target `U` occurs exactly when some interval starts with `T_p subset
U`, has every subsequent insertion label in `U`, and sees every member of
`U minus T_p` at least once.  Formula (2.6) is often a much smaller exact
upper oracle than enumerating all interval unions.

At `K17`, residence is the component floor four in item 1, while the upper
oracle in items 2--3 covers ranks 10 through 17 on the very same rooted
Hamilton path.

## 3. A guarded two-cut reversal

We now give a sufficient construction which preserves those two gates.

Let an exact-q1 Hamilton owner cycle be written cyclically as below, with
`AX` and `YB` two distinct vertex-disjoint cut edges:

\[
                 A,\ X=S_1,S_2,\ldots,S_\ell=Y,\
                 B=R_1,R_2,\ldots,R_t=A.                  \tag{3.1}
\]

The repeated `A` only displays the cyclic closure.  The opened linear word
at the edge `AX` is

\[
                         W_0=S R,                         \tag{3.2}
\]

where `S=(X,...,Y)` and `R=(B,...,A)` contain every owner exactly once.

Assume all four seams below are Johnson and put

\[
\begin{aligned}
 M&=A\cap X, &N&=Y\cap B,\\
 D&=A\cap Y, &N&=X\cap B.                              \tag{3.3}
\end{aligned}
\]

Thus the second equation deliberately requires the old and new far seam to
have the same colour.  Require `D != M`.

Delete `AX,YB` and add `AY,XB`.  Open the new cycle at `AY`.  Its linear
owner word is

\[
                         W_1=S^{\rm rev}R.                 \tag{3.4}
\]

### Lemma 3.1 (exact q1 current and boundary)

The q1 colour multiset of the new cycle is the old exact palette plus the
current

\[
                              -[M]+[D].                    \tag{3.5}

Hence `M` is the unique missing colour and `D` the unique duplicated colour.
The opened edge has colour `D`, and its endpoint `A` contains `M`; moreover

\[
                              A=M\cup D.                   \tag{3.6}

Thus (3.4) is a valid `h=1` fixed-boundary chronology.

#### Proof

Only the two cut edges change.  Their old colours are `M,N` and their new
colours are `D,N`, proving (3.5).  The distinct rank-`(r-1)` sets `M,D` are
both facets of the rank-`r` owner `A`, proving (3.6). \(\square\)

## 4. All-width upper preservation

For a word fragment `S`, put

\[
\begin{aligned}
 \mathcal P(S)&=\left\{\bigcup_{i=1}^jS_i:1\le j\le\ell\right\},\\
 \mathcal S(S)&=\left\{\bigcup_{i=j}^{\ell}S_i:1\le j\le\ell\right\}.
                                                               \tag{4.1}
\end{aligned}
\]

Also write `mathcal U(S)` for the set of all internal interval unions and
define

\[
\begin{aligned}
 \mathcal C_-(S,R)
   &=\{V\cup Z:V\in\mathcal S(S),\ Z\in\mathcal P(R)\},\\
 \mathcal C_+(S,R)
   &=\{V\cup Z:V\in\mathcal P(S),\ Z\in\mathcal P(R)\}.
                                                               \tag{4.2}
\end{aligned}
\]

Reversal gives the exact support identities

\[
\begin{aligned}
 \mathcal U(SR)
   &=\mathcal U(S)\cup\mathcal U(R)\cup\mathcal C_-(S,R),\\
 \mathcal U(S^{\rm rev}R)
   &=\mathcal U(S)\cup\mathcal U(R)\cup\mathcal C_+(S,R).
                                                               \tag{4.3}
\end{aligned}
\]

Thus preservation of every old interval-union value is **equivalent** to

\[
 \mathcal C_-(S,R)\subseteq
 \mathcal U(S)\cup\mathcal U(R)\cup\mathcal C_+(S,R).         \tag{4.4}
\]

This is the exact cross-grid oracle for a proposed cut pair.

### Theorem 4.1 (exact reversal-loss set)

Put

\[
 \mathcal L(S,R)=\mathcal C_-(S,R)\setminus
 \bigl(\mathcal U(S)\cup\mathcal U(R)\cup\mathcal C_+(S,R)\bigr). \tag{4.5}
\]

Then

\[
                  \mathcal U(W_0)\setminus\mathcal U(W_1)
                             =\mathcal L(S,R).             \tag{4.6}
\]

Every member of `mathcal L(S,R)` has rank at least `r+1`.  Consequently,
if `W_0` covers every upper target, then `W_1` does so if and only if

\[
                             \mathcal L(S,R)=\varnothing.  \tag{4.7}
\]

#### Proof

Equation (4.6) is immediate from the two identities (4.3).  A crossing
interval contains the old seam owners `Y,B`, which are distinct adjacent
rank-`r` owners, so its union has rank at least `r+1`.  Thus every lost value
is a required upper target.  If `W_0` is upper-complete, `W_1` is upper-
complete precisely when none is lost, proving (4.7). \(\square\)

The tempting context-free condition
`mathcal S(S) subseteq mathcal P(S)` would imply (4.7), but it is impossible
for a nontrivial owner-once rank-`r` segment: its singleton suffix `Y` could
equal no prefix union except the distinct singleton prefix `X`.  Therefore
(4.5), not that vacuous stronger condition, is the relevant finite oracle.

## 5. Exact residence aperture

Assume `W_0=SR` has internal positive-run floor `h`.  For a coordinate `x`,
let

* `epsilon_S(x)` and `epsilon_R(x)` be its first bits in `S,R`;
* `p_S(x),p_R(x)` be the lengths of the corresponding initial bit blocks;
* `c_S(x),c_R(x)` say that the entire fragment has that constant bit.

Only positive blocks (`bit=1`) matter below.

### Theorem 5.1 (one-seam residence criterion)

The reversed word `W_1=S^(rev)R` has internal positive-run floor `h` if and
only if, for every coordinate `x`, the following new-seam test holds.

1. If `epsilon_S=epsilon_R=1` and neither fragment is constantly one, then

   \[
                              p_S+p_R\ge h.                \tag{5.1}
   \]
2. If `epsilon_S=1, epsilon_R=0` and `S` is not constantly one, then

   \[
                              p_S\ge h.                    \tag{5.2}
   \]
3. If `epsilon_S=0, epsilon_R=1` and `R` is not constantly one, then

   \[
                              p_R\ge h.                    \tag{5.3}
   \]

There is no new positive condition when both first bits are zero.  The
negative-gap version is obtained by complementing every bit.

#### Proof

Reversal preserves every run internal to `S` and merely swaps its two
boundary blocks.  The old terminal block of `S` becomes the clipped left
boundary block of `W_1`, so it creates no internal obligation.  The old
initial block of `S` becomes the block immediately before the unique seam
`S^(rev)|R`.

If the two seam bits are one, the two displayed initial blocks merge; the
merged block is internal exactly when neither fragment is constantly one,
giving (5.1).  If the bits differ, each positive seam block terminates by
itself.  The `S` block is clipped exactly when `S` is constantly one, and
the `R` block is clipped exactly when `R` is constantly one, giving
(5.2)--(5.3).  Every other positive run is an unchanged internal run of one
fragment. \(\square\)

## 6. Guarded reversal lift theorem

### Theorem 6.1

Suppose the exact-q1 cycle (3.1) satisfies all of the following.

1. The opening `W_0=SR` covers every upper target.
2. It has internal positive-run floor `h`.
3. The four seam equations (3.3) hold with `D != M`.
4. The exact reversal-loss set (4.5) is empty.
5. The aperture rows (5.1)--(5.3) hold.

Then the two-cut rethread, opened at `AY`, is an `h=1` fixed-boundary
chronology with

* every owner exactly once;
* q1 load zero at `M`, load two at `D`, and load one elsewhere;
* every upper target covered; and
* internal positive-run floor `h`.

For `K17`, taking `h=4` closes the central, residence, and complete-upper
rows of the `h=1` outer carrier.  The age/refresh choice and the literal
rank-one-through-seven compiler remain separate.

#### Proof

The two-cut reconnection of the two opened owner paths is one Hamilton
cycle.  Lemma 3.1 proves the exact q1 current and boundary port.  Theorem
4.1 transports the complete upper deck from `W_0` to `W_1`.  Theorem 5.1
proves residence. \(\square\)

## 7. Exact scope and search consequence

The theorem is deliberately one-sided.  It does not assert that a known
carrier contains such cuts, and the cross-grid condition (4.5) can be
restrictive.
It does show that a successful `h=1` repair need not re-solve arbitrary
upper ranks after the rethread: a finite prefix/suffix signature plus the
single seam aperture is enough.

For a finite selector, one may therefore search cut pairs in the following
fail-closed order:

1. the four Johnson/q1 equations (3.3);
2. the exact cross-grid loss set (4.5), computed from first-arrival prefix
   and suffix unions;
3. the `k` aperture checks (5.1)--(5.3);
4. only then the lower age/refresh compiler.

No rank-11-through-`k` replay is needed after item 2, provided the old
opening `W_0` was authenticated upper-complete.
