# Rainbow all-width banks jointly with rooted upper-exact forests:
# blocker clutters, occurrence sections, and the exact fixed-selector min--max

**Date:** 2026-08-04  
**Scope:** pure fixed-factor, retained-old owner/immediate-upper mathematics  
**Status:** exact reductions and conditional sufficient criteria.  No
all-parameter rainbow bank, protected factor, source chronology, or `B+1`
upper bound is claimed.

## 0. Outcome

Let `F` be an occurrence-labelled directed cycle cover, let `u(e)` be the
immediate-upper colour of occurrence `e`, and let `P` be the protected pivot
bank.  The missing simultaneous choice can be stated without losing any of
its correlations.

1. If `D=E(F)-Q_0`, then a protected upper-exact forest carrying an old
   witness of every proper higher target exists exactly when
   
   * `D` uses the exact colour quotas `b_R=mu_R-1`;
   * `D` avoids `P`;
   * `D` meets every factor component; and
   * `D` is not a transversal of the witness intervals of any target.

   The forced-cut core `K_X` records precisely the one-element
   transversals.  A forest makes many cuts, so its exact guard is the full
   minimal-transversal clutter, not `K_X` alone.

2. Equivalently, choose one labelled occurrence `a_R` of every immediate-
   upper colour.  Higher targets and factor components become finite
   relations on these colour variables.  Their natural join is nonempty
   exactly when the joint rainbow forest exists.  If the relation scopes
   have a running-intersection tree (in particular, if they are laminar),
   separator consistency is necessary and sufficient by an exact join-tree
   recursion.

3. After a witness selector is fixed, the remaining extension is ordinary
   matroid intersection: the partition matroid of immediate-upper colours
   against the graphic matroid of `F`.  Edmonds' rank min--max is exactly the
   capacitated component-omission Hall theorem.  Thus the joint residual
   obstruction has the sharp scalar form
   
   \[
    \min_\sigma\ \max_{Y\subseteq\operatorname {Comp}(F)}
       \left(|Y|-\sum_{R:N_R^\sigma\cap Y\ne\varnothing}b_R\right).
   \]

4. Witness selection itself is an independent-transversal problem in a
   conflict graph.  Its compatible-token sets are not a matroid, even when
   every displayed witness is a two-edge interval.  Hence Rado or a single
   gammoid cannot be invoked directly on witness tokens.  This does not
   preclude an enlarged gadget reduction.

5. The omission row decouples from witness choice under an exact reserve
   Hall condition.  In particular, component--colour incidences containing
   at least two occurrences are immune to every rainbow bank, since such a
   bank can consume at most one of them.

These statements sharpen the interface but do not prove that the Boolean
middle-level instance has the required conflict expansion, laminar scopes,
or reserve Hall supply.

## 1. Fixed occurrence ground

Let

\[
 E=E(F),\qquad E_R=u^{-1}(R),\qquad
 \mu_R=|E_R|,\qquad b_R=\mu_R-1.                    \tag{1.1}
\]

Assume `u:E -> mathcal U_1` is surjective.  Parallel and oppositely
oriented edges remain different labelled occurrences.  Let `mathcal K` be
the directed-cycle component set of `F`.  The protected bank
`P subseteq E` is assumed rainbow:

\[
             |P\cap E_R|\le1\qquad(R\in\mathcal U_1). \tag{1.2}
\]

If (1.2) fails, no upper-exact set can contain `P`.

For each required proper higher target `X`, let `mathcal W_X` be its family
of old path or cyclic-interval witnesses in `F`, and write

\[
                         J(I)=E(I)\qquad(I\in\mathcal W_X). \tag{1.3}
\]

Thus `I` survives in a subset `Q subseteq E` precisely when `J(I) subseteq
Q`.  No quotient by colour is made in (1.3).

## 2. The exact multi-cut blocker theorem

Define the quota-and-component deletion family

