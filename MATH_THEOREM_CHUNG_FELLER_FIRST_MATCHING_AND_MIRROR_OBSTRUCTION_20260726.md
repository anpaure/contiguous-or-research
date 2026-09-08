# Chung--Feller first-cut completion: forced Catalan spikes, a rank-three counterexample, and the mirror twist

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let

\[
 {cal R}=D_{2r}^0,
 \qquad X_t(u)=f^t(u)\in D_{2r}^t
 \quad(0\le t\le r),
 \qquad |{cal R}|=C_r.
\]

Write a phase-respecting path factor as relative perfect matchings

\[
 \sigma_t:{\cal R}\longrightarrow{\cal R},
 \qquad X_t(u)\sim_JX_{t+1}(\sigma_tu).
\]

The proposed statement

> every floor/ceiling-balanced rainbow first relative matching can be
> completed through the later layers with exact upper palette and identity
> monodromy

does not hold in the form needed by the growing-port construction.

1.  Under the literal requirement that the deletion and insertion
    coordinate marginals of `sigma_0` be separately floor/ceiling balanced
    on `[2r]`, there is **no admissible first matching at all for `r>=3`**.
    Every first matching has the forced loads

    \[
       I_{2r}=C_{r-1},\qquad D_1=C_{r-1},
    \]

    whereas a balanced marginal of total mass `C_r` has maximum
    `ceil(C_r/(2r))<C_{r-1}`.

2.  Even after replacing literal balance by the strongest feasible version
    -- pairwise distinct first colours and optimally spread marginals away
    from the two forced spikes -- completion is false.  At `r=3` there is
    an explicit rainbow first matching whose five ordered exchange pairs
    are distinct and whose non-forced coordinate loads are all at most one,
    but no choice of the last two phase matchings can complete it.

3.  Complement mirroring has an exact central obstruction.  Complementing
    a cut and reversing its direction sends

    \[
      \sigma_t\longmapsto
      c_t\sigma_t^{-1}c_{t+1}^{-1}
    \]

    at the reflected cut.  If `r=2h`, a completely mirrored sequence has
    monodromy conjugate to the fixed-point-free central complement
    involution `c_h`; if `r=2h+1`, identity monodromy would force the central
    matching to equal the complement matching, which is not a Johnson
    matching.  Thus pure mirror completion never has zero monodromy for
    `r>=2`.

4.  Twisted factors nevertheless compose cleanly.  A factor with endpoint
    rule `P -> complement(tau P)` followed, across a complement-reversing
    seam, by one with twist `kappa` has total twist `kappa tau`.
    Inverse twists therefore cancel.  The automatically exact inverse is
    ordinary path reversal, but it transposes every deletion/insertion pair
    and hence cancels antisymmetric carrier imbalance.  Complement-reversal
    preserves every ordered pair, but it is exact only when the original
    intersection palette is rainbow.  The explicit rank-three twisted
    factor fails this latter test.

The negative conclusion is precise.  A useful two-slab construction needs
an independently exact inverse-twist atom, or a new theorem making the
intersection palette rainbow.  Mirror symmetry alone supplies neither.

## 1. The forced first-cut Catalan spikes

For an oriented first-cut edge

\[
 X_0(u)\longrightarrow X_1(\sigma_0u)
       =X_0(u)-\{a(u)\}+\{b(u)\},
\]

put

\[
 D_x=\#\{u:a(u)=x\},\qquad
 I_x=\#\{u:b(u)=x\}.
\]

Both marginal vectors have total mass `C_r`.

### Theorem 1.1 (no literal balanced first matching in growing rank)

For every perfect Johnson matching between `D_{2r}^0` and `D_{2r}^1`,

\[
                  D_1=C_{r-1},\qquad I_{2r}=C_{r-1}.       \tag{1.1}
\]

Consequently, for every `r>=3`, neither marginal is floor/ceiling balanced
on `[2r]`.

#### Proof

Every nonempty Dyck word begins with an up-step and ends with a down-step.
Thus every member of `D_{2r}^0` contains coordinate `1` and omits coordinate
`2r`.

Split a Dyck word according to its first return:

\[
                 P=1u0v,qquad |1u0|=2j.
\]

The Chung--Feller flip word begins by inserting coordinate `2j`.  It deletes
coordinate `1` at the first cut exactly when `j=1`.  Hence `f(P)` contains
`2r` exactly when `j=r`, and it omits `1` exactly when `j=1`.

