# Affine whole-chain loads, the exact retirement LP, and the full-chain matching obstruction

**Status (2026-08-21).**  Every theorem-level assertion below is proved.
This note analyzes the genuinely shared-offset token object for the affine
nested schedule.

There are three conclusions.

1.  The natural whole-chain orbit law has exact source and token load one,
    exact target load `T_(q,s)/P_(q,s)`, and explicitly computable pair
    loads.  Thus the affine scalar-capacity theorem is exactly the target
    marginal ledger of one formally legal nested-chain orbit law.
2.  An ordinary matching of edges which claim **all** targets
    `q=1,...,H` is the wrong simultaneous object.  Its aggregate rank
    deficit is

    \[
      \Omega(\sqrt b\,W_b),\qquad W_b={2b\choose b},             \tag{0.1}
    \]

    solely because every selected edge occupies a rank-`(b+H)` target.
    This is a sharp cardinality obstruction, not an order-bank subtlety.
3.  The correct fractional object is a chain with a nested real-claim
    prefix and a retirement time.  Its existence and optimum reduce exactly
    to a finite scalar path-packing LP.  Every feasible point of that LP
    lifts to a labelled retired-chain fractional matching whose maximum
    pair load is `O(1/b)` on the central payload band.

The note does **not** prove that the retirement LP has `o(W_b)` aggregate
deficit asymptotically, nor that its fractional solutions round integrally.
Merging equal-profile nodes in an ordinary network flow permits the flow to
change affine phase/token identity.  Preserving that identity is a colored
path constraint, and the labelled formulation retains the known
determinant-two non-TU face.  This is the exact shared-offset gate left by
the scalar theorem.

## 1. The affine path types and occurrence tokens

Let `b` be an odd prime, let `A,B` be disjoint `b`-sets, and put

\[
 W_b={2b\choose b},\qquad
 H=\Theta(\sqrt{b\log b}),\qquad
 g=\lfloor b/4\rfloor.                              \tag{1.1}
\]

Retain source splits

\[
 J=\{g,g+1,\ldots,b-g\},
 \qquad L_r={b\choose r}^{\!2}.                     \tag{1.2}
\]

The removed source mass is `e^(-Omega(b))W_b`.  On the type phases
`Z_b`, use the affine nested schedule

\[
 R(x)={b-1\over2}x\pmod b,
 \qquad P_r=\{x:R(x)<r\}.                           \tag{1.3}
\]

For a base phase `p`, define its prefix type counts and target profiles by

\[
 z_{r,p}(q)=|P_r\cap\{p+1,\ldots,p+q\}|,
 \qquad s_{r,p}(q)=r+z_{r,p}(q).                    \tag{1.4}
\]

One occurrence-token class is indexed by the complete path type
`i=(r,p)`.  Its token count is

\[
 a_i=|\mathcal O_{r,p}|={L_r\over b}.               \tag{1.5}
\]

This is an integer because `b` divides `binom(b,r)` for prime `b` and
`0<r<b`.  Across the `b` phases there are exactly `L_r` tokens, matching
the number of middle sources of split `r`.

Fix a source `U` of split `r`.  A labelled chain of type `(r,p)` is

\[
 U=V_0\subset V_1\subset\cdots\subset V_H,          \tag{1.6}
\]

where the `q`th new label lies in `A` precisely when
`p+q in P_r`.  Write `(n)_k=n(n-1)...(n-k+1)`.  The exact number of such
ordered chains from `U` is

\[
 D_i(H)=(b-r)_{z_{r,p}(H)}
        (r)_{H-z_{r,p}(H)}.                         \tag{1.7}
\]

The first factor orders distinct labels of `A\setminus U`; the second does
the same in `B\setminus U`.

## 2. The raw whole-chain hypergraph and its exact loads

Let `\mathcal C_H` have vertex classes consisting of all occurrence tokens,
all retained middle sources, and one copy of every rank-`(b+q)` target for
each `1<=q<=H`.  Its edges are

\[
 (o,U,V_1,\ldots,V_H)                               \tag{2.1}
\]

whenever `o in O_(r,p)` and (1.6) is a chain of type `(r,p)`.  Give every
such edge the weight

\[
 \theta_H(o,U,V_1,\ldots,V_H)
 ={1\over L_rD_i(H)}.                               \tag{2.2}
\]

This is the orbit-symmetrized whole-chain law.  It is not generally a
fractional matching because some target loads exceed one.

For later formulas put

\[
 P_{q,s}={b\choose s}{b\choose s-q},               \tag{2.3}
\]

