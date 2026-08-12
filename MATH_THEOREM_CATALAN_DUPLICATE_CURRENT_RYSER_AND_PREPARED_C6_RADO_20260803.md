# Catalan duplicate current: abstract Ryser connectivity and the prepared-C6 Rado gate

**Date:** 2026-08-03  
**Status:** unconditional palette-matrix theorem, exact physical-C6
comparison, and conditional protected Rado theorem.  It proves that
coordinate current is the only invariant of the abstract labelled palette
matrix.  It also proves that literal Boolean `C6` moves form a strict
subgraph of that matrix fibre, so reserve rows or a stronger circuit family
are genuinely necessary.  It does not construct the required global
reserve host.

## 0. Outcome

Let rows be selected rank-`(m+1)` upper colours and columns the `2m-1`
coordinates.  A row is its zero-one incidence vector.

1. Any two labelled zero-one matrices with equal row sums and equal column
   sums are connected by ordinary `2x2` row-coordinate switches.  Hence
   the coordinate current is the only invariant at the abstract labelled
   palette level.
2. A physical Boolean `C6` rectangle is exactly the special `2x2` switch
   whose two old rows intersect in rank `m-1`, equivalently are at Johnson
   distance two.  General Ryser switches need not have that geometry.
3. The restriction is real.  Two rank-`(m+1)` rows meeting in rank `m-2`
   can admit an ordinary current-preserving switch while supporting no
   physical `C6` move at all.
4. The obstruction is exactly catalytic at palette level: a
   palette-nontrivial switch between rows at difference `q>=2` factors into
   `q-1` distance-two switches using `q-2` tailored reserve rows, all
   restored afterward.
5. If a prepared atlas turns simultaneous rectangle selection into one
   matroid independence system, then Rado's inequalities are the exact
   global reserve-host criterion.  Atoms meeting a disjoint neutral `C8`
   socket are deleted before applying those inequalities.

Thus the missing global theorem is no longer a current calculation.  It is
the construction of a literal reserve atlas rich enough to lift the
abstract matrix switches.

For the Boolean application, write

\[
 \mathcal U={ [2m-1]\choose m+1},\qquad
 W={2m-1\choose m},\qquad
 U=|\mathcal U|,\qquad
 C=W-U=\operatorname{Cat}_m.                          \tag{0.1}
\]

## 1. The labelled fixed-margin fibre

Let `A` and `B` be zero-one matrices on the same labelled row set
`[b]` and column set `[v]`.  Assume

\[
 \sum_j A_{ij}=\sum_jB_{ij}\quad(i\in[b]),
 \qquad
 \sum_i A_{ij}=\sum_iB_{ij}\quad(j\in[v]).            \tag{1.1}
\]

A `2x2` switch chooses distinct rows `p,q` and columns `x,y` and replaces

\[
 \begin{pmatrix}1&0\\0&1\end{pmatrix}
 \longleftrightarrow
 \begin{pmatrix}0&1\\1&0\end{pmatrix}.              \tag{1.2}
\]

It preserves every row and column sum.

### Theorem 1.1 (self-contained Ryser switching)

Every two matrices satisfying (1.1) are connected by a finite sequence of
switches (1.2).

#### Proof

Colour an entry red when `A=1,B=0` and blue when `A=0,B=1`.  Equality of
all margins makes the red and blue degrees equal at every row and column.
Unless `A=B`, the red-blue symmetric difference therefore contains an
alternating cycle.  Choose one of minimum length and write it as

\[
 r_1-c_1-r_2-c_2-\cdots-r_t-c_t-r_1,                 \tag{1.3}
\]

where `r_i c_i` is red and `r_(i+1)c_i` is blue, with indices modulo `t`.

If `t=2`, the four cycle entries form (1.2), and switching `A` removes four
disagreements.

Assume `t>=3` and inspect the chord `(r_1,c_2)`.

* If `A_(r_1,c_2)=0`, switch `A` on rows `r_1,r_2` and columns `c_1,c_2`.
  The entries `(r_1,c_1),(r_2,c_1),(r_2,c_2)` become equal to `B`; the
  fourth entry creates at most one new disagreement.  The Hamming distance
  from `B` drops by at least two.