There are `C_{r-1}` Dyck words with first return `2`: they are `10v`, with
`v` arbitrary of semilength `r-1`.  There are also `C_{r-1}` primitive
Dyck words of semilength `r`: deleting their first and last steps gives an
arbitrary Dyck word of semilength `r-1`.  Since `f` bijects the root layer
onto the first flaw layer,

\[
 \#\{B\in D_{2r}^1:1\notin B\}=C_{r-1},
 \qquad
 \#\{B\in D_{2r}^1:2r\in B\}=C_{r-1}.
\]

The first equality forces `D_1=C_{r-1}` in every matching, because every
root contains `1`.  The second forces `I_{2r}=C_{r-1}`, because every root
omits `2r`.  This proves (1.1).

Finally

\[
 {C_{r-1}\over C_r}={r+1\over2(2r-1)}
\]

and therefore

\[
 C_{r-1}-{C_r\over2r}
 =C_r\,{r^2-r+1\over2r(2r-1)}>1                    \tag{1.2}
\]

for `r>=3`.  Indeed the rational factor in (1.2) is greater than `1/5`
and `C_r>=5`.  Thus

\[
                    C_{r-1}>\left\lceil{C_r\over2r}\right\rceil,
\]

which excludes floor/ceiling balance. \(\square\)

### Remark 1.2

At `r=2`, equality with the ceiling is possible, and both first-cut
matchings are completed by the familiar octahedral two-cut rectangle.
Thus the obstruction begins exactly at the first growing rank `r=3`.

## 2. A rainbow and optimally spread first matching which has no completion

The literal balanced class of Theorem 1.1 is empty, so the strongest useful
relaxation is to keep the two forced Catalan spikes and spread everything
else as evenly as possible.  Even this does not imply completion.

For `r=3`, index the five canonical rows by

\[
 a=123,\quad b=124,\quad c=125,\quad d=134,\quad e=135.
\]

Their canonical phase traces are

\[
\begin{array}{c|cccc}
u&X_0(u)&X_1(u)&X_2(u)&X_3(u)\\ \hline
a&123&136&146&456\\
b&124&126&156&356\\
c&125&145&345&346\\
d&134&234&236&256\\
e&135&235&245&246.
\end{array}                                             \tag{2.1}
\]

Choose the first-layer permutation

\[
 p_1:a\mapsto d,quad b\mapsto b,quad c\mapsto e,
        \quad d\mapsto c,quad e\mapsto a.             \tag{2.2}
\]

Thus the five first edges are

\[
 123\to234,quad124\to126,quad125\to235,
 \quad134\to145,quad135\to136.                       \tag{2.3}
\]

Every edge is a Johnson edge.  Its upper colours are

\[
                 1234,\quad1246,\quad1235,
                 \quad1345,\quad1356,                  \tag{2.4}
\]

which are pairwise distinct.  The ordered deletion/insertion pairs are

\[
                  (1,4),(4,6),(1,3),(3,5),(5,6).       \tag{2.5}
\]

They too are pairwise distinct.  The forced marginals are `D_1=2` and
`I_6=2`; every other positive marginal is one.  Hence (2.3) is maximally
spread subject to Theorem 1.1.

### Theorem 2.1 (rainbow first matching need not complete)

There are no permutations `p_2` and `p_3=id` which extend (2.2) to a
phase-respecting exact path factor.

#### Proof

Consider row `b`.  Its assigned first-layer state is `126` and its fixed
terminal state is `356`.  Among the five second-layer states in (2.1),
the only common Johnson neighbours of these two states are

\[
                              156\quad\hbox{and}\quad236. \tag{2.6}
\]

If row `b` uses `156`, its last upper colour is

\[
                              156\cup356=1356,
\]

which already occurs in the first palette (2.4).  Exact upper ownership
therefore forces row `b` to use `236`.

Now consider row `e`.  Its assigned first-layer state is `136` and its
terminal state is `246`.  Their only common second-layer neighbours are

\[
                              146\quad\hbox{and}\quad236. \tag{2.7}
\]

The state `236` has already been used by row `b`, while `p_2` must be a
permutation.  Hence row `e` is forced to use `146`.  But then its last
upper colour is

\[
                              146\cup246=1246,
\]

which is another colour already present in (2.4).  This contradicts exact
upper ownership. \(\square\)

The failure is simultaneous: it uses fixed endpoint monodromy, the
second-layer permutation ledger, and the aggregate upper palette.  No
cutwise palette restriction was imposed.

## 3. Complement reflection of phase matchings