\[
 T_{q,s}^{\rm aff}
 ={1\over b}\sum_{\substack{r\in J,\ p\in\mathbb Z_b\\
                             s_{r,p}(q)=s}}L_r.     \tag{2.4}
\]

This is exactly the affine capacity in the preceding scalar theorem.

### Theorem 2.1 (exact raw loads)

Under (2.2):

1. every retained middle source has load one;
2. every occurrence token has load one; and
3. every target `V` in profile `(q,s)` has load

   \[
     \boxed{\ell_\theta(V)={T_{q,s}^{\rm aff}\over P_{q,s}}.}    \tag{2.5}
   \]

#### Proof

Fix a source `U`.  For one phase type `i=(r,p)`, summing over its
`a_i=L_r/b` tokens and its `D_i(H)` chains gives load `1/b`; summing over
`p` gives one.  For a fixed token, summing over the `L_r` sources and their
`D_i(H)` chains also gives one.

Now fix `V` in profile `(q,s)`, and put `z=s-r`.  The number of split-`r`
sources contained in `V` is

\[
 N_{r,q,z}={s\choose r}{b+q-s\choose b-r},          \tag{2.6}
\]

while the number of possible rank-`q` targets of this profile from one
source is

\[
 B_{r,q,z}={b-r\choose z}{r\choose q-z}.            \tag{2.7}
\]

Uniform ordered completion of a chain hits a prescribed `V` with
probability `1/B_(r,q,z)`.  The choose-in-either-order identity is

\[
 {N_{r,q,z}\over B_{r,q,z}}={L_r\over P_{q,s}}.     \tag{2.8}
\]

Thus one compatible phase contributes `L_r/(bP_(q,s))` to the load of
`V`.  Summing (2.8) over the phase/path types in (2.4) proves (2.5).
\(\square\)

The equality (2.5) is important: the scalar phase capacity is not merely an
analogy to a joint chain law.  It is its exact target marginal.

## 3. Exact pair loads

The same counting gives all nonzero pair types.  A fixed compatible
token--source pair has load

\[
 {1\over L_r}.                                      \tag{3.1}
\]

A fixed token of type `(r,p)` and a compatible target in profile `(q,s)`
have pair load

\[
 {1\over P_{q,s}}.                                  \tag{3.2}
\]

A fixed source `U` and target `V` with `z=s-r` have pair load

\[
 {n_{r,q,z}^{\rm aff}\over bB_{r,q,z}},             \tag{3.3}
\]

where

\[
 n_{r,q,z}^{\rm aff}
 =|\{p:z_{r,p}(q)=z\}|.                             \tag{3.4}
\]

For target--target pairs, let `q<q'`, let `V subset V'`, and write their
profiles as `s,s'`.  Put