\[
 \begin{split}
 \mathfrak D(F,P)=\{D\subseteq E:\;&D\cap P=\varnothing,\\
 &|D\cap E_R|=b_R\quad(R\in\mathcal U_1),\\
 &D\cap E(K)\ne\varnothing\quad(K\in\mathcal K)\}.
 \end{split}                                           \tag{2.1}
\]

For a target `X`, its deletion-transversal upset is

\[
 \mathfrak T_X={D\subseteq E:
              D\cap J(I)\ne\varnothing
                    \text{ for every }I\in\mathcal W_X\}.          \tag{2.2}
\]

Let `mathfrak B_X` be the clutter of inclusion-minimal members of
`mathfrak T_X`.  If `mathcal W_X` is empty, then
`mathfrak B_X={emptyset}`.

### Theorem 2.1 (joint deletion--blocker equivalence)

The following are equivalent.

1. There is an upper-exact rooted forest `Q_0 subseteq F` which contains
   `P` and contains one complete old witness of every required proper
   higher target.
2. There is `D in mathfrak D(F,P)` such that
   
   \[
       D\notin\mathfrak T_X\qquad\text{for every }X.                \tag{2.3}
   \]
3. There is `D in mathfrak D(F,P)` such that
   
   \[
       B\nsubseteq D
       \qquad(X\text{ required},\ B\in\mathfrak B_X).              \tag{2.4}
   \]

For every such `D`, `Q_0=E-D`.  If `F` has `W` rooted vertices and
`|mathcal U_1|=U`, then `Q_0` has exactly `W-U=Cat_m` directed-path
components.  Choosing one surviving witness per target gives a rainbow
witness bank inside `Q_0` automatically.

#### Proof

The colour quota in (2.1) leaves exactly
`mu_R-b_R=1` occurrence of every colour.  Avoidance of `P` makes all
protected occurrences survive.  A subset of a directed cycle cover is a
forest exactly when its deletion complement meets every old cycle.  Finally,
`X` has a retained witness exactly when some `J(I)` avoids `D`, which is
equivalent to `D notin mathfrak T_X`.  Since `mathfrak T_X` is upward
closed, membership in it is equivalent to containing one member of its
minimal clutter.  This proves all three equivalences.

The surviving set has `U` edges on `W` vertices, so its forest has `W-U`
components.  Its maximum indegree and outdegree are at most one, hence all
components are directed paths.  Every selected witness lies inside a set
with one occurrence per colour, so their union with `P` is rainbow.
\(\square\)

### Proposition 2.2 (forced cores are exactly the singleton blockers)

For

\[
                         K_X=\bigcap_{I\in\mathcal W_X}J(I),        \tag{2.5}
\]

one has

\[
                  e\in K_X\quad\Longleftrightarrow\quad
                  \{e\}\in\mathfrak T_X.                          \tag{2.6}
\]

Thus the safe-opening theorem is exactly Theorem 2.1's target condition
on a one-edge deletion.  It does not control a multi-edge forest deletion.
For example, if the only two witnesses are disjoint intervals `J_1,J_2`,
then `K_X=emptyset`, while every set containing one edge of each interval
lies in `mathfrak T_X`.

#### Proof

The singleton `{e}` meets every witness precisely when `e` belongs to every
`J(I)`.  The example is immediate.  \(\square\)

Because every `D in mathfrak D(F,P)` has

\[
                              |D|=\sum_R b_R=W-U=Cat_m,             \tag{2.7}
\]

the old-channel robustness condition `tau_F(X)>=Cat_m+1` makes target `X`
automatic for every upper-exact extraction.  This is exact as a uniform
cardinality guard and usually much stronger than necessary; the structured
condition is (2.3).

## 3. One occurrence per colour: the exact section CSP

For each colour define its protected domain

\[
 \Omega_R=
 \begin{cases}
  \{p\},&P\cap E_R=\{p\},\\
  E_R,&P\cap E_R=\varnothing.
 \end{cases}                                           \tag{3.1}
\]

A global **occurrence section** is

\[
                       a=(a_R)_{R\in\mathcal U_1}
                       \in\prod_R\Omega_R,             \tag{3.2}
\]