Complementation maps flaw layer `t` bijectively to flaw layer `r-t`.
Define the induced root-label permutation

\[
 c_t=i_{r-t}^{-1}\circ(\text{complement})\circ i_t,
 \qquad i_t(u)=X_t(u).                                  \tag{3.1}
\]

Then

\[
                 c_{r-t}=c_t^{-1},\qquad c_0=c_r=1.     \tag{3.2}
\]

The endpoint identities in (3.2) are exactly the MSW endpoint theorem.

### Lemma 3.1 (reflected-cut formula)

If `sigma_t` is a Johnson perfect matching at cut `t`, its complemented
and direction-reversed edge set is the matching

\[
 \boxed{
 \sigma_{r-1-t}^{\vee}
     =c_t\sigma_t^{-1}c_{t+1}^{-1}.}                    \tag{3.3}
\]

If an old edge is

\[
              A\longrightarrow B=A-\{a\}+\{b\},
\]

then the reflected edge is

\[
              \overline B\longrightarrow\overline A
              =\overline B-\{a\}+\{b\}.              \tag{3.4}
\]

Thus reflection preserves the ordered deletion/insertion pair `(a,b)`.
Its upper colour is

\[
          \overline A\cup\overline B
             =J\setminus(A\cap B),                     \tag{3.5}
\]

not the complement of the old upper colour.

#### Proof

The old edge sends label `u` in layer `t` to `sigma_tu` in layer `t+1`.
After complementing and reversing, its initial label is
`c_{t+1}sigma_tu` in layer `r-t-1`, and its final label is `c_tu` in
layer `r-t`.  Solving for the latter as a function of the former gives
(3.3).  Equations (3.4)--(3.5) are direct set calculation. \(\square\)

### Theorem 3.2 (the exact central mirror obstruction)

Pure complement reflection of one half of the cuts never produces identity
monodromy for `r>=2`.

* If `r=2h`, choose arbitrary legal matchings
  `sigma_0,...,sigma_{h-1}` and define all later matchings by (3.3).  Put

  \[
                       p=\sigma_{h-1}\cdots\sigma_0.
  \]

  The total monodromy is

  \[
       \boxed{\sigma_{2h-1}\cdots\sigma_0
                    =p^{-1}c_h^{-1}p.}                 \tag{3.6}
  \]

  Here `c_h` is a fixed-point-free involution, so (3.6) is never the
  identity.

* If `r=2h+1`, reflect all noncentral cuts and let `mu=sigma_h` be the
  central matching.  Then

  \[
       \boxed{\sigma_{2h}\cdots\sigma_0
                    =p^{-1}c_h^{-1}\mu p.}             \tag{3.7}
  \]

  Identity monodromy would force `mu=c_h`.  But

  \[
       X_{h+1}(c_hu)=\overline{X_h(u)},                 \tag{3.8}
  \]

  so `mu=c_h` pairs complementary `r`-sets.  They have Johnson distance
  `r`, not one, and hence this is not a legal central matching for `r>1`.

#### Proof

For even `r`, multiply the reflected second-half matchings in decreasing
cut order.  The `c_t` terms telescope:

\[
\begin{aligned}
 \sigma_{2h-1}\cdots\sigma_h
 &= (c_0\sigma_0^{-1}c_1^{-1})
    (c_1\sigma_1^{-1}c_2^{-1})\cdots
    (c_{h-1}\sigma_{h-1}^{-1}c_h^{-1})\\
 &=p^{-1}c_h^{-1}.
\end{aligned}
\]

Multiplication by the first-half product `p` gives (3.6).  Complement on
the central layer has order two and no fixed `r`-set, proving the even
claim.  The same telescoping leaves the central factor `mu` in the odd
case and gives (3.7); (3.8) proves the last assertion. \(\square\)

This obstruction is independent of every floor/ceiling statistic.  It is
the exact monodromy left at the centre by the mirror ansatz.

## 4. Twisted factors and two-slab cancellation

### Definition 4.1

A twisted rooted path factor of twist `tau in Sym(R)` partitions the same
`X`- and `Y`-vertices as an ordinary port factor, but has endpoint rule

\[
                         P\longmapsto\overline{\tau P}. \tag{4.1}
\]

In the phase-permutation model this is simply `p_0=1`, `p_r=tau`.

### Theorem 4.2 (twists multiply across a complement-reversing seam)