\[
 E_{q,s}^{q',s'}
 ={b-s\choose s'-s}
  {s-q\choose(q'-q)-(s'-s)}.                       \tag{3.5}
\]

This is the number of compatible profile-`s'` extensions of a fixed
profile-`s` target.  Finally set

\[
 n_r(q,s;q',s')
 =|\{p:s_{r,p}(q)=s,\ s_{r,p}(q')=s'\}|.           \tag{3.6}
\]

Then the pair load is exactly

\[
 \boxed{
 \ell_\theta(V,V')
 ={1\over bP_{q,s}E_{q,s}^{q',s'}}
  \sum_{r\in J}n_r(q,s;q',s')L_r.}                 \tag{3.7}
\]

All incompatible pairs have load zero.

To prove (3.7), first choose a source inside `V`, then prescribe `V`, then
prescribe its extension `V'`; the three successive denominators are exactly
those in (2.8) and (3.5).  Equations (3.1)--(3.3) are the corresponding
one-step specializations.

On the central band, every nontrivial extension number in (2.7) or (3.5)
is at least `g-H`.  Consequently a target--target pair carries at most
`1/(g-H)` of the load of its first target.  This conditional small-codegree
fact survives every target-feasible thinning below.

## 4. Why a full-`H` matching is impossible at the required scale

Let `\mathcal M` be any ordinary matching in `C_H`, and put
`N=|\mathcal M|`.  Every edge contains one rank-`(b+H)` target, so

\[
 N\le M_H={2b\choose b+H}.                          \tag{4.1}
\]

The matching covers exactly `N` targets at every layer.  Therefore its
aggregate uncovered-target count is at least

\[
 \boxed{
 \sum_{q=1}^H(M_q-N)
 \ge\sum_{q=1}^H(M_q-M_H).}                        \tag{4.2}
\]

For `q<=c\sqrt b`, the exact product formula for `M_q/W_b` is bounded below
by a positive constant depending only on `c`.  On the other hand, (1.1)
gives

\[
 {M_H\over W_b}\le\exp(-c'H^2/b)=b^{-\Omega(1)}.   \tag{4.3}
\]

Taking `Theta(sqrt b)` terms in (4.2) proves (0.1).  Since
`sum_(q>=1)M_q=Theta(sqrt b W_b)`, the order of this obstruction is sharp.

The same obstruction applies to the most obvious full-chain fractional
thinning.  If

\[
 \rho_{q,s}=\min(1,P_{q,s}/T_{q,s}^{\rm aff})       \tag{4.4}
\]

and every path type `(r,p)` is scaled by

\[
 \kappa_{r,p}=\min_{1\le q\le H}
               \rho_{q,s_{r,p}(q)},                \tag{4.5}
\]

then all target loads become at most one, but the resulting fractional
edge mass is at most `M_H` by the rank-`H` target constraint.  Neither
small pair loads nor scalar surplus can defeat this last-shore bound.

## 5. The correct object: nested retirement

A physical chain may exist through the whole band while only an initial
prefix of its targets is declared real.  At a retirement time `ell`, its
real target vertices are

\[
 V_1,\ldots,V_\ell,                                 \tag{5.1}
\]

and all later observations are dummy claims.  This permits the number of
real chains to decrease with `q`, as the Boolean layer sizes do.

For every path type `i=(r,p)`, let `x_i(q)` be its surviving real mass at
offset `q`.  The exact scalar retirement LP is

\[
 0\le x_i(H)\le\cdots\le x_i(2)\le x_i(1)\le a_i, \tag{5.2}
\]

\[
 \sum_{\substack{i=(r,p)\\s_{r,p}(q)=s}}x_i(q)
 \le P_{q,s}\qquad(1\le q\le H).                  \tag{5.3}
\]

Its objective is

\[
 \Phi(x)=\sum_{q=1}^H\sum_i x_i(q).                \tag{5.4}
\]

Thus its quota-relative aggregate deficit is exactly

\[
 \mathfrak D_{\rm ret}
 =\sum_{q=1}^HM_q-\max\Phi(x).                     \tag{5.5}
\]

The variables retain the complete affine phase identity `i`; (5.2) forbids
retirement followed by revival.

Equivalently, let `y_i(ell)>=0` be the mass of path `i` whose last real
offset is `ell`.  The path-capacity constraints are
`sum_ell y_i(ell)<=a_i`, and a column `(i,ell)` uses the profile resource
`(q,s_i(q))` once for every `q<=ell`.  The exact LP dual is therefore

\[
 \min\left\{
  \sum_i a_i\alpha_i+\sum_{q,s}P_{q,s}\beta_{q,s}:
  \alpha_i+\sum_{q=1}^{\ell}\beta_{q,s_i(q)}\ge\ell
  \quad\forall i,\ell\right\},                    \tag{5.5a}
\]

with `alpha_i,beta_(q,s)>=0`.  Thus a counterexample to (7.2) can be given
sharply by a feasible dual family of cost at most
`sum_q M_q-Omega(W_b)`; more generally, the gap between `sum_q M_q` and
the dual cost exactly quantifies the certified retirement obstruction.  No
vague Hall condition is needed.

### Theorem 5.1 (exact labelled lift of every scalar retirement point)

Every feasible solution of (5.2)--(5.3) lifts to a fractional matching in
the variable-rank retired-chain hypergraph.  Its total real-target mass is
exactly `Phi(x)`, and every target in profile `(q,s)` has load

\[
 {1\over P_{q,s}}
 \sum_{\substack{i=(r,p)\\s_{r,p}(q)=s}}x_i(q)\le1. \tag{5.6}
\]

On the central payload band, its maximum fractional pair load is

\[
 \boxed{\alpha\le {1\over g-H}+e^{-\Omega(b)}=O(1/b).}          \tag{5.7}
\]

#### Proof

Put `x_i(H+1)=0` and define the retirement masses

\[
 y_i(\ell)=x_i(\ell)-x_i(\ell+1)
 \quad(1\le\ell\le H).                             \tag{5.8}
\]

The unused mass `a_i-x_i(1)` retires before the first real target.  For
`ell>=1`, let

\[
 D_i(\ell)=(b-r)_{z_{r,p}(\ell)}
            (r)_{\ell-z_{r,p}(\ell)}.              \tag{5.9}
\]

Give every compatible retired edge `(o,U,V_1,...,V_ell)` the weight

\[
 {y_i(\ell)\over a_i}\,{1\over L_rD_i(\ell)}.      \tag{5.10}
\]

There are `a_iL_rD_i(ell)` such edges, so their total mass is
`y_i(ell)`.  A fixed token has load
`sum_ell y_i(ell)/a_i=x_i(1)/a_i<=1`.  A fixed source receives
`x_i(1)/L_r` from phase `p`; summing over the `b` phases and using
`a_i=L_r/b` gives load at most one.

At rank `q`, exactly the retirement masses with `ell>=q` remain, and their
sum is `x_i(q)`.  The same orbit count as (2.8) distributes this mass
uniformly over the `P_(q,s)` targets of its profile.  This proves (5.6),
and summing (5.6) over all targets proves the objective assertion.

For pair loads, a token--source pair has load at most `1/L_r`; a
token--target pair at `(q,s)` has load at most `1/P_(q,s)`; and a
source--target pair is at most `1/B_(r,q,z)<=1/g`.  If `q<q'`, the exact
analogue of (3.7) has `x_i(q')` in place of `a_i`.  Since
`x_i(q')<=x_i(q)` and (5.3) holds, it is at most
`1/E_(q,s)^(q',s')<=1/(g-H)`.  The retained `L_r` and `P_(q,s)` are
exponential, proving (5.7).  \(\square\)

The edge sizes in this matching range up to `H+2`, whereas the
Molloy--Reed consequence used in the separate-offset theorem is stated for
fixed rank.  It is therefore not applicable here.  Even if one formally
retains its displayed rank dependence, the relevant factor would be

\[
 \alpha^{1/(H+2)}
 =\exp\!\left[-{\Theta(\log b)\over H}\right]=1-o(1),          \tag{5.11}
\]

not a vanishing loss.  Thus the previous 3-uniform rounding theorem does
not extend formally to this growing-rank object.

## 6. Why ordinary flow is not the retirement LP

If all path types meeting a profile node `(q,s)` are merged in a
time-expanded network, an incoming unit may leave on the continuation of a
different affine phase.  That operation preserves the scalar profile but
not the occurrence token.

There is a literal central example for every sufficiently large odd `b`.
Put `b=2m+1`, `r=m-2`, and compare phases `p=b-2` and `p=b-3`.  Their first
three profile paths are, in one order,

\[
 (r,r+1,r+1),\qquad (r+1,r+1,r+2).                 \tag{6.1}
\]

They meet at the profile node `(q,s)=(2,r+1)` but have different incoming
histories and different outgoing continuations.  A merged-node flow can
splice the first history to the second continuation.  No fixed `(r,p)`
path does that splice.

Constraints (5.2) preserve each path identity and therefore form a colored
path/packing problem, not an ordinary single-commodity flow after profile
merging.  At the labelled level the natural token--source--target matrix
already contains the determinant-two minor

\[
 \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},
 \qquad\det=-2,                                    \tag{6.2}
\]

from the fixed-offset coinstantiation theorem.  Adding retirement layers
does not remove that submatrix.  Hence neither scalar flow integrality nor
the existence of (5.10) implies an integral common-order construction.

## 7. Finite diagnostics and the exact surviving gate

The accompanying H100 audit solves (5.2)--(5.4) numerically for the explicit
half-step schedule.  For `b=31,41,61` and
`H=floor(sqrt(b log b))` (truncated at `b/4`), its optimum agrees, within
the stated solver feasibility tolerance, with the sum of the independent
per-layer scalar optima for the same central payload truncation; it incurs
no detected additional retirement loss.  This is finite evidence, not an
asymptotic theorem.

The same audit shows that the naive pathwise thresholds

\[
 x_i(q)=a_i\min_{j\le q}\rho_{j,s_i(j)}             \tag{7.1}
\]

are feasible but not exact: `rho_(q,s_i(q))` is not pathwise monotone.
Thus the finite LP success genuinely uses redistribution among phase paths
inside common profile capacities; it is not the separate-offset thinning
in disguise.

The exact next scalar question is now (5.5): prove

\[
 \mathfrak D_{\rm ret}=o(W_b)                       \tag{7.2}
\]

for the affine paths, or exhibit a dual family forcing a positive loss.
Even (7.2) would give only the joint fractional orbit theorem (5.10).
Integral rounding must exploit more than the pair bound (5.7), and the
actual physical lift must additionally coinstantiate the same labelled
tight-cycle orders across all tokens and payload ranks.  The raw full-chain
matching, the retired scalar LP, integral orbit rounding, and fixed-factor
order coinstantiation are four distinct levels; this note proves the first
is impossible at the required scale and identifies the latter three
without conflating them.