and `Q(a)={a_R:R in mathcal U_1}`.

For a target put

\[
 S_X=\bigcup_{I\in\mathcal W_X}u(J(I))                \tag{3.3}
\]

and define the relation

\[
\mathcal A_X=\left\{z\in\prod_{R\in S_X}\Omega_R:
   \exists I\in\mathcal W_X\ \forall e\in J(I),\ z_{u(e)}=e
                    \right\}.                       \tag{3.4}
\]

An interval using two different occurrences of one colour contributes no
tuple to (3.4).  A conflict with a protected occurrence also contributes no
tuple, because its domain in (3.1) is a singleton.

For a factor component put `S_K=u(E(K))` and

\[
\mathcal A_K=\left\{z\in\prod_{R\in S_K}\Omega_R:
       E(K)\nsubseteq\{z_R:R\in S_K\}\right\}.       \tag{3.5}
\]

If one colour occurs twice on `K`, (3.5) is automatically the full relation:
one occurrence section cannot select both labelled edges.

### Theorem 3.1 (occurrence-section equivalence)

A joint protected rainbow all-width rooted forest exists if and only if

\[
 \left(\Join_X\mathcal A_X\right)
       \Join\left(\Join_{K\in\mathcal K}\mathcal A_K\right)
                                                        \tag{3.6}
\]

is nonempty, where the join identifies coordinates carrying the same
immediate-upper colour.

#### Proof

A global tuple in (3.6) chooses exactly one occurrence of every colour and,
by (3.1), contains `P`.  Relation (3.4) supplies a complete old witness for
every target.  Relation (3.5) says that the selected set omits an edge of
every factor cycle, hence is a forest.  Conversely every forest in Theorem
2.1 defines its unique occurrence section and satisfies all these relations.
\(\square\)

This is a finite-domain CSP, not an assertion of total unimodularity.  It
keeps the same variable for a shared physical occurrence, so two targets may
reuse that occurrence without paying its colour capacity twice.

### Theorem 3.2 (running-intersection / join-tree criterion)

Index all relations in (3.6) by `i in mathcal I`, with scope `S_i`.  Suppose
there is a tree `T` on `mathcal I` such that, for every colour `R`, the nodes

\[
                         \{i:R\in S_i\}                              \tag{3.7}
\]

induce a connected subtree.  Root `T`.  For an oriented tree edge `i->j`,
let `M_(i->j)` be the set of assignments on `S_i cap S_j` which extend to
all relations in the component of `T-ij` containing `i`.  Recursively,

\[
 M_{i\to j}=\pi_{S_i\cap S_j}\left\{
 z\in\mathcal A_i:
 z|_{S_i\cap S_k}\in M_{k\to i}
 \text{ for every }k\in N_T(i)-\{j\}\right\}.        \tag{3.8}
\]

Then (3.6) is nonempty if and only if the root relation contains a tuple
compatible with every incoming message.  In particular, a laminar family
of scopes has an exact separator-consistency test.

#### Proof

The running-intersection property implies that a variable occurring on both
sides of `ij` occurs in the separator `S_i cap S_j`.  Induct from the leaves:
(3.8) is therefore exactly the set of separator assignments extendible over
the entire `i`-side subtree.  A surviving root tuple chooses compatible
subtree extensions recursively; two extensions agree on every variable they
share and hence glue to a global section.  Restriction of any global section
gives every message in the reverse direction.  This proves necessity and
sufficiency.  A laminar scope family admits the inclusion forest, with
disjoint roots joined arbitrarily, and satisfies (3.7).  \(\square\)

No claim is made that the scopes arising from the full Boolean target deck
are laminar or even acyclic.

## 4. Witness conflict graph and the nonmatroid obstruction

Make one token `(X,I)` for each witness whose union with `P` is individually
rainbow.  Join two tokens belonging to different targets when their edge
unions contain different occurrences of one common colour.  Call the
resulting graph `Gamma_W` and partition its vertices by target.

### Proposition 4.1 (rainbow selector = independent transversal)