Suppose two exact port slabs can be glued by the standard seam which
identifies the first slab's exit state `complement(Q)` with the second
slab's entrance port `Q`.  If their twists are `tau` and `kappa`, then the
composite has twist

\[
                              \kappa\tau.               \tag{4.2}
\]

In particular `kappa=tau^{-1}` gives identity endpoint monodromy.  No
additional ownership condition appears beyond the ordinary exact gluing
of the two disjoint slab ledgers.

#### Proof

The row entering the first slab at `P` exits as `complement(tau P)`.
Across the seam this is read as the second entrance label `tau P`.  The
second slab exits as `complement(kappa tau P)`, proving (4.2).  Exactness
of the state and colour ledgers is local to the two slabs and is preserved
by the assumed exact seam identification. \(\square\)

Thus nonidentity endpoint monodromy is not intrinsically fatal.  It can be
used as a packet atom, provided an independently exact inverse atom exists.

## 5. The inverse-copy dichotomy

There are two natural inversions of a twisted factor, and they have
opposite carrier behaviour.

### Proposition 5.1 (ordinary reversal is exact but reverses the carrier)

Reverse every path of a twisted factor `F_tau` without complementing its
states.  The resulting factor has the same `X`- and `Y`-ledgers and runs
from the complementary port shore back to the Dyck port shore with inverse
twist.  Every exchange pair `(a,b)` becomes `(b,a)`.

Hence an antisymmetric boundary-carrier score changes sign.  Pairing a slab
with its automatically exact path reversal cancels, rather than doubles,
that score.

### Proposition 5.2 (complement-reversal preserves the carrier but needs a
lower-rainbow theorem)

Complement every state and reverse every path.  The endpoint twist becomes
`tau^{-1}`, and by (3.4) every ordered exchange pair `(a,b)` is preserved,
at the reflected cut.  However, its upper palette is exact if and only if

\[
 \boxed{
 \biguplus_{A-B\text{ a transition of }F_\tau}\{A\cap B\}
       =\binom{J}{r-1}.}                                \tag{5.1}
\]

In words, the original intersection palette must itself be rainbow.

#### Proof

Ordinary reversal preserves every visited state and every intermediate
upper vertex, so it is automatically exact; it reverses every oriented
Johnson edge.  For complement-reversal, endpoint inversion was computed
before (4.1), and (3.4) preserves the ordered pair.  Equation (3.5) says
that the new upper colours are exactly the complements of the old
intersections.  Complementation bijects `binom(J,r-1)` with
`binom(J,r+1)`, proving (5.1). \(\square\)

The carrier statement is therefore exact:

* ordinary reversal gives an exact inverse but cancels antisymmetric
  deletion/insertion imbalance;
* complement-reversal preserves the sign and merely reflects its cut
  location, but exactness is a new depth-one rainbow condition.

There is no automatic sign-preserving inverse.

## 6. The rank-three twisted atom does not have an exact mirror

The explicit `r=3` degree-feasible path factor with endpoint three-cycle
from `MATH_ATTACK_S_PORT_PATH_FACTOR_HALL_20260726.md`, Proposition 7.2,
is a genuine twisted factor.  Its transition intersections are

\[
 13,\quad16,16,16,\quad56,\quad
 24,23,26,\quad25,35,34,\quad35,\quad14,45,24.          \tag{6.1}
\]

Thus `16` occurs three times, `24` and `35` occur twice, and the four
two-sets

\[
                              12,15,36,46               \tag{6.2}
\]

are missing.  Condition (5.1) fails.  Consequently its ordinary reverse is
an exact inverse-twist atom but reverses the carrier, while its
carrier-preserving complement-reverse is not an exact factor.

This converts the old rank-three monodromy obstruction into a conditional
atom, but not yet into a productive two-slab packet.

## 7. Exact remaining statement

After this audit, a productive growing Chung--Feller two-slab theorem must
supply one of the following genuinely new objects.

1. Two independently exact twisted factors of twists `tau` and
   `tau^{-1}` whose boundary-carrier increments have the same sign; or
2. one exact twisted factor satisfying the lower-rainbow condition (5.1),
   so that complement-reversal is an exact sign-preserving inverse; or
3. a multi-slab construction in which the transposed carrier increments
   from ordinary reversals are rerouted to different physical target
   classes instead of cancelling.

In addition, a useful first-cut balance condition must be calibrated to the
forced Catalan spikes (1.1), or imposed only after coordinate-conjugate
aggregation.  Literal local floor/ceiling balance is impossible.

No constant-one conclusion is claimed here.