* Suppose `A_(r_1,c_2)=1`.  If `B_(r_1,c_2)=0`, that red chord followed by
  the part of (1.3) from `c_2` through `r_3,...,c_t,r_1` is a shorter
  alternating cycle, contrary to the choice of (1.3).  Hence the chord is
  common: `A_(r_1,c_2)=B_(r_1,c_2)=1`.  Now switch `B` on the two ones
  `(r_1,c_2),(r_2,c_1)`.  The opposite entries `(r_1,c_1),(r_2,c_2)` are
  zero in `B`.  Three disagreements disappear and the removed common chord
  creates one; again the Hamming distance drops by two.

Thus a switch on one of the two matrices strictly decreases their Hamming
distance.  Induction reaches equality.  Reversing the switches made on
`B` gives one switch path from the original `A` to the original `B`.
\(\square\)

### Corollary 1.2 (coordinate current is the complete abstract invariant)

For labelled multisets of fixed-size subsets, equality of coordinate
degrees is necessary and sufficient for reachability by abstract `2x2`
switches.

In particular, let `mu` be the upper-colour multiplicity vector of any
cyclic owner factor.  A palette-only upper-surjective target `mu'` is in the
same abstract switch fibre exactly when

\[
 \begin{aligned}
 &\mu'_R\ge1 &&(R\in\mathcal U),\\
 &\sum_R\mu'_R=\sum_R\mu_R=W,\\
 &\sum_{R\ni x}\mu'_R=\sum_{R\ni x}\mu_R
                         &&(x\in[2m-1]).              \tag{1.4}
 \end{aligned}
\]

#### Proof

Label the `W` turn occurrences, use their colour incidences as the rows,
and label any target multiset arbitrarily.  Equations (1.4) are exactly the
row- and column-margin equalities.  Apply Theorem 1.1. \(\square\)

For two edge-disjoint perfect matchings of the middle-levels incidence
graph the last margin is the uniform current

\[
 2{2m-2\choose m-1}-{2m-2\choose m-2}.                \tag{1.5}
\]

Writing `mu'=1+nu`, condition (1.4) says precisely that the Catalan
duplicate multiset `nu` is a one-design:

\[
 \sum_R\nu_R=\operatorname{Cat}_m,
 \qquad
 \sum_{R\ni x}\nu_R=2\operatorname{Cat}_{m-1}.       \tag{1.6}
\]

Thus (1.6), not a particular choice of duplicate blocks, is the exact
abstract balanced-defect condition.

The required multidesign always exists.

### Proposition 1.3 (explicit cyclic Catalan duplicate design)

For every `m>=3`, there is a rank-`(m+1)` multidesign on `[2m-1]` with

\[
 b=\operatorname{Cat}_m
 \quad\hbox{blocks and replication}\quad
 \lambda=2\operatorname{Cat}_{m-1}.                  \tag{1.7}
\]

#### Proof

Put

\[
                         v=2m-1,qquad k=m+1.
\]

The Catalan identities give

\[
 bk=\operatorname{Cat}_m(m+1)
 ={2m\choose m}
 =(2m-1)\,2\operatorname{Cat}_{m-1}
 =v\lambda.                                           \tag{1.8}
\]

Identify the coordinates with `Z_v`.  For `0<=j<b`, take the block

\[
 D_j=\{jk,jk+1,\ldots,jk+k-1\}\pmod v.               \tag{1.9}
\]

Because `k<v`, every block has `k` distinct coordinates.  Before reduction
modulo `v`, the concatenated block slots are precisely the integers
`0,1,...,bk-1`.  Equation (1.8) says this interval contains every residue
class exactly `lambda` times.  Hence `(D_j)` is the required multidesign.
Repeated blocks are allowed. \(\square\)

### Corollary 1.4 (abstract upper-surjective target always exists)

Every two-perfect-matching cycle palette has an upper-surjective palette in
its abstract Ryser fibre.

#### Proof

Add one copy of every upper colour to the duplicate multidesign in
Proposition 1.3.  The resulting `W` rows have the total and coordinate
current (1.5).  Apply Corollary 1.2. \(\square\)

This is an abstract labelled-matrix conclusion.  It provides neither a
literal `C6` factorization without the catalytic rows of Theorem 2.3 nor an
occurrence-compatible owner factor.

## 2. Physical C6 rectangles are only distance-two switches

Put `k=m+1`, the size of an upper-colour row.  An abstract switch acts on
two old rows `P,Q`, choosing `a in P-Q` and `b in Q-P`, and replaces them
by

\[
                         P-a+b,\qquad Q-b+a.          \tag{2.1}
\]