A protected rainbow witness selector exists exactly when `Gamma_W` has an
independent set containing one token from every target part.

#### Proof

After individually nonrainbow tokens are discarded, a union fails to be
rainbow exactly when some pair of its tokens supplies two different
occurrences of one colour.  This is precisely an edge of `Gamma_W`.
\(\square\)

This permits standard independent-transversal criteria to be used without
confusing shared occurrences with collisions.  For example, Haxell's
independent-transversal theorem gives a selector if every nonempty target
part has size at least `2 Delta`, where `Delta` is the maximum degree of
`Gamma_W` (with nonemptiness imposed separately when `Delta=0`).  No such
degree or menu-size bound is proved here for the Boolean instance.

### Proposition 4.2 (two-edge interval augmentation obstruction)

Compatible witness-token sets need not form a matroid, even at the abstract
occurrence-interval interface with two-edge witnesses.

#### Proof

Take labelled occurrences

\[
 u(r_0)=u(r_1)=R,\qquad
 u(s_0)=u(s_1)=S,\qquad u(t)=T,                       \tag{4.1}
\]

and three two-edge interval tokens

\[
 J(\alpha)=\{r_0,s_0\},\qquad
 J(\beta)=\{r_1,t\},\qquad
 J(\gamma)=\{t,s_1\}.                               \tag{4.2}
\]

The first interval may lie on one path component and the latter two as
overlapping consecutive intervals on another; complete the paths to cycles
with fresh-colour filler occurrences if desired.  Both `{alpha}` and
`{beta,gamma}` have rainbow unions.  But neither `beta` nor `gamma` can
augment `{alpha}`: the first repeats colour `R` at another occurrence and
the second repeats `S`.  The augmentation axiom fails.

Every gammoid is a matroid.  Thus the witness tokens in general are not the
ground of a direct gammoid or Rado matroid.  The example does not rule out
an enlarged auxiliary-network or CSP reduction.  \(\square\)

The example is an interface obstruction; it is not asserted to be the
rooted occurrence table of a particular Boolean `M_0`.

## 5. Fixed selector: exact matroid intersection and Hall min--max

Fix a protected rainbow selector `sigma` and put

\[
                 H_\sigma=P\cup\bigcup_XJ(I_X).       \tag{5.1}
\]

Let `M_u` be the partition matroid on `E` with capacity one on every block
`E_R`, and let `M_g` be the graphic matroid of the occurrence-labelled
underlying multigraph of `F`.

### Theorem 5.1 (fixed-bank Edmonds criterion)

If `H_sigma` is independent in both matroids, it extends to an upper-exact
rooted forest if and only if

\[
 \min_{A\subseteq E-H_\sigma}
 \left[
  r_{M_u/H_\sigma}(A)+
  r_{M_g/H_\sigma}((E-H_\sigma)-A)
 \right]
                         \ge U-|H_\sigma|.             \tag{5.2}
\]

#### Proof

After contraction of the common independent set `H_sigma`, an extension is
a common independent set of size `U-|H_sigma|` in the two contracted
matroids.  Edmonds' matroid-intersection min--max says that the maximum
common-independent-set size is the left side of (5.2).  A size-`U`
independent set of `M_u` contains exactly one occurrence of every one of the
`U` colours, and independence in `M_g` is exactly the forest condition.
\(\square\)

For `K in mathcal K`, define

\[
 N_R^\sigma=\{K:K\text{ contains an }R\text{-occurrence outside }
 H_\sigma\}.                                          \tag{5.3}
\]

Put

\[
 \partial(H_\sigma)=
 \max_{Y\subseteq\mathcal K}
 \left(
 |Y|-\sum_{R:N_R^\sigma\cap Y\ne\varnothing}b_R
 \right).                                             \tag{5.4}
\]

The empty set makes `partial(H_sigma)>=0`.

### Theorem 5.2 (Hall form and exact joint residual)

For every protected rainbow selector, an upper-exact forest containing its
bank exists if and only if

\[
                            \partial(H_\sigma)=0.       \tag{5.5}
\]

