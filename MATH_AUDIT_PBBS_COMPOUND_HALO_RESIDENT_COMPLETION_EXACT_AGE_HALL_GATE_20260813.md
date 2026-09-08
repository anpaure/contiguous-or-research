# Audit of the compound-halo age-filtered completion reduction

**Date:** 2026-08-13  
**Audited source:**
`MATH_REDUCTION_PBBS_COMPOUND_HALO_RESIDENT_COMPLETION_EXACT_AGE_HALL_GATE_20260813.md`  
**Source SHA-256:**
`8dffc15beff40e46f318988c0031741636bd3b9b2a55851036fbdc958e428829`  
**Method:** literal matching-phase reconstruction, deterministic capped-age
updates, Hall, and the maximal-antecedent run criterion; no computation or
search.  
**Verdict:** **PASS as an exact fixed-age biresidence reduction, with one
essential scope correction.**  The absent-age singleton obstruction and
the final statement that biresident completion is the next PBBS carrier
gate do not apply to the weaker positive-residence condition actually
needed for a nonempty flat antecedent and ordinary upper rematerialization.
The exact positive-only gate is a strictly larger age-filtered Hall graph.

## 1. Rank orientation and the first matching are correct

The owner shore is

\[
                         X={ [2R-1]\choose R}.
\]

If the first matching sends `T` to the rank-`(R-1)` facet

\[
                         M_0(T)=T\setminus\{x_0\},       \tag{1.1}
\]

then a second incidence through that same facet reaches exactly

\[
 T_y=T\setminus\{x_0\}\cup\{y\},
 \qquad y\notin T.                                      \tag{1.2}
\]

There are `R-1` such heads: the facet has `R` rank-`R` supersets, and the
excluded one is `T` itself.  Dually every head has `R-1` tails.  Thus (3.1),
(4.1)--(4.2), and the claimed regularity are exact.

The rank orientation differs from the older convention in which owners
were the lower shore, but it is internally consistent: orient the
`M_0` incidence from the owner down to its facet and the second incidence
from that facet up to the successor owner.

## 2. The protected phasing really gives a forced successor matching

Every protected component used in the reduction is an owner-to-owner
incidence path.  After orienting it, alternate its incidence edges as
`F_0,F_1`.  Every protected lower facet is internal to that path and is
incident with exactly one edge of each colour.  Hence:

1. `F_0` and `F_1` are matchings;
2. a perfect matching `M_0` containing `F_0` cannot contain an edge of
   `F_1`, because the latter's lower endpoint is already occupied; and
3. each consecutive protected owner transition is one arc from the owner
   incident with `F_0` at that facet to the owner incident with `F_1`.

Distinct path transitions have distinct tails and distinct heads.  They
therefore form a matching `Q` between the split tail and head copies of
`X`, even though a head of one arc may be the tail of the next after the
two copies are identified.  The endpoint schedules are still load-bearing:
they must make every forced arc age-legal.  Subject to that declared local
premise, the phasing assertion in Section 3 is correct.

The polynomial protected matching-extension theorem applies to `F_0`
under the frozen polynomial-size and sub-half exposure bounds.  It supplies
an `M_0`; it does not supply the second age-filtered matching.

## 3. The biresident Hall theorem is exact

Fix `M_0`, a full signed capped-age vector `a`, and a forced matching

\[
                         Q\subseteq D_{M_0,a}.            \tag{3.1}
\]

For an arc `T -> T-x+y`, the update (2.3) is precisely the deterministic
update of the lengths of the current positive and zero runs, capped at
`L`.  Permitting a sign change only from age `L` is equivalent to requiring
every closed positive run and every closed zero gap to contain at least
`L` owners.  A coordinate constant around one completed component has
cyclically consistent capped age `L`.

After deleting the forced tails and heads, extending `Q` is literally a
perfect matching in

\[
 D_{M_0,a}[X\setminus Z_Q,X\setminus H_Q].               \tag{3.2}
\]

Hall is exactly (3.2) of the source.  The resulting second incidence
matching is disjoint from `M_0`: a self successor was excluded, and the
matching property of `M_0` prevents the same lower facet from being used
by two first incidences.  Thus their union is a simple spanning
two-factor containing both protected colours.  Conversely, orienting any
such biresident factor and recording its actual capped ages recovers the
same successor matching.  The iff and integrality claims are therefore
correct.

The subtour inequalities (3.3) are also exact.  The successor permutation
cycles are in bijection with the bipartite factor cycles, so a proper union
of cycles is precisely a proper nonempty set with no selected outgoing
arc.