The literal `C6` colour rectangle has the form

\[
 \{K+p+e,\ K+q+f\}
 \longleftrightarrow
 \{K+q+e,\ K+p+f\},
 \qquad |K|=k-2,                                     \tag{2.2}
\]

with `p,q,e,f` pairwise distinct outside `K`.

If `|P-Q|=1`, then (2.1) only interchanges the two complete row values
`P,Q`.  It changes their labelled placement but leaves the palette
multiset unchanged.  Such a switch is **palette-trivial** and is discarded
after occurrence-row labels are forgotten.  Hence every switch discussed
in Theorems 2.1 and 2.3 has `|P-Q|>=2`.

### Theorem 2.1 (exact nontrivial C6/matrix comparison)

A palette-nontrivial abstract switch (2.1), with the displayed pairing of
old and new rows fixed, is the palette projection of a simple upper-valid
Boolean `C6` rectangle if and only if

\[
                         |P\cap Q|=k-2=m-1.           \tag{2.3}
\]

For every such row-oriented switch there are `m-1` choices of the common
retained `C6` turn colour.

#### Proof

Every simple upper-valid `C6` has the top-and-exterior normal form.  After
cancelling its common turn, its four exclusive colours are exactly (2.2),
so the two old rows meet in `K` and satisfy (2.3).

Conversely, suppose (2.3).  Write

\[
 P=K+p+e,\qquad Q=K+q+f,\qquad K=P\cap Q.
\]

After possibly interchanging the names inside each two-element exclusive
part, (2.1) is exactly (2.2).  Choose any `b_0 in K` and put

\[
                         R=K+p+q.
\]

The `C6` top has holes `b_0,q,p` and exteriors `e,e,f` in the explicit
rectangle construction.  Its common turn is

\[
                         (R-b_0)+e.
\]

Different choices of `b_0` give the asserted `|K|=m-1` labelled common
turns. \(\square\)

The phrase *palette projection* is load-bearing.  The retained common
colour moves from one lower turn to another during the physical `C6`
toggle, so a literal move is not a two-row switch with all physical row
labels fixed.  After forgetting those occurrence labels and cancelling the
common colour, its multiplicity change is (2.2).  A host must additionally
supply the third common-colour turn and the six literal incidences.

Hence the **palette-projected** physical `C6` graph is the subgraph of the
Ryser fibre generated only by switches between rows at Johnson distance
two, together with the required common-turn transport.  The containment is
strict.

### Proposition 2.2 (sharp two-row frozen obstruction)

For every `m>=5`, there are two different labelled palette matrices with
row size `m+1` and the same column sums which are joined by one abstract
switch but whose initial matrix admits no physical `C6` switch.

#### Proof

Choose a set `I` of size `m-2` and six distinct points
`a,b,c,d,e,f` outside it; this uses `m+4<=2m-1` coordinates.  Put

\[
 \begin{aligned}
 P&=I+a+b+c,& Q&=I+d+e+f,\\
 P'&=I+a+b+d,&Q'&=I+c+e+f.
 \end{aligned}                                       \tag{2.4}
\]

The two-row matrices `(P,Q)` and `(P',Q')` have the same column sums, and
the latter is obtained from the former by the abstract switch `c<->d`.
But

\[
                         |P\cap Q|=m-2=k-3.           \tag{2.5}
\]

There is only one pair of rows, and it fails (2.3).  Thus the physical
`C6`-switch graph is isolated at `(P,Q)`. \(\square\)

This is a Boolean palette obstruction, not yet a Catalan-size one-design
or an occurrence-host obstruction.  It proves sharply that arbitrary
current-preserving switches cannot be factored through literal `C6`s
without extra reserve rows.

The reserve-row requirement is also sufficient at the abstract palette
level, with an exact linear cost.

### Theorem 2.3 (catalytic factorization through distance-two switches)

Let `P,Q` be two `k`-subsets and put

\[
                         q=|P-Q|=|Q-P|\ge2.
\]

Choose `a in P-Q` and `b in Q-P`.  The abstract switch

\[
                         (P,Q)\longmapsto(P-a+b,Q-b+a) \tag{2.6}
\]

is a composition of exactly `q-1` distance-two switches after adjoining
`q-2` labelled reserve rows.  Every reserve row is returned to its original
value at the end.