Moreover `partial(H_sigma)` is the minimum number of old factor components
which must remain unbroken under the exact deletion quotas while
`H_sigma` is protected.  Consequently, with value `+infinity` when no
protected rainbow selector exists,

\[
 \boxed{
 \Delta_{\rm joint}=
 \min_{\sigma\ {m protected\ rainbow}}
 \max_{Y\subseteq\mathcal K}
 \left(
 |Y|-\sum_{R:N_R^\sigma\cap Y\ne\varnothing}b_R
 \right)}                                             \tag{5.6}
\]

vanishes exactly when the joint retained-old rainbow forest exists.

#### Proof

Deleting exactly `b_R` occurrences of colour `R` is forced by upper
exactness.  Designate one deletion for every factor component to be broken.
Colour `R` can supply at most `b_R` designations and can serve component `K`
exactly when `K in N_R^sigma`.  Capacitated Hall gives (5.4)--(5.5), and its
deficiency theorem says that the maximum number of served components is
`|mathcal K|-partial(H_sigma)`.  Any designation extends colour by colour
to the exact quotas because a rainbow bank leaves at least `b_R`
occurrences of every colour outside it.  Conversely, choose one designated
edge in every component met by a quota deletion set.  This proves the
deficiency interpretation.

Minimizing that exact deficiency over all witness selectors proves (5.6).
The fixed-selector equivalence with (5.2) follows because both characterize
the same common-base extension.  \(\square\)

Formula (5.6) is an exact min--max obstruction, not a claimed closed-form
evaluation of the outer minimum.

## 6. Reserve Hall decouples omission from witness selection

For a component and colour put

\[
                    m_{K,R}=|E(K)\cap E_R|,
 \qquad N_R^{(2)}=\{K:m_{K,R}\ge2\}.                 \tag{6.1}
\]

### Theorem 6.1 (multiplicity-two immune omission bank)

If

\[
 |Y|\le
 \sum_{R:N_R^{(2)}\cap Y\ne\varnothing}b_R
             \qquad(Y\subseteq\mathcal K),           \tag{6.2}
\]

then every protected rainbow witness bank extends to an upper-exact rooted
forest.  Hence under (6.2) the only remaining retained-old selection row is
the independent transversal of Proposition 4.1.

#### Proof

A rainbow bank contains at most one occurrence of colour `R` in the whole
factor.  If `K` contains at least two such occurrences, at least one remains
outside the bank.  Therefore

\[
                         N_R^{(2)}\subseteq N_R^\sigma             \tag{6.3}
\]

for every rainbow selector.  Inequality (6.2) implies every Hall inequality
in (5.4), and Theorem 5.2 applies.  \(\square\)

There is a more flexible menu form.  Restrict each target to a declared
witness menu and let `A` contain `P` and every occurrence used by any menu
witness.  Define

\[
 N_R^{\rm res}(A)=
 \{K:(E(K)\cap E_R)-A\ne\varnothing\}.               \tag{6.4}
\]

### Corollary 6.2 (immutable reserve Hall)

If the restricted menus have a protected rainbow selector and

\[
 |Y|\le
 \sum_{R:N_R^{\rm res}(A)\cap Y\ne\varnothing}b_R
             \qquad(Y\subseteq\mathcal K),           \tag{6.5}
\]

then they have a joint upper-exact rooted forest.

#### Proof

Every selected bank is contained in `A`, so every occurrence counted by
`N_R^res(A)` remains available for deletion.  Thus
`N_R^res(A) subseteq N_R^sigma`; apply Theorem 5.2.  \(\square\)

Combining Corollary 6.2 with the independent-transversal size condition
after Proposition 4.1 gives a completely explicit, but conditional,
rainbow-plus-forest existence theorem.

## 7. A sharp component-profile obstruction

Specialize to the Boolean owner layer on `[2m-1]`.  A target of rank `m+q`
requires a `q`-edge old path witness.  Let the directed path components of
an upper-exact forest have edge lengths