## 4. The singleton obstruction is correct for biresidence

At the tail (1.1), the only possible event deletes `x_0` and inserts an
absent `y`.  Signed age legality requires

\[
                         a_T(x_0)=L,
 \qquad                  a_T(y)=L,                       \tag{4.1}
\]

as well as equality of the entire target age vector with the deterministic
update.  Therefore

\[
 \deg^+_{D_{M_0,a}}(T)
 \leq {\bf1}_{\{a_T(x_0)=L\}}
       |\{y\notin T:a_T(y)=L\}|                          \tag{4.2}
\]

is a valid upper bound, not an equality.  If `T` is an unforced residual
tail and either factor on the right is zero, `{T}` is indeed a failed Hall
shore.  The warning that seasoned event labels do not suffice without the
full target-vector equality is correct.

## 5. Essential scope correction: positive residence has no absent age

For an ordinary depth-`d` flat source compiler, put

\[
                         L=d+1.                            \tag{5.1}
\]

The maximal cyclic candidate for an oriented Johnson owner component is

\[
                         P_p=\bigcap_{j=0}^{d}T_{p-j}.     \tag{5.2}
\]

Because `d<R`, every such intersection is nonempty: along `d` Johnson
steps at most `d` elements of the first rank-`R` owner can be deleted.
Moreover

\[
                         \bigcup_{p=i}^{i+d}P_p=T_i       \tag{5.3}
\]

for every `i` if and only if every nonconstant cyclic **positive** run has
length at least `L`.  Zero-gap length is absent from this criterion.

The one-sided capped state therefore records only the age of a coordinate
while it is present.  For

\[
                         T'=T-x+y,                         \tag{5.4}
\]

positive-age legality is:

\[
\begin{array}{c|c|c}
 &T&T'\\ \hline
x&(1,L)&0\\
y&0&(1,1)\\
z\notin\{x,y\},\ z\in T&(1,a)&(1,\min\{L,a+1\})\\
z\notin\{x,y\},\ z\notin T&0&0.
\end{array}                                               \tag{5.5}
\]

There is **no condition on the length of the zero gap before inserting
`y`**.  Let `D^+_{M_0,a}` be the successor graph filtered only by (5.5).
Exactly the same proof as in Section 3 gives the positive-resident gate

\[
 \boxed{
 |N_{D^+_{M_0,a}}(S)\setminus H_Q|\geq|S|
 \quad(S\subseteq X\setminus Z_Q).}                      \tag{5.6}
\]

It is strictly weaker than the source's signed-age Hall system.  At a tail
with `M_0(T)=T-x_0`, seasoning of `x_0` is necessary, but seasoning of
absent insertion labels is not:

\[
 \deg^+_{D^+_{M_0,a}}(T)
 \leq {\bf1}_{\{a_T(x_0)=L\}}(R-1),                      \tag{5.7}
\]

with further loss possible only from target-vector incompatibility.  In
particular,

\[
 a_T(y)<L\quad\hbox{for every }y\notin T                  \tag{5.8}
\]

does **not** imply zero positive-age outdegree and is not a PBBS
positive-residence obstruction.  Only the first alternative
`a_T(x_0)<L` in (4.5), or a full target-vector conflict, survives.

Once (5.3) holds, every long source interval obeys the purely algebraic
identity

\[
 \bigcup_{p=a}^{b}P_p=\bigcup_{i=a}^{b-d}T_i
 \qquad(b-a+1\geq d+1).                                  \tag{5.9}
\]

Thus an upper target already present in the nonwrapping consecutive-owner
union deck is rematerialized without any zero-gap hypothesis.  The same is
true of the protected halo identities: after positive residence makes
`P` a genuine antecedent, their literal source intervals are genuine
cells.

## 6. Corrected conclusion

The audited source proves exactly:

\[
 \boxed{
 \text{fixed signed ages + fixed first phase}
 \Longrightarrow
 \text{biresident completion iff the signed-age residual Hall system}.}
\]

It also correctly proves that the ordinary uncoloured protected-factor
theorem does not imply that stronger Hall system.

It does **not** establish that signed-age/biresident Hall is the next
necessary PBBS compiler gate.  For the ordinary maximal antecedent and
owner-union upper support, the proof-safe next gate is the positive-only
Hall system (5.6).  Biresidence remains relevant if a later construction
uses complement-dual residence, flag-convex cyclic fusion, or another
interface which explicitly requires long zero gaps; that additional need
must be cited separately rather than inferred from source factorization.