Consequently every palette-nontrivial Ryser switch has a palette-level
factorization into Boolean `C6` rectangles once its tailored reserve colours
and common turns are available.  When `q=1`, (2.1) merely exchanges the two
labelled row contents and is the identity after forgetting occurrence
labels, so it requires no palette move.

#### Proof

Induct on `q`.  For `q=2`, Theorem 2.1 gives one distance-two switch and no
reserve row.

Assume `q>2`.  Choose

\[
 a_2\in(P-Q)-\{a\},
 \qquad
 b_2\in(Q-P)-\{b\},
\]

and adjoin the reserve row

\[
                         H=(P-\{a,a_2\})+\{b,b_2\}.   \tag{2.7}
\]

The rows `P,H` intersect in `k-2` coordinates.  Perform the distance-two
switch exchanging `a` and `b`.  It gives the desired final first row

\[
                         P'=P-a+b
\]

and changes the reserve to

\[
                         H'=H-b+a=P-a_2+b_2.          \tag{2.8}
\]

Now

\[
 |H'-Q|=|Q-H'|=q-1,                                  \tag{2.9}
\]

because `H'` has gained exactly the common point `b_2` relative to the
original pair.  Apply the induction hypothesis to `H',Q`, again exchanging
`a` and `b`.  It uses `q-3` further reserve rows and `q-2` distance-two
switches, and ends with

\[
 H'-a+b=H,
 \qquad
 Q-b+a.
\]

Thus the first reserve is restored, as are all inductive reserves.  The
total costs are

\[
 1+(q-2)=q-1\quad\hbox{switches},
 \qquad
 1+(q-3)=q-2\quad\hbox{reserve rows}.
\]

This proves the claim. \(\square\)

The theorem is a palette factorization, not a literal host theorem.  Every
distance-two step still needs the third common-colour turn supplied by
Theorem 2.1, and the reserve rows must occur at mutually compatible
physical positions.  Proposition 2.2 is the sharp `q=3` demonstration of
what fails when its one necessary reserve is absent.

## 3. Exact balanced repair vectors

Throughout this section assume `mu` is the turn-colour multiplicity vector
of two edge-disjoint perfect middle-levels matchings.  In particular,

\[
 \sum_R\mu_R=W,
 \qquad
 \sum_{R\ni x}\mu_R
 =2{2m-2\choose m-1}-{2m-2\choose m-2}               \tag{3.0}
\]

for every coordinate `x`.  This two-perfect-matching hypothesis is what
turns the general fixed-margin repair condition into the Catalan
one-design equation (1.6).

Put

\[
                         H=\{R:\mu_R=0\}.             \tag{3.1}
\]

A lossless palette repair is an integer vector `z` such that

\[
 \boxed{
 \sum_Rz_R=0,\qquad
 \sum_{R\ni x}z_R=0\ (x\in[2m-1]),\qquad
 z_R\ge1\ (R\in H),\qquad
 z_R\ge1-\mu_R\ (R\notin H).}                       \tag{3.2}
\]

The last two inequalities are equivalently `mu+z>=1`.

### Theorem 3.1 (minimal balanced-defect criterion)

There exists an abstract palette-only repair of all missing colours if and
only if (3.2) has an integer solution.  Equivalently, there is a Catalan
duplicate one-design `nu` satisfying (1.6) such that

\[
                         \mu+z=1+\nu.                 \tag{3.3}
\]

When it exists, every labelled realization of `mu` is connected to every
labelled realization of `1+nu` by abstract switches.

Under the standing two-perfect-matching hypothesis, such a solution always
exists by Proposition 1.3; the criterion records the exact allowable signed
repair vectors and target designs.

#### Proof

Necessity follows from fixed turn count, coordinate-current conservation,
and nonnegative final duplicate multiplicities.  Conversely, (3.2) makes
`mu+z` an upper-surjective multiset with the same row count and coordinate
margins as `mu`.  Theorem 1.1 connects their labelled matrices.  Subtracting
one complete upper layer gives (3.3) and (1.6). \(\square\)

Every physical `C6` rectangle contributes one particular homogeneous
current-kernel vector

\[
 1_{K+q+e}+1_{K+p+f}
 -1_{K+p+e}-1_{K+q+f}.                                \tag{3.4}
\]

Therefore the semigroup generated by available literal rectangles can be
strictly smaller than the homogeneous integer kernel defined by the first
two equalities in (3.2), even though the full abstract switch graph has no
further invariant.

## 4. The prepared reserve-host Rado theorem