\[
                  \ell_1,\ldots,\ell_{Cat_m},
                  \qquad\sum_i\ell_i=U.               \tag{7.1}
\]

### Proposition 7.1 (all-width run-capacity inequalities)

If the forest internally witnesses every target of rank `m+q`, then

\[
 \boxed{
 \sum_i(\ell_i-q+1)_+
       \ge {2m-1\choose m+q}}
 \qquad(2\le q\le m-2).                              \tag{7.2}
\]

For `m>=4`, in particular, if `s_+=|{i:ell_i>0}|`, the width-two row
requires

\[
                s_+\le U-{2m-1\choose m+2},           \tag{7.3}
\]

and the top proper row requires

\[
       \sum_i(\ell_i-m+3)_+\ge2m-1.                  \tag{7.4}
\]

#### Proof

A directed path with `ell` edges has exactly `(ell-q+1)_+` directed
`q`-edge subpaths.  Each such subpath has one fixed owner union and therefore
can witness at most one rank-`m+q` target.  Distinct required targets need
distinct witnessing subpaths, proving (7.2).  Equation (7.3) is the case
`q=2`, because `sum_i(ell_i-1)_+=U-s_+`.  Equation (7.4) is `q=m-2`, using
`binom(2m-1,2m-2)=2m-1`.  \(\square\)

These are necessary, not sufficient.  They apply only to the strategy in
which the higher witnesses lie already in `Q_0`; new connector seams may
deliver targets outside this count.

## 8. Proof-safe frontier

The fixed-factor retained-old problem now has four exact, mutually
consistent faces.

* The deletion face is the quota family (2.1) avoiding every target blocker
  clutter.
* The assignment face is the occurrence-section join (3.6), with an exact
  join-tree theorem when the scopes have running intersection.
* The witness face is an independent transversal, not a matroid on witness
  tokens in general.
* After the witnesses are fixed, the extension face is ordinary partition--
  graphic matroid intersection, equivalently the exact component-omission
  Hall deficiency (5.4).

The forced-cut cores, pivot bank, `q1` capacities, and component omissions
are all literal parts of these formulations.  What remains unproved is a
Boolean all-parameter reason that makes one of the following hold:

1. the full occurrence-section join is nonempty;
2. its scopes admit a useful running-intersection decomposition;
3. a large low-conflict witness menu and immutable reserve Hall bank coexist;
   or
4. the outer minimum in (5.6) is zero.

Ordered component-port Hall may then add connectors without deleting
`Q_0`, so every selected witness survives.  A switch route still needs the
separate retained-or-redelivered test.  The monotone pivot insertion remains
transparent under its original containment hypothesis.  None of those
downstream statements supplies the missing joint section proved equivalent
above.

## 9. Input ledger

The following files were read in full.  SHA-256 values refer to the exact
workspace bytes used for this theorem.

* `MATH_THEOREM_BPLUS1_ALLWIDTH_RAINBOW_WITNESS_BANK_AND_SAFE_OPENING_20260803.md`  
  `f44ff6af870e6ef188444193e7c1755bb1441832f3a477a11bc0bda0505d5958`
* `MATH_THEOREM_PROTECTED_UPPER_EXACT_CATALAN_FOREST_FORWARD_ATLAS_PULL_ABSORBER_20260803.md`  
  `b2b3c1dcfdcab1338aaffb2783f8a5edc26b8e21a1358e2604696fedaa8333d1`
* `MATH_THEOREM_BPLUS1_PROTECTED_COMPONENT_PORT_HALL_AND_OCTAGON_HAMILTONIZATION_20260803.md`  
  `401aa24568e869909e332c61d222e72d6a0310c585168484e0b30267d6739392`
* `MATH_THEOREM_BPLUS1_CATALAN_HAMILTON_PATH_CERTIFICATE_20260801.md`
  (the directly named input of the component-port theorem)  
  `a6329c0f3e5f1c7dc5e5ab76338ff52a955f874901e282dc1a17fffae4d7a503`

No finite search, solver, random experiment, or candidate computation is
used.