Fix a current two-factor, a set `H` of missing colours, and one protected
neutral `C8` parity socket.  Delete every `C6` atom meeting the socket.

For each `R in H`, let `mathcal A_R` be a menu of **oriented complete
rectangle atoms**.  An atom in `mathcal A_R` consists of

* one literal old-phase `C6` and its new phase;
* the designation of `R` as one new-only colour;
* one already covered companion new-only colour;
* two named reserve occurrences for the old-only colours; and
* every physical owner, lower, incidence, and reserve token used by the
  toggle.

Thus selecting one atom from `mathcal A_R` repairs `R` and, in isolation,
loses no covered colour.

Assume a matroid `N` on the atom ground has the exact interpretation

\[
 I\text{ is independent in }N
 \quad\Longleftrightarrow\quad
 \text{all atoms in }I\text{ can be applied simultaneously}. \tag{4.1}
\]

The premise (4.1) must hold for the **entire** joint compatibility system,
including every socket-capacity constraint.  It holds on the pure
private-socket face of Corollary 4.2, or whenever all constraints have been
encoded in one proved partition, graphic, gammoid, or other matroid.  An
intersection of separately supplied matroid constraints is not licensed by
this sentence.

### Theorem 4.1 (protected rectangle Rado criterion)

There is a simultaneous choice of one complete lossless `C6` absorber for
every missing colour if and only if

\[
 \boxed{
 r_N\left(\bigcup_{R\in X}\mathcal A_R\right)\ge |X|
 \qquad(X\subseteq H).}                               \tag{4.2}
\]

When (4.2) holds, applying the selected rectangles makes the factor
upper-surjective, preserves every endpoint capacity and the coordinate
current, and leaves the disjoint neutral `C8` parity toggle available.

#### Proof

Equation (4.2) is exactly Rado's independent-transversal theorem.  Each
selected atom repairs its designated missing colour and has named reserve
witnesses for both displaced colours.  Independence in `N` gives the joint
physical application promised by (4.1), so no reserve or support is used
twice.  The local rectangle theorem preserves endpoints and old colour
coverage; circuit current conservation preserves (1.5).  Every selected
atom avoids the protected `C8`, whose two phases have identical palette
multisets, so it remains available for the final topology parity choice.
\(\square\)

### Corollary 4.2 (Hall face)

If the atlas consists of a bank \(\mathcal S\) of pairwise private complete
sockets and only the assignment of missing colours to sockets remains,
form the bipartite graph \(H\sqcup\mathcal S\) in which `R` is adjacent to
a socket that has a complete atom repairing `R`.  Write \(\Gamma(X)\) for
the socket neighbourhood of \(X\subseteq H\).  Then all missing colours are
repaired if and only if

\[
                    |\Gamma(X)|\ge |X|\qquad(X\subseteq H). \tag{4.3}
\]

This is Theorem 4.1 for the rank-one-per-socket partition matroid of the
private bank; that partition matroid is also transversal.

## 5. Why raw resource-disjointness is not automatically Rado

The family of pairwise resource-disjoint compound atoms is not generally a
matroid.  Let one atom use resources `{1,2}` and two other atoms use
`{1}` and `{2}` separately.  The singleton containing the first atom and
the two-element family containing the latter atoms are both feasible, but
no member of the larger family augments the singleton.  The matroid
exchange axiom fails.

Therefore (4.2) is not licensed merely by listing raw C6 rectangles.
One must first prove a private-socket, gammoid, graphic, or other genuine
matroid representation of their complete compatibility.  Without that
preparation the exact object is a multi-resource hypergraph matching, and
ordinary Hall/Rado inequalities are insufficient.

## 6. Sharp remaining theorem

The local and abstract mathematics reduce the global owner/q1 repair to:

> **Catalan reserve-atlas theorem.**  Construct, in one integral factor
> with duplicate current (1.6), a complete C6 atom system avoiding one
> neutral C8 socket, such that either:
>
> 1. its compatibility is represented by a matroid satisfying (4.2); or
> 2. it contains a private Hall subatlas satisfying (4.3).

The exact current obstruction is (3.2); there is no additional abstract
palette invariant by Theorem 1.1.  Proposition 2.2 proves that current
balance alone does not lift without reserves, while Theorem 2.3 proves that
tailored reserve rows remove every palette-level obstruction.  The
genuinely open content is therefore reserve-row, common-turn, and
occurrence-host supply.
